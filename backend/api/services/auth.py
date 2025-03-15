from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



def obtain_pair(user_data):
    token_pair = TokenObtainPairSerializer().validate(user_data)
    return token_pair