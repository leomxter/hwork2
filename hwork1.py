from aiogram import Bot, Dispatcher, types, executor
import config

bot = Bot(token = config.token)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer(f"Здравствуйте {message.from_user.first_name}. Выберите одно направление из 5: /backend /frontend /uxui /android /ios")

@dp.message_handler(commands = 'backend')
async def backend(message: types.Message):
    await message.answer('Backend — это внутренняя часть сайта и сервера и т.д\n'
                         'Стоимость 10000 сом в месяц\n'
                         'Обучение: 5 месяц')

executor.start_polling(dp)