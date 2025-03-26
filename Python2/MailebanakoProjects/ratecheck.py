import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Get the current rate
rate = engine.getProperty('rate')
print(f"Current rate: {rate}")

# Set a slower rate (e.g., 100 WPM)
engine.setProperty('rate', 100)

# Set the text you want to be spoken
text = "Hello, this is a slower rate of speech."

# Make the engine speak the text
engine.say(text)

# Wait for the speaking to finish
engine.runAndWait()