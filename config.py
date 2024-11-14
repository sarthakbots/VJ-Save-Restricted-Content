import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "29087369"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "40ed2d8463429caabbdd97569f9de5a3")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://sarthak31052013:rWFezcypdZS65G11@cluster0.jepsg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
