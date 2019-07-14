"""Serializers for the Favourite things API."""
from rest_framework import serializers
from thingsApi.models import Category
from thingsApi.helpers.favourite_things_helper import (
    create_favourite_thing,
    update_favourite_thing)


class FavouriteThingSerializer(serializers.Serializer):
    """Favourite things serializer."""

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(
        required=False, default='', allow_null=True
    )
    ranking = serializers.IntegerField(required=False, allow_null=True)
    # meta_data = serializers.CharField(
    #     required=False, allow_null=True, default=''
    # )
    category_id = serializers.IntegerField()
    category = serializers.ReadOnlyField(source='category.name')
    user = serializers.ReadOnlyField(source='user.email')

    def create(self, validated_data):
        """Create Favourite thing."""
        user_id = self.context['request'].user.id
        validated_data['user_id'] = user_id
        return create_favourite_thing(validated_data)

    def update(self, instance, validated_data):
        """Update the favourite thing."""
        return update_favourite_thing(instance, validated_data)


class CategorySerializer(serializers.Serializer):
    """Serializer for the categories."""

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=500)
    created_at = serializers.CharField(max_length=100, read_only=True)
    user = serializers.ReadOnlyField(source='user.email')

    def create(self, validated_data):
        """Creating a category."""
        validated_data['user_id'] = self.context['request'].user.id
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Update/modify the category."""
        for field in validated_data:
            instance.__setattr__(field, validated_data.get(field))
        instance.save()
        return instance
