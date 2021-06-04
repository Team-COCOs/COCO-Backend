from django.shortcuts import render
from .models import Acceleration, Sound
from .serializers import AccPutSerializer, SoundCountSerializer, SoundPutSerializer,SoundCountSerializer, AccCountSerializer
import json
from django.views import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse

class AccCreateAPIView(APIView):
    """
    POST 
    """
    def post(self, request):
        accSerializer = AccPutSerializer(data=request.data) #Request의 data를 UserSerializer로 변환
 
        if accSerializer.is_valid():
            accSerializer.save() #UserSerializer의 유효성 검사를 한 뒤 DB에 저장
            return Response(accSerializer.data, status=status.HTTP_201_CREATED) #client에게 JSON response 전달
        else:
            return Response(accSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request,  **kwargs):
        if kwargs.get('id') is None:
            query = Acceleration.objects.all() #모든 User의 정보를 불러온다.
            accSerializer = AccPutSerializer(query, many=True)
            return Response(accSerializer.data, status=status.HTTP_200_OK)
        else:
            id = kwargs.get('id')
            accSerializer = AccPutSerializer(Acceleration.objects.get(id=id)) #id에 해당하는 User의 정보를 불러온다
            return Response(accSerializer.data, status=status.HTTP_200_OK)


class SoundCreateAPIView(APIView):
    """
    POST 
    """
    def post(self, request):
        soundSerializer = SoundPutSerializer(data=request.data) #Request의 data를 UserSerializer로 변환
 
        if soundSerializer.is_valid():
            soundSerializer.save() #UserSerializer의 유효성 검사를 한 뒤 DB에 저장
            return Response(soundSerializer.data, status=status.HTTP_201_CREATED) #client에게 JSON response 전달
        else:
            return Response(soundSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request,  **kwargs):
        if kwargs.get('id') is None:
            query = Sound.objects.all() #모든 User의 정보를 불러온다.
            soundSerializer = SoundPutSerializer(query, many=True)
            return Response(soundSerializer.data, status=status.HTTP_200_OK)
        else:
            id = kwargs.get('id')
            soundSerializer = SoundPutSerializer(Sound.objects.get(id=id)) #id에 해당하는 User의 정보를 불러온다
            return Response(soundSerializer.data, status=status.HTTP_200_OK)

class SoundGetAPIView(APIView):
    def get(self,request, **kwargs):
        if kwargs.get('id') is None:
            query = Sound.objects.all()
            countSerializer = SoundCountSerializer(query, many=True)
            return Response(countSerializer.data, status=status.HTTP_200_OK)
        else:
            id = kwargs.get('id')
            countSerializer = SoundCountSerializer(Sound.objects.get(id=id))
            return Response(countSerializer.data, status=status.HTTP_200_OK)

class AccGetAPIVIEW(APIView):
    def get(self,request, **kwargs):
        if kwargs.get('id') is None:
            query = Acceleration.objects.all()
            countSerializer = AccCountSerializer(query,many = True)
            return Response(countSerializer.data, status=status.HTTP_200_OK)
        else:
            id = kwargs.get('id')
            countSerializer = AccCountSerializer(Acceleration.objects.get(id=id))
            return Response(countSerializer.data, status=status.HTTP_200_OK)

class CountGetAPI(APIView):
    def get(self,request,**kwargs):
        if kwargs.get('id') is None:
            acccountSerializer = AccCountSerializer(Acceleration.objects.all() ,many = True)
            soundcountSerializer = SoundCountSerializer(Sound.objects.all(), many=True)
            counts = { "acc" : acccountSerializer.data, "sound" : soundcountSerializer.data}
            print(json.dumps(counts))
            print("main pages")
            return Response(counts, status=status.HTTP_200_OK)


class ScoreGetAPI(APIView):
    def get(self,request,**kwargs):
        if kwargs.get('id') is None:
            data = {"score" : 38}
            return Response(data, status=status.HTTP_200_OK)