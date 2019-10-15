from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models
from . import serializers

@api_view(["GET"])
def home(request):
    return Response({"message":"Welcome Home!"},
                    status=status.HTTP_200_OK)

class ArticleListCreateAPIView(APIView):
    
    def get(self, request):
        articles = models.Article.objects.all()
        serializer = serializers.ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetailAPIView(APIView):
    
    def get(self, request, pk):
        article = models.Article.objects.get(id=pk)
        serializer = serializers.ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk):
        article = models.Article.objects.get(id=pk)
        serializer = serializers.ArticleSerializer(article, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = models.Article.objects.get(id=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)