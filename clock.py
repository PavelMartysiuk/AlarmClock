from time import sleep
from sys import argv
#from winsound import Beep
from datetime import datetime
import os
from gtts import gTTS
def sound (text):
    sound = gTTS(text = text, lang = 'en')
    sound.save('Clock_sound.mp3')
    #os.system('Clock_sound.mp3')
def clock():
    while True: 
        time = datetime.today()
        only_clock = time.strftime('%H:%M:%S')
        break_point = argv
        print('\r' + str(only_clock), end = '')
        sleep(1)
        if only_clock  in break_point:
            os.system('Clock_sound.mp3')                            
            #Beep(900,1000)
if __name__ == '__main__':
    sound('Good morning,time to work')
    clock()
