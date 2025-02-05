import os
import logging
import pathlib
from pyrogram import Client, filters, types, enums
from downloader import download_and_upload_video
from flask import Flask

# Initialize the Pyrogram client
api_id = os.environ.get("27536109")  # Replace with your actual api_id
api_hash = os.environ.get("b84d7d4dfa33904d36b85e1ead16bd63")  # Replace with your actual api_hash
bot_token = os.environ.get("8038725964:AAEkw01YH9JJ_soMDKAyqNSQz9q3JhX_yt0")  # Replace with your actual bot_token

app_user = Client("ytdl-main", 
                  api_id=api_id, 
                  api_hash=api_hash, 
                  bot_token=bot_token
              )

AUTHORIZED_USERS = set(os.environ.get("AUTHORIZED_USERS", "6428531614").split())

@app_user.on_message(filters.command(["start"]))
def start_handler(client: Client, message: types.Message):
    logging.info("Welcome to m3u8DL bot!")
    client.send_message(message.chat.id, "Welcome to m3u8DL bot!")

@app_user.on_message(filters.incoming & (filters.text | filters.document))
def handle_message(client: Client, message: types.Message):
    chat_id = message.from_user.id
    client.send_chat_action(chat_id, enums.ChatAction.TYPING)
    user_message = message.text

    if chat_id not in AUTHORIZED_USERS:
        client.send_message(chat_id, "You are not authorized to use this bot.")
        return

    if user_message.startswith("https://") or user_message.startswith("http://"):
        save_dir = "/tmp/m3u8D/cache"  # Replace with your temporary directory path
        os.makedirs(save_dir, exist_ok=True)

        text = "Your task was added to active queue.\nProcessing...\n\n"
        bot_msg = message.reply_text(text, quote=True)

        download_and_upload_video(app_user, client, bot_msg, user_message, save_dir)

    else:
        client.send_message(chat_id, "Please provide a valid URL.")


app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Render assigns PORT dynamically
    app.run(host="0.0.0.0", port=port)
  

