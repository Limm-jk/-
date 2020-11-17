## 충남대 컴공과 공지사항 크롤러
그저 공지보다가 매일보기 귀찮아서 만들었습니다 ㅎㅎㅎㅎ

### Require
>python 3.7  
request 2.22.0  
beautifulsoup 4.9.0 #소스코드 객체변환  
PyInstaller 3.6 #실행파일

### Command
```
# 실행파일 명령어
pyinstaller --icon=comp_icon.ico --onefile .\Crawling\CNUCSECrawling.py

# Testing
pytest .
```

### Update
20.04.09 Ver 1.0
> 크롤러 생성  
new tag 붙은 글 따로 보여주기

20.10.27 ~ ing
> 공지 이메일 전송기 생성중

20.11.17
> 취업정보 게시판 추가
