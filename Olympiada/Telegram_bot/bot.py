import asyncio
from aiogram import Bot, types, Dispatcher

from bot_config import TOKEN

# Инициализируем бота
bot = Bot(token=TOKEN)
# Инициализируем диспетчера бота
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")

# Обработка события
# Обрабатываем текстовые сообщения
@dp.message_handler()
async def echo_message(msg: types.Message):
    # метод send_message принимает два обязательных параметра - айди чата, куда отправляем, и сам текст сообщения, которое отправляем.
    await bot.send_message(msg.from_user.id, msg.text)

# Чтобы получать сообщения от серверов Telegram воспользуемся поллингом
# (polling. to poll - опрашивать) - постоянным опросом сервера на наличие новых обновлений.
if __name__ == '__main__':
    executor.start_polling(dp)
    asyncio.run(main())
