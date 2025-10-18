from django.urls import path
from .views import RegisterView, CheckBalanceView, AddPointsView, register_page, send_data

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('balance/', CheckBalanceView.as_view(), name='balance'),
    path('add-points/', AddPointsView.as_view(), name='add-points'),
    path('register-page/', register_page, name='register-page'),
    path('send-data/', send_data, name='send-data'),  # Новый маршрут для Telegram MiniApp
]
