from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns=[
    path("booking/",views.BookingView.as_view()),
    path('menu/',views.MenuView.as_view())
]