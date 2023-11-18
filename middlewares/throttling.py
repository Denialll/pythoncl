from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.dispatcher.flags import get_flag
from aiogram.types import Message
from cachetools import TTLCache
from constsants import THROTTLE_TIME_DEFAULT, THROTTLE_TIME_FILES


class ThrottlingMiddleware(BaseMiddleware):
    caches = {
        "default": TTLCache(maxsize=10_000, ttl=THROTTLE_TIME_DEFAULT),
        "files": TTLCache(maxsize=10_000, ttl=THROTTLE_TIME_FILES)

    }

    def __init__(self, bot):
        self.bot = bot

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any],
    ) -> Any:
        throttling_key = get_flag(data, "throttling_key")
        if throttling_key is not None and throttling_key in self.caches:
            if event.chat.id in self.caches[throttling_key]:
                """if throttling_key == "files":
                    await self.bot.send_message(
                        chat_id=event.chat.id,
                        text=f"Слишком много запросов!\n"
                             f"Повторите попытку через {THROTTLE_TIME_FILES} секунд !"
                    )
                else:
                    await self.bot.send_message(
                        chat_id=event.chat.id,
                        text=f"Слишком много запросов!\n"
                             f"Повторите попытку через {THROTTLE_TIME_DEFAULT} секунду !"
                    )""" #надо сделать антифлуд, как rate_limit в 2 версии aiogram
                return
            else:
                self.caches[throttling_key][event.chat.id] = None
        return await handler(event, data)
