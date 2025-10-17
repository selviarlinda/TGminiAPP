from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import CustomUser
from .serializers import UserRegistrationSerializer, BalanceSerializer
from rest_framework.permissions import AllowAny

class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Пользователь успешно зарегистрирован!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CheckBalanceView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = BalanceSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AddPointsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        points = request.data.get('points')
        if not points:
            return Response({'error': 'Необходимо указать количество баллов.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            points = float(points)
        except ValueError:
            return Response({'error': 'Баллы должны быть числом.'}, status=status.HTTP_400_BAD_REQUEST)

        user = request.user
        user.balance += points
        user.save()
        return Response({'message': f'{points} баллов успешно добавлено!'}, status=status.HTTP_200_OK)
