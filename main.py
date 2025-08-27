import asyncio

from aiogram import Bot, Dispatcher

import start_handler
import takrorlovchi_handler

bot = Bot("8192599397:AAHfR9y24YitPuutkEvGp6urEKmlYOgmSjI")
dp = Dispatcher()

dp.include_router(start_handler.router)
dp.include_router(takrorlovchi_handler.router)


async def main():
    print("bot ishga tushdi")
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())