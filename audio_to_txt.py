#encoding:utf-8
from aip import AipSpeech
'''你的　APPID AK ID '''
APP_ID = '14130589'
API_KEY = 'HwMq9wrFppmIjtatrhpG4BO1'
SECRET_KEY = 'Vzn21eRLc9Kek8Hcrf9RmnNhSyvX3jDd'
client = AipSpeech(APP_ID,API_KEY,SECRET_KEY)
#获取语音文件
def get_file_content(filePath):
    with open(filePath,'rb') as fp:
        return fp.read()
#识别本地文件
result = client.asr(get_file_content(r'C:\Users\ASUS\Desktop\16k.wav'),'wav',16000,{'dev_pid':1536})
#建立包含语音内容的Buffer对象, 语音文件的格式，pcm 或者 wav 或者 amr。不区分大小写
#语音文件的格式，pcm 或者 wav 或者 amr。requests.packages.urllib3.disable_warnings()
#返回接收结果

print(result['result'][0])