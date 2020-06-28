from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    discord_id = db.Column(db.Integer, unique = True, nullable = False)
    xp = db.Column(db.Integer, default = 0)
    messages = db.Column(db.Integer, default = 0)
    voice_time = db.Column(db.Integer, default = 0)#В минутах

    def __repr__(self):
        return f"User Object <{self.discord_id}>"
