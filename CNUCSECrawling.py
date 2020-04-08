import requests
import os
from bs4 import BeautifulSoup

# 지정 url
Saupdan_url = 'https://computer.cnu.ac.kr/computer/notice/project.do'
ilban_url = 'https://computer.cnu.ac.kr/computer/notice/notice.do'
haksa_url = 'https://computer.cnu.ac.kr/computer/notice/bachelor.do'

def crawling(url):
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
        if link.has_attr('href'): # href 속성이 있을때
            if link.get('href').find('articleNo') != -1: # href에서 해당 문자열이 있을경우
                print((link.text).strip())

print('\n***학사공지***\n')
crawling(haksa_url)
print('\n')
print('\n***일반공지***\n')
crawling(ilban_url)
print('\n')
print('\n***사업단공지***\n')
crawling(Saupdan_url)
print('\n')

os.system("pause")