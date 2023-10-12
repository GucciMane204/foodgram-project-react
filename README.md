# Foodgram - инновационная социальная сеть для гурманов

![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)


## О проекте
Этот проект был создан в рамках образовательной программы и представляет собой инновационную социальную сеть для обмена рецептами между гурманами. Здесь вы найдете рецепты, которые вдохновят вас на приготовление новых блюд, а также возможность делиться своими кулинарными шедеврами с другими.


### Возможности
- Регистрация и аутентификация пользователей.
- Создание, редактирование и удаление собственных рецептов.
- Поиск рецептов по различным критериям.
- Подписка на других пользователей и просмотр их рецептов.
- Создание списков продуктов для покупки.
- Возможность скачать списки продуктов в удобном формате.


## Технологии
В проекте используются следующие технологии:

 - Python 3.9
 - Django 3.2.3
 - Django REST framework 3.12.4
 - JavaScript
 - Nginx
 - Gunicorn
 - Docker
 - PostgreSQL


## Запуск из Docker-контейнеров
Для запуска проекта из контейнеров Docker выполните следующие шаги:

1. Создайте папку для проекта:

sudo mkdir foodgram-project-react

2. Перейдите в созданную папку:

cd foodgram-project-react

3. Сохраните файл `docker-compose.production.yml` в эту папку.

4. Запустите контейнеры:

sudo docker-compose -f docker-compose.production.yml up

Это приведет к скачиванию образов, распаковке и запуску контейнеров.


## Запуск проекта из исходных кодов на GitHub

Если вы хотите запустить проект из исходных кодов на GitHub, выполните следующие действия:

1. Клонируйте репозиторий:

git clone git@github.com:GucciMane204/foodgram-project-react.git

2. Запустите проект:

sudo docker-compose -f docker-compose.yml up


## После запуска

После успешного запуска проекта выполните следующие шаги:

1. Примените миграции:

sudo docker-compose -f docker-compose.production.yml exec backend python manage.py makemigrations recipes
sudo docker-compose -f docker-compose.production.yml exec backend python manage.py makemigrations users
sudo docker-compose -f docker-compose.production.yml exec backend python manage.py migrate


2. Соберите и скопируйте статику проекта:

sudo docker-compose -f docker-compose.production.yml exec backend python manage.py collectstatic
sudo docker-compose -f docker-compose.production.yml exec backend cp -r /app/collected_static/. /collected_static


3. Загрузите базу данных ингредиентов:

sudo docker-compose -f docker-compose.production.yml exec backend python manage.py load_ingredients


## Остановка проекта

Чтобы остановить проект, выполните следующие действия:

1. Завершите работу в консоли, удерживая клавиши Ctrl+C.

2. Или в другом окне терминала выполните:

sudo docker-compose -f docker-compose.yml down


Проект временно доступен по адресу: https://foodgram204.sytes.net/


## Автор
Алексей Коринтели
GitHub: [GucciMane204](https://github.com/GucciMane204)
