def getcookies():
    cookies_str = ''
    with open('cookies.data') as fp:
        cookies_str = fp.read()
    return cookies_str
