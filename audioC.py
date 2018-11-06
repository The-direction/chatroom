from socket import *
import threading
import pyaudio
import wave
import sys
import zlib
import struct
import pickle
import time
import numpy as np

# 设置音频参数
CHUNK = 1024
FORMAT = pyaudio.paInt16  # 设置样本格式
CHANNELS = 2  # 设置通道数
RATE = 44100  # 设置音频处理速率
RECORD_SECONDS = 0.5  # 设置记录秒


# class Audio_Client(threading.Thread):##创建类继承threading.Thread方法
#     def __init__(self ,ip, port, version):
#         #创建多线程
#         threading.Thread.__init__(self)
#         self.setDaemon(True)
#         self.ADDR = (ip, port)
#         #创建套解字
#         if version == 4:
#             self.sock = socket(AF_INET, SOCK_STREAM)
#         else:
#             self.sock = socket(AF_INET6, SOCK_STREAM)
#         #调用pyaudio
#         self.p = pyaudio.PyAudio()
#         #设置音频流为空
#         self.stream = None

class Audio_Client():  # 创建类继承threading.Thread方法
    def __init__(self, ADDR3):
        # 创建多线程
        # threading.Thread.__init__(self)
        # self.setDaemon(True)
        self.ADDR3 = ADDR3
        # 创建套解字
        # if version == 4:
        self.sock = socket(AF_INET, SOCK_STREAM)
        # else:
        #     self.sock = socket(AF_INET6, SOCK_STREAM)
        # 调用pyaudio
        self.p = pyaudio.PyAudio()
        # 设置音频流为空
        self.stream = None
        self.run()

    # 初始化del函数
    def __del__(self):
        # 退出的时候自动关闭套接字
        self.sock.close()

        # 如果退出时音频流不为空,也要关闭
        # 判断音频流是否为空
        if self.stream is not None:
            # 停止音频流传输
            self.stream.stop_stream()
            # 关闭音频流
            self.stream.close()
        # 关闭pyaudio
        self.p.terminate()

    # 启动
    def run(self):
        print("AUDIO client starts...")
        print(self.ADDR3)

        # 创建循环连接服务端
        while True:
            try:
                # 连接上服务端就关闭循环
                self.sock.connect(self.ADDR3)
                break
            except:
                # 发生异常就等待三秒重新连接
                time.sleep(3)
                continue
        print("AUDIO client connected...")
        # 开启音频流
        self.stream = self.p.open(format=FORMAT,
                                  channels=CHANNELS,
                                  rate=RATE,
                                  input=True,
                                  frames_per_buffer=CHUNK)

        while self.stream.is_active():
            # 创建列表
            frames = []
            # 循环录音
            for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                # 或者从流中读取音频数据
                data = self.stream.read(CHUNK)
                # 把音频数据添加到列表
                frames.append(data)

            senddata = pickle.dumps(frames)
            try:
                self.sock.sendall(struct.pack("L", len(senddata)) + senddata)
            except:
                break


# a = Audio_Client('0.0.0.0', 9999, 4)
# a.run()
