# -*- coding: utf-8 -*-
# Author: Hu Ying Jie ( huyingjie2123@163.com )
from handle import json_use
import jieba


def index_in_str(str_t):
    return str(str_t).find('大象') + 4


def is_greet(json_t=None):
    str_t = json_use.get_final(json_t)
    return (len(str_t) - index_in_str(str_t)) < 1


def is_greet_on(str_t):
    return (len(str_t) - index_in_str(str_t)) < 1


if __name__ == '__main__':
    t = '我是大象要飞，你好'
    print(index_in_str(t))
    print(len(t))
