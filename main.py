from create_bot import dp
from handlers.client import register_client_handlers
from aiogram.utils import executor

register_client_handlers(dp)

executor.start_polling(dp, skip_updates=True)