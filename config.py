import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7988382678:AAF28iuo2taxdZL5J8FJvVDJVjxpy7T-6Ew")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "22528446"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "0d81bf18019c5f3839037d0ae737c358")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "633111330"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://vikassonawale0:JWyQFas7vlG1bkaL@cluster0.beermge.mongodb.net/?retryWrites=true&w=majority") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "Cluster0")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
