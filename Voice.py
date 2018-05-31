from gtts import gTTS
import playsound as ps
import os
tex = "These are my first words"

obj = gTTS(text=tex,lang='en')
obj.save("First.mp3")

ps.playsound('First.mp3')

os.remove('First.mp3')
