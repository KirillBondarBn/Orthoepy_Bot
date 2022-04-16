from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards.answers_kb import kb_start

async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'text', reply_markup=kb_start)

def register_client_handlers(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])