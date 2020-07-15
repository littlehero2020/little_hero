현재 local 가상환경에서 실행해 본 파일입니다.<br>
**api 호출하실 때는 db column이름을 snake_case 에서 camelCase로 바꿔주세요!**<br>

## Before you use..
- pip install django
- pip install requests
- pip install bs4
- pip install djangorestframework
- pip install rest-framework-swagger
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

<br>더 필요하다고 생각되는 내용이 있으면 언제든 SLACK ME!.



___
## To Do
 1. **해결!** ~~현재까지 완성된 크롤러는 1365 홈의 1번 페이지만 긁어오도록 되어 있음. 모든 페이지를 긁어오도록 수정해야 함.~~
 2. **해결!!** ~~http connection을 비롯한 error handling 필요. 하나도 안되어있음..ㅎ...~~
 3. 공고 상세 내용에 img 있는 건 어떻게 할건지 합의 후 해결하기,,
 4. 지도 api?
 5. AWS에 환경 설치해야 함. django는 Apache 쓴다던데 그것도 더 찾아봐야 함...
 6. do_date 수정해야하나? string 대신 date form 이 필요하지 않나.. 프론트에서 호출하는 거 고려하면?
 7. domain도 저장된거 보면 기타 > 기타 이런 형식으로 저장되어 있는데 컬럼을 두개로 나눠야 하지 않나?
 
