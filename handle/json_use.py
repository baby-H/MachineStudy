# -*- coding: utf-8 -*-
# Author: Hu Ying Jie ( huyingjie2123@163.com )
import json
import time


def get_final(xun_fei_str=None):
    xun_fei_json = json.loads(xun_fei_str)
    str_t = ''
    for x_t in xun_fei_json['cn']['st']['rt'][0]['ws']:
        str_t += x_t['cw'][0]['w']
    return str_t


def get_status(xun_fei_str=None):
    xun_fei_json = json.loads(xun_fei_str)
    return xun_fei_json['cn']['st']['type']


if __name__ == '__main__':
    temp = "{\"cn\":{\"st\":{\"bg\":\"820\",\"ed\":\"0\",\"rt\":[{\"ws\":[{\"cw\":[{\"w\":\"啊\",\"wp\":\"n\"}],\"wb\":0,\"we\":0},{\"cw\":[{\"w\":\"喂\",\"wp\":\"n\"}],\"wb\":0,\"we\":0},{\"cw\":[{\"w\":\"！\",\"wp\":\"p\"}],\"wb\":0,\"we\":0},{\"cw\":[{\"w\":\"你好\",\"wp\":\"n\"}],\"wb\":0,\"we\":0},{\"cw\":[{\"w\":\"！\",\"wp\":\"p\"}],\"wb\":0,\"we\":0},{\"cw\":[{\"w\":\"我\",\"wp\":\"n\"}],\"wb\":0,\"we\":0},{\"cw\":[{\"w\":\"是\",\"wp\":\"n\"}],\"wb\":0,\"we\":0},{\"cw\":[{\"w\":\"上\",\"wp\":\"n\"}],\"wb\":0,\"we\":0}]}],\"type\":\"1\"}},\"seg_id\":5}\n"
    print(time.time())
    print(get_final(temp))
    print(time.time())
