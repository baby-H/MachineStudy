# -*- coding: utf-8 -*-
import requests
import time
import hashlib
import base64
import urllib.parse

URL = "http://api.xfyun.cn/v1/service/v1/iat"
APPID = "5c933e31"
API_KEY = "7ce9cb832b16436d31c22addf5a16f95"


def getHeader(aue=None, engineType=None):
    curTime = str(int(time.time()))
    param = "{\"aue\":\"" + aue + "\"" + ",\"engine_type\":\"" + engineType + "\"}"
    paramBase64 = str(base64.b64encode(param.encode('utf-8')), 'utf-8')
    m2 = hashlib.md5()
    m2.update((API_KEY + curTime + paramBase64).encode('utf-8'))
    checkSum = m2.hexdigest()
    header = {
        'X-CurTime': curTime,
        'X-Param': paramBase64,
        'X-Appid': APPID,
        'X-CheckSum': checkSum,
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    }
    return header


def getBody(filepath):
    binfile = open(filepath, 'rb')
    data = {'audio': base64.b64encode(binfile.read())}
    temp = urllib.parse.urlencode(data)
    return data


if __name__ == '__main__':
    aue = "raw"
    engineType = "sms16k"
    audioFilePath = r"E:\source\python-speech-recognition\audio_files\test_1.pcm"
    r = requests.post(URL, headers=getHeader(aue, engineType), data=getBody(audioFilePath))
    print(r.content.decode(encoding='utf8'))
