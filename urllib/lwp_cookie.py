# @Author ZhangGJ
# @Date 2021/01/24 22:52

import http.cookiejar
import urllib.request

cookie = http.cookiejar.LWPCookieJar()
cookie.load('../resources/cookies_lwp.txt', ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))
