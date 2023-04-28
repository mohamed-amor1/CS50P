# Importing the required libraries
import cowsay
import pyttsx3

# Initializing the text-to-speech engine
engine = pyttsx3.init()

# Getting the input from the user
this = input("What's this? ")

# Using cowsay library to display the input as an ASCII cow speech bubble
cowsay.tux(this)

# Setting the voice property of the text-to-speech engine to a female voice
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

# Using the text-to-speech engine to speak the input aloud
engine.say(this)
engine.runAndWait()
