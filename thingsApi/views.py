from rest_framework import generics
from django.views.generic import TemplateView
from thingsApi.serializers import FavouriteThingSerializer
from thingsApi.models import FavouriteThing


class Home(TemplateView):
    template_name = 'index.html'


class FavouriteThingList(generics.ListCreateAPIView):
    queryset = FavouriteThing.objects.all()
    serializer_class = FavouriteThingSerializer


class SingleFavouriteThing(generics.RetrieveUpdateDestroyAPIView):
    queryset = FavouriteThing.objects.all()
    serializer_class = FavouriteThingSerializer
