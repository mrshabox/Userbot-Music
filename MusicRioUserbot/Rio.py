from random import randint
from pyrogram import Client, filters
from config import HNDLR, bot as USER
from MusicRioUserbot.helpers.decorators import authorized_users_only
from pyrogram.errors import UserAlreadyParticipant
from pyrogram.raw.functions.phone import CreateGroupCall


@Client.on_message(filters.command(["join"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def join(client, message):
    chat_id = message.chat.id
    try:
        link = await client.export_chat_invite_link(chat_id)
    except BaseException:
        await message.reply("**Error:**\nThêm tôi làm quản trị viên nhóm của bạn!")
        return
    try:
        await USER.join_chat(link)
        await message.reply("**TgramMusicBot đã tham gia**")
    except UserAlreadyParticipant:
        await message.reply("**TgramMusicBot đã tham gia**")


@Client.on_message(filters.command(["voicechat"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def opengc(client, message):
    flags = " ".join(message.command[1:])
    if flags == "channel":
        chat_id = message.chat.title
        type = "channel"
    else:
        chat_id = message.chat.id
        type = "group"
    try:
        await USER.send(CreateGroupCall(
            peer=(await USER.resolve_peer(chat_id)),
            random_id=randint(10000, 999999999)
        )
        )
    except Exception:
        await message.reply(
            "**Error:** Thêm TgramMusicBot làm quản trị viên nhóm/kênh của bạn với quyền **Có thể quản lý cuộc trò chuyện thoại**"
        )
