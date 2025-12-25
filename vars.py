#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "28389286"))
API_HASH = environ.get("API_HASH", "b88da5f4f338cca30f8ea5fb53cb083b")
BOT_TOKEN = environ.get("BOT_TOKEN", "8304937637:AAGl0NXbjoxceaUXxpbiIyGuc2rn1TrsCds")

OWNER = int(environ.get("OWNER", "6334323103"))
CREDIT = environ.get("CREDIT", "💫『 𝒟𝒾𝓋𝓎𝒶𝓃𝓈𝒽 𝓈𝒽𝓊𝓀𝓁𝒶 』💫")

TOTAL_USER = os.environ.get('TOTAL_USERS', '8056097370').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '8056097370').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set









