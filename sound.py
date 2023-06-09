from gtts import gTTS 
import os

text = "Привет!"
language = "ru"

tts = gTTS(text=text, lang=language)
tts.save("hello.mp3")
#os.system("mpg321, hello.mp3")