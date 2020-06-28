from flask import render_template, session, redirect, url_for
from app import app
from app import oauth
from app import models
from config import SERVER_URL

@app.route("/")
def index():
    token = session.get('discord_token')
    if token:
        username, desc, avatar = oauth.get_profile(token)
        if oauth.if_server_admin(token):
            print("OK")
            server_url = None
            users =  models.User.query.all()
        else:
            print("Ne OK")
            server_url = SERVER_URL
            users = []
        print(server_url)
        return render_template(
            'index.html',
            fl = True,
            username = username,
            desc = desc,
            avatar = avatar,
            url = server_url,
            users = users
        )
    return render_template(
        'index.html',
        fl = False
    )

#####################    User Urls  ##########################
@app.route('/auth')
def auth():
    if session.get('discord_token'):
        return redirect(url_for('index'))
    return redirect(oauth.get_auth_link())


@app.route('/callback')
def callback():
    if session.get('discord_token'):
        return redirect(url_for('index'))
    token = oauth.get_token()
    session['discord_token'] = token
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session['discord_token'] = None
    return redirect(url_for('index'))
###############################################################

#####################   Discord Users Operations        #######    