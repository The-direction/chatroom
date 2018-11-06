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


class Audio_Server():  # 创建类继承threading.Thread方法
    def __init__(self, addr):
        # 创建多线程
        # threading.Thread.__init__(self)
        # self.setDaemon(True)
        self.ADDR = addr
        # 创建套解字
        # if version == 4:
        self.sock = socket(AF_INET, SOCK_STREAM)
        # else:
        #     self.sock = socket(AF_INET6 ,SOCK_STREAM)
        # #调用pyaudio
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
        print("AUDIO server starts...")
        # 绑定渎职
        self.sock.bind(self.ADDR)
        print(self.ADDR)
        # 设置监听
        self.sock.listen(1)
        # 等待处理客户端连接请求
        print("等待客户端音频套接字链接")
        conn, addr = self.sock.accept()
        print("remote AUDIO client success connected...")
        # 创建空字符串　以utf-8对data进行编码
        data = "".encode("utf-8")
        # 计算整形格式所描述的结构的大小
        payload_size = struct.calcsize("L")
        # 开启音频流
        self.stream = self.p.open(format=FORMAT,
                                  channels=CHANNELS,
                                  rate=RATE,
                                  output=True,
                                  frames_per_buffer=CHUNK
                                  )
        # 循环播放
        while True:
            # 接收音频
            while len(data) < payload_size:
                data += conn.recv(81920)
            # 处理音频
            packed_size = data[:payload_size]
            data = data[payload_size:]
            # 返回一个由解包数据(packed_size)得到的一个元组
            msg_size = struct.unpack("L", packed_size)[0]
            # 接收音频
            while len(data) < msg_size:
                data += conn.recv(81920)
            # 音频解包
            frame_data = data[:msg_size]
            data = data[msg_size:]
            frames = pickle.loads(frame_data)
            # 播放音频流
            for frame in frames:
                self.stream.write(frame, CHUNK)


# a = Audio_Server(9999, 4)
# a.run()
