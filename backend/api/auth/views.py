from django.contrib.auth import get_user_model
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.exceptions import TokenError
#from api.models import CustomUser
from .serializers import *
from .services import *


class UserView(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request: Request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer) 
        else:
            return Response({'message': serializer.errors})
        
        headers = self.get_success_headers(serializer.data)
        token_pair = obtain_pair(request.data)
        user_data = serializer.data
        
        return Response(
            {
                "message": "Created an account successfully!", 
                **token_pair,
                "userData": user_data
            }, 
            status=201, 
            headers=headers
        )
    
    def patch_user_data(self, request: Request, id: int):
        user = self.queryset.get(pk=id)
        if user != request.user:
            return Response({"message": "You can't modify other users' data!"}, status=401)
        else:
            serializer = self.serializer_class(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Updated profile data successfully!", **serializer.data}, status=200)
            else:
                return Response({"message": serializer.errors}, status=400)

    def refresh_user_data(self, request: Request):
        #can just do this lmao
        user = request.user
        if user.is_authenticated:
            serializer = self.serializer_class(user)
            return Response(serializer.data, status=200)
        else:
            return Response({"message": "User is not authenticated!"}, status=401)

        """
        access_token = request.data.get('access')
        try:
            user = decode_access(access_token)
        except TokenError:
            return Response({"message": "Access token is invalid!"}, status=502)
    
        serializer = self.serializer_class(user)
        return Response(serializer.data)
        """
class CustomTokenObtainPairView(TokenObtainPairView):
        permission_classes = []
        
        def post(self, request: Request, *args, **kwargs) -> Response:
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                user = decode_access(serializer.validated_data['access']) #serializer.data is empty Xd
                user_data = UserSerializer(user).data
                return Response(
                    {
                        "message": "Logged in successfully!", 
                        **serializer.validated_data,
                        "userData": user_data
                    }, 
                    status=200
                )
            else:
                return Response({"message": serializer.errors}, status=400)