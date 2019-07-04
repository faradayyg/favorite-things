from django.contrib import admin
from thingsApi.models import FavouriteThing, Category, CustomUser

# Register your models here.
admin.site.register(FavouriteThing)
admin.site.register(Category)
admin.site.register(CustomUser)
