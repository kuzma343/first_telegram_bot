import sys
import os
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("НАПИШИ ОЦІНКУ")

@dp.message_handler()
async def echo_message(msg: types.Message):
    user_input = msg.text

    print(f"Received message from user {msg.from_user.id}: {user_input}")  # Вивід повідомлення в консоль

    if user_input.isdigit():
        num = int(user_input)

        if num > 12:
            await msg.reply("Помилка: число більше 12")
        elif num >= 10: 
            await msg.reply("Відміник")
        elif num >= 7: 
            await msg.reply("Харашист")
        elif num >= 1: 
            await msg.reply("Старайся краще")
        else:
            await msg.reply("Помилка: число менше 1")
    else:
        await msg.reply("нечисло")

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

