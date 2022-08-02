
import os

import logging

from aiogram import Bot, Dispatcher, executor, types

#from config import TOKEN
TOKEN = os.getenv('TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

translit_dict = {'А':	'A',
	'Б':	'B',
	'В':    'V',
	'Г':	'G',
	'Д':	'D',
	'Е':	'E',
	'Ё':	'E',
	'Ж':	'ZH',
	'З':	'Z',
	'И':	'I',
	'Й':	'I',
	'К':	'K',
	'Л':	'L',
	'М':	'M',
	'Н':	'N',
	'О':	'O',
	'П':	'P',
	'Р':	'R',
	'С':	'S',
	'Т':	'T',
	'У':	'U',
	'Ф':	'F',
	'Х':	'KH',
	'Ц':	'TS',
	'Ч':	'CH',
	'Ш':	'SH',
	'Щ':	'SHCH',
	'Ы':	'Y',
    'Ь':    '',
	'Ъ':	'IE',
	'Э':	'E',
	'Ю':	'IU',
	'Я':	'IA'}

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}! Напиши свое имя на кириллице, и я, используя магию лунного света и приказ МИД России от 12.02.2020 N 2113, переведу его на латиницу!'
    logging.info(f'{user_name=} {user_id=} sent message: {message.text}')
    await message.reply(text)


@dp.message_handler()
async def send_translit(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    for char in translit_dict.keys():
         text = text.upper().replace(char, translit_dict.get(char))
    logging.info(f'{user_name=} {user_id=} sent message: {message.text}')
    await bot.send_message(user_id, text)

if __name__ == '__main__':
    executor.start_polling(dp)
    
