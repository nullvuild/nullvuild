# App 만들기
1. python manage.py startapp ***앱이름
2. setting.py > INSTALLED_APPS에 추가


# Django 서버 시작
1. 서버 시작
python manage.py runserver


# DE 변경
1. 장고 ORM을 사용하여 DB 테이블 만들기
python manage.py makemigrations **앱이름

2. 마이그레이션 파일 생성 (make migrations)
python manage.py migrate

# DB 내 슈퍼계정 만들기
python manage.py createsuperuser

# DB 테이블 변경
일단.. db.qlite3를 삭제하고 다시하는 게 가장 빠름


# Rule
[NV-00001] 여기에 추가하고, setting.py에 추가하면 이 함수는 계속 실행됨
[NV-00002] 이 경로를 만들어주면 각 앱에서 teamplate 하위 경로로 찾아감