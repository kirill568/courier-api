## Как запустить
1. Установите [docker](https://docs.docker.com/engine/install/)
2. В корне проекта создайте копию файла `.env.example` с именем `.env` и переопределите дефолтные значения, если это необходимо
3. Выполните команду `docker compose build`
4. Выполните команду `docker compose up`
5. Откройте браузер по адресу `http://127.0.0.1:9000`

## Миграции  
1. Чтобы сгенерировать миграцию выполните команду `docker compose exec web poetry run alembic revision --autogenerate -m "migration name"`  
2. Чтобы выполнить миграции запустите команду `docker compose exec web poetry run alembic upgrade head`  

Просмотр базы данных доступен по адресу - `http://127.0.0.1:8080/`  
Документация доступна по адресу - `http://127.0.0.1:9000/docs`