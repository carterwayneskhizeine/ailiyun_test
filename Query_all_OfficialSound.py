from typing import List
import os
import dashscope
from dashscope.audio.tts_v2 import VoiceEnrollmentService

# 配置API密钥
dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')

def query_official_voices():
    """查询官方音色列表"""
    print("===== 查询官方音色列表 =====")
    
    # 创建语音服务实例
    service = VoiceEnrollmentService()
    
    # 查询所有官方音色
    try:
        voices = service.list_voices()
        print(f"\n共找到 {len(voices)} 个官方音色:")
        
        # 打印每个音色的详细信息
        for voice in voices:
            print(f"\n音色ID: {voice.get('voice_id', 'N/A')}")
            print(f"音色名称: {voice.get('name', 'N/A')}")
            print(f"音色类型: {voice.get('type', 'N/A')}")
            print(f"语言: {voice.get('language', 'N/A')}")
            print(f"性别: {voice.get('gender', 'N/A')}")
            print("-" * 50)
            
    except Exception as e:
        print(f"查询失败: {str(e)}")

if __name__ == "__main__":
    query_official_voices()