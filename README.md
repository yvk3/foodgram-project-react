
[![.github/workflows/main.yml](https://github.com/yvk3/foodgram-project-react/actions/workflows/main.yml/badge.svg)]
(https://github.com/yvk3/foodgram-project-react/action/workflows/main.yml)
# praktikum_new_diplom - "Продуктовый помощник."

Cайт Foodgram, «Продуктовый помощник». На этом сайте пользователи смогут публиковать рецепты, 
подписываться на публикации других пользователей, добавлять понравившиеся рецепты
в список «Избранное». Перед походом в магазин можно скачать сводный список продуктов для приготовления лбимых блюд.
Взаимодействие с сайтом возможно онлайн и с помощью API.

## Технологии

![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) 
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white) 
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat&logo=Yandex.Cloud&logoColor=56C0C0&color=008080)](https://cloud.yandex.ru/)

- [Python 3.9](https://www.python.org/downloads/)
- [Django 3.2.3](https://www.djangoproject.com/download/)
- [Django REST framework 3.12.4](https://pypi.org/project/djangorestframework/#files)
- [Docker](https://docs.docker.com/)
- [Nginx](https://nginx.org/en/docs/)
- [Gunicorn](https://pypi.org/project/gunicorn/20.1.0/)
- [PostgreSQL](https://www.postgresql.org/docs/)

## Уровни доступа пользователей:
- Гость (неавторизованный пользователь)
- Авторизованный пользователь
- Администратор
## Неавторизованные пользователи могут:
- Создать аккаунт.
- Просматривать рецепты на главной.
- Просматривать отдельные страницы рецептов.
- Просматривать страницы пользователей.
- Фильтровать рецепты по тегам.
## Авторизованные пользователи:
- Входить в систему под своим логином и паролем.
- Выходить из системы.
- Менять свой пароль.
- Создавать/редактировать/удалять собственные рецепты
- Просматривать рецепты на главной.
- Просматривать страницы пользователей.
- Просматривать отдельные страницы рецептов.
- Фильтровать рецепты по тегам.
- Работать с персональным списком избранного: добавлять в него рецепты или удалять их, просматривать свою страницу избранных рецептов.
- Работать с персональным списком покупок: добавлять/удалять любые рецепты, выгружать файл со количеством необходимых ингредиентов для рецептов из списка покупок.
- Подписываться на публикации авторов рецептов и отменять подписку, просматривать свою страницу подписок.

## Установка проекта локально:
***- Клонируйте репозиторий:***
```
git clone git@github.com:yvk3/foodgram-project-react.git
```

***- Установите и активируйте виртуальное окружение:***
- для MacOS/Linux
```
python3 -m venv venv
source env/bin/activate
```
- для Windows
```
python -m venv venv
source venv/Scripts/activate
```

***- Установите зависимости из файла requirements.txt:***
```
python -m pip install --upgrade pip
cd backend
pip install -r requirements.txt
```

***- Примените миграции:***
```
python manage.py migrate
```
***- Загрузка отдельных данных об ингредиентах:***
- загрузка исходной базы ингредиентов из файла формата .csv
```
python manage.py import_data
```
- загрузка исходной базы ингредиентов из файла формата .json
```
python manage.py load_data
```

***- Создание суперпользователя:***
```
python manage.py createsuperuser
```
***- Запуск проекта:***
```
python manage.py runserver
```

### Доступные запросы API:
- ```api/tags/``` - получение, списка тегов (GET);
- ```api/ingredients/``` - получение, списка ингредиентов (GET);
- ```api/ingredients/``` - получение ингредиента с соответствующим id (GET);
- ```api/tags/{id}``` - получение, тега с соответствующим id (GET);
- ```api/recipes/``` - получение списка с рецептами и публикация рецептов
     (GET, POST);
- ```api/recipes/{id}``` - получение, изменение, удаление рецепта с
     соответствующим id (GET, PUT, PATCH, DELETE);
- ```api/recipes/{id}/shopping_cart/``` - добавление рецепта с соответствующим
     id в список покупок и удаление из списка (GET, DELETE);
- ```api/recipes/download_shopping_cart/``` - скачать файл со списком покупок
     shopping_cart.txt (GET);
- ```api/recipes/{id}/favorite/``` - добавление рецепта с соответствующим id в
     список избранного и его удаление (GET, DELETE).
- ```api/users/``` - получение информации о пользователе и регистрация новых
     пользователей (GET, POST);
- ```api/users/{id}/``` - получение информации о пользователе (GET);
- ```api/users/me/``` - получение и изменение данных своей учётной записи.
     Доступна любым авторизованными пользователям (GET);
- ```api/users/set_password/``` - изменение собственного пароля (PATCH);
- ```api/users/{id}/subscribe/``` - подписаться на пользователя с
     соответствующим id или отписаться от него (GET, DELETE);
- ```api/users/subscribe/subscriptions/``` - просмотр пользователей на которых
     подписан текущий пользователь (GET).

### Примеры запросов:

**`POST` | Создание пользователя: `http://127.0.0.1:8000/api/users/`**

Request:
```
{
    "email": "y1@mail.ru",
    "id": 3,
    "username": "y1",
    "first_name": "y1",
    "last_name": "y1"
}
```
***'POST' | Получение токена: 'http://127.0.0.1:8000/api/auth/token/login'***
Request:
```python
{
    "auth_token": "75dc02e6fb349ec4702b7692cff5b8bb3bd6****"
}
```