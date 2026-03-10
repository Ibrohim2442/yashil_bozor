from rest_framework import serializers

from .models import User, UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone',)

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('first_name','last_name','middle_name','birth_date','gender','email')