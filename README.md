# Спринт 9 - Проект «API для Yatube»

## Описание

__Yatube__ - это социальная сеть, предназначеная для публикации постов.

__Зарегистрированные пользователи__ социальной сети имеют право публиковать собственные записи, подписываться и отписываться от других пользователей, а также комментировать записи авторов.

__Незарегистрированные пользователи__ могут только просматривать посты. Комментирование, подписки для них закрыты.

## Использемые программы

* Python 3.11,
* Django 4.2,

## Запуск проекта в dev-режиме

- Клонировать репозиторий на рабочий компьютер.
- Установить и активировать виртуальное окружение c учетом версии Python 3.7 (выбираем python не ниже 3.7):

#### Команда для Windows:
```
python -m venv venv
```
```bash
source venv/Scripts/activate
```

#### Команда для Linux и macOS:
```
python3 -m venv venv
```
```bash
source venv/bin/activate
```

- Затем нужно установить зависимости из файла requirements.txt

```bash
cd yatube_api
```

```bash
pip install -r requirements.txt
```

- Выполнить миграции:

```bash
python manage.py migrate
```

- Создать суперпользователя:

```bash
python manage.py createsuperuser
```

- Запустить проект:

```bash
python manage.py runserver
```

## Примеры работы с API для всех пользователей

Для неавторизованных пользователей работа с API доступна в режиме чтения, что-либо изменить или создать не получится.

```r
GET api/v1/posts/ - получить список всех публикаций.
При указании параметров limit и offset выдача должна работать с пагинацией
GET api/v1/posts/{id}/ - получение публикации по id
GET api/v1/groups/ - получение списка доступных сообществ
GET api/v1/groups/{id}/ - получение информации о сообществе по id
GET api/v1/{post_id}/comments/ - получение всех комментариев к публикации
GET api/v1/{post_id}/comments/{id}/ - Получение комментария к публикации по id
```

## Примеры работы с API для авторизованных пользователей

- Для создания публикации используем:

```r
POST /api/v1/posts/
```

в body

```json
{
"text": "string",
"image": "string",
"group": 0
}
```

- Обновление публикации:

```r
PUT /api/v1/posts/{id}/
```

в body

```json
{
"text": "string",
"image": "string",
"group": 0
}
```

- Частичное обновление публикации:

```r
PATCH /api/v1/posts/{id}/
```

в body

```json
{
"text": "string",
"image": "string",
"group": 0
}
```

- Частичное обновление публикации:

```r
DEL /api/v1/posts/{id}/
```

Получение доступа к эндпоинту /api/v1/follow/ (подписки) доступен только для авторизованных пользователей.

подписка пользователя от имени которого сделан запрос на пользователя переданного в теле запроса. Анонимные запросы запрещены.

```r
GET /api/v1/follow/
```

- Авторизованные пользователи могут создавать посты, комментировать их и подписываться на других пользователей.
- Пользователи могут изменять(удалять) контент, автором которого они являются.

## Добавить группу в проект нужно через админ панель Django:

после авторизации, переходим в раздел Groups и создаем группы.

```r
admin/
```

- Доступ авторизованным пользователем доступен по JWT-токену (Joser), который можно получить выполнив POST запрос по адресу:

```r
POST /api/v1/jwt/create/
```

- Передав в body данные пользователя (например в postman):

```json
{
"username": "string",
"password": "string"
}
```

- Полученный токен добавляем в headers (postman), после чего буду доступны все функции проекта:

```r
Authorization: Bearer {your_token}
```

- Обновить JWT-токен:

```r
POST /api/v1/jwt/refresh/
```

- Проверить JWT-токен:

```r
POST /api/v1/jwt/verify/
```

- Так же в проекте API реализована пагинация (LimitOffsetPagination):

```r
GET /api/v1/posts/?limit=5&offset=0
```
