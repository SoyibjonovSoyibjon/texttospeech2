from aiogram import types, Dispatcher, Bot, F, html
import asyncio
from aiogram.filters import CommandStart
from gtts import gTTS
from aiogram.types import Message

bot= Bot(token='7421161964:AAG6uHtxK6i4UBuTYUPJJg5VSn9fnLhiN4s')
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {message.from_user.full_name}!")


@dp.message()
async def echo(message: types.Message):
    tts = gTTS(message.text, lang="en")
    tts.save(f'{message.chat.id}.mp3')
    
    file = types.input_file.FSInputFile(path=f'{message.chat.id}.mp3')
    await message.answer_voice(voice=file)


async def main():
    await dp.start_polling(bot)
# Kanal @Ahrorbek_Python
if __name__ == '__main__':
    asyncio.run(main())