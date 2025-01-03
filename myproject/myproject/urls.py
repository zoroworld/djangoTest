"""
URL configuration for myproject project.

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
# from .views import myfirstweb, myfirstweb2, mywebname, users
# from .views.users import update_delete_users, get_post_users
# from .views.better_views import UserListCreateApiView, UserRetrieveUpdateDestroyAPIView
from .views.custom_api_vews import UserListCreateAPIView
urlpatterns = [
    # path('', 'Hello to my world'),
    path('admin/', admin.site.urls),
    # path('hello/', myfirstweb),
    # path('hello2/', myfirstweb2),
    # path('helloname/<name>', mywebname)
    # path('users/', users),
    # path('users/', get_post_users),
    # path('users/<id>', update_delete_users),
    # path('users/', UserListCreateApiView.as_view()),
    # path('users/<id>', UserRetrieveUpdateDestroyAPIView.as_view()),
    path('users/', UserListCreateAPIView.as_view()),
]
