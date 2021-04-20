from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import callback_query
from aiogram.utils import executor

from config import TOKEN
# from keyboards import kb
from keyboards import kb_bf

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot)

@dp.message_handler(content_types=["text"])
async def process_start_command(message: types.Message):
    await message.reply("testing kb", reply_markup=kb_bf.keyboardmain)

@dp.callback_query_handler(lambda callback_query: True)
async def callback_inline(callback_query: types.CallbackQuery):
    if call.data == "mainmenu":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="menu", reply_markup=kb_bf.keyboardmain)

    if call.data == "first":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="replaced text", reply_markup=kb_bf.keyboard_1)

    elif call.data == "second":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="replaced text", reply_markup=kb_bf.keyboard_2)

    elif call.data == "1" or call.data == "2" or call.data == "3":
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="alert")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="last layer", reply_markup=kb_bf.keyboard_3)


# @dp.callback_query_handler(func=lambda c: c.data == 'button1')
# async def process_callback_button1(callback_query: types.CallbackQuery):
#     await bot.answer_callback_query(callback_query.id)
#     await bot.send_message(callback_query.from_user.id, 'Нажата первая кнопка!')


# @dp.message_handler(message=['text'])
# async def process_message(message: types.Message):
#     await message.reply('Довідка - /help', reply_markup=kb_bf.keyboardmain)


if __name__ == '__main__':
    executor.start_polling(dp)