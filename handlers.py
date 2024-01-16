from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from keyboards import information_keyboard
from test_data import *
from motor.motor_asyncio import AsyncIOMotorClient
client = AsyncIOMotorClient('mongodb://localhost:27017')
collection = client.MongoDB.MongoCollection
router = Router()
user_router = Router()


@user_router.callback_query(F.data == "information",)
async def get_information(callback: CallbackQuery):
    """Получение информации"""
    print(100)
    await callback.message.answer(
        text="Выбирайте тему для получения запроса", reply_markup=information_keyboard()
    )
    print(600)

import asyncio
@user_router.callback_query(F.data == "1",)
async def get_one_information(callback: CallbackQuery):
    """Получение информации"""
    print(101)
    t = {}
    z = await collection.find_one({"author": "author"})
    print(z, 1)
    await callback.message.answer(
        text=f"{z['name']}", 
    )



async def run():
    t = []
    
        #print(doc, 123)
   
   

@user_router.callback_query(F.data == "Inserting information",)
async def inserting_information(callback: CallbackQuery):
    """Получение информации"""
    print(500)
    collection.insert_many(books_data)
    print(464646)
    await callback.message.answer(
        text="Информация добавлена в БД")