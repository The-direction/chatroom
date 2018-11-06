import pyaudio
import wave

#设置参数
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 20
WAVE_OUTPUT_FILENAME = "output.wav"

#调用pyaudio
p = pyaudio.PyAudio()

#设置播放参数
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")


frames = []

#播放流
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()#停止播放
stream.close()#关闭流
p.terminate()#终止portaudio会话

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')#以读写打开文件
wf.setnchannels(CHANNELS)#设置音频文件的声道数
wf.setsampwidth(p.get_sample_size(FORMAT))#设置音频文件每个采样值得保存位数
wf.setframerate(RATE)#设置采样率
wf.writeframes(b''.join(frames))#保存
wf.close()#关闭文件
