import logging

from aiogram import Router, types
from aiogram.utils.callback_answer import CallbackQuery
from datetime import datetime
import re
from .keyboards import get_points_keyboard
from ..config import MAX_POINTS, POINTS_INCREMENT

router = Router()

user_points = {}

@router.message(lambda message: message.text == "/start")
async def statr_message(message: types.Message):
    logging.info("Команда start получена")
    user_id = message.from_user.id
    if user_id not in user_points:
        user_points[user_id] = 0
    await message.reply("Здравствуйте, укажите ваш год рождения.")

@router.message()
async def check_age(message: types.Message):
    pattern = r'(\d{4})\s*(?:родился|рождения|г\.р\.|года|году|г\.|в)\s*'
    match = re.search(pattern, message.text, re.IGNORECASE)

    if match:
        birth_year = int(match.group(1))
        current_year = datetime.now().year
        age = current_year - birth_year

        if age >= 18:
            await message.reply(f"Ваш возраст: {age} лет.", reply_markup=get_points_keyboard())
        else:
            await message.reply("Вы еще несовершеннолетний!")
    else:
        await message.reply(
            "Не удалось определить ваш год рождения. Пожалуйста, укажите его в формате: 'Я родился в 2000 г.' или 'Мой год рождения: 2000'.")

@router.callback_query(lambda callback_query: callback_query.data.startswith("add_points"))
async def add_points(callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    if user_id not in user_points:
        user_points[user_id] = 0

    if user_points[user_id] < MAX_POINTS:
        user_points[user_id] += POINTS_INCREMENT
        await callback_query.message.edit_text(f"У вас {user_points[user_id]} баллов", reply_markup=get_points_keyboard())
    else:
        await callback_query.answer("Вы достигли максимального количества баллов", show_alert=True)

@router.callback_query(lambda callback_query: callback_query.data.startswith("subtract_points"))
async def subtrakt_points(callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    if user_id not in user_points:
        user_points[user_id] = 0
    if user_points[user_id] > 0:
        user_points[user_id] -= POINTS_INCREMENT
        await callback_query.message.edit_text(f"У вас {user_points[user_id]} баллов", reply_markup=get_points_keyboard())
    else:
        await callback_query.answer("У вас больше нет баллов", show_alert=True)