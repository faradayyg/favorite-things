from rest_framework import serializers
from thingsApi.models import FavouriteThing, Category


class FavouriteThingSerializer(serializers.Serializer):
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
        user = self.context['request'].user
        validated_data['user'] = user
        return FavouriteThing.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for field in validated_data:
            instance.__setattr__(field, validated_data.get(field))
        instance.save()
        return instance


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=500)
    created_at = serializers.CharField(max_length=100, read_only=True)
    user = serializers.ReadOnlyField(source='user.email')

    def create(self, validated_data):
        validated_data['user_id'] = self.context['request'].user.id
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for field in validated_data:
            instance.__setattr__(field, validated_data.get(field))
        instance.save()
        return instance
