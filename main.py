import logging
import asyncio
import os
import pathlib
from config_reader import config
from aiogram import Bot, Dispatcher, types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.dispatcher.filters.callback_data import CallbackData
from aiogram.dispatcher.filters.command import Command
from aiogram.dispatcher.filters import CommandObject

from aiogram.dispatcher.filters.text import Text
from aiogram import F
from aiogram.types import FSInputFile

#Объявление переменных среды
API_TOKEN = config.bot_token.get_secret_value()
ADMIN_PAROL = config.admin_parol.get_secret_value()

# Configure logging
# Initialize bot and dispatcher

from handlers.RegistrationHandlers import RegistrationMainRouter
from handlers.WorkHandlers import WorkMainRouter
from middlwares.AuthorizationDataMiddleware import AuthorizationDataMiddlewareCallback, AuthorizationDataMiddlewareMessage


async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()

    dp.message.outer_middleware(AuthorizationDataMiddlewareMessage())
    dp.callback_query.outer_middleware(AuthorizationDataMiddlewareCallback())

    dp.include_router(RegistrationMainRouter.router)
    dp.include_router(WorkMainRouter.router)
    logging.basicConfig(level=logging.INFO)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())