import json
from flask import session, request
from requests_oauthlib import OAuth2Session
from config import CLIENT_KEY, CLIENT_SECRET, AUTH_URL, TOKEN_URL, USER_URL, GUILDS_URL, SCOPE, REDIRECT_URL, MEDIA_URL, SERVER_ID, GUILDS_URL



def make_session( token = None, state = None, scope = None):
    return OAuth2Session(
        client_id = CLIENT_KEY,
        token = token,
        state = state,
        scope = scope,
        redirect_uri = REDIRECT_URL
    )

def get_auth_link():
    discord = make_session(scope = SCOPE)
    auth_url, state = discord.authorization_url(AUTH_URL)
    session['state'] = state
    return auth_url

def get_token():
    discord = make_session(state = session.get('state'))
    token = discord.fetch_token(
        TOKEN_URL,
        client_secret = CLIENT_SECRET,
        authorization_response = request.url
    )
    return token['access_token']


def get_profile(token):
    data = {}
    data['access_token'] = token
    discord = make_session(token = data)
    user = discord.get(USER_URL).json()
    avatar_href = "{}avatars/{}/{}.png?size=128".format(
        MEDIA_URL,
        user['id'],
        user['avatar']
    )
    return user['username'], user['discriminator'], avatar_href

def if_server_admin(token):
    data = {}
    data['access_token'] = token
    discord = make_session(token = data)
    guilds = discord.get(GUILDS_URL).json()
    for guild in guilds:
        if SERVER_ID == int(guild['id']):
            return True
    return False

