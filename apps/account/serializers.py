from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'bio', 'email', 'role')

    def validate(self, attrs):
        if not self.partial and User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({'email': 'Пользователь с таким email уже создан'})
        return attrs


class UserSelfSerializer(UserSerializer):
    role = serializers.CharField(read_only=True)
