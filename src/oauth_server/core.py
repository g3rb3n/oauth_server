import random
import string

from oauth_server.models import Configuration
from oauth_server.oauth import OAuth
from oauth_server.settings import PORT, REDIRECT_URI


configurations = {}
codes = {}


def generate_shortcode():
    return ''.join(random.choice(string.ascii_uppercase) for i in range(4))


def initialize(data: Configuration):
    shortcode = generate_shortcode()
    configurations[shortcode] = data
    return shortcode


def get_redirect_url(shortcode: str):
    config = configurations[shortcode]
    client_id = config.client_id
    client_secret = config.client_secret
    scope = config.scope
    auth_manager = OAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=REDIRECT_URI,
        scope=scope,
        open_browser=False,
    )
    return auth_manager.get_authorize_url()


def callback(code):
    shortcode = generate_shortcode()
    codes[shortcode] = code
    return shortcode


def get_code(shortcode):
    return codes[shortcode]
