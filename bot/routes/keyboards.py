from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def get_points_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Добавить 5 баллов", callback_data="add_points"),
            InlineKeyboardButton(text="Вычесть 5 баллов", callback_data="subtract_points")
        ]
    ])
    return keyboard