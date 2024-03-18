from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import AccessToken
from users.models import User

import base64
import jwt

class CustomJWTAuthentication(JWTAuthentication):

    def authenticate(self, request):
        # Get the Authorization header from the request
        auth_header = request.headers.get('Authorization')
        
        if not auth_header:
            return None

        try:
            auth_type, token = auth_header.split()
        except ValueError:
            # If the header does not contain both type and token, return None
            return None

        if auth_type == 'Octoxlabs':
            try:
                decoded_token_ = base64.b64decode(token).decode('utf-8')
                try:
                    decoded_payload = jwt.decode(decoded_token_, settings.SECRET_KEY, algorithms=["HS256"])
                except:
                    raise AuthenticationFailed('Invalid token')
                user_id = decoded_payload['user_id']
                user = User.objects.get(id=user_id)
                if not user:
                    raise AuthenticationFailed('User not found')
                return (user, None)
            except (ValueError, UnicodeDecodeError):
                raise AuthenticationFailed('Invalid token')
        
        return None