import json
import requests
import os

# scheduler.py 中的修改
class MangaScheduler:
    def __init__(self, workflow_path="workflow_api.json", comfy_url="http://你的渲染服务器地址:8188"):
        self.comfy_url = comfy_url
        with open(workflow_path, 'r') as f:
            self.workflow = json.load(f)
    
    def send_to_comfy(self, workflow):
        # 这里的 URL 改为云端渲染节点的 API 地址
        response = requests.post(f"{self.comfy_url}/prompt", json={"prompt": workflow})
        return response.json()
