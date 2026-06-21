import os
from dotenv import load_dotenv

load_dotenv()

import requests


def publish_to_discord(message):
    webhook_url = os.environ["DISCORD_WEBHOOK_URL"]
    response = requests.post(webhook_url, json={"content": message[:1990]}, timeout=10)
    response.raise_for_status()


if __name__ == "__main__":
    publish_to_discord("Test message from my AI digest bot.")