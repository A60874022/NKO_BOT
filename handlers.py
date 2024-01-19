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
    z = await run()
    await callback.message.answer(
        text=f"{z}", 
    )



async def run():
    a = []
    collection.create_index( { 'name': "text"} )
    x = collection.find( { "$text": { "$search": "Hands-On" } })
    async for document in x:
        a.append(document['name'])
    '''async for document in collection.find( { "$text": { "$search": "Python Crash Course" } }):
         a.append(document)'''a      
    return (*a,)
  
  

     

      
  

        
   
   

@user_router.callback_query(F.data == "Inserting information",)
async def inserting_information(callback: CallbackQuery):
    """Получение информации"""
    print(500)
    collection.insert_many(books_data)
    print(464646)
    await callback.message.answer(
        text="Информация добавлена в БД")