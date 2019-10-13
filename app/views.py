from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def home(request):
    return Response({"message":"Welcome Home!"},
                    status=status.HTTP_200_OK)