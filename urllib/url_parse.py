# @Author ZhangGJ
# @Date 2021/01/24 23:10

from urllib.parse import urlparse

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result)
