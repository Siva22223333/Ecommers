from django.shortcuts import render
from .models import Useraccount
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound ,AuthenticationFailed
from .serializers import SignInSerializer,SignIngetSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
import secrets
from cryptography.fernet import Fernet 
from django.contrib.auth.hashers import check_password,make_password


# Create your views here.


@api_view(['POST'])
def signindatalist(request):
    if request.method == 'POST':
        serializer = SignInSerializer(data=request.data)
        if serializer.is_valid():
            user_data=serializer.validated_data

            #Token creation
            token = secrets.token_hex(16)
            user_data['token']=token

            #Encryp password
            
            
            hashed_password = make_password(user_data['password'])
            user_data['password'] = hashed_password
         
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class logindatalist(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
           
            user = Useraccount.objects.get(email=email)
        except Useraccount.DoesNotExist:
           
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)
        if check_password(password, user.password):
           
            token = secrets.token_hex(16)
            user.token = token
            user.save() 
            
            return Response({'message': 'Login successful', 'token': token}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)

class signindataget(APIView):
    def get(self, request, id):

        token=request.headers.get('Authorization')

        if not token:
            return Response({'message':'token is not found'},status=status.HTTP_401_UNAUTHORIZED)
        try:
            data = Useraccount.objects.get(id=id,token=token) 

        except Useraccount.DoesNotExist:
            raise NotFound("user not found")
        
        serializer = SignIngetSerializer(data)
        return Response(serializer.data)

class signindataput(APIView):
    def put(self, request, id):
        try:
            data = Useraccount.objects.get(id=id)
        except Useraccount.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SignInSerializer(data, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class signindatadelete(APIView):
    def delete(self,request,id):
        data=Useraccount.objects.get(id=id)
        data.delete()
        return Response(status=status.HTTP_200_OK)
        


