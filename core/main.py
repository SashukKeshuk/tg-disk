import asyncio
from aiogram import Bot, Dispatcher
from handlers import launch
from config import TKN

async def on_startup(_):
	print('bot online')

async def main():
    bot = Bot(token=TKN)
    dp = Dispatcher()

    dp.include_router(launch.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, skip_updates=True, on_startup=on_startup)


if __name__ == "__main__":
    asyncio.run(main())