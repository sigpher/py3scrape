# import urllib.request as request
# import urllib.parse as parse
# # urllib.request.urlopen(url)的响应是一个'http.client.HTTPResponse'对象，主要包含read，readinto, getheaders, getheader,flieno等方法
# # 以及msg, version,status,reason,debuglevel,closed等属性


# response = request.urlopen('https://www.python.org/')
# # print(respone.read().decode('utf-8'))
# print('charset=utf-8' in response.getheader('Content-Type'))
# headers = response.getheaders()
# for h in headers:
#     print(f'{h[0]}: {h[1]}')
# print(response.status)

# data = bytes(parse.urlencode({'name': 'germy'}), encoding='utf-8')

# response = request.urlopen('https://www.httpbin.org/post', data=data)
# print(response.read().decode('utf-8'))

# choi = {
#     'username': 'choi',
#     'age': 20
# }
# data = bytes(parse.urlencode(choi), encoding='utf-8')
# resp = request.urlopen('https://www.httpbin.org/post', data=data)
# print(resp.read().decode('utf-8'))

# import urllib.request
# import urllib.parse

# url = 'https://www.httpbin.org/post'
# user = {
#     'username': 'choi',
#     'age': 30,
#     'dept': 'qa',
#     'phone': '668880',
# }
# data = bytes(urllib.parse.urlencode(user), encoding='utf-8')

# resp = urllib.request.urlopen(url, data)
# print(resp.read().decode('utf-8'))

# from urllib import request, parse

# user = {
#     "username": "choi",
#     "age": 30,
# }

# url = 'https://httpbin.org/post'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/8',
#     'Host': 'www.httpbin.org',
# }
# data = bytes(parse.urlencode(user), encoding='utf-8')
# req = request.Request(url=url, method='POST', data=data, headers=headers)
# resp = request.urlopen(req)

# print(resp.read().decode('utf-8'))

from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

username = "admin"
password = "admin"

url = 'https://ssr3.scrape.center'

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)

auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)