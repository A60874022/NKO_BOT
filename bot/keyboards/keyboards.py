from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from bot.lexicon.lexicon import BUTTONS


def start_keyboard():
    """Клавиатура при старте бота."""
    button_1 = InlineKeyboardButton(
        text=BUTTONS["Тема"],
        callback_data="information"
    )
    button_2 = InlineKeyboardButton(
        text=BUTTONS["Поиск слов"],
        callback_data="word_information"
    )
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[button_1],
                         [button_2], ])
    return keyboard


def information_keyboard(documents):
    """Клавиатура инлайн-кнопок  для получения запроса статей."""
    kb_builder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []
    if documents:
        for button in documents:
            buttons.append(InlineKeyboardButton(
                text=f"{button}",
                callback_data=f"{button}"))
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()
