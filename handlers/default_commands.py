from aiogram import F, types, Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.const_buttons import start_kb

router = Router()
flags = {"throttling_key": "default"}

@router.message(Command("start"), flags=flags)
@router.message(F.text == "Главное меню", flags=flags)
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=start_kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите раздел"
    )
    await message.answer("Воспользуйтесь кнопками", reply_markup=keyboard)


@router.message(Command("help"), flags=flags)
async def cmd_help(message: Message):
    help_text = \
        "Бот предоставляет информацию по предмету 'ЭБНЭ'\n" \
        "Для взаимодействия с ботом используются только кнопки !\n" \
        "Установлены ограничения: 1 сообщение от пользователя в секунду," \
        "а также 1 сообщение на получение файла раз в 5 секунд!\n" \
        "Большие файлы отправляются до 30 секунд."\
        "Что-то не работает ? - /start"
    await message.answer(help_text)
