from app import db, lm
from flask_login import UserMixin, login_user

class LoginUser(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    discord_token =  db.Column(db.String(64), nullable = False, unique = True)

    @staticmethod
    def login(token):
        user = LoginUser.query.filter_by(discord_token = token).first()
        if not user:
            user = LoginUser(discord_token = token)
            db.session.add(user)
            db.session.commit()
        login_user(user, True)



@lm.user_loader
def load_user(id):
    return LoginUser.query.get(id)