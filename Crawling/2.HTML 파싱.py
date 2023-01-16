"""
날짜 : 2023/01/16
이름 : 공민혁
내용 : 파이썬 HTML 파싱 실습
"""
import requests as req
from bs4 import BeautifulSoup as bs

# HTML 요청
url = 'http://chhak.click/parsing/sample1.html'
html = req.get(url).text

print(html)

# 문서객체 생성
dom = bs(html, 'html.parser')

# 문서파싱
tit = dom.html.body.h1.text
desc = dom.select_one('#txt').text
print('tit :', tit)
print('txt :', txt)