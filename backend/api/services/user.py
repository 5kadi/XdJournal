from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken
from api.serializers import UserSerializer

def decode_access(request):
    access_token = request.data.get('access')
    access_token_d = AccessToken(access_token)
    access_token_d.verify()

    user_id = access_token_d.get('user_id')
    user = get_user_model().objects.get(id=user_id)
    return user




