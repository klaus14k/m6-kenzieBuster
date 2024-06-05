from rest_framework import serializers
from users.models import User
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(min_length=2, validators=[UniqueValidator(queryset=User.objects.all(), message="username already taken.")])
    email = serializers.EmailField(max_length=127, validators=[UniqueValidator(queryset=User.objects.all(), message="email already registered.")])
    birthdate = serializers.DateField(allow_null=True, default=None)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    password = serializers.CharField(min_length=2, write_only=True)
    is_employee = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data: dict) -> User:
        superuser = validated_data.get("is_employee")
        if superuser == True:
            return User.objects.create_superuser(**validated_data)
        return User.objects.create_user(**validated_data)
    
    def update(self, instance: User, validated_data: dict):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.set_password(validated_data.get("password", instance.password))
        instance.save()
        return instance