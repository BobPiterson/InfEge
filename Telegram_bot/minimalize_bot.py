###################################################################
# Мой первый минималистичный Бот
# Выводит в чат текущее время по заданному интервалу
# Команды не принимает
###################################################################
import configparser # для работы с файлами .ini
import datetime     # для работы с датой
import asyncio      # модуль позволяет заниматься асинхронным программированием с применением конкурентного выполнения кода
#import logging     # для логов в терминал
from aiogram import Router, Bot, Dispatcher # библиотека для ботов telegram
from apscheduler.schedulers.asyncio import AsyncIOScheduler # Планировщик, например, для выполнения скриптов по времени

# Читаем файл bot.ini - создать экземпляр
config = configparser.ConfigParser()
# прочитать файл .ini
config.read('C:/Users/vngorlachev/Documents/VisualStudioCode/Projects/InfEge/Telegram_bot/bot.ini')
# read values from a section "default"
token = config.get("default", "Token")
user_id = config.get("default", "Id")
scheduler = AsyncIOScheduler(timezone='Europe/Moscow')

async def main():
    # Инициализируем бота
    bot = Bot(token=token)
    # Инициализируем диспетчера бота
    dp = Dispatcher()

    start_router = Router()

    # отправляем сообщение по указанному user_id
    await bot.send_message(user_id, text = 'Bot started...', parse_mode = 'HTML')
    await bot.send_message(user_id, text = '------------------------------------------------------------------------------', parse_mode = 'HTML')

    async def auto_posting():
        now = datetime.datetime.now()
        text = now.strftime("%H:%M:%S")
        await bot.send_message(user_id, text = text, parse_mode = 'HTML')

    # Создает фоновый планировщик по умолчанию
    scheduler = AsyncIOScheduler()
    # планирование задания с заданным интервалом
    scheduler.add_job(auto_posting, 'interval', seconds=5)
    # Запуск запланированных заданий
    scheduler.start()

    # Добавляем роутер start_router в диспетчер dp. Это позволяет диспетчеру знать о всех обработчиках команд, которые определены в start_router
    dp.include_router(start_router)
    # Запускаем бота в режиме опроса (polling). Бот начинает непрерывно запрашивать обновления с сервера Telegram и обрабатывать их
    await dp.start_polling(bot)

if __name__ == '__main__':
#    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())