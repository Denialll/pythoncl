from aiogram import Router
from aiogram import types, F
from aiogram.types import URLInputFile
from aiogram.utils.media_group import MediaGroupBuilder

from keyboards.file_buttons import get_practises_kb, get_lectures_kb, get_tasks_kb, get_materials_kb
from lectures.dao import LecturesDAO
from materials.dao import MaterialsDAO
from practises.dao import PractisesDAO
from quesions.dao import QuestionsDAO
from tasks.dao import TasksDAO

router = Router()

flags_default = {"throttling_key": "default"}
flags_files = {"throttling_key": "files"}


@router.message(F.text == "Лекции", flags=flags_default)
async def chose_lect(message: types.Message):
    keyboard = await get_lectures_kb()
    await message.answer("Выберите лекцию", reply_markup=keyboard)


@router.message(F.text == "Практики", flags=flags_default)
async def chose_pract(message: types.Message):
    keyboard = await get_practises_kb()
    await message.answer("Выберите практики",
                         reply_markup=keyboard)


@router.message(F.text == "Задания", flags=flags_default)
async def get_pract(message: types.Message):
    keyboard = await get_tasks_kb()
    await message.answer("Выберите задание",
                         reply_markup=keyboard)

@router.message(F.text == "ЧаВо", flags=flags_files)
async def get_faq(message: types.Message):
    result = await QuestionsDAO.find_files(one=False)
    result = list(dict(file) for file in result)
    if len(result) == 0:

        await message.answer("Файл отсутствует!")
    else:
        media_group = MediaGroupBuilder()
        try:
            for file in result:
                document = URLInputFile(
                    file["link"],
                    filename=file["file_name"])
                media_group.add(type="document", media=document)
            await message.answer_media_group(media_group.build())
        except Exception as e:
            print(e)
            await message.answer("Не удалось загрузить файл !")


@router.message(F.text.regexp(r'Лекция \d'), flags=flags_files)
async def get_lect(message: types.Message):
    id = int(message.text.split()[1])
    result = dict(await LecturesDAO.find_files(id=id))
    try:
        file = URLInputFile(
            result["link"],
            filename=result["file_name"])
        await message.answer_document(file)
    except Exception as e:
        print(e)
        await message.answer("Не удалось загрузить файл !")


@router.message(F.text.regexp(r'Практика \d'), flags=flags_files)
async def get_pract(message: types.Message):
    id = int(message.text.split()[1])
    result = dict(await PractisesDAO.find_files(id=id))
    try:
        file = URLInputFile(
            result["link"],
            filename=result["file_name"])
        await message.answer_document(file)
    except Exception as e:
        print(e)
        await message.answer("Не удалось загрузить файл !")


@router.message(F.text.regexp(r'\d_'), flags=flags_files)
async def get_task(message: types.Message):
    id = int(message.text.split("_")[0])
    keyboard = await get_materials_kb(id)
    result = dict(await TasksDAO.find_files(id=id))
    try:
        file = URLInputFile(
            result["link"],
            filename=result["file_name"])
        await message.answer_document(file, reply_markup=keyboard)
    except Exception as e:
        print(e)
        await message.answer("Не удалось загрузить файл !")


@router.message(F.text.regexp(r'Получить материалы:\s\d'), flags=flags_files)
async def get_materials(message: types.Message):
    id = int(message.text.split(":")[1])
    keyboard = await get_materials_kb(id)
    result = await MaterialsDAO.find_files(one=False, task_id=id)
    result = list(dict(file) for file in result)
    if len(result) == 0:
        await message.answer("Для данного задания отсутсвуют материалы.")
    else:
        media_group = MediaGroupBuilder()
        try:
            for file in result:
                document = URLInputFile(
                    file["link"],
                    filename=file["file_name"])
                media_group.add(type="document", media=document)
            await message.answer_media_group(media_group.build(), reply_markup=keyboard)
        except Exception as e:
            print(e)
            await message.answer("Не удалось загрузить файл !")
