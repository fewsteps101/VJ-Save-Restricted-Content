import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "20963218"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "f563ddc5e2332a0788c58d50cbd166ca")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://kulabkarm04:pdOQrphU3D5BQ664@cluster0.hj1la.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
