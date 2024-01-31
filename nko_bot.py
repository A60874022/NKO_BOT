# для проверки инлайнов


from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('TELEGRAM_TOKEN')

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Создаем объекты инлайн-кнопок
url_button_1 = InlineKeyboardButton(
    text='Вот здесь какая-то информация',
    url='https://i.pinimg.com/564x/db/9a/63/db9a6371b5eec52c84d031f291a2dd50.jpg'
)
url_button_2 = InlineKeyboardButton(
    text='И здесь тоже',
    url='https://i.pinimg.com/564x/4e/16/d2/4e16d2cf75397346dd9c0850dcab67c1.jpg'
)
url_button_3 = InlineKeyboardButton(
    text='Тестим кнопочки',
    url='https://i.pinimg.com/564x/2b/3b/5e/2b3b5ea7485898de00a588bac15e03ad.jpg'
)

# Создаем объект инлайн-клавиатуры
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[url_button_1],
                     [url_button_2],
                     [url_button_3]]
)


# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру c url-кнопками
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Это инлайн-кнопки с параметром "url"',
        reply_markup=keyboard
    )


if __name__ == '__main__':
    dp.run_polling(bot)
