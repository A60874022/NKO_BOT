from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from keyboards import information_keyboard
from test_data import *
from motor.motor_asyncio import AsyncIOMotorClient
client = AsyncIOMotorClient('mongodb://localhost:27017')
collection = client.MongoDB.MongoCollection
router = Router()
user_router = Router()
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from word_cloud import word_cloud
storage = MemoryStorage()
class Data(StatesGroup):
    """Машина состояний для реализации сценариев диалогов с пользователем."""

    information = State()
   

@user_router.callback_query(F.data == "information",)
async def get_information(callback: CallbackQuery):
    """Получение информации"""
    await callback.message.answer(
        text="Выбирайте тему для получения запроса", reply_markup=information_keyboard()
    )

from aiogram import types
from aiogram.types import FSInputFile

@user_router.callback_query(F.data == "1",)
async def get_one_information(callback: CallbackQuery, state: FSMContext):
    """Вывод запрашиваемой информации """
    await state.set_state(Data.information)
    await callback.message.answer("Введите, что вы хотите найти")
  

@user_router.message(Data.information)
async def process_add_task_name(message: Message, state: FSMContext, bot):
    """Вывод запрашиваемой информации."""
    z = await run(message.text)
    s = " ".join(z)
    file = await word_cloud(s)
    await bot.send_photo(message.chat.id, FSInputFile(file))
    await message.answer(
        text=f"{z}", 
    )
    await state.clear()

      
async def run(name):
    a = []
    collection.create_index( { 'name': "text"} )
    x = collection.find( { "$text": { "$search": f"{name}" } })
    async for document in x:
        a.append(document['name'])
    return (*a,)
  
  
@user_router.callback_query(F.data == "Inserting information",)
async def inserting_information(callback: CallbackQuery):
    """Получение информации"""
    print(500)
    collection.insert_many(books_data)
    print(464646)
    await callback.message.answer(
        text="Информация добавлена в БД")