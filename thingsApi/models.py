"""Models for app."""
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Extend the abstract user class."""

    class Meta:
        """More info."""

        db_table = 'user'
    name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        """Property to represent class with."""
        return self.email


class Category(models.Model):
    """Category class of Favorite thing."""

    class Meta:
        """More info."""

        db_table = 'category'
        verbose_name_plural = 'categories'
    name = models.CharField(max_length=200)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Property to represent class with."""
        return self.name


class FavouriteThing(models.Model):
    """Favourite thing class."""

    class Meta:
        """More info."""

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

    def __init__(self, *args, **kwargs):
        """Magic init method, to load original values."""
        super().__init__(*args, **kwargs)
        self.__original_ranking = self.ranking

    def save(self, *args, **kwargs):
        """Override save method."""
        if self.ranking is None or self.ranking == '':
            # Get Last ranking
            least_ranking_thing = FavouriteThing.objects.filter(
                category_id=self.category_id,
                user_id=self.user_id
            ).order_by('-ranking').first()

            # reorder and save
            if least_ranking_thing:
                new_least_ranking = least_ranking_thing.ranking + 1
            else:
                new_least_ranking = 1

            self.ranking = new_least_ranking
        # Check if the user manually set ranking
        else:
            self.reorder_rankings()

        super().save(*args, **kwargs)

    def reorder_rankings(self):
        """Update the rankings of other favourite things."""
        # check for items in positions below the intended position
        subsequent_positions = FavouriteThing.objects.filter(
            ranking__gte=self.ranking,
            category_id=self.category_id,
            user_id=self.user_id
        )

        if not self._state.adding:
            subsequent_positions = subsequent_positions.exclude(
                id=self.id
            )

        # shift other ranks accordingly
        count = 1
        intended_ranking = self.ranking
        for favourite_thing in subsequent_positions:
            print("shifting for =>", favourite_thing.title, " new ranking =>", intended_ranking + count)
            self.increment_ranking(favourite_thing, intended_ranking + count)
            count += 1

        # check if increment worked
        integrity_check = FavouriteThing.objects.filter(
            ranking=intended_ranking,
            category_id=self.category_id,
            user_id=self.user_id
        ).exclude(id=self.id).first()
        if integrity_check is None:
            return True
        else:
            raise Exception('An Error Occurred, rankings were not updated')

    def increment_ranking(self, favourite_thing, new_ranking):
        """Increment ranking of favourite thing."""
        favourite_thing.ranking = new_ranking
        favourite_thing.save()
        return favourite_thing

    def __str__(self):
        """Property to represent class with."""
        return "%s ranking => %s" % (self.title, self.ranking)
