# -*- coding: utf-8 -*-
# Author: Hu Ying Jie ( huyingjie2123@163.com )
# Copyright 2019 @ Hu Ying Jie

import speech_recognition as sr

# Recognizer() 使用系统默认
# Recognizer().listen(Microphone()) 指定使用 Microphone() 参数 device_index=default
if __name__ == '__main__':
    mic = sr.Microphone(device_index=0)
    r = sr.Recognizer()
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        temp = r.recognize_google(audio)
        print(temp)
