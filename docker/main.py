import os
import logging
import pathlib
from pyrogram import Client, filters, types, enums
from downloader import download_and_upload_video

# Initialize the Pyrogram client
api_id =  os.environ.get("27536109") # Replace with your actual api_id
api_hash = os.environ.get("b84d7d4dfa33904d36b85e1ead16bd63")  # Replace with your actual api_hash
bot_token = os.environ.get("")  # Replace with your actual bot_token

    app_user = Client("app_user")
app = Client("ytdl-main", api_id=api_id, api_hash=api_hash, bot_token=bot_token)
# Only authenticated users can use the bot and enter the account ID.
authorized_users_env = os.environ.get


@app.on_message(filters.command(["start"]))
def start_handler(client: Client, message: types.Message):
    logging.info("Welcome to m3u8DL bot!")
    client.send_message(message.chat.id, "Welcome to m3u8DL bot!")


@app.on_message(filters.incoming & (filters.text | filters.document))
def handle_message(client: Client, message: types.Message):
    chat_id = message.from_user.id
    client.send_chat_action(chat_id, enums.ChatAction.TYPING)
    user_message = message.text
    

    if chat_id not in AUTHORIZED_USERS:
        client.send_message(chat_id, "You are not authorized to use this bot.")
        return

    if user_message.startswith("https://") or user_message.startswith("http://"):
        # Create a temporary directory for the downloaded video
        save_dir = "/tmp/m3u8D/cache"  # Replace with your temporary directory path
        os.makedirs(save_dir, exist_ok=True)

        # Tell the user that the url has been added to the download queue.
        text = "Your task was added to active queue.\nProcessing...\n\n"
        bot_msg: typing.Union[types.Message, typing.Coroutine] = message.reply_text(text, quote=True)
        if: 
            download_and_upload_video(app_user, client, bot_msg, user_message, save_dir)
        else:
            download_and_upload_video(app, client, bot_msg, user_message, save_dir)

    else:
        client.send_message(chat_id, "Please provide a valid URL.")


# Start client
if  app_user.start()
    app.run()
else:
    app.run()
