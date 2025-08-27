import asyncio

from aiogram import Bot, Dispatcher

bot = Bot("8192599397:AAHfR9y24YitPuutkEvGp6urEKmlYOgmSjI")
dp = Dispatcher()


async def main():
    print("bot ishga tushdi")
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())