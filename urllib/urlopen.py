# @Author ZhangGJ
# @Date 2021/01/24 10:06

import urllib.request

response = urllib.request.urlopen('http://www.python.org')
print(type(response))
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))
