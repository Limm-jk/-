# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-04-09 13:37:25
#  * @modify date 2020-04-09 13:37:25
#  * @desc [충남대학교 컴퓨터공학과 공지 크롤러 '이제누가공지해주냐']
#  */
import requests
import os
from bs4 import BeautifulSoup

# 지정 url
Saupdan_url = 'https://computer.cnu.ac.kr/computer/notice/project.do'
ilban_url = 'https://computer.cnu.ac.kr/computer/notice/notice.do'
haksa_url = 'https://computer.cnu.ac.kr/computer/notice/bachelor.do'

def date_crawl(url):
    date_arr = []
    # url 객체 생성
    response = requests.get(url)

    #웹 소스코드 추출
    html = response.text

    # print(html) #소스코드 확인

    #소스코드를 파이썬 객체로 변환
    soup = BeautifulSoup(html, 'html.parser')

    nameList = soup.findAll("span", {"class":"b-date"})

    for name in nameList:
        date_arr.append(name.get_text().strip())

    return date_arr
      
    
def title_crawling(url):
    title_arr = []
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
                title_arr.append((link.text).strip())
                # print((link.text).strip())

    return title_arr


def crawling2(url):
    title_arr = title_crawling(url)
    date_arr = date_crawl(url)
    for i in range(len(title_arr)):
        print(title_arr[i])
        print("->업데이트 날짜 : ",date_arr[i])

def crawling(url):
    arr = []
    # url 객체 생성
    response = requests.get(url)

    #웹 소스코드 추출
    html = response.text

    # print(html) #소스코드 확인

    #소스코드를 파이썬 객체로 변환
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.findAll('div', {"class":"b-title-box"})

    for link in links:
        arr.append([link.find("a").text.strip(), link.find("span",{"class":"b-date"}).text.strip()])
    for i in range(len(arr)):
        print(arr[i][0])
        print("->업데이트 날짜 : ",arr[i][1])


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