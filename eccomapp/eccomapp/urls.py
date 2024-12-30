"""
URL configuration for eccomapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from eccomapp.views import ListCreateProductAPIView, DairyListCreateAPIView, DairyRetrieveUpdateDestroyAPIView
from eccomapp.views import UserListCreateAPIView, ShippingAddressListCreateAPIView, UserRetrieveUpdateDestroyAPIView
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('product/', ListCreateProductAPIView.as_view()),
    path('dairy/', DairyListCreateAPIView.as_view()),
    path('dairy/<int:pk>/', DairyRetrieveUpdateDestroyAPIView.as_view()),
    path("user/", UserListCreateAPIView.as_view()),
    path("user/<int:pk>", UserRetrieveUpdateDestroyAPIView.as_view()),
    path("user/<int:user_id>/shipping/", ShippingAddressListCreateAPIView.as_view()),
] + debug_toolbar_urls()
