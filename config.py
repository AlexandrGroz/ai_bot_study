import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_PATH = os.getenv("WEBHOOK_PATH", "/sorcer")
WEBHOOK_HOST = os.getenv("WEBHOOK_HOST", "https://fpvhr-5-1-53-226.a.free.pinggy.link")
WEBHOOK_URL = WEBHOOK_HOST + WEBHOOK_PATH
PORT = int(os.getenv("PORT", 8000))