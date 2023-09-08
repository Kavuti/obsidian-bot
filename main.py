from pyrogram import Client, filters
from gdrive import create_note
import logging
import json
from pprint import pprint

logging.basicConfig(format="%(asctime)s %(levelname)s:%(name)s - %(message)s")
logger = logging.getLogger("obsidian-bot")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)

with open("bot-secret.json") as bot_secret_file:
    bot_secret = json.loads(bot_secret_file.read())
    logger.info("Secrets read from file")

app = Client(
    "obsidian-bot",
    api_id=bot_secret["api_id"],
    api_hash=bot_secret["api_hash"],
    bot_token=bot_secret["bot_token"],
)

@app.on_message(filters.user(bot_secret["my_id"]) & filters.text)
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
