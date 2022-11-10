from aiogram import types, Dispatcher
from create_bot import bot, dp
from keyboards import kb_client


# @dp.message_handler(commands=['start', 'help'])
async def commands_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привет, я бот который помогает поварам монтаны. Я могу помочь тебе с заказом продуктов или подсказать как делается блюдо', reply_markup=kb_client)
        await message.delete()
    except: 
        await message.reply('Общение с ботом через ЛС. Напишите мне! : \nt.me/PizzaMontanaBot ')

# @dp.message_handler(commands=['recipes'])
async def commands_recipes(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Тут будут выводится всю блюда и при на их нажатии будет рецепт  с грамовками')
        await message.delete()
    except: 
        await message.reply('Общение с ботом через ЛС. Напишите мне! : \nt.me/PizzaMontanaBot ')

# @dp.message_handler(commands=['order'])
async def commands_order(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Функция в разработке!')
        await message.delete()
    except: 
        await message.reply('Общение с ботом через ЛС. Напишите мне! : \nt.me/PizzaMontanaBot ')


def register_handlers_clien(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])    
    dp.register_message_handler(commands_recipes, commands=['recipes'])
    dp.register_message_handler(commands_order, commands=['order'])