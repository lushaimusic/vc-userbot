# Telegram Voice Chat User Bot
A Telegram Userbot to play Audio and Video songs / files in Telegram Voice Chats.

It's made with [PyTgCalls](https://github.com/pytgcalls/pytgcalls) and [Pyrogram](https://github.com/pyrogram/pyrogram)

# Environment Variables
- `API_ID`
- `API_HASH`
- `SESSION` - A Pyrogram String Session. Get one from [Here](https://replit.com/@ZauteKm/GenerateStringSession)
- `HNDLR` - Your Userbot Handler (Default is !)
- `GROUP_MODE` - if Value is set to `True`, Anyone can Play. Set it to `False` to restrict play access to Sudo Users/Contacts only.

## Deployment

### Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://telegram.dog/XTZ_HerokuBot?start=bHVzaGFpbXVzaWMvdmMtdXNlcmJvdCBtYXN0ZXI)
<a href="https://youtu.be/1IFe5wBxOL4"><img src="https://img.shields.io/badge/How%20to%20Deploy%20on%20Heroku-blue.svg?logo=Youtube"></a>
<a href="https://youtu.be/1IFe5wBxOL4"><img src="https://img.shields.io/youtube/views/1IFe5wBxOL4?style=social"></a>

### Local Deploy
1) Installing NodeJS
```bash
curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -
sudo apt-get install -y nodejs
```

2) Installing Dependencies
```bash
sudo apt-get install git ffmpeg -y
sudo apt-get install youtube-dl -y
```

3) Cloning the Repo
```bash
git clone https://github.com/lushaimusic/vc-userbot
cd vc-userbot
```

4) Rename `example.env` to `.env` and Fill in the Environment Variables

5) Installing Requirements
```bash
pip3 install -U -r requirements.txt
```

6) Run the Bot
```bash
python3 main.py
```

## Commands and Usage
1) Start the Userbot, check if the Userbot is running by `!ping`.
2) Commands of this userbot are accessible to and can be used by the Account itself and it's Contacts.
3) Check `!help` for commands.

## Credits ✨
- [Dan](https://github.com/delivrance) for [Pyrogram](https://github.com/pyrogram/pyrogram)
- [Laky](https://github.com/Laky-64) for [PyTgCalls](https://github.com/pytgcalls/pytgcalls)
