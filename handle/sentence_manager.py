# -*- coding: utf-8 -*-
# Author: Hu Ying Jie ( huyingjie2123@163.com )
from handle import json_use, str_use, model_use


def get_final_sentence(json_t=None):
    if str_use.is_greet(json_t):
        return '您好啊！！！！'
    else:
        positive_list_t = json_use.get_list(json_t)
        return model_use.get_sentence(positive=positive_list_t)


def get_final_sentence_on(str_t):
    if str_use.is_greet_on(str_t):
        return '好的！！！！'
    else:
        list_t = json_use.get_list_on(str_t)
        return model_use.get_sentence(list_t)


if __name__ == '__main__':
    temp = "{\"cn\":{\"st\":{\"bg\":\"820\",\"ed\":\"0\",\"rt\":[{\"ws\":[{\"cw\":[{\"w\":\"啊\",\"wp\":\"n\"}],\"wb\":0,\"we\":0},{\"cw\":[{\"w\":\"我\",\"wp\":\"n\"}],\"wb\":0,\"we\":0},{\"cw\":[{\"w\":\"头疼\",\"wp\":\"p\"}],\"wb\":0,\"we\":0},{\"cw\":[{\"w\":\"发烧\",\"wp\":\"n\"}],\"wb\":0,\"we\":0},{\"cw\":[{\"w\":\"头晕\",\"wp\":\"p\"}],\"wb\":0,\"we\":0},{\"cw\":[{\"w\":\"流鼻涕\",\"wp\":\"n\"}],\"wb\":0,\"we\":0},{\"cw\":[{\"w\":\"大象\",\"wp\":\"n\"}],\"wb\":0,\"we\":0},{\"cw\":[{\"w\":\"要飞\",\"wp\":\"n\"}],\"wb\":0,\"we\":0}]}],\"type\":\"1\"}},\"seg_id\":5}\n"
    print(json_use.get_list(temp))
    print(get_final_sentence(temp))
