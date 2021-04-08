#!/usr/bin/python3.6

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
# from quicklock import singleton
import os, sys
import psutil
import logging

from config import TOKEN

# singleton = singleton('main_03.py', dirname='/home/ha419353/botozona.icu/www/anketa/lock')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
# os.excel("restart.sh","")

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Доброго дня!\nДля початку роботи обери потрібний код за МКХ-11 нижче\n/і10\n/і25\n/і24\nі так далі або почни строку зі слеш...")

@dp.message_handler(commands=['hipertonia'])
async def process_start_command(message: types.Message):
    await message.reply("МКХ-10\nГипертония - код - 10\nICPC2: A-11, A-12, C-15")

@dp.message_handler(commands=['i10'])
async def process_start_command(message: types.Message):
    await message.reply("Код за МКХ-11: і10\nГипертония\nСупутні коди за ICPC2:\nA-11, A-12, C-15")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")

@dp.message_handler(message=['Привет - ты бот?'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nСам такой!")

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)

def restart_program():
    """Restarts the current program, with file objects and descriptors
       cleanup
    """

    try:
        p = psutil.Process(os.getpid())
        for handler in p.get_open_files() + p.connections():
            os.close(handler.fd)
    except Exception:
        logger.error("something bad happened", exc_info=True)

    python = sys.executable
    os.execl(python, python, "\"{}\"".format(sys.argv[0]))

"""
def force_restart_script():
    python = sys.executable
    os.execl(python, python, * sys.argv)
"""