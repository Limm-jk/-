import requests
from bs4 import BeautifulSoup

# 지정 url
url = 'https://computer.cnu.ac.kr/computer/notice/project.do'

# url 객체 생성
response = requests.get(url)

#웹 소스코드 추출
html = response.text

print(html)

# #소스코드를 파이썬 객체로 변환
# soup = BeautifulSoup(html, 'html.parser')

# #
