"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
# from scrumboard.api import CardViewSet, ListViewSet
from rest_framework.routers import DefaultRouter



# router = DefaultRouter()
# router.register(r'lists',ListViewSet)
# router.register(r'cards',CardViewSet)

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path(''. views.home, name='home')
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', views.home, name='home'),
    path('<str:room>/',views.room,name='room'),
    path('checkview',views.checkview,name='checkview'),
    path('send',views.send,name='send'),
    path('getMessages/<str:room>/',views.getMessages,name='getMessages'),
    ]



# urlpatterns = router.urls