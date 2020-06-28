class AppConfig:
    SECRET_KEY = 'i-never-asked-for-this'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CSRF_ENABLED = True
    DEBUG = True

#BASE SETTINGS
HOST = '127.0.0.1'
PORT = 5000

#OAUTH DISCORD
CLIENT_KEY = "707497788736536588"
CLIENT_SECRET = "uUPYvb0RqmM72yJpt7X4jVc8wO8vGeY8"
SCOPE = "identify guilds"
BASE_URL = "https://discordapp.com/api/"
AUTH_URL = BASE_URL + "oauth2/authorize"
TOKEN_URL = BASE_URL + "oauth2/token"
USER_URL = BASE_URL + "users/@me"
GUILDS_URL = BASE_URL + "users/@me/guilds"
MEDIA_URL = "https://cdn.discordapp.com/"
GUILDS_URL = BASE_URL + "users/@me/guilds"
REDIRECT_URL = "http://{}:{}/callback".format(
    HOST, PORT
)

#BOT SERVER SETTINGS
BOT_TOKEN = 'NzA3NDk3Nzg4NzM2NTM2NTg4.XvImkA.D4gx23u9eH8Hty_i_8JVDuW7T_s'
SERVER_ID = 665609184670121995
ONLINE_CHANNEL_ID = 712630705544364062
USERS_CHANNEL_ID = 712630741489549322
SERVER_URL = "https://discord.gg/DRV9x2d"