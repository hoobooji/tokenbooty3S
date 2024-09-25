#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6742876658:AAHTNUdKKZVaCQgsGRa0B8qv6kVLBk5RH2U")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "21118585"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "ee05a7c74bd7dc0a8b2c6d0cbb0caf47")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002005291746"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7035291765"))

#Port
PORT = os.environ.get("PORT", "8089")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://wtflinksofficial:wtflinksofficial@cluster0.e69xg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "wtflinksofficial")

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "kingurl.in")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "a4f87c9ef2aeae5e49fe9192569ddf5c9a2ebac8")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID","nottyopen/7")


#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002151464281"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002213062086"))
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "-1001995558393"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\n𝖨 𝖼𝖺𝗇 𝗌𝗍𝗈𝗋𝖾 𝗉𝗋𝗂𝗏𝖺𝗍𝖾 𝖿𝗂𝗅𝖾𝗌 𝗂𝗇 𝖲𝗉𝖾𝖼𝗂𝖿𝗂𝖾𝖽 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 𝖺𝗇𝖽 𝗈𝗍𝗁𝖾𝗋 𝗎𝗌𝖾𝗋𝗌 𝖼𝖺𝗇 𝖺𝖼𝖼𝖾𝗌𝗌 𝗂𝗍 𝖿𝗋𝗈𝗆 𝗌𝗉𝖾𝖼𝗂𝖺𝗅 𝗅𝗂𝗇𝗄.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n𝖸𝗈𝗎 𝖭𝖾𝖾𝖽 𝖳𝗈 𝖩𝗈𝗂𝗇 𝖨𝗇 𝖮𝗎𝗋 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 𝖳𝗈 𝖴𝗌𝖾 𝖬𝖾.")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "This video/Photo/anything is available on the internet. We @LeakHubd or its subsidiary channel doesn't produce any of them.")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌ 🥰 𝖬𝖺𝗍𝗍 𝖪𝖺𝗋 𝖮𝗒𝖾 𝗈𝗇𝗅𝗒 𝖥𝗂𝗅𝖾 𝖲𝗁𝖺𝗋𝖾 𝖻𝗈𝗍 𝗁𝗎."

ADMINS.append(OWNER_ID)
ADMINS.append(1392566136)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
