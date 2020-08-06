## NOTES
현재 local 가상환경에서 실행해 본 파일입니다.<br>
 - 1365 의 공고를 크롤링해서 DB에 저장
 - 127.0.0.1:8000/api/doc 로 접속시 사용 가능한 api 확인할 수 있습니다.
 - 확인 후 사용하세요.
 - **api 호출하실 때는 db column이름을 snake_case 에서 camelCase로 바꿔주세요!**

<br>

돌려보시다가 혹시라도 error 발생하면 해당 부분과 error msg 캡처해서 @sookylee 에게 알려주세요.<br>
감사합니다.


## Before you use..
- pip install django
- pip install requests
- pip install bs4
- pip install selenium
- pip install djangorestframework
- pip install django-rest-swagger
- pip install django-filter

### error 발생 시!
1. 
만약 venv 환경에서 설치 오류시 <br>
```
    'python -m pip install <pkg name>'
```
시도해 보세요.

2. 
api/docs 에서 문제가 발생하면,
```
packages/rest_framework_swagger/templates/rest_framework_swagger/index.html
```
에 들어가서, 두번째 줄의 
```
{% load staticfiles %} 를
{% load static %} 로 바꾸세요.
```

## 공고와 관련된 DB table(model)
* **created_at** : (레코드 저장 시) 생성 시각. 자동으로 값 들어감.
* **site_domain** : 1365인지 vms 인지. 1365면 1, vms면 2 값을 가짐. (다른 사이트가 추가될 것을 대비..) _db_utils.py에 enum 정의되어 있음.
* **regist_no** : 공고 게시글 id
* **url** : 게시글 링크
* **title** : 공고 제목
* **address_city** : 봉사 주소 중 '시/도'에 해당 (ex. 서울특별시, 경기도 등)
* **address_gu** : 봉사 주소 중 '구'에 해당 (ex. 마포구)
* **address_remainder** : 시/도 와 구를 제외한 나머지 주소
* **recruit_status** : 모집중인지 아닌지의 여부. Boolean type. 모집중이면 true이며 default 값은 true임.
* **adult_status**: 성인인지 학생인지의 여부. 성인이면 true, 학생이면 false
* **telephone** : 모집기관 전화번호
* **domain**: 봉사 분야
* **text** = 공고 내용
* **start_date** = 활동 시작일. yyyy-mm-dd 형태.
* **end_date** = 활동 종료일. yyyy-mm-dd 형태.
* **do_date_extra** = 활동 요일/시간 등의 세부 정보
* **recruit_company** = 기관명
* **recurit_member** = 모집 인원 수

## variable type
 - regist_no : big integer
 - site_domain : integer
 - recruit_satus, adult_status: boolean
 - start_date, end_date : django datefield. yyyy-mm-dd.
 - else: String

<br>더 필요하다고 생각되는 내용이 있으면 언제든 말씀해주세요!<br>
 

### MINE
 - AWS 에 chromedriver 설치하기: https://dvpzeekke.tistory.com/1
