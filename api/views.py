from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import News, CustomUser, Project
from .serializers import NewsSerializer, CustomUserSerializer, ProjectSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class HelloView(APIView):
    def get(self, request):
        return Response(data={"message": "Hello, World!"}, status=status.HTTP_200_OK)


class CustomRegisterView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        
        if serializer.is_valid():
            first_name = request.data.get("first_name")
            last_name = request.data.get("last_name")
            username = request.data.get("username")
            email = request.data.get("email")
            city = request.data.get("city")
            password = request.data.get("password")

            if CustomUser.objects.filter(email=email).exists():
                return Response({"message": "Eamil already exists!"}, status=status.HTTP_400_BAD_REQUEST)
            
            if CustomUser.objects.filter(username=username).exists():
                return Response({"message": "Username already exists!"}, status=status.HTTP_400_BAD_REQUEST)      


            user = CustomUser.objects.create_user(first_name=first_name, last_name=last_name, email=email, city=city, username=username, password=password)
            refresh = RefreshToken.for_user(user)
            
            return Response({
                "message": "User registered successfully!",
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors)

class NewsView(APIView):
    def get(self, request):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ProjectView(APIView):
    def get(self, request):
        serializer = ProjectSerializer(Project.objects.all(), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, requset):
        serializer = ProjectSerializer(data=requset.data)
        
        if not requset.user.is_verified:
            return Response({"message": "User is not verified!"}, status=status.HTTP_400_BAD_REQUEST)
        
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
