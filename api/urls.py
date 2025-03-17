from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='test'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.CustomRegisterView.as_view(), name='register'),
    path('news/', views.NewsView.as_view(), name='news'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name='news_detail'),
    path('projects/', views.ProjectView.as_view(), name='report'),
]