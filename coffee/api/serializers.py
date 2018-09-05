from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class CoffeeSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'description', 'location', 'images', 'created_at', 'updated_at',)
        model = models.Coffee

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    coffees = serializers.PrimaryKeyRelatedField(many=True, queryset=models.Coffee.objects.all())
    favourites = serializers.PrimaryKeyRelatedField(many=True, queryset=models.Coffee.objects.all())

    class Meta:
        fields = ('user', 'coffees', 'favourites',)
        model = models.Profile
