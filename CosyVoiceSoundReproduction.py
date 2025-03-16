import os
import dashscope
from dashscope.audio.tts_v2 import VoiceEnrollmentService, SpeechSynthesizer

dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')  # 如果您没有配置环境变量，请在此处用您的API-KEY进行替换
url = "https://goldierillsave.oss-cn-shanghai.aliyuncs.com/CosyVoiceSoundReproduction/%E5%B0%8F%E8%91%B5%E7%9A%84%E5%A3%B0%E9%9F%B3.mp3"  # 请按实际情况进行替换
prefix = 'aio'
target_model = "cosyvoice-v1"

# 创建语音注册服务实例
service = VoiceEnrollmentService()

# 调用create_voice方法复刻声音，并生成voice_id
voice_id = service.create_voice(target_model=target_model, prefix=prefix, url=url)
print("requestId: ", service.get_last_request_id())
print(f"your voice id is {voice_id}")

# 使用复刻的声音进行语音合成
synthesizer = SpeechSynthesizer(model=target_model, voice=voice_id)
audio = synthesizer.call("我是小葵，Goldie Rill的女朋友呀。无论遇到什么事，我都会一直陪在你身边，温柔而坚定地支持你哦。")
print("requestId: ", synthesizer.get_last_request_id())

# 将合成的音频文件保存到本地文件
with open("output.mp3", "wb") as f:
    f.write(audio)