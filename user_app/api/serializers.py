import re
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from user_app.models import CustomUser


# Custom Password Validator function
def password_validator_check(password):
    if len(password) < 8:
        raise serializers.ValidationError(
            "Make sure your password is at lest 8 letters"
        )
    elif re.search("[0-9]", password) is None:
        raise serializers.ValidationError("Make sure your password has a number in it")
    elif re.search("[A-Za-z]", password) is None:
        raise serializers.ValidationError(
            "Make sure your password has a alphabet in it"
        )
    else:
        return password


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "password"]

    @staticmethod
    def validate_password(value: str) -> str:
        # Regular expression for strong password
        password_validator_check(value)
        # Function to hash password
        return make_password(value)

    @staticmethod
    def validate_username(value: str) -> str:
        # Len validator
        if len(value) < 4:
            raise serializers.ValidationError(
                {"Error": "Username must contains minimum 4 words"}
            )
        return value

    def create(self, validated_data) -> object:
        return CustomUser.objects.create(**validated_data)
