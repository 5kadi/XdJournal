from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken
from api.serializers import UserSerializer


def obtain_pair(user_data):
    token_pair = TokenObtainPairSerializer().validate(user_data)
    return token_pair


def decode_access(access_token):
    access_token_d = AccessToken(access_token)
    access_token_d.verify()

    user_id = access_token_d.get('user_id')
    user = get_user_model().objects.get(id=user_id)
    return user