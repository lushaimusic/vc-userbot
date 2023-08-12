import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")
    
# Necessary Vars
API_ID = int(os.getenv("API_ID", "26386173"))
API_HASH = os.getenv("API_HASH", "26c1c98f03eb6742f17ee511295b6ff1")
SESSION = os.getenv("SESSION" , "BQC5ryZ_OjysEvM2-gS3EExbexnbUlM1yMcmNBaXeYV2-_LUWYd82AeMpVkeZBpXv1rv2bVOLLSpTYgKere_QxIim6StXBTUXUmTaZrrRB77SFwiW1mSiOwWj4vFEDNzlUH_I6Lb8J8W6v9fiS0uFuvQXaIaRtlFzlD0hOq4bRnfF_4toS4qY17TdudK3Nmthr1q8ArKUj48x5B07dcsoQOOcfQBpqKC-11BZLfuf2zXalOJh7t6FVgXZ4w9PDejGxH8Ir-7AiuMqjI3BrQmRUXlV4GtKrOZhmcbjZsmbLxWqsYCS8qxBdRKdXoHB9Pe8aWLq2xATbwe8wVkOJkWXJQPAAAAAV1ALWYA")
HNDLR = os.getenv("HNDLR", "!")
GROUP_MODE = os.getenv("GROUP_MODE", "True")


contact_filter = filters.create(
    lambda _, __, message:
    (message.from_user and message.from_user.is_contact) or message.outgoing
)


if GROUP_MODE == ("True" or "true"):
    grp = True
else:
    grp = False

GRPPLAY = grp
bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="plugins"))
call_py = PyTgCalls(bot)
