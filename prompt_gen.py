import requests
import json
import os

def llamacpp_generate(url, prompt, n_predict=100):
    header = {"Content-Type": "application/json"}
    data = json.dumps({"prompt": prompt, "n_predict": n_predict})
    res = requests.post(url=url, headers=header, data=data)
    return json.loads(res.text)["content"]

url = "http://localhost:8080/completion"
topics_file = open("./topics/topics.txt", "r")
result_file = open("./prompts/demoprompts.txt", "w")
topics = topics_file.read().split("---")
LIMIT_TOKENS = 20

for t in topics:
    res = llamacpp_generate(url, t, LIMIT_TOKENS)
    print(res)
    to_write = t + "\n" + res + "\n---\n"
    result_file.write(to_write)

topics_file.close()
result_file.close()
