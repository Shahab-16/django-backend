from django.urls import path,include
from rest_framework.routers import DefaultRouter

from apps.users.views.user_login import UserLoginViewSet

router=DefaultRouter()

router.register('login',UserLoginViewSet,basename='login')

urlpatterns = [
    path('',view=include(router.urls)),
]