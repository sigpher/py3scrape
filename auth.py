# import requests
# from requests.packages import urllib3
# resp = requests.get('https://ssr2.scrape.center/',verify=False)
# urllib3.disable_warnings()
# print(resp.status_code)

import requests

url = 'https://ssr3.scrape.center'
r = requests.get(url,auth=('admin','admin'))
print(r.status_code)
