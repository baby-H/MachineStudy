# -*- coding: utf-8 -*-
# Author: Hu Ying Jie ( huyingjie2123@163.com )
# Copyright 2019 @ Hu Ying Jie

import speech_recognition as sr
import os


def get_test_result(path=None, duration=None, offset=None, has_noise=0):
    """
    Has_noise = 0, 没有噪音， Has_noise = 1, 有噪音
    """
    r = sr.Recognizer()
    harvard = sr.AudioFile(path)
    with harvard as source:
        if has_noise == 1:
            r.adjust_for_ambient_noise(source, duration=0.8)
        audio = r.record(source=source, duration=duration, offset=offset)
        return r.recognize_google(audio)


if __name__ == '__main__':
    # jackhammer 噪音测试样例
    # harvard 无噪音测试
    base_dir = 'E:\\source\\python-speech-recognition\\audio_files'
    temp = get_test_result(path=os.path.join(base_dir, 'harvard.wav'), duration=3)
    print(temp)
    temp = get_test_result(path=os.path.join(base_dir, 'jackhammer.wav'), duration=3, has_noise=1)
    print(temp)

