import logging
import time
import config
from aiogram import Bot, Dispatcher, executor, types
import weather_info
from googletrans import Translator
from weather_en import clear_phrase

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(
                     "Hi " + message.from_user.first_name +
                     " 🤗\nJust write me the name of the city\n\n"
                     + "Привет " + message.from_user.first_name +
                     "\nПросто напиши мне название города\n")
@dp.message_handler(commands=['lang'])
async def welcome_lang(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=3)
    inline_btn_1 = types.InlineKeyboardButton('🇰🇬 KG', callback_data='kg')
    inline_btn_2 = types.InlineKeyboardButton('🇹🇷 TR', callback_data='tr')
    inline_btn_3 = types.InlineKeyboardButton('🇬🇧 EN', callback_data='en')
    inline_btn_4 = types.InlineKeyboardButton('🇷🇺 RU', callback_data='ru')
    keyboard_markup.add(inline_btn_1, inline_btn_2, inline_btn_3, inline_btn_4)

    await message.answer("Выберите язык \nChoose language:", reply_markup=keyboard_markup)

@dp.callback_query_handler(text='kg')
@dp.callback_query_handler(text='tr')
@dp.callback_query_handler(text='ru')
@dp.callback_query_handler(text='en')
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    answer_data = query.data

    if answer_data == 'kg':
        config.lang = 'kg'
        text = config.vocabulary['kg'][7]
    elif answer_data == 'tr':
        config.lang = 'tr'
        text = config.vocabulary['tr'][7]
    elif answer_data == 'ru':
        config.lang = 'ru'
        text = config.vocabulary['ru'][7]
    elif answer_data == 'en':
        config.lang = 'en'
        text = config.vocabulary['en'][7]
    else:
        text = f'Unexpected callback data {answer_data!r}!'

    await bot.send_message(query.from_user.id, text)

@dp.message_handler(commands=['help'])
async def welcome(message: types.Message):
    if config.lang == 'kg' or config.lang == 'ru':
        text = config.text_ru
    elif config.lang == 'en':
        text = config.text_en
    elif config.lang == 'tr':
        text = config.text_tr
    await message.reply(text)

@dp.message_handler()
async def getCity(message: types.Message):
    if config.lang == "ru":
        config.old_city = clear_phrase(message.text)
        trans = Translator()
        city = trans.translate(config.old_city, src='en')
        config.new_city = city.text
    elif config.lang == "tr":
        config.old_city = clear_phrase(message.text)
        trans = Translator()
        city = trans.translate(config.old_city, src='en')
        config.old_city = city.text
    elif config.lang == "kg":
        config.old_city = clear_phrase(message.text)
        trans = Translator()
        city = trans.translate(config.old_city, src='en')
        config.old_city = city.text
    else:
        config.old_city = clear_phrase(message.text)
        trans = Translator()
        city = trans.translate(config.old_city,src='en')
        config.old_city = city.text

    answer1, answer2 = weather_info.getInfo(message)
    await message.answer(answer1, parse_mode="HTML")
    time.sleep(2)
    await message.answer(answer2, parse_mode="HTML")
#------------------------------------------------------

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
