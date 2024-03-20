from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login as auth_login
from .serializers import *
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

class RegisterApiView(APIView):
    def  post(self,request,format=None):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)
            response = {'status':'success','message': 'User Created Successfully',"token":str(token)}
            return Response(response,status=status.HTTP_201_CREATED)
        else:
            #return HttpResponse("Invalid data")
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class LoginApiView(APIView):
    def  post(self,request,format=None):
        username = request.DATA['username']
        password = request.DATA['password']
        user =authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                token = Token.objects.get_or_create(user=user)
                response={'status':'login successfull','token': str(token[0])}
                return Response(response,status=status.HTTP_200_OK)
            else:
                return Response({'error':'Unauthorized'},status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error':'Invalid Credentials'},status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    def post(self, request):
        try:
            token = request.user.auth_token
            token.delete()
            return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)