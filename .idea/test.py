import speech_recognition as sr

@app.route("/process", methods=['POST'])
def process():
	# Record audio from microphone
	r = sr.Recognizer()
	with sr.Microphone() as source:
	    print("Speak:")
	    audio = r.listen(source)

	# Convert speech to text using Google Speech Recognition
	try:
	    text = r.recognize_google(audio)
	    return text
	except sr.UnknownValueError:
	    return "Unable to understand speech"
	except sr.RequestError as e:
	    return "Error during speech recognition: {0}".format(e)
