import os
import httpx
from openai import OpenAI
from content import USER_QUERY  # 导入问题文本变量

def stream_chat():
    # 创建一个自定义的httpx客户端，禁用SSL验证（仅用于测试环境）
    http_client = httpx.Client(verify=False)
    
    # 初始化OpenAI客户端，使用环境变量中的API密钥
    client = OpenAI(
        api_key=os.getenv("DASHSCOPE_API_KEY"),  # 从环境变量获取API Key
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",  # 阿里云DashScope兼容OpenAI的base_url
        http_client=http_client,  # 使用自定义的HTTP客户端
    )
    
    # 创建流式聊天完成请求
    stream = client.chat.completions.create(
        model="qwen-turbo-latest",  # 指定使用qwen-plus模型
        messages=[
            {"role": "system", "content": "你是一个有帮助的助手。"},
            {"role": "user", "content": USER_QUERY}  # 使用导入的变量
        ],
        stream=True  # 启用流式输出
    )
    
    # 处理流式响应
    print("开始接收流式回复：")
    full_response = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            print(content, end="", flush=True)
            full_response += content
    
    print("\n\n完整回复：")
    print(full_response)

if __name__ == "__main__":
    # 显示警告信息，提醒用户禁用SSL验证仅用于测试
    import warnings
    warnings.filterwarnings("ignore", message=".*Unverified HTTPS request.*")
    print("注意：当前脚本禁用了SSL验证，仅用于测试环境，不建议在生产环境中使用。")
    
    stream_chat()


