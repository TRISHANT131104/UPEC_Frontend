"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from .views import __get__group__messages__,__get__personal__chat__,__get__ai__messages__,__get__user__data__,__get__users__recent__chat__,__create__project__,__send__generated__prd__,__get__details__of__project__,__client__accept__bid__,__send__generated__workflow__

urlpatterns = [
    path('__get__group__messages__/<uuid:pk>', __get__group__messages__.as_view()),
    path('__get__personal__chat__/<int:pk>', __get__personal__chat__.as_view()),
    path('__get__ai__messages__', __get__ai__messages__.as_view()),
    path('__get__user__data__',__get__user__data__.as_view()),
    path('__get__users__recent__chat__',__get__users__recent__chat__.as_view()),
    path('__create__project__/',__create__project__.as_view()),
    path('__send__generated__prd__/', __send__generated__prd__.as_view()),
    path('__get__details__of__project__/<int:pk>', __get__details__of__project__.as_view()),
    path('__client__accept__bid__/', __client__accept__bid__.as_view()),
    path('__send__generated__workflow__/', __send__generated__workflow__.as_view()),

]
