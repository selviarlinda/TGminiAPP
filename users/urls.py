from django.urls import path
from .views import RegisterView, CheckBalanceView, AddPointsView, register_page

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('balance/', CheckBalanceView.as_view(), name='balance'),
    path('add-points/', AddPointsView.as_view(), name='add-points'),
    path('register-page/', register_page, name='register-page'),  # Новый маршрут для страницы регистрации
]
