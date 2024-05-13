import logging
from logging.handlers import RotatingFileHandler
from aiogram import Bot, Dispatcher
import os
from dotenv import load_dotenv
from bot.handlers.handlers import user_router

#LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()


rotating_handler = RotatingFileHandler(
        filename="program.log",
        maxBytes=50000000,
        backupCount=3,
        encoding="utf-8",
    )
logging.basicConfig(
    #level = LOGLEVEL,
    format='%(asctime)s, %(levelname)s, %(message)s, %(name)s',
    handlers=[rotating_handler],
)

logger = logging.getLogger(__name__)


load_dotenv()
BOT_TOKEN = os.getenv('TELEGRAM_TOKEN')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

dp.include_router(user_router)
if __name__ == '__main__':
    dp.run_polling(bot)
