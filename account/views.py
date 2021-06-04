from django.shortcuts import render
from .serializers import UserSerializer
from .models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, logout, login
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from rest_framework.decorators import permission_classes,api_view
from rest_framework.permissions import AllowAny


class signupView(APIView):
    @csrf_exempt
    def post(self, request):
        user = User.objects.create_user(email=request.data['email'], nickname=request.data['nickname'], gender=request.data['gender'], birth_date=request.data['birth_date'],password=request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"Token": token.key})

permission_classes = (AllowAny,)
@api_view(('POST',))
@csrf_exempt
def signin(request):
    if request.method == 'POST':
        mail = request.POST.get('email','abcd@gmail.com')
        pw = request.POST.get('password','1234')
        user = authenticate(email=mail, password=pw)
        print(user)
        if user is not None:
            login(request, user)
            print("login success!")

            return Response({"nickname":user.nickname, "birth_date":user.birth_date})
        else:
            print("login failed!")
            return Response({"mail":mail, "pw":pw})
    else:
        return  HttpResponse('POST 아님')

def signout(request):
        # simply delete the token to force a login
    logout(request)
    return HttpResponse('logout!')


class myinfo(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            user_id = request.user.id
            infoSerializer = UserSerializer(User.objects.get(id=user_id))
            return Response(infoSerializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=401)
