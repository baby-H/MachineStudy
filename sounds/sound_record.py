# -*- coding: utf-8 -*-
# Author: Hu Ying Jie ( huyingjie2123@163.com )

import speech_recognition as sr
import sys
sys.path.append('E:/')
from sounds import xunfei_ontime_sound_text

# Recognizer() 使用系统默认
# Recognizer().listen(Microphone()) 指定使用 Microphone() 参数 device_index=default
if __name__ == '__main__':
    print(sr.Microphone.list_microphone_names())
    client = xunfei_ontime_sound_text.Client()
    mic = sr.Microphone()
    r = sr.Recognizer()
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        temp = client(audio)
        print(temp)
