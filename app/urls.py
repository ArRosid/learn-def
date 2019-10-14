from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('article', views.ArticleListCreateAPIView.as_view())
]