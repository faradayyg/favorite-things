from django.contrib import admin
from django.urls import path
from thingsApi.views import FavouriteThingList, SingleFavouriteThing

urlpatterns = [
    path('things/<int:pk>', SingleFavouriteThing.as_view()),
    path('', FavouriteThingList.as_view()),
]
