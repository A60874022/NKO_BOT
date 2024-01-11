from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           Message, ReplyKeyboardMarkup, KeyboardButton,
                           ReplyKeyboardRemove)
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('TELEGRAM_TOKEN')

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Создаем объекты кнопок
button_1 = KeyboardButton(text='Тема 1')
button_2 = KeyboardButton(text='Тема 2')
admin_button_1 = KeyboardButton(text='Логика добавления вопроса в кнопку и БД')
admin_button_2 = KeyboardButton(text='Логика добаления ответа в кнопку и БД')

# Создаем объект клавиатуры, добавляя в него кнопки
# keyboard = ReplyKeyboardMarkup(keyboard=[[button_1, button_2]],
#                                resize_keyboard=True,
#                                one_time_keyboard=True)


# # Создаем объект клавиатуры для админа, добавляя в него кнопки
# keyboard_admin = ReplyKeyboardMarkup(keyboard=[[button_1, button_2,
#                                                 admin_button_1,
#                                                 admin_button_2]],
#                                      resize_keyboard=True,
#                                      one_time_keyboard=True)

# Инициализируем билдер
keyboard = ReplyKeyboardBuilder()

# Создаем список с кнопками
buttons: list[KeyboardButton] = [
    button_1, button_2
]

# Распаковываем список с кнопками в билдер, указываем, что
# в одном ряду должно быть 2 кнопки
keyboard.row(*buttons, width=2)


# Инициализируем билдер
keyboard_admin = ReplyKeyboardBuilder()

# Создаем список с кнопками
buttons_admin: list[KeyboardButton] = [
    button_1, button_2, admin_button_1, admin_button_2
]

# Распаковываем список с кнопками в билдер, указываем, что
# в одном ряду должно быть 2 кнопки
keyboard_admin.row(*buttons_admin, width=2)


# # Создаем объекты инлайн-кнопок
# url_button_1 = InlineKeyboardButton(
#     text='Вот здесь какая-то информация',
#     url='https://i.pinimg.com/564x/db/9a/63/db9a6371b5eec52c84d031f291a2dd50.jpg'
# )
# url_button_2 = InlineKeyboardButton(
#     text='И здесь тоже',
#     url='https://i.pinimg.com/564x/4e/16/d2/4e16d2cf75397346dd9c0850dcab67c1.jpg'
# )
# url_button_3 = InlineKeyboardButton(
#     text='Тестим кнопочки',
#     url='https://i.pinimg.com/564x/2b/3b/5e/2b3b5ea7485898de00a588bac15e03ad.jpg'
# )

# # Создаем объект инлайн-клавиатуры
# keyboard = InlineKeyboardMarkup(
#     resize_keybord=True,
#     inline_keyboard=[[url_button_1],
#                      [url_button_2],
#                      [url_button_3]]
# )


# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру c кнопками
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text=(f'{message.from_user.first_name}, привет! \nВы находитесь в '
              f'интерактивной библиотеке материалов Нижегородского женского '
              f'кризисного центра. \n\nЗдесь вы найдете короткие гайды о том, '
              f'как распознать насилие и как помочь человеку, который '
              f'столкнулся c домашним насилием. \n\nВведите интересующую вас '
              f'тему в поле ввода или воспользуйтесь содержанием, чтобы '
              f'найти материал по названию темы.')
    )
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer((f'{message.from_user.first_name}, вы '
                             'авторизовались как администратор'),
                             reply_markup=keyboard_admin.as_markup())
    else:
        await message.answer(reply_markup=keyboard.as_markup())


# Этот хэндлер будет срабатывать на кнопку Тема 1
@dp.message(F.text == 'Тема 1')
async def process_answer_1(message: Message):
    await message.answer(
        text='текст из БД',
    )


# Этот хэндлер будет срабатывать на кнопку Тема 2
@dp.message(F.text == 'Тема 2')
async def process_answer_2(message: Message):
    await message.answer(
        text='текст из БД',
    )


# Этот хэндлер будет срабатывать на админа
@dp.message(F.text == 'Логика добавления вопроса в кнопку и БД')
async def process_admin_1(message: Message):
    await message.answer(
        text='Логика добавления вопроса в кнопку и БД',
    )


# Этот хэндлер будет срабатывать на админа
@dp.message(F.text == 'Логика добаления ответа в кнопку и БД')
async def process_admin_2(message: Message):
    await message.answer(
        text='Логика добавления ответа в кнопку и БД',
    )


if __name__ == '__main__':
    dp.run_polling(bot)
