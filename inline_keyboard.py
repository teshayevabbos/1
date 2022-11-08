from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

btn1 = InlineKeyboardButton(text="o'zbek",callback_data='uz')
btn2 = InlineKeyboardButton(text="Rus",callback_data='ru')
btn3 = InlineKeyboardButton(text="Arab",callback_data='ar')
btn4 = InlineKeyboardButton(text="Rus",callback_data='en')
keyboard_btn = InlineKeyboardMarkup(row_width=4).add(btn1,btn2,btn3,btn4)
