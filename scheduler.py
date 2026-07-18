import json
import requests
import os

class MangaScheduler:
    def __init__(self, workflow_path="workflow_api.json"):
        with open(workflow_path, 'r') as f:
            self.workflow = json.load(f)

    def update_prompt(self, positive_prompt, image_path):
        # 假设 node 6 是文本输入, node 10 是图片路径
        self.workflow["6"]["inputs"]["text"] = positive_prompt
        self.workflow["10"]["inputs"]["image"] = image_path
        return self.workflow

    def send_to_comfy(self, workflow):
        p = {"prompt": workflow}
        requests.post("http://127.0.0.1:8188/prompt", json=p)
        print("任务已提交至渲染队列")
