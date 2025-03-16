import os
import dashscope
from dashscope.audio.tts_v2 import SpeechSynthesizer

# 配置API密钥
dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')  # 如果您没有配置环境变量，请在此处用您的API-KEY进行替换

# 使用现有的voice ID
voice_id = "cosyvoice-goldie02-21b5100d79a34f9c9a1f3798ac75ad3a"
target_model = "cosyvoice-v1"

# 创建语音合成器实例
synthesizer = SpeechSynthesizer(model=target_model, voice=voice_id)

# 要合成的文本内容
text_to_synthesize = "老铁，我跟你讲啊，画画这个事儿呢，靠的就是感觉。你得相信自己的眼睛，看准了，就果断下笔。色调啊、构图啊，咱们别整得太复杂，舒服就行了。"

# 调用语音合成
audio = synthesizer.call(text_to_synthesize)
print("请求ID: ", synthesizer.get_last_request_id())

# 将合成的音频文件保存到本地
output_filename = "generated_speech.mp3"
with open(output_filename, "wb") as f:
    f.write(audio)

print(f"语音已生成并保存到文件: {output_filename}") 