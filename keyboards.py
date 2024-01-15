from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


def information_keyboard() -> InlineKeyboardMarkup:
    """Создаем объекты инлайн-кнопок для получения запроса"""
    one_information = InlineKeyboardButton(
        text="one_information", callback_data="1"
    )
    two_information = InlineKeyboardButton(
        text="two_information", callback_data="2"
    )
    three_information = InlineKeyboardButton(
        text="three_information", callback_data="3"
    )
    four_information = InlineKeyboardButton(
        text="four_information", callback_data="4")
    five_information = InlineKeyboardButton(
        text="five_information", callback_data="5")
    # Создаем объект инлайн-клавиатуры
    information_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
       inline_keyboard=[[one_information],
                        [two_information],
                        [three_information],
                        [four_information],
                        [five_information],
                        ]
)
    return information_keyboard