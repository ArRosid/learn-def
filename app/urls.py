from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"article", views.ArticleViewSet)

urlpatterns = [
    # path('', views.home),
    path("login/", views.login),
    path("", include(router.urls)),
    # path('article/', views.ArticleViewSet.as_view()),
    # path('article/<int:pk>/', views.ArticleDetailView.as_view())
]