# -*- coding: utf-8 -*-
# Author: Hu Ying Jie ( huyingjie2123@163.com )
import speech_recognition as sr
from sounds import xunfei_ontime_sound_text
import pyttsx3
import threading
from handle import wake_use


def throw_wake_thread():
    wake = wake_use.Wake()
    r = sr.Recognizer()
    print(wake.get_wake())
    with sr.Microphone() as source:
        if wake.get_wake() == 0:
            r.adjust_for_ambient_noise(source)
            audio_w = r.listen(source)
            wav_w = audio_w.get_wav_data(convert_rate=16000)
            client_w = xunfei_ontime_sound_text.Client()
            client_w.send(wav_w[44:])
        else:
            engine = pyttsx3.init()
            r.adjust_for_ambient_noise(source, duration=2)
            engine.say("您好, 我在, 有问题可以随时问我的哦！")
            engine.runAndWait()
            audio = r.listen(source)
            engine.say("问题已签收, 大想要飞高速计算中")
            wav = audio.get_wav_data(convert_rate=16000)
            client = xunfei_ontime_sound_text.Client(wake)
            client.send(wav[44:])
            engine.runAndWait()


if __name__ == '__main__':
    w = threading.Thread(target=throw_wake_thread())
    w.start()

