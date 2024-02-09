import logging

from aiogram import Bot, Dispatcher
import os
from dotenv import load_dotenv
from handlers import user_router


logging.basicConfig(
    filename='program.log', 
    format='%(asctime)s, %(levelname)s, %(message)s, %(name)s'
)
logger = logging.getLogger(__name__)


load_dotenv()
BOT_TOKEN = os.getenv('TELEGRAM_TOKEN')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

dp.include_router(user_router)
if __name__ == '__main__':
    dp.run_polling(bot)
