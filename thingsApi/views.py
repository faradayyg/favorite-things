"""All views for the thingsApi project."""
from rest_framework import generics
from rest_framework.views import APIView
from django.views.generic import TemplateView
from thingsApi.serializers import FavouriteThingSerializer, CategorySerializer
from thingsApi.models import FavouriteThing, Category
from thingsApi.permissions import IsOwner
from rest_framework.response import Response


class Home(TemplateView):
    """View for the base html file."""

    template_name = 'index.html'


class FavouriteThingList(generics.ListCreateAPIView):
    """Class based view for listing favorite things."""

    queryset = FavouriteThing.objects.all()
    permission_classes = (IsOwner,)
    serializer_class = FavouriteThingSerializer

    def list(self, request):
        """To retrieve the favourite thing created by logged in user."""
        queryset = FavouriteThing.objects.filter(user=request.user)
        serializer = FavouriteThingSerializer(queryset, many=True)
        return Response(serializer.data)


class SingleFavouriteThing(generics.RetrieveUpdateDestroyAPIView):
    queryset = FavouriteThing.objects.all()
    permission_classes = (IsOwner,)
    serializer_class = FavouriteThingSerializer


class CategoriesList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SingleCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsOwner,)


class CategoryThings(generics.RetrieveUpdateDestroyAPIView):
    queryset = FavouriteThing.objects.all()
    serializer_class = FavouriteThingSerializer

    # To retrieve the favourite thing created by logged in user
    def retrieve(self, request, pk=None):
        queryset = FavouriteThing.objects.filter(
            user=request.user, category_id=pk
        )
        serializer = FavouriteThingSerializer(queryset, many=True)
        return Response(serializer.data)


class NotFound(APIView):
    def get(self, request, format=None):
        return Response({"message": "The resource you are looking\
         for does not exist"}, 404)
