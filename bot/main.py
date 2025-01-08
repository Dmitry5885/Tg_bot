from aiogram import Bot, Dispatcher
import asyncio
from bot.routes.commands import *


API_TOKEN = ''

# Настройка логирования
logging.basicConfig(level=logging.INFO)


# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


# Подключение маршрутизатора
dp.include_router(router)

dp.bot = bot

async def main():
    await dp.start_polling(bot)
# Запуск бота
if __name__ == '__main__':
    asyncio.run(main())
