import re
import os
import requests
import json

def get_score(string):
    regex = r"\d+\.\d+|\d+"
    match = re.search(regex, string)
    if match:
        number = match.group()
        return number
    else:
        return 0

def llamacpp_generate(url, prompt):
    header = {"Content-Type": "application/json"}
    data = json.dumps({"prompt": prompt})
    res = requests.post(url=url, headers=header, data=data)
    return json.loads(res.text)["content"]

url = "http://localhost:8080/completion"
metaprompt = open("./metaprompts/eval_text_100.txt", "r").read()
prompt = open("./prompts/sum_two_numbers.txt", "r").read()
raw_result_file = open("./scores/raw/demo.txt", "w")

prompts = prompt.split("---\n")

for p in prompts:
    final_prompt = metaprompt.format(content=p)
    print(final_prompt, end="")
    res = llamacpp_generate(url, final_prompt)
    score = get_score(res)
    print(score)
    to_write = final_prompt + str(score) + "---\n"
    print("......................")
    raw_result_file.write(to_write)

raw_result_file.close()
