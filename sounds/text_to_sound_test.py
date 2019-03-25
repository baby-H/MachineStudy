# -*- coding: utf-8 -*-
import requests
import time
import hashlib
import base64
import wave
from pyaudio import PyAudio

URL = "http://api.xfyun.cn/v1/service/v1/tts"
AUE = "raw"
APPID = "5c933e31"
API_KEY = "4367306353c6fa0b55f4212f82b0429a"


def getHeader():
    curTime = str(int(time.time()))

    param = "{\"aue\":\"" + AUE + "\",\"auf\":\"audio/L16;rate=16000\",\"voice_name\":\"xiaoyan\",\"engine_type\":\"intp65\"}"
    print("param:{}".format(param))

    paramBase64 = str(base64.b64encode(param.encode('utf-8')), 'utf-8')
    print("x_param:{}".format(paramBase64))

    m2 = hashlib.md5()
    m2.update((API_KEY + curTime + paramBase64).encode('utf-8'))

    checkSum = m2.hexdigest()
    print('checkSum:{}'.format(checkSum))

    header = {
        'X-CurTime': curTime,
        'X-Param': paramBase64,
        'X-Appid': APPID,
        'X-CheckSum': checkSum,
        'X-Real-Ip': '127.0.0.1',
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    }
    print(header)
    return header


def getBody(text):
    data = {'text': text}
    return data


def writeFile(file, content):
    with open(file, 'wb') as f:
        f.write(content)
    f.close()


def play(sid=None):
    chunk = 1024  # 2014kb
    wf = wave.open(r"audio/" + sid + '.wav', 'rb')
    p = PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(),
                    rate=wf.getframerate(), output=True)

    data = wf.readframes(chunk)  # 读取数据

    while True:
        data = wf.readframes(chunk)
        if data == "":
            break
        stream.write(data)
    stream.stop_stream()  # 停止数据流
    stream.close()
    p.terminate()  # 关闭 PyAudio


r = requests.post(URL, headers=getHeader(), data=getBody("内容"))
contentType = r.headers['Content-Type']
sid = ''
if contentType == "audio/mpeg":
    sid = r.headers['sid']
    if AUE == "raw":
        print(r.content)
        writeFile("audio/" + sid + ".wav", r.content)
    else:
        print(r.content)
        writeFile("audio/" + "xiaoyan" + ".mp3", r.content)
    print("success, sid = " + sid)
else:
    print(r.text)
play(sid)



