import os
import dashscope
from dashscope.audio.tts_v2 import VoiceEnrollmentService

# 配置API密钥
dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')  # 如果您没有配置环境变量，请在此处用您的API-KEY进行替换

# 创建语音注册服务实例
service = VoiceEnrollmentService()

# 1. 查询所有音色
print("===== 查询所有音色 =====")
all_voices = service.list_voices()
print(f"请求ID: {service.get_last_request_id()}")
print(f"共找到 {len(all_voices)} 个音色:")
for voice in all_voices:
    print(f"音色ID: {voice['voice_id']}")
    print(f"创建时间: {voice['gmt_create']}")
    print(f"修改时间: {voice['gmt_modified']}")
    print(f"状态: {voice['status']}")
    print("-" * 50)

'''
# 2. 专门查询前缀为"aio"的音色
print("\n===== 查询前缀为aio的音色 =====")
aio_voices = service.list_voices(prefix="aio")
print(f"请求ID: {service.get_last_request_id()}")
print(f"共找到 {len(aio_voices)} 个aio前缀的音色:")
for voice in aio_voices:
    print(f"音色ID: {voice['voice_id']}")
    print(f"创建时间: {voice['gmt_create']}")
    print(f"修改时间: {voice['gmt_modified']}")
    print(f"状态: {voice['status']}")
    print("-" * 50)

# 如果想查询更多页的结果，可以使用page_index和page_size参数
# 例如：第二页，每页10个结果
# more_voices = service.list_voices(page_index=1, page_size=10)
'''
