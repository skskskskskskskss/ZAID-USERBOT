import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "28283744")) #optional
API_HASH = getenv("API_HASH", "c4e77e41df678ea346e7a146a6718433") #optional


SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5821324361").split()))
OWNER_ID = int(getenv("OWNER_ID", "5821324361"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://ftvpn:ftvpn@cluster0.4adsj6j.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "6182394661:AAGGJo4kx7h-gZjnFzWon-ON_1MQPnkQHis")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://telegra.ph/file/3c52a01057865f7511168.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER", "924550148")
LOG_GROUP = getenv("LOG_GROUP" ,"924550148")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change

STRING_SESSION1 = getenv("STRING_SESSION1", "BQBiMZkARpgY1GmO6VR-ujlqg2u7ZKmCfTimg05GQqubjfSU823Jg8VKtF7k55aLpN0yKkF8bugB8oK5EIOATfJ09k3IOJF9KeEajrvlKFg5lcBWNkbZgcJMpxtlxcIzQ9OeztJ9vNZxRIBEll1a_7eb5KXG2abveKQipF9dllfrMLxvf4eH9vLSNWfbzTHuSwBSafdmMbMScyi24JwYDpekQebBPsT8FNHuGAsLwpjyHnBhJSnevQO-4M0WzBUVkMpYIxGS-evSXIFwvMipa3P-2MDfMtPoDCgQYQv_MEzyJLcSHcDjbfGL03vnCftFi9MJ14ISpApmZiWop3FWXSBz-Ud6aAAAAAFa-lxJAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
