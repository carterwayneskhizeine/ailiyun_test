# coding=utf-8
# Installation instructions for pyaudio:
# APPLE Mac OS X
#   brew install portaudio
#   pip install pyaudio
# Debian/Ubuntu
#   sudo apt-get install python-pyaudio python3-pyaudio
#   or
#   pip install pyaudio
# CentOS
#   sudo yum install -y portaudio portaudio-devel && pip install pyaudio
# Microsoft Windows
#   python -m pip install pyaudio
#将LLM生成的文本通过扬声器实时播放（全双工流式合成）
#以下代码展示调用成功后，通过本地设备播放通义千问大语言模型（qwen-turbo）实时返回的文本内容。

import os
import pyaudio
import dashscope
from dashscope.audio.tts_v2 import *


from http import HTTPStatus
from dashscope import Generation

dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')
model = "cosyvoice-v1"
voice = "cosyvoice-goldie02-21b5100d79a34f9c9a1f3798ac75ad3a"


class Callback(ResultCallback):
    _player = None
    _stream = None

    def on_open(self):
        print("websocket is open.")
        self._player = pyaudio.PyAudio()
        self._stream = self._player.open(
            format=pyaudio.paInt16, channels=1, rate=22050, output=True
        )

    def on_complete(self):
        print("speech synthesis task complete successfully.")

    def on_error(self, message: str):
        print(f"speech synthesis task failed, {message}")

    def on_close(self):
        print("websocket is closed.")
        # stop player
        self._stream.stop_stream()
        self._stream.close()
        self._player.terminate()

    def on_event(self, message):
        print(f"recv speech synthesis message {message}")

    def on_data(self, data: bytes) -> None:
        print("audio result length:", len(data))
        self._stream.write(data)


def synthesizer_with_llm():
    callback = Callback()
    synthesizer = SpeechSynthesizer(
        model=model,
        voice=voice,
        format=AudioFormat.PCM_22050HZ_MONO_16BIT,
        callback=callback,
    )

    messages = [{"role": "user", "content": "请介绍一下你自己"}]
    responses = Generation.call(
        model="qwen-turbo",
        messages=messages,
        result_format="message",  # set result format as 'message'
        stream=True,  # enable stream output
        incremental_output=True,  # enable incremental output 
    )
    for response in responses:
        if response.status_code == HTTPStatus.OK:
            print(response.output.choices[0]["message"]["content"], end="")
            synthesizer.streaming_call(response.output.choices[0]["message"]["content"])
        else:
            print(
                "Request id: %s, Status code: %s, error code: %s, error message: %s"
                % (
                    response.request_id,
                    response.status_code,
                    response.code,
                    response.message,
                )
            )
    synthesizer.streaming_complete()
    print('requestId: ', synthesizer.get_last_request_id())


if __name__ == "__main__":
    synthesizer_with_llm()