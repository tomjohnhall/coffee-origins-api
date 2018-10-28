from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.CoffeeList.as_view()),
    path('<int:pk>/', views.CoffeeDetail.as_view()),
    path('profile/<int:user>/', views.ProfileDetail.as_view()),
    path('login/', views.CustomAuthToken.as_view()),
    path('staff-login/', views.AdminAuthToken.as_view()),
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/', include('rest_auth.registration.urls')),
    path('auth/account-confirm-email/<str:key>', views.CustomEmailConfirm),
]
