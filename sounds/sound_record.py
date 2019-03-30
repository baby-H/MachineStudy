# -*- coding: utf-8 -*-
# Author: Hu Ying Jie ( huyingjie2123@163.com )
import speech_recognition as sr
from sounds import xunfei_ontime_sound_text
import pyttsx3
from handle import wake_use
from sounds import xunfei_sound_to_text
from handle import sentence_manager
import json


def throw_wake_thread():
    wake = wake_use.Wake()
    r = sr.Recognizer()
    print(wake.get_wake())
    engine = pyttsx3.init()
    with sr.Microphone() as source:
        if wake.get_wake() == 0:
            r.adjust_for_ambient_noise(source)
            engine.say("您好, 有问题可以随时问我的哦！")
            engine.runAndWait()
            audio_w = r.listen(source)
            engine.say("问题已签收, 小老弟高速计算中")
            engine.runAndWait()
            wav_w = audio_w.get_wav_data(convert_rate=16000)
            client_w = xunfei_ontime_sound_text.Client(wake)
            client_w.send(wav_w[44:])

        else:
            r.adjust_for_ambient_noise(source, duration=2)
            engine.say("您好, 我在, 有问题可以随时问我的哦！")
            engine.runAndWait()
            audio = r.listen(source)
            engine.say("问题已签收, 小老弟高速计算中")
            wav = audio.get_wav_data(convert_rate=16000)
            client = xunfei_ontime_sound_text.Client(wake)
            client.send(wav[44:])
            engine.runAndWait()


def create_con():
    r = sr.Recognizer()
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 20)
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1.3)
        engine.say("在，叫我干啥")
        engine.runAndWait()
        audio_w = r.listen(source)
        engine.say("您的话, 朕已阅, 正在处理中")
        wav_w = audio_w.get_wav_data(convert_rate=16000)
        temp_t = xunfei_sound_to_text.send(wav_w[44:])
        result_json = json.loads(temp_t)
        print(result_json['data'])
        t = sentence_manager.get_final_sentence_on(result_json['data'])
        engine.say(t)
        engine.runAndWait()


if __name__ == '__main__':
    while True:
        create_con()

