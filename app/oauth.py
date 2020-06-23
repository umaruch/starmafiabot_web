import json
from flask import session, request
from requests_oauthlib import OAuth2Session
from config import CLIENT_KEY, CLIENT_SECRET, AUTH_URL, TOKEN_URL, USER_URL, GUILDS_URL, SCOPE, REDIRECT_URL


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