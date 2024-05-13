import pytest
import time
import base64
import os

from motor.motor_asyncio import AsyncIOMotorClient


MONGO_HOST = "127.0.0.1"#os.getenv("MONGO_HOST", "localhost")
MONGO_PORT = "27017"#os.getenv("MONGO_PORT", 27017)
MONGO_URL = f"mongodb://{MONGO_HOST}:{MONGO_PORT}/"


@pytest.fixture
async def db():
    """Фикстура соединения приложения с БД."""
    client = AsyncIOMotorClient(MONGO_URL)
    db = client.bd.admin
    yield db
    await db.drop()
    client.close()


@pytest.fixture
async def test_insert():
    """Фикстура для тестирования БД."""
    with open("tests//12.jpg", "rb") as imageFile:
        str = base64.b64encode(imageFile.read())
    return [{"title": "Миша", "description":
             "Миша живет в Saint Petersburg",
             "image": str},
            {"title": "Anton",
             "description": ("Антон приехал в командировку в "
                             "Москву из Новосибирска"),
             "image": str}]


@pytest.mark.asyncio
async def test_get_information_title(db, test_insert):
    """Проверка вывода названия статьи."""
    await db.insert_many(test_insert)
    document = await db.find_one({'title': "Anton"})
    document1 = await db.find_one({'title': "Миша"})
    assert document["title"] == "Anton", "неправильно название"
    assert document1["title"] == "Миша", "неправильно название"


@pytest.mark.asyncio
async def test_get_description(db, test_insert):
    """Проверка вывода статьи."""
    await db.insert_many(test_insert)
    document = await db.find_one({'title': "Anton"})
    assert document["description"] == ("Антон приехал в "
                                       "командировку в Москву из Новосибирска")


@pytest.mark.asyncio
async def test_search_information(test_insert):
    """Проверка поиска статьи по ключевому слову."""
    client = AsyncIOMotorClient(MONGO_URL)
    db = client.bd.admin
    a = []
    await db.insert_many(test_insert)
    db.create_index({'description': "text"})
    time.sleep(1)
    x = db.find({"$text": {"$search": "приехал"}})
    async for document in x:
        a.append(document)
    assert a[0]['description'] == ("Антон приехал в "
                                   "командировку в Москву из Новосибирска")


@pytest.mark.asyncio
async def test_get_image(db, test_insert):
    """Проверка вывода изображения из БД."""
    with open("tests//12.jpg", "rb") as imageFile:
        str = base64.b64encode(imageFile.read())
    await db.insert_many(test_insert)
    document = await db.find_one({'title': "Anton"})
    base64_img = document["image"]
    assert base64_img[:1000] == str[:1000]
