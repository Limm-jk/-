import requests
from bs4 import BeautifulSoup

# 지정 url
url = 'https://computer.cnu.ac.kr/computer/notice/project.do'

# url 객체 생성
response = requests.get(url)

#웹 소스코드 추출
html = response.text

# print(html) #소스코드 확인

#소스코드를 파이썬 객체로 변환
soup = BeautifulSoup(html, 'html.parser')

#필요 요소 추출
links = soup.select('a')

for link in links:
    if link.has_attr('href'):
        if link.get('href').find('article.offset') != -1:
            print((link.text).strip())