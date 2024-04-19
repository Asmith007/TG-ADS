import os
from telethon import TelegramClient
import asyncio

# Retrieve api_id and api_hash from environment variables (or set them manually here)
api_id = int(os.getenv('API_ID'))  # Convert API ID to integer
api_hash = os.getenv('API_HASH')

# Specify the session file path (e.g., 'anon.session')
session_file = 'anon.session'

# Initialize the Telegram client with the session file, api_id, and api_hash
client = TelegramClient(session_file, api_id, api_hash)

async def send_message():
    try:
        # Send a message to the specified user
        await client.send_message('testing6977', 'Hello')
        print("Message sent to testing6977")
    except Exception as e:
        print(f"Error sending message: {e}")

async def main():
    while True:
        # Start the send_message coroutine
        await send_message()

        # Wait for 10 seconds before restarting the loop
        await asyncio.sleep(60)

# The following code block handles the client initialization and runs the main function
async def start():
    async with client:
        # Run the main function asynchronously with the client session
        await main()

# Run the start function in the asyncio event loop
asyncio.run(start())
