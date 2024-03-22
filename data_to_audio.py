#data conversion into speech

from gtts import gTTS
import os
text=open('filepgm.txt','r').read()
language='ml'
output=gTTS(text=text,lang=language,slow=False)
output.save('filepg.mp4')
os.system('start filepg.mp4')