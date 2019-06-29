from gtts import gTTS
import speech_recognition as sr
import os
from time import ctime
import webbrowser
import smtplib
import wikipedia
import Database

def speak(audio):
	tts = gTTS(text=audio, lang='en')
	tts.save('audio.mp3')
	os.system('audio.mp3')
	
def reply(message):
	print(message)
	speak(message)

def mic():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		reply("How can I help you?\nListening...")
		r.pause.threshold = 1
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
	
	try:
		command = r.recognize_google(audio)
		print("Recognizing: ", command)
	except sr.UnknownValueError:
		reply("Google Speech Recognition couldn't understand, please try again.")
	except sr.RequestError as e:
		print("Couldn't request results;{0}".format(e))
	return command
	
def bot(command):
	for x in greet:
		if x == command:
			reply('Hello Sir')
			
	if "What time is it" or "Tell me the time" in command:
		speak(ctime())
		
	if "Where is" in command:
		command = command.split(" ")
		location = command[2]
		reply("Hold on, I will check.")
		chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s' #change directory to your browser
		webbrowser.get(chrome_path).open("https://www.google.nl/maps/place/" + location + "/&amp;")

	if 'email' in command:
		reply('Who is the recipient?')
		recipient = mic()
		if x in recipient:
			if x in maildict:
				reply('What should I say?')
				content = mic()
				mail = smtplib.SMTP('smtp.gmail.com', 587)
				mail.ehlo()
				mail.starttls()
				mail.login('Your Email', 'Your Password')
				mail.sendmail(x, maildict[x], content)
				mail.close()
				reply('Email sent.')
            
		else:
			reply('I don\'t know what you mean!')

	if "wikipedia" in command:
		command = command.replace("wikipedia", " ")
		information = wikipedia.summary(command, sentences = 2)
		reply("Wikipedia says...\n" information)
	
	if "open youtube" in command:
		webbrowser.open("https://youtube.com")
		speak("Opening")

	if "open my channel" or "open my youtube channel" in command:
		webbrowser.open("https://www.youtube.com/channel/UCGTIYo3TPAEHVFbY2uU22ig") #change URL to your channel
		speak("Opening")

	if "open my blog" or "open my website" in command:
		webbrowser.open("https://www.creeware.blogspot.com/") #change URL to your website
		speak("Opening")
	
	if "open google" in command:
		webbrowser.open("https://google.com")
		speak("Opening")

	if 'play songs' in command:
		music_dir = 'D:\\Songs' #change music_dir to your own directory
		songs = os.listdir(music_dir)
		os.startfile(os.path.join(music_dir, songs[0]))


reply('Hi, I am Alexa, a virtual assistant program, your desktop companion.\nHow can I help you?')

while True:
	command = mic()
	
