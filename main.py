import asyncio
import logging
from middlewares.throttling import ThrottlingMiddleware
from aiogram import Bot, Dispatcher, F

from config import settings
from handlers import default_commands, user
from ui_commands import set_bot_commands

logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.BOT_TOKEN)

dp = Dispatcher()

dp.include_router(default_commands.router)
dp.include_router(user.router)

dp.message.middleware(ThrottlingMiddleware(bot))
dp.message.filter(F.chat.type == "private")


async def main():
    await dp.start_polling(bot)
    await set_bot_commands(bot)

if __name__ == "__main__":
    asyncio.run(main())
