import os
import dashscope
from dashscope.audio.tts_v2 import VoiceEnrollmentService, SpeechSynthesizer

dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')  # 如果您没有配置环境变量，请在此处用您的API-KEY进行替换
url = "https://goldierillsave.oss-cn-shanghai.aliyuncs.com/CosyVoiceSoundReproduction/goldierill_%20voice%E5%8E%9F%E5%A3%B0.wav"  # 请按实际情况进行替换
prefix = 'goldie02'  # 已缩短为8个字符，符合10个字符以内的限制
target_model = "cosyvoice-v1"

# 创建语音注册服务实例
service = VoiceEnrollmentService()

# 调用create_voice方法复刻声音，并生成voice_id
voice_id = service.create_voice(target_model=target_model, prefix=prefix, url=url)
print("requestId: ", service.get_last_request_id())
print(f"your voice id is {voice_id}")

# 使用复刻的声音进行语音合成
synthesizer = SpeechSynthesizer(model=target_model, voice=voice_id)
audio = synthesizer.call("老铁，我跟你讲啊，画画这个事儿呢，靠的就是感觉。你得相信自己的眼睛，看准了，就果断下笔。色调啊、构图啊，咱们别整得太复杂，舒服就行了。兄弟你这次的创作，颜色选的是真的很可以，画面特别干净，一看就有故事。你知道吧，有时候简单点儿反而更难，能抓住人眼睛的，那才叫真本事。这种感觉啊，你一定要保持住，以后绝对越来越稳！")
print("requestId: ", synthesizer.get_last_request_id())

# 将合成的音频文件保存到本地文件
with open("output.mp3", "wb") as f:
    f.write(audio)