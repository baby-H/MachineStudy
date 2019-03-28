# -*- coding: utf-8 -*-
# Author: Hu Ying Jie ( huyingjie2123@163.com )
import json
import time
import jieba


def get_final(xun_fei_str=None):
    xun_fei_json = json.loads(xun_fei_str)
    str_t = ''
    for x_t in xun_fei_json['cn']['st']['rt'][0]['ws']:
        str_t += x_t['cw'][0]['w']
    return str_t


def get_list(xun_fei_str=None):
    xun_fei_json = json.loads(xun_fei_str)
    li = []
    judge = 0
    for x_t in xun_fei_json['cn']['st']['rt'][0]['ws']:
        if x_t['cw'][0]['w'] in ['我', '她', '它', '他']:
            judge += 1
            continue
        if judge == 1:
            li.append(x_t['cw'][0]['w'])
    return li


def get_list_on(xun_fei_str=None):
    t = jieba.cut(xun_fei_str)
    li = []
    judge = 0
    for i in t:
        if i in ['！', '？', '。', '，']:
            continue
        if i in ['我', '她', '它', '他']:
            judge += 1
            continue
        if judge == 1:
            li.append(i)
    print(li)
    return li


def get_status(xun_fei_str=None):
    xun_fei_json = json.loads(xun_fei_str)
    return xun_fei_json['cn']['st']['type']


if __name__ == '__main__':
    temp = "{\"cn\":{\"st\":{\"bg\":\"820\",\"ed\":\"0\",\"rt\":[{\"ws\":[{\"cw\":[{\"w\":\"啊\",\"wp\":\"n\"}],\"wb\":0,\"we\":0},{\"cw\":[{\"w\":\"我\",\"wp\":\"n\"}],\"wb\":0,\"we\":0},{\"cw\":[{\"w\":\"腿疼\",\"wp\":\"p\"}],\"wb\":0,\"we\":0},{\"cw\":[{\"w\":\"头晕\",\"wp\":\"n\"}],\"wb\":0,\"we\":0},{\"cw\":[{\"w\":\"恶心\",\"wp\":\"p\"}],\"wb\":0,\"we\":0},{\"cw\":[{\"w\":\"头疼\",\"wp\":\"n\"}],\"wb\":0,\"we\":0},{\"cw\":[{\"w\":\"胸闷\",\"wp\":\"n\"}],\"wb\":0,\"we\":0},{\"cw\":[{\"w\":\"气短\",\"wp\":\"n\"}],\"wb\":0,\"we\":0}]}],\"type\":\"1\"}},\"seg_id\":5}\n"
    print(time.time())
    print(get_final(temp))
    print(time.time())
