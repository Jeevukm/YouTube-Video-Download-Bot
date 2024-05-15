import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7013794241:AAHhxQIbbVap_dMdbqVOd0EmDbDjFJlEcgo")
    API_ID = int(os.environ.get("API_ID", "23775436" ))
    API_HASH = os.environ.get("API_HASH", "e1d373b4fdf87794e8d8eaeb7ae43e0a")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "-1002132976766")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ''
