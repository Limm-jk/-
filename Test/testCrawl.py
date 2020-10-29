import pytest

import os
import requests
from bs4 import BeautifulSoup

# 상위 경로 설정
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Crawling import CNUCSECrawling as crw

# 연결확인 200 -> 정상연결 code
def test_connect():
    res = requests.get('https://computer.cnu.ac.kr')
    bs = BeautifulSoup(res.text, 'html.parser')
    assert res.status_code == 200


def test_CSE_title():
    # 검색어 '5기 글로벌 SW인재트랙 선발 공지' URL
    res = crw.title_crawling('https://computer.cnu.ac.kr/computer/notice/project.do?mode=list&srSearchKey=&srSearchVal=5%EA%B8%B0+%EA%B8%80%EB%A1%9C%EB%B2%8C+SW%EC%9D%B8%EC%9E%AC%ED%8A%B8%EB%9E%99+%EC%84%A0%EB%B0%9C+%EA%B3%B5%EC%A7%80')
    assert res[0] == '[SW중심대학] 5기 글로벌 SW인재트랙 선발 공지'

if __name__ == '__main__':
    pytest.main()
