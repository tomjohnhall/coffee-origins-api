from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.CoffeeList.as_view()),
    path('<int:pk>/', views.CoffeeDetail.as_view()),
]
