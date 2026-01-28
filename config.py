import re
import os
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Required credentials
API_ID = 
API_HASH = ""
BOT_TOKEN = ""
MONGO_DB_URI = ""
OWNER_ID = 7926944005
LOG_GROUP_ID = -1002777786186

# Optional / deployment-related
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")

UPSTREAM_REPO = os.getenv("UPSTREAM_REPO", "https://github.com/itzarjuna1/InfinityDark")
UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = os.getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "https://t.me/dark_musictm")
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "https://t.me/snowy_hometown")
PRIVACY_LINK = os.getenv("PRIVACY_LINK", "https://graph.org/privacy-policy--aliya-music-bot-01-18")

DURATION_LIMIT_MIN = int(os.getenv("DURATION_LIMIT", 10000))
DURATION_LIMIT = DURATION_LIMIT_MIN * 60

AUTO_LEAVING_ASSISTANT = bool(os.getenv("AUTO_LEAVING_ASSISTANT", False))

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", None)
PLAYLIST_FETCH_LIMIT = int(os.getenv("PLAYLIST_FETCH_LIMIT", 25))

TG_AUDIO_FILESIZE_LIMIT = int(os.getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(os.getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))

STRING1 = os.getenv("STRING_SESSION1", "")
STRING2 = os.getenv("STRING_SESSION2", None)
STRING3 = os.getenv("STRING_SESSION3", None)
STRING4 = os.getenv("STRING_SESSION4", None)
STRING5 = os.getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# Image URLs
START_IMG_URL = os.getenv("START_IMG_URL", "https://files.catbox.moe/frpk8m.jpg")
PING_IMG_URL = os.getenv("PING_IMG_URL", "https://files.catbox.moe/h8e04a.jpg")
PLAYLIST_IMG_URL = "https://files.catbox.moe/h8e04a.jpg"
STATS_IMG_URL = "https://files.catbox.moe/frpk8m.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/h8e04a.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/h8e04a.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/frpk8m.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/h8e04a.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/frpk8m.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/h8e04a.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/frpk8m.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/h8e04a.jpg"

# Time converter
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

# Validate links
if SUPPORT_CHANNEL and not re.match("(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - Your SUPPORT_CHANNEL url is wrong. It must start with https://")

if SUPPORT_GROUP and not re.match("(?:http|https)://", SUPPORT_GROUP):
    raise SystemExit("[ERROR] - Your SUPPORT_GROUP url is wrong. It must start with https://")
