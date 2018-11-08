
"""PyAudio example: Record a few seconds of audio and save to a WAVE file."""

import pyaudio
import wave


#设置参数
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 8000
RECORD_SECONDS = 60
WAVE_OUTPUT_FILENAME = "output.wav"  #保存的文件名

p = pyaudio.PyAudio()  #调用pyaudio

#设置录制参数
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

#存储录制语音
frames = []
count = 1
#录制流
print('---录制----')
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    # print('---录制----')
    data = stream.read(CHUNK)
    frames.append(data)
    count += 1
    if count > 50:
        break

print("* done recording")

#停止录制
stream.stop_stream()
#关闭流
stream.close()
#终止portaudio会话
p.terminate()

#以读写打开文件
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS) #设置音频文件的声道数
wf.setsampwidth(p.get_sample_size(FORMAT)) #设置音频文件每个采样值得保存位数
wf.setframerate(RATE) #设置采样率
wf.writeframes(b''.join(frames))  #保存
wf.close() #关闭文件


