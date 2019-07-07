from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    class Meta:
        db_table = 'user'
    name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.email


class Category(models.Model):
    class Meta:
        db_table = 'category'
        verbose_name_plural = 'categories'
    name = models.CharField(max_length=200)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class FavouriteThing(models.Model):
    class Meta:
        db_table = 'favourite_thing'
        ordering = ('ranking', 'created_at')

    title = models.CharField("name of favourite thing", max_length=100)
    description = models.CharField(max_length=500, null=True)
    ranking = models.PositiveSmallIntegerField()
    meta_data = models.TextField(default=None, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
