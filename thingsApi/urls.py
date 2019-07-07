from django.contrib import admin
from django.urls import path, re_path

from thingsApi.views import (
	FavouriteThingList, 
	SingleFavouriteThing, 
	CategoriesList, 
	SingleCategory, 
	CategoryThings ,
	NotFound
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('things/<int:pk>/', SingleFavouriteThing.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('things/', FavouriteThingList.as_view()),
    path('things/categories/', CategoriesList.as_view()),
    path('things/categories/<int:pk>/', SingleCategory.as_view()),
    path('things/categories/<int:pk>/items/', CategoryThings.as_view()),
    re_path(r".*", NotFound.as_view()),
]
