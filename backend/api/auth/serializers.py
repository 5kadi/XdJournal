from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "last_login",
            "password",
            "email",
            "username",
            "is_active",
            "join_date",
            "avatar"
        ]
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
        
    #password somehow won't be hashed without this function
    def create(self, validated_data):
        #print(validated_data)
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user
    

class UserListSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "username",
            "is_active",
            "avatar"
        ]