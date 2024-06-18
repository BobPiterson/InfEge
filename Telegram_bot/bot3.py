import configparser
import asyncio
import logging
from aiogram import Router, Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
# Планировщик, например, для выполнения скриптов по времени
from apscheduler.schedulers.asyncio import AsyncIOScheduler
# from work_time.time_func import send_time_msg

# создать экземпляр
config = configparser.ConfigParser()
# прочитать файл .ini
config.read('C:/Users/vngorlachev/Documents/VisualStudioCode/Projects/InfEge/Telegram_bot/bot.ini')
# read values from a section
token = config.get("default", "Token")
user_id = config.get("default", "Id")
scheduler = AsyncIOScheduler(timezone='Europe/Moscow')

# функция - задание
# async def prompt(bot: Bot):
#     await bot.send_message(user_id, text="text")
#     print("Executing Task...")


async def main():


    # Создает фоновый планировщик по умолчанию
    #scheduler = AsyncIOScheduler()
    # планирование задания
    #scheduler.add_job(prompt, 'interval', seconds=10)
    # Запуск запланированных заданий
    #scheduler.start()

    # Инициализируем бота
    bot = Bot(token=token)
    # Инициализируем диспетчера бота
    dp = Dispatcher()

    start_router = Router()

    # CommandStart и Command – это встроенные фильтры.
    # CommandStart срабатывает на команду /start
    @start_router.message(CommandStart())
    async def cmd_start(message: Message):
        # параметр message отправляет сообщение в ответ тому пользователю, от которого пришла команда
        await message.answer('Запуск сообщения по команде /start используя фильтр CommandStart()')

    # Command активируется при любой команде, переданной аргументом
    # В этом случае мы явно указали команду, на которую должен реагировать бот (/my)
    @start_router.message(Command('stop'))
    async def cmd_stop(message: Message):
        await message.answer('Запуск сообщения по команде /stop используя фильтр Command()')
        #await bot.stop_poll('@bob_message_bot')

    @start_router.message(F.text == '/start_3')
    async def cmd_start_3(message: Message):
        await message.answer('Запуск сообщения по команде /start_3 используя магический фильтр F.text!')

    # Настраиваем и запускаем бота в режиме опроса
    # Добавляем роутер start_router в диспетчер dp. Это позволяет диспетчеру знать о всех обработчиках команд, которые определены в start_router
    dp.include_router(start_router)
    # Запускаем бота в режиме опроса (polling). Бот начинает непрерывно запрашивать обновления с сервера Telegram и обрабатывать их
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())