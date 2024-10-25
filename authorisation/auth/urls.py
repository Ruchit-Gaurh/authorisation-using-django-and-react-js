
from django.urls import path
from .views import welcome, TokenPairView, TRefreshView, logout, register

urlpatterns = [
    path('token/', TokenPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TRefreshView.as_view(), name='token_refresh'),
    path('welcome/', welcome),
    path('logout/', logout),
    path('register/', register),
]