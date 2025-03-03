from pyrogram import Client, filters
import asyncio
import os
from pytube import YouTube
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from youtubesearchpython import VideosSearch
from AlexaSongBot.mrdarkprince import ignore_blacklisted_users, get_arg
from AlexaSongBot import app, LOGGER
from AlexaSongBot.sql.chat_sql import add_chat_to_db


def yt_search(song):
    videosSearch = VideosSearch(song, limit=1)
    result = videosSearch.result()
    if not result:
        return False
    else:
        video_id = result["result"][0]["id"]
        url = f"https://youtu.be/{video_id}"
        return url


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("song"))
async def song(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    add_chat_to_db(str(chat_id))
    args = get_arg(message) + " " + "song"
    if args.startswith(" "):
        await message.reply("Digite o nome de uma música. Verificar /help")
        return ""
    status = await message.reply("🔎Pesquisando música no YouTube 📺.. Por favor espere um pouco ⏳️\n\nDuvidas : @TioMorty ")
    video_link = yt_search(args)
    if not video_link:
        await status.edit("😔Música não encontrada.")
        return ""
    yt = YouTube(video_link)
    audio = yt.streams.filter(only_audio=True).first()
    try:
        download = audio.download(filename=f"{str(user_id)}")
    except Exception as ex:
        await status.edit("Falha ao baixar música ")
        LOGGER.error(ex)
        return ""
    rename = os.rename(download, f"{str(user_id)}.mp3")
    await app.send_chat_action(message.chat.id, "upload_audio")
    await app.send_audio(
        chat_id=message.chat.id,
        audio=f"{str(user_id)}.mp3",
        duration=int(yt.length),
        title=str(yt.title),
        performer=str(yt.author),
        reply_to_message_id=message.message_id,
    )
    await status.delete()
    os.remove(f"{str(user_id)}.mp3")

@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("song"))
async def song(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    add_chat_to_db(str(chat_id))
    args = get_arg(message) + " " + "vsong"
    if args.startswith(" "):
        await message.reply("Digite o nome de uma música. Verificar /help")
        return ""
    status = await message.reply("🔎Pesquisando música no YouTube 📺.. Por favor espere um pouco ⏳️\n\nDuvidas : @TioMorty ")
    video_link = yt_search(args)
    if not video_link:
        await status.edit("😔Música não encontrada.")
        return ""
    yt = YouTube(video_link)
    audio = yt.streams.filter(only_video=True).first()
    try:
        download = video.download(filename=f"{str(user_id)}")
    except Exception as ex:
        await status.edit("Falha ao baixar música ")
        LOGGER.error(ex)
        return ""
    rename = os.rename(download, f"{str(user_id)}.mp4")
    await app.send_chat_action(message.chat.id, "upload_video")
    await app.send_video(
        chat_id=message.chat.id,
        Video=f"{str(user_id)}.mp4",
        duration=int(yt.length),
        title=str(yt.title),
        performer=str(yt.author),
        reply_to_message_id=message.message_id,
    )
    await status.delete()
    for files in (sedlyf, file_stark):
        if files and os.path.exists(files):
            os.remove(files)
