from aiogram import types

from lectures.dao import LecturesDAO
from practises.dao import PractisesDAO
from tasks.dao import TasksDAO


async def get_lectures_kb():
    result = await LecturesDAO.find_all()
    result = [dict(i) for i in list(result)]
    buttons = [[
        types.KeyboardButton(
            text=f"Лекция {lect_dict['id']}"
        )] for lect_dict in result
    ]
    buttons.append([types.KeyboardButton(
        text="Главное меню"
    )])
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        input_field_placeholder="Выберите лекцию"
    )
    return keyboard


async def get_practises_kb():
    result = await PractisesDAO.find_all()
    result = [dict(i) for i in list(result)]
    buttons = [[
        types.KeyboardButton(
            text=f"Практика {pr_dict['id']}"
        )] for pr_dict in result
    ]
    buttons.append([types.KeyboardButton(
        text="Главное меню"
    )])
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        input_field_placeholder="Выберите практику"
    )
    return keyboard


async def get_tasks_kb():
    result = await TasksDAO.find_all()
    result = [dict(i) for i in list(result)]
    buttons = [[
        types.KeyboardButton(
            text=f"{task_dict['file_name'].split('-')[0]}"
        )] for task_dict in result
    ]
    buttons.append([types.KeyboardButton(
        text="Главное меню"
    )])
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        input_field_placeholder="Задания отсортированы по делайну. Выберите задание."
    )
    return keyboard


async def get_materials_kb(num: int):
    buttons = [
        [types.KeyboardButton(
            text=f"Получить материалы: {num}"
        )],
        [types.KeyboardButton(
            text="Задания"
        )],
        [types.KeyboardButton(
            text="Главное меню"
        )]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        input_field_placeholder="Выберите задание."
    )
    return keyboard
