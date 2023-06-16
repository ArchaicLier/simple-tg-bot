from aiogram import Bot, Dispatcher, executor, types
import logging

API_TOKEN = ''

with open('secret.txt', 'r') as token:
    API_TOKEN = token.readline()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
users = {}

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text=message.text)

executor.start_polling(dp, skip_updates=True)
