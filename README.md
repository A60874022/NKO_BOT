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



Шаги добавления тапа (tap) MongoDB. 
Откройте терминал и выполните следующие команды:

brew tap mongodb/brew
brew install mongodb-community

Эти команды добавят тап MongoDB и установят MongoDB Community Edition на вашем macOS. 


для указания корректного пути бд:

mongod --dbpath /Users/Maria/Dev/backend/data/db


запустим консольную оболочку:

mongosh 

и введем там следующую команду:

use Bot_db


uvicorn admin_main:app --reload

Откройте файл view.py, который расположен по следующему пути: /Users/Maria/Dev/admin-starlette/venv/lib/python3.10/site-packages/starlette_admin/contrib/odmantic/converters.py.

Найдите следующую строку:

python
Copy code
"type": type.pydantic_field.annotation,


"type": type.pydantic_field.outer_type_,