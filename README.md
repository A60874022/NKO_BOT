# Чат-бот НЖКЦ #

## Описание ##

## Стек технологий ##
+ Python 3.10.10
+ Aiogram
+ Docker

## Установка
Клонировать репозиторий и перейти в него в командной строке:
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
```

Cоздайте и активируйте виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установите зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполните сборку образа:
```
docker build -t backend . 
```

Запустите контейнер (в режиме демона):
```
docker run --name backend_container --rm -p 443:443 -d backend
```

Проверьте состояние контейнера:
```
docker ps
```