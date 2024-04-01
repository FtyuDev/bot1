from aiogram import Bot, Dispatcher, types, executor
from backend import alldownloader
from keyboards import key

token = '6875469116:AAGS4TnHwsV2qmpl5Wo6e9amz8RBWvV5Eyk'
bot = Bot(token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start','help'])
async def start(message: types.Message):
    print(message.from_user.full_name)
    await bot.send_message(6390845130, f"<code>{message.from_user.full_name}</code>")
    await message.answer_photo('https://avatars.mds.yandex.net/i?id=7c391094db327bb0ec618ca54fcc1ab0c2a531cc-7662450'
                               '-images-thumbs&n=13',"<b>Bu bot orqali Instagram YouTubeshorts Facebook TikTok ijtimiy "
                                                     "tarmoqlardan video yuklashingiz mumkin\n\nBotni ishlatish uchun "
                                                     "video manzilini yuboring</b>\n\n❗️Eslatma: Video davomiyligi 3 daqiqadan oshmasin!!!\n\nYaratuvchi: "
                                                     "@Ftyu_Dev",reply_markup=key)


@dp.message_handler(content_types=types.ContentType.TEXT)
async def download(message: types.Message):
    await message.answer("<b>Yuklanmoqda...🚀</b>")
    print(message.from_user.full_name)
    data = alldownloader(message.text)
    if data == 'xato':
        await message.answer_photo('https://avatars.mds.yandex.net/i?id=61fa83a26de52629547486546cd3110cff848058'
                                   '-9291097-images-thumbs&n=13',"Noto'g'ri url yubordingiz tekshirib qayta urinib "
                                                                 "ko'ring")
    else:
        await message.answer_video(f"{data['video']}", caption=data['title'], reply_markup=key)


executor.start_polling(dp, skip_updates=True)
