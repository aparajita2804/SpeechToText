# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 20:08:07 2019

@author: Admin
"""

import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print('Speak:')
    audio = r.listen(source)
    
    try:
        text = r.recognize_google(audio)
        print('You said: {}'.format(text))
    except:
        print('Sorry could not recognise your voice. Try again. Thank you!!!')