"""
URL configuration for api app.

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
from django.urls import path

from .views import (
    __create__project__,
    __get__ai__messages__,
    __get__all__projects__,
    __get__details__of__project__,
    __get__direct__chat__users__,
    __get__each__project__,
    __get__group__chat__users__,
    __get__group__messages__,
    __get__personal__chat__,
    __get__project__recommendations__,
    __get__project__related__groups__,
    __get__user__data__,
    __get__users__recent__chat__,
    __learning__resource__,
    __project__management__,
    __get__all__projects__,
    __get__each__project__,
    __get__project__recommendations__,
    __get__users__ongoing__projects__,
    __get__team__related__to__project__,
    __send__generated__prd__,
    __send__generated__workflow__,
    __learning__resources__for__talents__,

)

urlpatterns = [
    path("__get__group__messages__/", __get__group__messages__.as_view()),
    path("__get__personal__messages__/", __get__personal__chat__.as_view()),
    path("__get__direct__chat__users__/<int:pk>", __get__direct__chat__users__.as_view()),
    path("__get__group__chat__users__/<int:pk>", __get__group__chat__users__.as_view()),
    path("__get__project__related__groups__/<int:pk>",__get__project__related__groups__.as_view(),),
    path("__get__ai__messages__", __get__ai__messages__.as_view()),
    path("__get__user__data__/<int:pk>", __get__user__data__.as_view()),
    path("__get__users__recent__chat__", __get__users__recent__chat__.as_view()),
    path("__create__project__/", __create__project__.as_view()),
    path("__send__generated__prd__/", __send__generated__prd__.as_view()),
    path("__get__details__of__project__/<int:pk>", __get__details__of__project__.as_view(),),
    path("__send__generated__workflow__/", __send__generated__workflow__.as_view()),
    path("__learning__resource__/", __learning__resource__.as_view()),
    path("__learning__resources__for__talents__/", __learning__resources__for__talents__.as_view()),
    path("__project__management__/", __project__management__.as_view()),
    path("__get__all__projects__/",__get__all__projects__.as_view()),
    path("__get__each__project__/<int:pk>",__get__each__project__.as_view()),
    path("__get__project__recommendations__/", __get__project__recommendations__.as_view()),
    path("__get__users__ongoing__projects__/<int:pk>",__get__users__ongoing__projects__.as_view()),
    path("__get__team__related__to__project__/<int:pk>",__get__team__related__to__project__.as_view()),
    path("__get__all__projects__/", __get__all__projects__.as_view()),
    path("__get__each__project__/<int:pk>", __get__each__project__.as_view()),
    path("__get__project__recommendations__/",__get__project__recommendations__.as_view(),),
]
