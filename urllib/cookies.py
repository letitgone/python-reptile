# @Author ZhangGJ
# @Date 2021/01/24 22:40

import http.cookiejar, urllib.request

filename = '../resources/cookies_lwp.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name + "=" + item.value)
cookie.save(ignore_discard=True, ignore_expires=True)
