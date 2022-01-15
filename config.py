# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

import logging
import os
from logging.handlers import RotatingFileHandler

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5054049656:AAGprHngT_jjX4HpZb8FhQ5n7xUNw6BRKPo")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "10536502"))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "711a8b2117137ce049845112d9f1dbb2")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001796982933"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5077269579"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "DkLink")

# Database
DB_URI = os.environ.get("DATABASE_URL", "postgres://xipareiv:fhpCSYJ10x7BdyGuiVj3krJRbloMKAPH@rosie.db.elephantsql.com/xipareiv")

# Username CH & Group
CHANNEL = os.environ.get("CHANNEL", "Lunatic0de")
GROUP = os.environ.get("GROUP", "SharingUserbot")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001773790754"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "-1001518010896"))


TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\n<b>Saya dapat menyimpan file pribadi di Channel Tertentu dan pengguna lain dapat mengaksesnya dari link khusus.</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hello {first}\n\nAnda harus bergabung di Channel/Grup saya Terlebih dahulu untuk Melihat File yang saya Bagikan\n\nSilakan Join Ke Channel & Group Terlebih Dahulu</b>",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == "True"

ADMINS.append(OWNER_ID)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
