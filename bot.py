import os
from telethon import TelegramClient
import asyncio

# Retrieve api_id and api_hash from environment variables
api_id = int(os.getenv('API_ID'))  # Cast API ID to integer
api_hash = os.getenv('API_HASH')

# Initialize the Telegram client with the session name 'anon', api_id, and api_hash
client = TelegramClient('anon', api_id, api_hash)

async def send_message():
    # Sending messages in a 10-second interval
    while True:
        try:
            # Send a message to the specified user
            await client.send_message('testing6977', 'Hello')
            print("Message sent to testing6977")
        except Exception as e:
            print(f"Error sending message: {e}")

        # Wait for 10 seconds before sending the next message
        await asyncio.sleep(10)

async def main():
    # Start the send_message coroutine
    await send_message()

with client:
    # Run the main function asynchronously with the client session
    client.loop.run_until_complete(main())
  
