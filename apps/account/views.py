from django.shortcuts import get_object_or_404
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import User
from .permissions import IsAdminPermission
from .serializers import UserSerializer, UserSelfSerializer


class UserListAPIView(ListCreateAPIView):
    permission_classes = (IsAdminPermission, )
    serializer_class = UserSerializer
    filter_backends = [SearchFilter]
    queryset = User.objects.all()
    search_fields = ('username', )


class UserDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminPermission]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])


class UserSelfDetailAPIView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSelfSerializer

    def get_object(self):
        return self.request.user
