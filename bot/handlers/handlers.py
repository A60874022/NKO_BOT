import logging
import os

from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from aiogram.filters import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import FSInputFile

from bot.keyboards.keyboards import (information_keyboard,
                                     start_keyboard,
                                     back_keyboard)
from bot.lexicon.lexicon import LEXICON
from bot.utils.utils import (get_title,
                             get_information_title,
                             search_information,
                             get_image)

logger = logging.getLogger(__name__)

router = Router()
user_router = Router()
storage = MemoryStorage()


class Data(StatesGroup):
    """Машина состояний для реализации сценариев диалогов с пользователем."""

    information = State()
    title = State()


@user_router.message(CommandStart())
async def process_start_command(message: Message):
    """Получение тем из БД."""
    await message.answer(
        text=LEXICON["start"],
        reply_markup=start_keyboard()
    )


@user_router.callback_query(F.data == "information",)
async def get_title_db(callback: CallbackQuery, state: FSMContext):
    """Получение тем из БД."""
    try:
        documents = await get_title()
        if not documents:
            await callback.message.answer(
                    LEXICON["Нет информации"],
                )
            await state.clear()
            return
        await state.set_state(Data.title)
        await callback.message.answer(
            text=LEXICON["Тема"],
            reply_markup=information_keyboard(documents))
    except Exception as err:
        logger.error(f"Ошибка при получении информации из БД: {err}")
        await state.clear()


@user_router.callback_query(Data.title)
async def get_information(callback: CallbackQuery, state: FSMContext, bot):
    """Вывод запрашиваемой информации."""
    try:
        information_title = await get_information_title(callback.data)
        description = information_title.get('description', False)
        if not (information_title and description):
            await callback.message.answer(
                    LEXICON["Нет информации по теме"],
                )
            await state.clear()
            await callback.message.answer(LEXICON["Назад"],
                                          reply_markup=start_keyboard())
        file_id = information_title.get('image', False)
        if file_id:
            await get_image(file_id)
            file = "image.png"
            await callback.bot.send_photo(callback.message.chat.id,
                                          FSInputFile(file))
            os.remove("image.png")
        await callback.message.answer(f"{description}",
                                      reply_markup=back_keyboard(),)
    except Exception as err:
        logger.error(f"Ошибка при получении информации из БД: {err}")
    finally:
        await state.clear()


@user_router.callback_query(F.data == "word_information",)
async def get_one_information(callback: CallbackQuery, state: FSMContext):
    """Поиск информации по словам."""
    await state.set_state(Data.information)
    await callback.message.answer(LEXICON["Введите слово"])


@user_router.message(Data.information)
async def process_team_name(message: Message, state: FSMContext):
    """Обрабатывает введенное слово пользователем."""
    try:
        word = await search_information(message.text)
        if not word:
            await message.answer(
                    LEXICON["Слово отсутствует"],
                )
            await state.clear()
            await message.answer(LEXICON["Назад"],
                                 reply_markup=start_keyboard())
            return
        await state.set_state(Data.title)
        await message.answer(LEXICON["Тема"],
                             reply_markup=information_keyboard(word),)
    except Exception as err:
        logger.error(f"Ошибка при получении информации из БД: {err}")
        await state.clear()


@user_router.callback_query(F.data == "back",)
async def process_back_command(callback: CallbackQuery):
    """Воврат в главное меню"""
    await callback.message.answer(LEXICON["Назад"],
                                  reply_markup=start_keyboard())
