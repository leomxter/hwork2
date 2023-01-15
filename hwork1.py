from aiogram import Bot, Dispatcher, types, executor
import config
import random
numbers = [1, 2, 3]

bot = Bot(token = config.token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Я загадал число от 1 до 3 угадайте')
    
@dp.message_handler(text = [random.choice(numbers)])
async def num(message: types.Message):
    await message.answer('Правильно вы отгадали')

@dp.message_handler()
async def num(message: types.Message):
    await message.answer('Не правильно, не хотите еще раз?)')

executor.start_polling(dp)