from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = 29245477
        self.API_HASH = "0abc83883262245c90ca337b7a0375c4"
        self.BOT_TOKEN = ""
        self.MONGO_URL = "mongodb+srv://musicxrobot:8Up92WwJbgUS39FV@cluster0.ys1jirt.mongodb.net/"

        self.LOGGER_ID = (-1002456565415)
        self.OWNER_ID = 8667251104
        
        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", 60)) * 60
        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", 20))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", 20))

        self.SESSION1 = "BQFnJzYANPOCB0yOj2b9gxY4sdgozS1JMu0rk_44EnUC9JrZGVFxHqpX0KqlZiSR0PbBrUcSww5ic8oI0ZwY0SbC1arBZfP95eONbiU_oAGEMNRA4Om1Kg7fE4jCBWiqzgWXn_m2TY9RZyRv3rDo2OaBsj0srTuu2VUukMq4tuZ7kkFwhBPbs_NyZJvcsefoZdmAfHRLnhitxh9w1VoIoMkhbQW8fXAUsYmbKBo28BQEZwPwvM_c4GkLVLTxgmFBZGr2COlHjkc1zQQX4KFLKeazpRduQDSSPTx3EO9TFcBbh2WLMqwlaZImFj4QdNMxyb7H9sUvx_SDCVCwxFSHQ5ZeDyoA9AAAAAICq5w1AA"
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/AnimeNexusNetwork/160")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Anime_Chatting_Groups")

        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", "False").lower() == "true"
        self.AUTO_END: bool = getenv("AUTO_END", "False").lower() == "true"
    
        self.THUMB_GEN: bool = getenv("THUMB_GEN", "False").lower() == "true"
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", "True").lower() == "true"

        self.LANG_CODE = getenv("LANG_CODE", "en")

        self.COOKIES_URL = [
            url for url in getenv("COOKIES_URL", "https://batbin.me/conjugation").split(" ")
            if url and "batbin.me" in url
        ]
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://files.catbox.moe/1cdfqm.jpg")
        self.PING_IMG = getenv("PING_IMG", "https://files.catbox.moe/1cdfqm.jpg")
        self.START_IMG = getenv("START_IMG", "https://files.catbox.moe/1cdfqm.jpg")

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
