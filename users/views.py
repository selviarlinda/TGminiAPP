from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import render
from .models import CustomUser
from .serializers import UserRegistrationSerializer, BalanceSerializer
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

class RegisterView(APIView):
    """
    Конечная точка для регистрации нового пользователя.
    Методы:
    - GET: возвращает приветственное сообщение.
    - POST: создает нового пользователя.
    """
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({'message': 'Добро пожаловать на страницу регистрации!'}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Пользователь успешно зарегистрирован!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CheckBalanceView(APIView):
    """
    Конечная точка для проверки баланса пользователя.
    Метод:
    - GET: возвращает текущий баланс аутентифицированного пользователя.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if not user:
            return Response({'error': 'Пользователь не найден.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = BalanceSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AddPointsView(APIView):
    """
    Конечная точка для добавления баллов пользователю.
    Метод:
    - POST: добавляет указанное количество баллов к текущему балансу пользователя.
    """
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
        if user.balance is None:
            return Response({'error': 'Баланс пользователя не установлен.'}, status=status.HTTP_400_BAD_REQUEST)

        user.balance += points
        user.save()
        return Response({'message': f'{points} баллов успешно добавлено!'}, status=status.HTTP_200_OK)

def register_page(request):
    """
    Отображение HTML-страницы регистрации.
    """
    return render(request, 'users/register.html')
    
    

@csrf_exempt
def send_data(request):
    """
    Получение данных от Telegram MiniApp.
    """
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('user_id')
        username = data.get('username')

        # Логика обработки данных (например, сохранение в БД)
        print(f"Получены данные от пользователя {username} с ID {user_id}")

        return JsonResponse({'status': 'success', 'message': 'Данные успешно обработаны!'})

    return JsonResponse({'status': 'error', 'message': 'Метод не поддерживается.'}, status=400)
