from rest_framework import serializers
from .models import Token, Portfolio, PortfolioToken, UserProfile, User

class UserSerializer(serializers.ModelSerializer):
    profile_pic_url = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'profile_pic_url']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_pic_url = validated_data.pop('profile_pic_url', None)
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(user=user, profile_pic_url=profile_pic_url)  # Create UserProfile for the new user
        return user

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'

class PortfolioTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioToken
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'
