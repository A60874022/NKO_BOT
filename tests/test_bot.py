import pytest

from unittest.mock import AsyncMock

from bot.handlers.handlers import process_start_command
from bot.keyboards.keyboards import start_keyboard
from bot.lexicon.lexicon import LEXICON


@pytest.mark.asyncio
async def test_start_handler():
    message = AsyncMock()
    await process_start_command(message)
    message.answer.assert_called_with(text=LEXICON["start"],
                                      reply_markup=start_keyboard())
