# -*- coding: utf-8 -*-
# Author: Hu Ying Jie ( huyingjie2123@163.com )

import speech_recognition as sr
from sounds import xunfei_ontime_sound_text
import numpy as np
import pyttsx3


def wav_to_pcm(wav_file):
    with open(wav_file, 'rb') as file_wav:
        file_wav.seek(0)
        file_wav.read(44)
        data = np.fromfile(file_wav, dtype=np.int16)
        data.tofile("temp.pcm")
        return "temp.pcm"


# Recognizer() 使用系统默认
# Recognizer().listen(Microphone()) 指定使用 Microphone() 参数 device_index=default
if __name__ == '__main__':
    print(sr.Microphone.list_microphone_names())
    engine = pyttsx3.init()
    mic = sr.Microphone()
    r = sr.Recognizer()
    with mic as source:
        r.adjust_for_ambient_noise(source, duration=2)
        engine.say("您好, 请一秒后回答？")
        engine.runAndWait()
        audio = r.listen(source)
        engine.say("录音结束, 识别中")
        engine.runAndWait()
        wav = audio.get_wav_data(convert_rate=16000)
        with open("temp.wav", "wb") as f:
            f.write(wav)
        pcm_file = wav_to_pcm('temp.wav')
        client = xunfei_ontime_sound_text.Client()
        client.send(pcm_file)

