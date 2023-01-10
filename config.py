import os
import ProxyCloud
# Bot
BOT_TOKEN = '5118830566:AAEvpUEOOSpbJVtzwJoBqJ24XjsCE1qrJSI'
TG_API_ID = '14000256'
TG_API_HASH = '61158815c58e158cfa9520c85676a450'
TG_ADMIN = 'andres950108'
TG_USER = 'andres950108'
static_proxy = 'socks5://KIDKKKYIJHJFGIYKJDGJGIYGKKHKJFRJFKLJDJLJ'
PROXY = ProxyCloud.parse(static_proxy)
# Database
DB_LOCAL = False
DB_HOST = 'db4free.net'
DB_HOST_USERNAME = 'andres950108'
DB_HOST_PASSWORD = 'andres950108'
DB_NAME = ''

if DB_LOCAL:
    # Database Local
    DB_HOST = ''
    DB_HOST_USERNAME = 'root'
    DB_HOST_PASSWORD = ''
    DB_NAME = 'clutilprodb'

