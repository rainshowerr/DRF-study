from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

@api_view(['GET']) # 데코레이터
def HelloAPI(request):
	return Response("Hello world!")

# Create your views here.
