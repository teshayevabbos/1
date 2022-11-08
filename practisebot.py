api_token = "5716270446:AAFd7S4qFcMcyyZclPHYm-8ST2mJops26IA"
from aiogram import Bot,Dispatcher,executor,types
bot = Bot(token=api_token)
dp=Dispatcher(bot)

# import wikipedia
# wikipedia.set_lang('ru')




@dp.message_handler(commands=['start'])
async def help(message:types.Message):
    await message.answer("hello world")
# @dp.message_handler()
# async def sendwiki(message:types.Message):
#     try:
#         respond = wikipedia.summary(message.text)
#         await message.answer(respond)
#     except:
#         await message.answer("Bu mavzuga doir maqola topilmadi")



# @dp.message_handler()
# async def echo(message:types.Message):
#     # await message.answer(message.text)
#     #await bot.send_message(chat_id=message.chat.id,text="Hello")
#     await bot.send_message(chat_id=message.from_user.id,text="Hello")




# @dp.message_handler(commands=['help'])
# async def help(message:types.Message):
#    await bot.send_message(chat_id=message.from_user.id,text="Hello!,parse_made='HTML")



# @dp.message_handler(commands=['image'])
# async def send_image(message:types.Message):
#     await bot.send_video(chat_id=message.chat.id,video="https://www.youtube.com/watch?v=ayUBlf9pvn0&list=PLe-iIMbo5JOJm6DRTjhleHojroS-Bbocr&index=1")









if __name__=="__main__":
    executor.start_polling(dp)