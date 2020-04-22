# Falcon-simple-API
First project on Falcon

1. Установка
pip install peewee falcon gunicorn(Linux)|waitress(Windows) bzt(Visual C++ 14.0 requires http://go.microsoft.com/fwlink/?LinkId=691126&fixForIE=.exe.)

2. Создаем в PostgreSQL БД orgdb и пользователя orguser
Создадим таблицы
python
from app import *
init_tables()
generate_users(50)

Проверяем работу api по http://localhost:8000/users
(Linux) gunicorn app:api -b 0.0.0.0:8000 | (Windows) waitress-serve --listen=*:8000 app:api

3. Тестируем api
$ bzt bzt-config.yml -report
В консоли выводится Taurus, a -report открывает в браузере вкладку с отчетом в BlazeMeter
