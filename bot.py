import os
from telethon import TelegramClient
import asyncio

# Retrieve api_id and api_hash from environment variables
api_id = int(os.getenv('API_ID'))  # Cast API ID to integer
api_hash = os.getenv('API_HASH')

# Specify the session file path (e.g., 'anon.session')
session_file = 'anon.session'

# Initialize the Telegram client with the session file, api_id, and api_hash
client = TelegramClient(session_file, api_id, api_hash)

async def send_message():
    # Sending messages in a 10-second interval
    while True:
        try:
            # Send a message to the specified user
            await client.send_message('testing6977', 'Hello its me')
            print("Message sent to testing6977")
        except Exception as e:
            print(f"Error sending message: {e}")

        # Wait for 10 seconds before sending the next message
        await asyncio.sleep(300)

async def main():
    # Start the send_message coroutine
    await send_message()

# The following code block handles the client initialization and runs the main function
async def start():
    # Start the Telegram client
    async with client:
        # Run the main function asynchronously with the client session
        await main()

# Run the start function in the asyncio event loop
asyncio.run(start())
