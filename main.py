from pyrogram import Client, filters
from gdrive import create_note
import logging
import json
from dotenv import load_dotenv
import os

logging.basicConfig(format="%(asctime)s %(levelname)s:%(name)s - %(message)s")
logger = logging.getLogger("obsidian-bot")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)

app = Client(
    "obsidian-bot",
    api_id=os.getenv("TG_API_ID"),
    api_hash=bot_secret["TG_API_HASH"],
    bot_token=bot_secret["TG_BOT_TOKEN"],
)

@app.on_message(filters.user(bot_secret["TG_MY_ID"]) & filters.text)
async def handle_message(client, message):
    logger.info(f"Saving new note")
    note = create_note(message.text)
    logger.info(
        f"Successfully create a new note. Title: {note['title']}. Id: {note['id']}"
    )
    await message.reply(f"Nota salvata. Titolo: {note['title']}. Id: {note['id']}")

# @app.on_message(filters.user(bot_secret["my_id"]) & filters.photo)
# async def handle_photo(client, photo):
#     file = await app.download_media(photo, in_memory=True)
#     file_name = file.name
#     file_bytes = bytes(file.getbuffer())


logger.info("Bot starting")
app.run()
