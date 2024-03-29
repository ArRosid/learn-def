from django.shortcuts import render
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import (IsAuthenticated,
                                        IsAdminUser,
                                        IsAuthenticatedOrReadOnly)

from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token

from . import models
from . import serializers
from .permissions import IsOwnArticleOrReadOnly

# @api_view(["GET"])
# def home(request):
    # return Response({"message":"Welcome Home!"},
    #                 status=status.HTTP_200_OK)

# class ArticleListCreateAPIView(APIView):
    
    # def get(self, request):
    #     articles = models.Article.objects.all()
    #     serializer = serializers.ArticleSerializer(articles, many=True)
    #     return Response(serializer.data)

    # def post(self, request):
    #     serializer = serializers.ArticleSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ArticleDetailAPIView(APIView):
    
    # def get(self, request, pk):
    #     article = models.Article.objects.get(id=pk)
    #     serializer = serializers.ArticleSerializer(article)
    #     return Response(serializer.data)

    # def put(self, request, pk):
    #     article = models.Article.objects.get(id=pk)
    #     serializer = serializers.ArticleSerializer(article, request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk):
    #     article = models.Article.objects.get(id=pk)
    #     article.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

# class ArticleListCreateView(generics.ListCreateAPIView):
    # queryset = models.Article.objects.all()
    # serializer_class = serializers.ArticleSerializer

# class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = models.Article.objects.all()
    # serializer_class = serializers.ArticleSerializer

@csrf_exempt
@api_view(['POST'])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None and password is None:
        return Response({'error':'Please provide both username & password'},
                        status=status.HTTP_400_BAD_REQUEST)
    
    user = authenticate(username=username, password=password)

    if not user:
        return Response({'error': 'Invalid credentials'},
                        status=status.HTTP_404_NOT_FOUND)
    
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token':token.key},
                    status=status.HTTP_200_OK)

class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ArticleSerializer
    queryset = models.Article.objects.all()
    permission_classes = [IsAuthenticated, IsOwnArticleOrReadOnly]