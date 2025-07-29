import logging
from aiogram import Bot, Dispatcher, executor, types
import asyncio
import datetime

API_TOKEN = 'توکن رباتت اینجا'  # بین '' توکن واقعی‌تو بذار
CHAT_ID = 123456789  # عدد آی‌دی تلگرامت اینجا

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

async def morning_message():
    while True:
        now = datetime.datetime.now()
        if now.hour == 8 and now.minute == 0:
            await bot.send_message(CHAT_ID, "🌞 صبح بخیر رفیق! روزت پر از موفقیت")
        await asyncio.sleep(60)

async def night_message():
    while True:
        now = datetime.datetime.now()
        if now.hour == 0 and now.minute == 0:
            await bot.send_message(CHAT_ID, "🌙 شب خوش! فردا دوباره پرانرژی برگردیم")
        await asyncio.sleep(60)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("سلام! من منتور شخصی تو هستم. آماده‌ای بترکونیم؟")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("🔁 پیام دریافت شد!")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(morning_message())
    loop.create_task(night_message())
    executor.start_polling(dp, skip_updates=True)
