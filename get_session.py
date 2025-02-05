from pyrogram import Client, filters, types, enums
api_id = "27536109"
api_hash = "b84d7d4dfa33904d36b85e1ead16bd63" 
bot_token = ""

app_user = Client("app_user", api_id=api_id, api_hash=api_hash, phone_number=phone_number)

app_user.run()
