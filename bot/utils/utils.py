from bson.objectid import ObjectId
from io import BytesIO
import base64
from PIL import Image
from motor.motor_asyncio import AsyncIOMotorClient
from admin.settings import MONGO_URL


client = AsyncIOMotorClient(MONGO_URL)
collection = client.test.topic
image_collection = client.test.fs.chunks


async def get_title():
    """Поиск информации в БД названий статей."""
    documents = []
    cursor = await collection.find().to_list(None)
    for document in cursor:
        documents.append(document["title"])
    return (documents)


async def get_information_title(name):
    """Функция поиска информации в БД по теме."""
    document = await collection.find_one({'title': f"{name}"})
    return document


async def search_information(name):
    """Функция поиска информации в БД по введенному слову."""
    a = []
    collection.create_index({'description': "text"})
    x = collection.find({"$text": {"$search": f"{name}"}})
    async for document in x:
        a.append(document['title'])
    return a


async def get_image(id):
    """Функция поиска картинок."""
    document = await image_collection.find_one({"files_id": ObjectId(f'{id}')})
    base64_img = document["data"]
    base64_bytes = base64.b64encode(base64_img)
    im = Image.open(BytesIO(base64.b64decode(base64_bytes)))
    im.save("image.png", 'PNG')
