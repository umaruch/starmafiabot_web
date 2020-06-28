from flask import jsonify, request, session, abort
from app import app, db
from app import models
import config
import sys


@app.route('/bot/start', methods = ['GET'])
def start():
    if request.json and request.json.get('key', False):
            if request.json.get('key') == 'poiiielnahui':
                return jsonify(
                    {
                        'bot_token': config.BOT_TOKEN,
                        'server_id': config.SERVER_ID,
                        'online_id': config.ONLINE_CHANNEL_ID,
                        'users_id': config.USERS_CHANNEL_ID
                    } 
                )       
    abort(401)

@app.route('/bot/update/settings', methods = ['GET'])
def update_settings():
    if request.json and request.json.get('key', False):
            if request.json.get('key') == 'poiiielnahui':
                return jsonify(
                    {
                        'server_id': config.SERVER_ID,
                        'online_id': config.ONLINE_CHANNEL_ID,
                        'users_id': config.USERS_CHANNEL_ID
                    } 
                )       
    abort(401)

@app.route('/bot/update/users', methods = ['POST'])
def update_users():
    if request.json :
        if request.json.get('key') == 'poiiielnahui':
            users = request.json.get('users')
            #print(users, file=sys.stdout)
            for user_id in users:

                print(user_id, file=sys.stdout)
                db_user = models.User.query.filter_by(discord_id = user_id).first()
                user_info = users[user_id]
                print(user_info, file=sys.stdout)
                if not db_user:
                    db_user = models.User(discord_id = user_id, xp = user_info['xp'], messages = user_info['messages'], voice_time = user_info['voice_time'])
                    db.session.add(db_user)
                else:
                    db_user.xp += user_info['xp']
                    db_user.messages += user_info['messages']
                    db_user.voice_time += user_info['voice_time']
                
                db.session.commit()

            return jsonify({'status':'OK'})

    abort(401)


@app.route('/bot/info/user/<int:user_id>')
def get_user_info(user_id):
    if request.json:
        if request.json.get('key') == 'poiiielnahui':
            user = models.User.query.filter_by(discord_id = user_id).first()
            if not user:
                user = models.User(discord_id = user_id, xp = 0, messages = 0, voice_time = 0)
                db.session.add(user)
                db.session.commit()
            return jsonify({
                'xp': user.xp,
                'messages': user.messages,
                'voice_time': user.voice_time
            })
    abort(401) 
