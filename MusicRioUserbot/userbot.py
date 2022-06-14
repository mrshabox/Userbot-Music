import os
import sys
from datetime import datetime
from time import time
from pyrogram import Client, filters
from pyrogram.types import Message
from config import HNDLR, SUDO_USERS

# System Uptime
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ("Minggu", 60 * 60 * 24 * 7),
    ("Hari", 60 * 60 * 24),
    ("Jam", 60 * 60),
    ("Menit", 60),
    ("Detik", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)

@Client.on_message(filters.command(["ping"], prefixes=f"{HNDLR}"))
async def ping(client, m: Message):
   start = time()
   current_time = datetime.utcnow()
   m_reply = await m.edit("Pinging...")
   delta_ping = time() - start
   await m_reply.edit("0% ▒▒▒▒▒▒▒▒▒▒")
   await m_reply.edit("20% ██▒▒▒▒▒▒▒▒")
   await m_reply.edit("40% ████▒▒▒▒▒▒")
   await m_reply.edit("60% ██████▒▒▒▒")
   await m_reply.edit("80% ████████▒▒")
   await m_reply.edit("100% ██████████")
   end = datetime.now()
   uptime_sec = (current_time - START_TIME).total_seconds()
   uptime = await _human_time_duration(int(uptime_sec))
   await m_reply.edit(f"**┞◈𝗣𝗼𝗻𝗴!! TgramMusicBot 🏓**\n**┞◈Pinger**  - {delta_ping * 1000:.3f} ms \n**┞◈Uptime** - {uptime}")


@Client.on_message(filters.command(["pong"], prefixes=f"{HNDLR}"))
async def pong(client, m: Message):
   start = time()
   current_time = datetime.utcnow()
   pong = await m.edit("Pinging...")
   delta_ping = time() - start
   await pong.edit("❏◈===❏")
   await pong.edit("❏=◈==❏")
   await pong.edit("❏==◈=❏")
   await pong.edit("❏===◈❏")
   await pong.edit("❏==◈=❏")
   await pong.edit("❏=◈==❏")
   await pong.edit("❏◈===❏")
   await pong.edit("❏=◈==❏")
   await pong.edit("❏==◈=❏")
   await pong.edit("❏===◈❏")
   await pong.edit("❏==◈=❏")
   await pong.edit("❏=◈==❏")
   await pong.edit("❏◈===❏")
   await pong.edit("❏=◈==❏")
   await pong.edit("❏==◈=❏")
   await pong.edit("❏===◈❏")
   await pong.edit("❏===◈❏◈")
   await pong.edit("❏====❏◈◈")
   await pong.edit("**◈PINGGGG!**")
   end = datetime.now()
   uptime_sec = (current_time - START_TIME).total_seconds()
   uptime = await _human_time_duration(int(uptime_sec))
   await pong.edit(
       f"**❏TgramMusicBot**\n**❏Pinging** : {delta_ping * 1000:.3f} ms\n**❏Bot Uptime** : {uptime}")

@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["restart"], prefixes=f"{HNDLR}")
)
async def restart(client, m: Message):
    await m.delete()
    loli = await m.reply("1")
    await loli.edit("2")
    await loli.edit("3")
    await loli.edit("4")
    await loli.edit("5")
    await loli.edit("6")
    await loli.edit("7")
    await loli.edit("8")
    await loli.edit("9")
    await loli.edit("**✅ Tgram Music Bot đã được khởi động lại**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()


@Client.on_message(filters.command(["help"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HELP = f"""
<b>👋 Chào {m.from_user.mention}!
🛠 MENU TRỢ GIÚP NGƯỜI CHƠI NHẠC
⚡ LỆNH CHO MỌI NGƯỜI
• {HNDLR}play [tên bài hát |  liên kết youtube |  trả lời tệp âm thanh] - chơi một bài hát
• {HNDLR}videoplay [tiêu đề video |  liên kết youtube |  trả lời các tệp video] - chơi một video
• {HNDLR}playlist để xem danh sách phát
• {HNDLR}ping - để kiểm tra trạng thái
• {HNDLR}id - để xem id người dùng
• {HNDLR}video - tiêu đề video |  liên kết youtube để tìm kiếm video
• {HNDLR}song - bài hát |  liên kết youtube để tìm kiếm bài hát
• {HNDLR}help - để xem danh sách các lệnh
• {HNDLR}join- tham gia |  nhóm 
⚡ PERINTAH UNTUK SEMUA ADMIN
• {HNDLR}resume - để tiếp tục phát một bài hát hoặc video
• {HNDLR}pause - để tạm dừng phát một bài hát hoặc video
• {HNDLR}skip - để bỏ qua các bài hát hoặc video
• {HNDLR}end - để kết thúc phát nhạc</b>
"""
    await m.reply(HELP)


@Client.on_message(filters.command(["repo"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    REPO = f"""
<b>👋 Chào {m.from_user.mention}!
🗃️ Website: https://www.tgram.vn
🔰 Blog: https://sanlink.xyz
📝 Persyaratan
• Python 3.8+
• FFMPEG
• Nodejs v16+
"""
    await m.reply(REPO, disable_web_page_preview=True)
