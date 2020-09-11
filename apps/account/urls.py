from django.urls import path

from .views import UserListAPIView, UserDetailAPIView, UserSelfDetailAPIView

app_name = 'user'

urlpatterns = [
    path('', UserListAPIView.as_view(), name='users_list'),
    path('me/', UserSelfDetailAPIView.as_view(), name='users_detail'),
    path('<str:username>/', UserDetailAPIView.as_view(), name='users_detail'),
]
