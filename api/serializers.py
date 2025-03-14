from rest_framework import serializers
from .models import News, CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email', 'city', 'password')



class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
