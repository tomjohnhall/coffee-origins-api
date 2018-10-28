from rest_framework import generics, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse

from . import models
from . import serializers

class OwnProfilePermission(permissions.BasePermission):
    """
    Object-level permission to only allow updating his own profile
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # obj here is a UserProfile instance
        return obj.user == request.user

class CoffeeList(generics.ListCreateAPIView):
    permissions_classes = permissions.DjangoModelPermissionsOrAnonReadOnly
    queryset = models.Coffee.objects.all()
    serializer_class = serializers.CoffeeSerializer

class CoffeeDetail(generics.RetrieveUpdateDestroyAPIView):
    permissions_classes = permissions.DjangoModelPermissionsOrAnonReadOnly
    queryset = models.Coffee.objects.all()
    serializer_class = serializers.CoffeeSerializer

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    lookup_field = 'user'
    permission_classes = (OwnProfilePermission,)

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
        })

class AdminAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        if user.is_staff:
            return Response({
                'token': token.key,
                'user_id': user.pk,
            })
        else:
            return HttpResponse('Unauthorized', status=401)

def CustomEmailConfirm(request):
    JsonResponse({'success': True})
