from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializer import UserRegSer

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

class TokenPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            tokens = response.data

            access_token= tokens['access']
            refresh_token= tokens['refresh']

            res = Response()
            res.data = {'success': True}

            res.set_cookie(
                key="access_token",
                value=access_token,
                httponly=True,
                secure=True,
                samesite='None',
                path='/',
            )

            res.set_cookie(
                key="refresh_token",
                value=refresh_token,
                httponly=True,
                secure=True,
                samesite='None',
                path='/',
            )

            return res

        except:
            return Response({'success':False})
        
class TRefreshView(TokenRefreshView):
    def post(self,request, *args, **kwargs):
        try:
            refresh_token= request.COOKIES.get("refresh_token")

            request.data['refresh'] = refresh_token
            response = super().post(request, *args, **kwargs)

            tokens = response.data
            access_token = tokens['access']

            res = Response()
            res.data = {'refresed': True}

            res.set_cookie(
                key='access_token',
                value=access_token,
                httponly=True,
                secure=True,
                samesite='None',
                path='/',
            )
            return res
        except:
            return Response()
        
@api_view(['POST'])
def logout(request):
    try:
        res = Response()
        res.data = {"success": True}
        res.delete_cookie('access_token', path='/', samesite='None')
        res.delete_cookie('refresh_token', path='/', samesite='None')
        return res
    except:
        return Response({'success': False})


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    seri = UserRegSer(data=request.data)
    if seri.is_valid():
        seri.save()
        return Response(seri.data)
    return Response(seri.error)

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def welcome(request):
    user = request.user
    return Response("Hi User")