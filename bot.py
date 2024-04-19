import os
from telethon import TelegramClient
import asyncio
from aiohttp import web

# Retrieve api_id and api_hash from environment variables (or set them manually here)
api_id = int(os.getenv('API_ID'))  # Convert API ID to integer
api_hash = os.getenv('API_HASH')

# Specify the session file path (e.g., 'anon.session')
session_file = 'anon.session'

# Initialize the Telegram client with the session file, api_id, and api_hash
client = TelegramClient(session_file, api_id, api_hash)

# Define the recipient you want to send messages to (Telegram username or user ID)
recipient = 'testing6977'  # Replace with the recipient's Telegram username or user ID

# Define the port number for the HTTP server
PORT = int(os.getenv('PORT', 10000))

# Function to log when the bot goes live
def log_bot_live():
    print("Bot is live")

# Define the HTTP server response
async def handle(request):
    return web.Response(text="HTTP server is running.")

async def send_message():
    try:
        # Send a message to the specified user
        await client.send_message(recipient, 'Hello')
        print(f"Message sent to {recipient}")
    except Exception as e:
        print(f"Error sending message: {e}")

async def main():
    # Log when the bot goes live
    log_bot_live()

    while True:
        # Send a message and wait for 2 minutes
        await send_message()
        await asyncio.sleep(120)

async def start():
    # Initialize the Telegram client and run the main function
    async with client:
        await main()

# Create the aiohttp application
app = web.Application()
app.router.add_get("/", handle)

# Run the HTTP server and the bot script concurrently
async def run():
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", PORT)
    await site.start()
    await start()

# Start the asyncio event loop to run both tasks concurrently
asyncio.run(run())
