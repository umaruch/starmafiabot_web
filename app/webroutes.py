from flask import render_template, session, redirect, url_for
from flask_login import current_user, logout_user
from app import app
from app import oauth
from app import models

@app.route("/")
def index():
    if current_user.is_anonymous:
        return url_for('auth')
    return url_for('logout')


#####################    User Urls  ##########################
@app.route('/auth')
def auth():
    if not current_user.is_anonymous:
        return redirect(url_for('index'))
    return redirect(oauth.get_auth_link())


@app.route('/callback')
def callback():
    if not current_user.is_anonymous:
        return redirect(url_for('index'))
    token = oauth.get_token()
    models.LoginUser.login(token)
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
###############################################################

#####################   Discord Users Operations        #######    