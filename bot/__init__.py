import os
from pyrogram import Client
from dotenv import load_dotenv

if os.path.exists('config.env'):
  load_dotenv('config.env')

api_id = int(os.environ.get("API_ID", 11873433))
api_hash = os.environ.get("API_HASH", "96abaf0d59cd1f5482bdc93ba6030424")
bot_token = os.environ.get("BOT_TOKEN", "5269784341:AAFAz_umXmT9iaj5ds5mlZK0Jh0AwaT6hRQ")
download_dir = os.environ.get("DOWNLOAD_DIR", "downloads/")
sudo_users = list(set(int(x) for x in os.environ.get("SUDO_USERS", "1485677797").split()))

app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

data = []

if not download_dir.endswith("/"):
  download_dir = str(download_dir) + "/"
if not os.path.isdir(download_dir):
  os.makedirs(download_dir)
