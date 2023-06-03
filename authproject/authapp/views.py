from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .models import User
from .serializers import UserRegistrationserializer , UserLoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
       
        'access': str(refresh.access_token),
    }


class UserRegistrationView(APIView):
    
    def post(self,request,format=None):
        serializer = UserRegistrationserializer(data = request.data )
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token=get_tokens_for_user(user)
            return Response({'token':token,"mgs" :"Registration sucessful"},
            status = status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user=authenticate(email=email,password=password)
            if user is not None:
                token=get_tokens_for_user(user)
                return Response({'token':token,"msg":"Login Sucess"},status=status.HTTP_200_OK)
            else:
                return Response({"errors":{'non_field_errors':['Email or password is not valid'] }} , status=status.HTTP_404_NOT_FOUND)