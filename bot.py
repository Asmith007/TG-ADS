import os
from telethon import TelegramClient
import asyncio
import time

# Retrieve api_id and api_hash from environment variables (or set them manually here)
api_id = int(os.getenv('API_ID'))  # Convert API ID to integer
api_hash = os.getenv('API_HASH')

# Specify the session file path (e.g., 'anon.session')
session_file = 'anon.session'

# Initialize the Telegram client with the session file, api_id, and api_hash
client = TelegramClient(session_file, api_id, api_hash)

# Define the recipient you want to notify (your own Telegram username or user ID)
recipient = 'testing6977'  # Replace with the recipient's Telegram username or user ID

async def send_message():
    try:
        # Send a message to the specified user
        await client.send_message(recipient, 'Hello')
        print(f"Message sent to {recipient}")
    except Exception as e:
        print(f"Error sending message: {e}")

async def keep_alive():
    while True:
        # Send a keep-alive message to the server every 10 seconds
        await client.send_message('me', 'keep-alive')
        print("Keep-alive message sent")
        await asyncio.sleep(300)  # Wait for 5 minutes before next keep-alive message

async def main():
    while True:
        # Start the send_message coroutine
        await send_message()

        # Wait for 10 seconds before restarting the loop
        await asyncio.sleep(120)

async def start():
    try:
        # Initialize the Telegram client
        async with client:
            # Run the keep-alive coroutine to maintain the connection
            keep_alive_task = client.loop.create_task(keep_alive())

            # Run the main function asynchronously
            await main()

            # Ensure keep-alive task runs while the script is active
            await keep_alive_task
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the start function in the asyncio event loop
asyncio.run(start())
