import logging
import requests

class DiscordHandler(logging.Handler):
    def __init__(self, webhook_url, level=logging.ERROR):
        super().__init__(level=level)
        self.webhook_url = webhook_url

    def emit(self, record):
        try:
            data = {
                "content": f"Error: {record.getMessage()}"
            }
            headers = {"Content-Type": "application/json"}
            response = requests.post(self.webhook_url, json=data, headers=headers)

            if response.status_code == 204:
                print("Error message sent to Discord successfully")
            else:
                print(f"Failed to send error message to Discord. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error sending message to Discord: {e}")

# Replace 'YOUR_DISCORD_WEBHOOK_URL' with your actual Discord webhook URL
discord_webhook_url = 'https://discordapp.com/api/webhooks/1189611631861317663/H2yKT7Bm3CNUErlhPFdctUSiqQhCoavnUTDOfEP8bWawN9_Ww02eMYrA2x8e8vP11qh4'

# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)  # Set the logger level to only capture errors

# Create DiscordHandler and add it to the logger
discord_handler = DiscordHandler(webhook_url=discord_webhook_url)
logger.addHandler(discord_handler)

# Test log messages
try:
    1 / 0  # Producing an intentional error for testing
except Exception as e:
    logger.error(f"This is an error message sent to Discord: {str(e)}")
