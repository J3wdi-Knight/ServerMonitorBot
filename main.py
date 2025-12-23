import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from handlers import start, status

async def main():
    # Turn up the logging of events
    logging.basicConfig(level=logging.INFO)
    # Dispather
    bot = Bot(token='6755764250:AAGj9ratxPWFo52FHcHmqs2RT3qSlA-5QTk')
    dp = Dispatcher()

    dp.include_routers(start.router, status.router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
