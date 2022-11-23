import os, re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']
USERBOT_STRING_SESSION = environ.get('USERBOT_STRING_SESSION')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')




# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 1800))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', '         https://telegra.ph/file/ebef13d4970e8b3890b8f.jpg https://telegra.ph/file/eb40522f8856591fa4c1b.jpg https://telegra.ph/file/b2179df41ca9c35f3dee3.jpg https://telegra.ph/file/1aff95f3fd9e5b1263243.jpg https://telegra.ph/file/bc0db6afb659a9b81c4ad.jpg https://telegra.ph/file/5c8fc7cc44e099332aef5.jpg          
TUTORIAL = environ.get("M_NT_F", "https://telegra.ph/file/b9c8a8240590623ba43ee.jpg")



#part 1

DEL_SEC = int(os.environ.get("DEL_SEC", "10"))

DEL_SECOND = int(os.environ.get("DEL_SECOND", "300"))
CREATOR_USERNAME = os.environ.get("CREATOR_USERNAME", "sahid_malik")
CREATOR_NAME = os.environ.get("CREATOR_NAME", "sahid malik")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "hjhjvjjjvbot")

#part 2
MALIK = environ.get("malik", "https://telegra.ph/file/a35a995c9c411048adfab.jpg")
MALIK5 = environ.get("malik5", "https://telegra.ph/file/a00c405a374d21ea7cfb7.jpg")


AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
AUTO_DELETE2 = is_enabled((environ.get('AUTO_DELETE2', "True")), True)

#part 3

FILTER_BUTTONS = os.environ.get("FILTER_BUTTONS", "10")
DB_AUTO_DELETE = is_enabled((environ.get('DB_AUTO_DELETE', "True")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)




# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5217619970').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '1001687091406').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Lovely:Lovely@cluster0.fsid0.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Rajappan")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
LOG_CHANNEL2 = int(environ.get('LOG_CHANNEL2', 0))
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'm_house786')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "False")), False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", None)
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", None) #<b>🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

SHORTENER_API = environ.get("SHORTENER_API", "iQ2iqO9EXFbcjek412Dg5j6stWu2")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "shareus.in")
SHORT_URL = is_enabled((environ.get('SHORT_URL', "True")), True)
TUTORIAL_LINK = environ.get("TUTORIAL_LINK", "https://youtu.be/MKNd7AP5xLE")



LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

DELL_SEC = int(os.environ.get("DELL_SECOND", "60"))
DELL_SECOND = int(os.environ.get("DELL_SECOND", "60"))

MBGH = """Hay {}.\n\n {} results are already available for your query"""
MAINTENANCE_MODE = is_enabled((environ.get('MAINTENANCE_MODE', "False")), False)
PM_MAINTENANCE_MODE = is_enabled((environ.get('PM_MAINTENANCE_MODE', "False")), False)



SHORT_URLL = is_enabled((environ.get('SHORT_URLL', "False")), False)
SHORTENER_API2 = environ.get("SHORTENER_API", None)
LONG_MEGHA_URL = environ.get("LONG_MEGHA_URL", False)


REQ_GRPOUP = int(environ.get('REQ_GRPOUP'))

REQ_GRP = int(environ.get('REQ_GRP', '-1001566860282')



