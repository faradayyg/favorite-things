from django.contrib.auth.models import User, Group
from rest_framework import serializers
from thingsApi.models import FavouriteThing


class FavouriteThingSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(required=False)
    ranking = serializers.IntegerField(required=False)
    meta_data = serializers.CharField(required=False)
    category_id = serializers.IntegerField()
    category = serializers.ReadOnlyField(source='category.name')

    def create(self, validated_data):
        category_id = validated_data['category_id']
        if 'ranking' in validated_data:
            # check what position
            intended_ranking = validated_data['ranking']
            subsequent_positions = FavouriteThing.objects.filter(
                ranking__gte=intended_ranking, category_id=category_id)

            # shift other ranks accordingly
            for favourite_thing in subsequent_positions:
                self.increment_ranking(favourite_thing)
            # check if increment worked
            integrity_check = FavouriteThing.objects.filter(
                ranking=intended_ranking, category_id=category_id).first()
            if integrity_check is None:
                return FavouriteThing.objects.create(**validated_data)
            else:
                raise Exception('An Error Occurred, rankings were not updated')
        else:
            # Get Last ranking
            least_ranking_thing = FavouriteThing.objects.filter(
                category_id=category_id).order_by('-ranking').first()

            # increment and save
            if least_ranking_thing:
                new_least_ranking = least_ranking_thing.ranking + 1
            else:
                new_least_ranking = 1

            validated_data['ranking'] = new_least_ranking
            return FavouriteThing.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for field in validated_data:
            instance.__setattr__(field, validated_data.get(field))
        instance.save()
        return instance

    def increment_ranking(self, favourite_thing):
        favourite_thing.ranking = favourite_thing.ranking + 1
        favourite_thing.save()
        return favourite_thing
