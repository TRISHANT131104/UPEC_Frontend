from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
import logging
from rest_framework.exceptions import ValidationError
from urllib.parse import urlparse, parse_qs
from django.contrib.auth import get_user_model
User = get_user_model()
import requests  # Import the requests library to make API calls

logger = logging.getLogger(__name__)

class CustomGoogleOAuth2Adapter(GoogleOAuth2Adapter):

    def complete_login(self, request, app, token, **kwargs):
        login = super().complete_login(request, app, token, **kwargs)

        query_parameters = parse_qs(urlparse(request.get_full_path()).query)
        role = query_parameters.get("role", None)

        # Check if this is the first signup
        is_first_signup = not User.objects.filter(email=login.user.email).exists()

        if is_first_signup:
            # Fetch the user's profile information including the profile image
            profile_url = 'https://www.googleapis.com/oauth2/v2/userinfo'
            headers = {'Authorization': f'Bearer {token.token}'}
            response = requests.get(profile_url, headers=headers)

            if response.status_code == 200:
                user_info = response.json()

                profile_image_url = user_info.get('picture')
                
                if profile_image_url:
                    login.user.image = profile_image_url
                if role is not None:
                    login.user.username = login.user.first_name + login.user.last_name
                    login.user.role = role[0]
                else:
                    raise ValidationError('User\'s Role Must Be Specified')
            else:
                raise ValidationError('Failed to fetch user profile information')

        return login