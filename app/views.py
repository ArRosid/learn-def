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