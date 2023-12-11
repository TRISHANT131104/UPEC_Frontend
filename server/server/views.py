from .adapters import CustomGoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView

class GoogleLogin(SocialLoginView): # if you want to use Authorization Code Grant, use this
    adapter_class = CustomGoogleOAuth2Adapter
    callback_url = "http://localhost:3000"
    client_class = OAuth2Client