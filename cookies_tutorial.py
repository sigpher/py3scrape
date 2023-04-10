import requests

cookies = '''_octo=GH1.1.1397640270.1679764315; _device_id=7caca11af03032c968d7226a0f156008; user_session=LuODIx5lQbUSr-YrIiAhyJjKlIkU91g8pbhAhI3Fp4MsngFT; __Host-user_session_same_site=LuODIx5lQbUSr-YrIiAhyJjKlIkU91g8pbhAhI3Fp4MsngFT; logged_in=yes; dotcom_user=sigpher; has_recent_activity=1; color_mode={"color_mode":"auto","light_theme":{"name":"light","color_mode":"light"},"dark_theme":{"name":"dark","color_mode":"dark"}}; preferred_color_mode=light; tz=Asia/Shanghai; _gh_sess=eYtDpIxIs5V/bjKDNaEsYSxSCnPumursUpvXKAXEIpxENGGPEX0W/Vo/Dj2cjMbSSv18n9s4nd1QVHDp2svAvyGrdCKlpldOAmmwsUN930WsyRv8OZcnaoeyE69g8/gQ/fAsj4T3mg4i0ZMogxh49sxcFfHyAMv1cciovzfDnIC47nl1uj7UbKp7WK731Jd/A1aDgKdgqKw6K456Jyi82v1hWXuhzgGDVLO4YxxjHjOV4xZIl5GiWzB9JY9KDAWa3NdGZHaChbckH1iqfbSnW25VLuaonO2iWoMTLOh68J/7YmKc3rdZplU=--svK05+WDN9sK1ksN--7x84LiRTNpAEYzoZXgQwpw=='''
jar = requests.cookies.RequestsCookieJar()
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
for cookie in cookies.split(";"):
    key, value = cookie.split("=", 1)
    jar.set(key, value)

r = requests.get('https://github.com/', cookies=jar, headers=headers)
print(r.text)