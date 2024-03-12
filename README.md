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
touch .env.dev
```

Добавьте в env-file данные:
```python
TELEGRAM_TOKEN=телеграм_токен_бота
MONGO_HOST=127.0.0.1
MONGO_PORT=27017

LOGLEVEL=(установите уровень логирования)
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


