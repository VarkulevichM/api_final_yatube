# api_final_yatube
### Описание: 
API, которое для социальной сети Yatube. Это API позволяет аутентифицированным создавать посты, 
комментировать эти посты и посты других пользователей, просматривать их, удалять и подписываться на других пользователей.

### Как запустить проект:
Клонировать репозиторий:
```
git@github.com:VarkulevichM/api_final_yatube.git
```
Перейти в каталог с проектом в командной строке:
```
cd yatube_api/
```
Cоздать и активировать виртуальное окружение:
(для Windows везде использовать python а не python3)
```
python3 -m venv env 
```
```
source env/bin/activate
```
Обносить pip и установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip 
```
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```

### Примеры запросов
Запрос с помощью **GET** метода на страницу: http://127.0.0.1:8000/api/v1/posts/

    {
        "id": 1,
        "author": "mixail",
        "text": "Текст поста",
        "pub_date": "2022-11-23T12:18:45.772143Z",
        "image": null,
        "group": null
    }
]
Запрос с помощью **POST** метода на страницу: http://127.0.0.1:8000/api/v1/posts/
    
    {
    "text": "Новый текст поста"
    }
    
    {
        "id": 1,
        "author": "mixail",
        "text": "Текст поста номер1 изминил 23.11.2022 19:20",
        "pub_date": "2022-11-23T12:18:45.772143Z",
        "image": null,
        "group": null
    }