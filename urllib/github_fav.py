# @Author ZhangGJ
# @Date 2021/01/25 23:04

import requests

r = requests.get("https://github.com/favicon.ico")
print(r.text)
print(r.content)

with open('../resources/favicon.ico', 'wb') as f:
    f.write(r.content)
