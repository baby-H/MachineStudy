# -*- coding: utf-8 -*-
# Author: Hu Ying Jie ( huyingjie2123@163.com )

import speech_recognition as sr
from sounds import xunfei_ontime_sound_text
import time
import pyttsx3


# Recognizer() 使用系统默认
# Recognizer().listen(Microphone()) 指定使用 Microphone() 参数 device_index=default
if __name__ == '__main__':
    print(sr.Microphone.list_microphone_names())
    engine = pyttsx3.init()
    while True:
        mic = sr.Microphone()
        r = sr.Recognizer()
        with mic as source:
            r.adjust_for_ambient_noise(source, duration=2)
            engine.say("您好, 我是大象要飞, 有问题可以随时问我？")
            engine.runAndWait()
            audio = r.listen(source)
            engine.say("问题已签收, 本天才高速计算中")
            engine.runAndWait()
            wav = audio.get_wav_data(convert_rate=16000)
            client = xunfei_ontime_sound_text.Client()
            client.send(wav[44:])
        time.sleep(4)
