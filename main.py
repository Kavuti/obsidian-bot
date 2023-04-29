from pyrogram import Client, filters
from gdrive import create_note
import logging
import json

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


@app.on_message()
async def handle_message(client, message):
    if message.from_user.id == bot_secret["my_id"]:
        logger.info(f"Saving new note")
        note = create_note(message.text)
        logger.info(
            f"Successfully create a new note. Title: {note['title']}. Id: {note['id']}"
        )
        await message.reply(f"Nota salvata. Titolo: {note['title']}. Id: {note['id']}")
    else:
        logger.warning(
            f"Received message from unknown user {message.from_user.username}: '{message.text}'"
        )


logger.info("Bot starting")
app.run()
