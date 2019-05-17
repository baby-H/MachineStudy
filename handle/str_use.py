# -*- coding: utf-8 -*-
# Author: Hu Ying Jie ( huyingjie2123@163.com )
from handle import json_use
import jieba


def index_in_str(str_t):
    print(str(str_t).find('我'))
    if str(str_t).find('我') >= 0 or str(str_t).find('饿') >= 0 or str(str_t).find('俄') >= 0:
        print("我")
        return -1
    else:
        return 0


def is_greet(json_t=None):
    str_t = json_use.get_final(json_t)
    return (len(str_t) - index_in_str(str_t)) < 3


def is_greet_on(str_t):
    return (len(str_t) - index_in_str(str_t)) < 1


if __name__ == '__main__':
    t = '大象要飞，你好'
    if index_in_str(t):
        print(index_in_str(t))
    # print(index_in_str(t))
    # print(len(t))
