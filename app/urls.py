from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('article/', views.ArticleListCreateView.as_view()),
    path('article/<int:pk>/', views.ArticleDetailView.as_view())
]