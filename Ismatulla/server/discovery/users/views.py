from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from .serializers import QuestionSerializer
from .utils import disc_map


class SignUpView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SignInView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            # Perform login, session management, or token generation here
            return Response({'message': 'Successfully signed in.'})
        else:
            return Response({'message': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

class QuestionTestView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            sum_chars = serializer.validated_data['sum_chars']
            # Process the number as needed
            res = int(sum_chars)  # For example, double the number
            character = next((value for key, value in disc_map.items() if res in key), 'Counselor (Si)')
            response_data = {'result': character}
            return Response(response_data)
        return Response(serializer.errors, status=400)
