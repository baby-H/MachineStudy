# -*- encoding:utf-8 -*-
# Author: Hu Ying Jie ( huyingjie2123@163.com )
import hashlib
from hashlib import sha1
import hmac
import base64
from socket import *
import json, time, threading
import websocket
from websocket import create_connection
from urllib.parse import quote
import logging
from handle import json_use

logging.basicConfig()
base_url = "ws://rtasr.xfyun.cn/v1/ws"
app_id = "5c933e31"
api_key = "6435190c7ab54be46fca125adc77991e"
file_path = "test_1.pcm"
end_tag = "{\"end\": true}"


class Client():
    def __init__(self):
        # 生成鉴权参数
        ts = str(int(time.time()))
        tmp = app_id + ts
        hl = hashlib.md5()
        hl.update(tmp.encode(encoding='utf8'))
        my_sign = hmac.new(api_key.encode(encoding='utf8'),
                           str(hl.hexdigest()).encode(encoding='utf'),
                           sha1).digest()
        signa = base64.b64encode(my_sign)
        self.ws = create_connection(base_url + "?appid=" + app_id + "&ts=" + ts + "&signa=" + quote(signa))
        self.trecv = threading.Thread(target=self.recv)
        self.trecv.start()

    def send(self, data_t):
        try:
            index = 1280
            while True:
                if index > len(data_t):
                    self.ws.send(data_t[index - 1280:len(data_t)])
                    break
                else:
                    self.ws.send(data_t[index - 1280:index])
                index += 1280
        finally:
            print('结束')
            self.ws.send(bytes(end_tag.encode(encoding='utf8')))
        print("send end tag success")

    def recv(self):
        try:
            while self.ws.connected:
                result = str(self.ws.recv())
                if len(result) == 0:
                    print("receive result end")
                    break
                result_dict = json.loads(result)

                # 解析结果
                if result_dict["action"] == "started":
                    print("handshake success, result: " + result)

                if result_dict["action"] == "result":
                    final_result = result_dict['data']
                    if json_use.get_status(final_result) == '0':
                        print(json_use.get_final(final_result))
                if result_dict["action"] == "error":
                    print("rtasr error: " + result)
                    self.ws.close()
        except websocket.WebSocketConnectionClosedException as e:
            self.ws.close()
            print("receive result end")

    def close(self):
        self.ws.close()
        print("connection closed")


if __name__ == '__main__':
    client = Client()
    client.send(file_path)
