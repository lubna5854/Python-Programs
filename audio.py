# audio converter

from gtts import gTTS
import os
text="Today is a good day"
output=gTTS(text=text,lang='ml',slow=False)
output.save('good.mp4')
os.system('start good.mp4')