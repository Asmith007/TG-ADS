import os
import asyncio
from telethon import TelegramClient
from flask import Flask

# Retrieve api_id and api_hash from environment variables (or set them manually here)
api_id = int(os.getenv('API_ID'))  # Convert API ID to integer
api_hash = os.getenv('API_HASH')

# Specify the session file path (e.g., 'anon.session')
session_file = 'anon.session'

# Initialize the Telegram client with the session file, api_id, and api_hash
client = TelegramClient(session_file, api_id, api_hash)

# Define the recipient you want to send messages to (Telegram username or user ID)
recipient = 'testing6977'  # Replace with the recipient's Telegram username or user ID

# Define the Flask app and the route
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

# Function to log when the bot goes live
def log_bot_live():
    print("Bot is live")

# Function to send a message
async def send_message():
    try:
        # Send a message to the specified user
        await client.send_message(recipient, 'Hello')
        print(f"Message sent to {recipient}")
    except Exception as e:
        print(f"Error sending message: {e}")

# Function to run the Telegram bot
async def run_bot():
    # Log when the bot goes live
    log_bot_live()

    while True:
        # Send a message and wait for 2 minutes
        await send_message()
        await asyncio.sleep(120)

# Function to run the Flask server
async def run_flask():
    port = 3000
    app.run(host='0.0.0.0', port=port)

# Function to concurrently run the bot and Flask server
async def main():
    # Run both the bot and Flask server concurrently
    await asyncio.gather(run_bot(), run_flask())

# Start the asyncio event loop and run the main function
asyncio.run(main())
