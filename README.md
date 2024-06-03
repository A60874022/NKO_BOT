# Чат-бот НЖКЦ #

## Описание ##

## Стек технологий ##
+ Python 3.10.10
+ Aiogram
+ Docker

## Установка
Клонируйте репозиторий и перейдите в него в командной строке:
```
git clone git@github.com:chatbotnko/backend.git
```

```
cd backend
```

Создайте env-file:
```python
touch .env
```

Добавьте в env-file данные:
```python
TELEGRAM_TOKEN=123
MONGO_PORT=27017
MONGO_INITDB_ROOT_USERNAME=Anton
MONGO_INITDB_ROOT_PASSWORD=rt105112up0073!
LOGLEVEL=INFO
LOG = False
SECRET=secret
MONGO_HOST=mongodb
```

Cоздайте и активируйте виртуальное окружение:

```
python -m venv venv
```
```
source venv/Scripts/activate
```


Установите зависимости из файла requirements.txt:


```
pip install -r requirements.txt
```

Выполните сборку образа:
```
docker compose up -d --build
```

