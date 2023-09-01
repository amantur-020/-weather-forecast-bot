from bot import bot,dp
from aiogram.utils import executor
from aiogram.types import Message,InlineKeyboardMarkup,InlineKeyboardButton,ReplyKeyboardRemove,ReplyKeyboardMarkup
from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from request import req


class Weather(StatesGroup):
    start=State()



@dp.message_handler(commands='start')
async def start_commands(message:Message):
    await Weather.start.set()
    await message.answer("Введите название города:")

@dp.message_handler(commands="cancel",state=Weather.start)
async def starting(message:Message,state:FSMContext):
    await state.finish()
    await message.answer("Программа остановлена!")

@dp.message_handler(state=Weather.start)
async def starting(message:Message,state:FSMContext):
    async with state.proxy()as data:
        data["start"]=message.text
        try:
            await message.answer(req(data['start']))
        except Exception:
            await message.answer("Вы ввели название города не правильно!")








if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)






