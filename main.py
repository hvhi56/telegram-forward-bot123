from telethon import TelegramClient, events
import requests

api_id = 25863606
api_hash = '34f981178528c8167680f1429bb526c6'

# טוקן של הבוט שלך
bot_token = '7723230187:AAFNSF3UusSY81rq5d9qrZDxhSTcwlgEams'

# כאן תשלח את ההודעות – משתמש ששלח לבוט קודם
chat_id = None  # נשלים בהמשך

source_channel = 'https://t.me/Moshepargod'

client = TelegramClient('session', api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    if chat_id is None:
        return
    message_text = event.raw_text
    if message_text.strip() == "":
        return

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        'chat_id': chat_id,
        'text': message_text
    }
    requests.post(url, data=data)

client.start()
client.run_until_disconnected()
