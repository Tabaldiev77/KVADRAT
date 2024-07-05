from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from myapp.models import CustomUser
from myapp.serializers import *
from django.views import View
from django.http import HttpResponse
from rest_framework.generics import ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView


class RegisterView(APIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'email': user.email, 'first_name': user.first_name, 'last_name': user.last_name}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class VerifyEmail(View):
    def get(self, request, uidb64, token):
        # Your verification logic here
        return HttpResponse("Email verified")

      
class GetUserAPIView(ListAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer

