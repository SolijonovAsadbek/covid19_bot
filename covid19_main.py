import aiogram
import logging

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

API_TOKEN = 'TOKEN HERE'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    try:
        regi_url = 'url1 here'
        info_url = 'url2 here'
        inline = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text='🦠 1 🦠', url=regi_url)
        btn_2 = types.InlineKeyboardButton(text='🦠 2 🦠', url=info_url)
        inline.add(btn_1, btn_2)
        start_txt = f"Assalomu aleykum {message.chat.full_name}\n" \
                    f"Covid19 So'rovnoma botiga xush kelipsiz!\n\n" \
                    "1-tugma\n🦠 Covid19 infeksiyasi bilan kasallanganlar uchun so'rovnoma.\n\n" \
                    "2-tugma\n🦠 Covid 19 so'rovnomasi. O'zingiz va yaqinlaringiz sog'liqlari uchun bu muhum."
        await message.reply(start_txt, reply_markup=inline)
    except:
        await message.reply("Bu botda siz faqat tugmalardan birini tanlashiz mumkin.")



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
