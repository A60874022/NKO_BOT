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
TELEGRAM_TOKEN=телеграм_токен_бота
MONGO_HOST=
MONGO_PORT=
LOGLEVEL=(установите уровень логирования)
SECRET=secret
ADMIN=admin_name
PASS=admin_password
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


