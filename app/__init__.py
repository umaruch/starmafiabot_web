from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

import os
from config import AppConfig
#Для того чтобы позволить работать входу через дискорд работать в хттп(БЕЗ "С")
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask('SpaceMafiaBot')
app.config.from_object(AppConfig)
db = SQLAlchemy(app)
lm = LoginManager(app)

from app import webroutes, botroutes


#Дропаем базу данных только в случае неполадок которые лень исправлять или если просто делать нехер
def drop_db():
    try:
        from app import models

        db.drop_all()
        db.create_all()
        return "DATABASE CREATED"
    except Exception as e:
        return e