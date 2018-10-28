from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class CoffeeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'type', 'roaster', 'country', 'region', 'grower',
        'process', 'tasting', 'shopURL', 'location', 'images', 'last_in', 'next_in', 'created_at', 'updated_at',)
        model = models.Coffee

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = ('user', 'coffees', 'favourites',)
        model = models.Profile
