# -*- coding: utf-8 -*-
# Author: Hu Ying Jie ( huyingjie2123@163.com )
# Copyright 2019 @ Hu Ying Jie

import pyttsx3


if __name__ == '__main__':
    engine = pyttsx3.init()
    # engine = pyttsx.init()
    engine.say(text='hello 雪桐我去你大爷')
    engine.runAndWait()
