import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://www.dr-chuck.com/page2.htm'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')


# retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
