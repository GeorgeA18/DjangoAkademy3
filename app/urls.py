from django.urls import path
from django.urls import include
from .views import HomePageView

urlpatterns=[
    path("",HomePageView.as_view(),name = "home")
]
