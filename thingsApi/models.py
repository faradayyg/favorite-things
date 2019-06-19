from django.db import models

# Create your models here.


class Category(models.Model):
    class Meta:
        db_table = 'category'
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class FavouriteThing(models.Model):
    class Meta:
        db_table = 'favourite_thing'
        ordering = ('ranking', 'created_at')

    title = models.CharField("name of favourite thing", max_length=100)
    description = models.CharField(max_length=500)
    ranking = models.PositiveSmallIntegerField()
    meta_data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
