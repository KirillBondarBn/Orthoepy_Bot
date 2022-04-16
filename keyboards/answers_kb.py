from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

button_start = KeyboardButton('Начать')
button_category_selector = KeyboardButton('Выбрать категорию')
button_stats = KeyboardButton('Статистика ошибок')

kb_start = ReplyKeyboardMarkup(resize_keyboard=True)
kb_start.add(button_start).row(button_category_selector, button_stats)
