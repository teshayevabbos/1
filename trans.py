import asyncio
api_token = "5640635635:AAGiW0hipGmOLNdOay1HvGKwThyv4NcO2ps"
from aiogram import Bot,Dispatcher,executor,types
from inline_keyboard import *
from aiogram.utils.exceptions import BotBlocked



bot = Bot(token=api_token)
dp=Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def bot_start(message:types.Message):
    await asyncio.sleep(10)
    await message.answer("hello world",reply_markup=keyboard_btn)

@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked_handler(update:types.Update,exception:BotBlocked):
    print("sdsdsdsds")
    return True



@dp.message_handler(commands=["audio"])
async def bot_start(message:types.Message):
    
    file = open()


# @dp.message_handler(commands=["tarjima"])
# async def bot_start(message:types.Message):
#     await message.answer("Qaysi tilni kiritasiz",reply_markup=keyboard_btn)



if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)