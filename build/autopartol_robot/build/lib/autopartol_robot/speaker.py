import rclpy
from rclpy.node import Node
from autopatrol_interfaces.srv import SpeechText

# 导入语音合成库
import espeakng

class Speaker(Node):
    def __init__(self):
        super().__init__('speaker')
        # 创建服务 服务端
        self.speech_server_ = self.create_service(SpeechText, 'speech_text',
                                                   self.speech_text_callback)
        self.speaker_ = espeakng.Speaker()
        self.speaker_.voice = 'zh'
    
    def speech_text_callback(self, request, response):
        self.get_logger().info(f'正在准备朗读{request.text}')
        self.speaker_.say(request.text)
        self.speaker_.wait() # 等待说完
        response.result = True
        return response

def main():
    rclpy.init()
    node = Speaker()
    rclpy.spin(node)
    rclpy.shutdown()