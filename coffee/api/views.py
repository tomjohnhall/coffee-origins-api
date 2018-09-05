from rest_framework import generics

from . import models
from . import serializers

class CoffeeList(generics.ListCreateAPIView):
    queryset = models.Coffee.objects.all()
    serializer_class = serializers.CoffeeSerializer

class CoffeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Coffee.objects.all()
    serializer_class = serializers.CoffeeSerializer

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
