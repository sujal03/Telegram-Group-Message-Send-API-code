# from telegram import Bot
# import asyncio

# TOKEN = "7467227167:AAG8uRLOrx2wT_W6QH7fw7jlF19-rmxX3xw"
# CHAT_ID = "1046040651" 

# async def send_message():
#     bot = Bot(token=TOKEN)
#     await bot.send_message(chat_id=CHAT_ID, text="Raghav bhai kesa h?")
#     print("Message sent successfully")

# if __name__ == "__main__":
#     asyncio.run(send_message())














# from telegram import Bot
# import asyncio

# TOKEN = "7467227167:AAG8uRLOrx2wT_W6QH7fw7jlF19-rmxX3xw"

# async def get_chat_info():
#     bot = Bot(token=TOKEN)
#     try:
#         # Send a message to the group and forward the ID
#         updates = await bot.get_updates()
#         for update in updates:
#             if update.message:
#                 chat_id = update.message.chat.id
#                 chat_type = update.message.chat.type
#                 print(f"Chat ID: {chat_id}")
#                 print(f"Chat Type: {chat_type}")
#     except Exception as e:
#         print(f"Error: {e}")

# if __name__ == "__main__":
#     asyncio.run(get_chat_info())
















# from telegram import Bot
# import asyncio

# TOKEN = "7467227167:AAG8uRLOrx2wT_W6QH7fw7jlF19-rmxX3xw"
# GROUP_CHAT_ID = "-1002342054150"  # Note the minus sign

# async def send_group_message():
#     bot = Bot(token=TOKEN)
#     try:
#         await bot.send_message(
#             chat_id=GROUP_CHAT_ID,
#             text="aditya sir kese h?"
#         )
#         print("Message sent successfully!")
#     except Exception as e:
#         print(f"Error sending message: {e}")

# if __name__ == "__main__":
#     asyncio.run(send_group_message())















from flask import Flask, jsonify, request
from telegram import Bot
import asyncio
from dotenv import load_dotenv
import os
from flask_cors  import CORS

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
# Get environment variables with fallback values
TOKEN = os.getenv("TELEGRAM_TOKEN")
GROUP_CHAT_ID = os.getenv("GROUP_CHAT_ID")


# Verify environment variables are loaded
if not TOKEN or not GROUP_CHAT_ID:
    raise ValueError("Missing required environment variables. Check your .env file.")

async def send_telegram_message(message_text):
    bot = Bot(token=TOKEN)
    try:
        await bot.send_message(
            chat_id=GROUP_CHAT_ID,  
            text=message_text
        )
        return True, "Message sent successfully!"
    except Exception as e:
        return False, f"Error sending message: {e}"

@app.route('/send-message', methods=['POST'])
def send_message():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({
            "success": False,
            "message": "Please provide a message in the request body"
        }), 400
    
    success, message = asyncio.run(send_telegram_message(data['message']))
    return jsonify({
        "success": success,
        "message": message
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')