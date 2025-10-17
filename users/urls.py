from django.urls import path
from .views import RegisterView, CheckBalanceView, AddPointsView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('balance/', CheckBalanceView.as_view(), name='balance'),
    path('add-points/', AddPointsView.as_view(), name='add-points'),
]
