"""The models test file."""
from django.test import TestCase
from thingsApi.models import CustomUser, Category, FavouriteThing


class TestModels(TestCase):
    """Test for all model functionality."""

    def setUp(self):
        """Set up requirements and data."""
        self.user = CustomUser.objects.create(
            email='test@test.com',
            username='test_user',
            name='user'
        )

        self.category = Category.objects.create(
            name='test_category',
            user=self.user
        )

        self.favourite_thing = FavouriteThing.objects.create(
            title='favourite thing',
            description='the thing I love most',
            user_id=self.user.id,
            category=self.category
        )

        self.second_favourite_thing = FavouriteThing.objects.create(
            title='second favourite thing',
            description='the thing I love most',
            user_id=self.user.id,
            category=self.category
        )

    def refresh_all_columns(self):
        """Refresh the columns."""
        self.favourite_thing.refresh_from_db()
        self.second_favourite_thing.refresh_from_db()

    def test_user_has_custom_field_name(self):
        """Check that the custom user model has the custom field 'user'."""
        self.assertEquals(self.user.name, 'user')

    def test_user_has_favourite_thing(self):
        """Check that a user has favourite thing saved against their name."""
        self.assertEquals(self.user.id, self.favourite_thing.user_id)

    def test_favourite_thing_reorder(self):
        """
        Test that favourite things reorder.

        Check that creating a new favorite thing in an existing
        position shifts others of the same category by the same user downwards.
        """
        third_favorite_thing = FavouriteThing.objects.create(
            title='third favourite thing',
            description='the thing I love most',
            user_id=self.user.id,
            category=self.category,
            ranking=1
        )

        self.refresh_all_columns()
        self.assertEquals(third_favorite_thing.ranking, 1)
        self.assertEquals(self.second_favourite_thing.ranking, 3)
        self.assertEquals(self.favourite_thing.ranking, 2)

    def test_thing_is_added_in_least_rank_if_no_ranking(self):
        """
        Verify Favourite thing is added in least position.

        Test that favourite thing is added at the least rank
        when ranking is not specified in the input.
        """
        third_thing = FavouriteThing.objects.create(
            title='second favourite thing',
            description='the thing I love most',
            user_id=self.user.id,
            category=self.category,
        )
        third_thing.save()
        self.assertEquals(third_thing.ranking, 3)

    def test_favourite_thing_updates_ranking_and_reorders(self):
        """Favourite thing should reorder when ranking is updated."""
        self.second_favourite_thing.ranking = 1
        self.second_favourite_thing.save()
        self.refresh_all_columns()
        self.assertEquals(self.second_favourite_thing.ranking, 1)
        self.assertEquals(self.favourite_thing.ranking, 2)
