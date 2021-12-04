import os
from pyrogram import Client, idle
from pytgcalls import PyTgCalls
from pytgcalls import idle as pyidle
from config import bot, call_py

bot.start()
print("UserBot Started")
call_py.start()
print("Vc Client Started")
pyidle()
idle()
