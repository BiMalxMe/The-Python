import os
import time
import pyperclip
import pyautogui
import pyttsx3
from gtts import gTTS
# while True:
# a=pyautogui.position()
# print(a)
#1
pyautogui.click(409,745)
time.sleep(1)#Gives one second time for clicking
  
 #2
pyautogui.click(377,18)
time.sleep(1)

#3
pyautogui.click(968,676)
time.sleep(6)

#4
pyautogui.moveTo(398,221)
pyautogui.dragTo(969,677,duration=1.0,button='left')
time.sleep(1)

#5
print("copying the text")
# time.sleep(30)
pyautogui.hotkey('ctrl','c')
# time.sleep(1)

#6
print("here is the copied text")
text=pyperclip.paste()
print(text)

engine=pyttsx3.init()
engine.setProperty('rate', 100)
engine.say(text)
engine.runAndWait()



# Text to be spoken
# Create a gTTS object
# tts = gTTS(text=text, lang='en', slow=False)

# # Save the spoken text to an audio file
# tts.save("output2.mp3")

# # Play the audio file
# os.system("start output2.mp3")  # On Windows