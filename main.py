import os
from telethon import TelegramClient, events
from telegram import Bot
import re

# הגדרות שלך
api_id = 25863606
api_hash = '34f981178528c8167680f1429bb526c6'
bot_token = '7723230187:AAFNSF3UusSY81rq5d9qrZDxhSTcwlgEams'
source_channel = 'https://t.me/Moshepargod'  # הערוץ לעקוב אחריו
chat_id = 6708985488  # ID של הצ'אט שלך

# חיבור לטלגרם
client = TelegramClient('session', api_id, api_hash)
bot = Bot(token=bot_token)

def should_forward(message):
    text = message.text or ""
    
    # בדיקה אם יש לינק
    links = re.findall(r'https?://t\.me/[^\s]+', text)
    
    if links:
        # אם הלינקים הם אך ורק מ-Moshepargod – נאשר
        only_allowed_links = all('https://t.me/Moshepargod' in link for link in links)
        return only_allowed_links
    
    return True  # אם אין קישורים בכלל, כן להעביר

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    try:
        if should_forward(event.message):
            text = event.message.text or "<ההודעה לא כוללת טקסט>"
            await bot.send_message(chat_id=chat_id, text=text, parse_mode="HTML")
    except Exception as e:
        print("⚠️ שגיאה בטיפול בהודעה:", e)

def main():
    print("🤖 הבוט פעיל וממתין להודעות...")
    client.start()
    client.run_until_disconnected()

if __name__ == '__main__':
    main()

