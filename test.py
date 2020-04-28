import requests
import os
from bs4 import BeautifulSoup


haksa_url = 'https://computer.cnu.ac.kr/computer/notice/bachelor.do'

title_arr = []
# url 객체 생성
response = requests.get(haksa_url)

#웹 소스코드 추출
html = response.text

# print(html) #소스코드 확인

#소스코드를 파이썬 객체로 변환
soup = BeautifulSoup(html, 'html.parser')

#필요 요소 추출
links = soup.findAll("p", {"class":"b-new"})
# print(type(links))


for link in links:
    # print(type(link.parent))
    entity = link.parent.parent
    print(entity.find("a").text.strip())
    print(entity.find("span",{"class":"b-date"}).text.strip())
    

# links = soup.select('div')

# for link in links:

#     print(type(link))
#     # for ch in link.children:
#     #     print(type(ch))
#     #     print(1)
#     childre = link.findChildren("", {"class":"b-new"})
#     break
# for chil in childre.tr.next_siblings:
#     print(type(chil.parent))