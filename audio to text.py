import pyaudio
import wave
import speech_recognition as sr
def play_audio(filename):
	print('1')
	chunk = 1024#we're reading 1024 bites or kb of file we're reading at a time
	wf=wave.open(filename,'rb')#opening file as binary wave file
	pa = pyaudio.PyAudio()#creating instance of pyaudio class
	#creatig stream from this file
	stream = pa.open(
		format = pa.get_format_from_width(wf.getsampwidth ()),
		channels = wf.getnchannels(),
		rate = wf.getframerate(),
		output = True
		)
	data_stream = wf.readframes(chunk)# reads first initial chink of bits from file
	while data_stream:
		stream.write(data_stream)
		data_stream = wf.readframes(chunk) #to continue reading the next chunk of frames
	stream.close()
	pa.terminate()

r = sr.Recognizer()
def initSpeech():
	#print("listening")
	play_audio("laugh.wav")
	with sr.Microphone() as source :
		r.adjust_for_ambient_noise(source, duration=1)
		print(r.energy_threshold)
		print("format rate :", source.format)
		print("Say something!...")
		print(r.energy_threshold)
		r.energy_threshold += 280
		audio = r.listen(source)
         #Speech r
	play_audio("laugh.wav")
	command = ""
	try:
		command = r.recognize_google(audio,language = 'en-GB')#en-Gb to recognize indian accent
	except:
		print('didn"t get you' )
	print("your command:")
	print(command)
	text_file = open("Output.txt", "w")
	text_file.write("your command: %s" %command)
	text_file.close()
initSpeech()  
