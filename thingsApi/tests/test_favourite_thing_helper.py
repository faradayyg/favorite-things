"""The models test file."""
from django.test import TestCase
from thingsApi.models import CustomUser, Category
from thingsApi.helpers.favourite_things_helper import (
    create_favourite_thing,
    update_favourite_thing
)


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

        self.favourite_thing = create_favourite_thing(
            {
                'title': 'Favourite thing First',
                'description': 'this is the first one',
                'user_id': self.user.id,
                'category_id': self.category.id
            }
        )
        self.second_favourite_thing = create_favourite_thing(
            {
                'title': 'Favourite thing Second',
                'description': 'this is the second too',
                'user_id': self.user.id,
                'category_id': self.category.id
            }
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

        Check that creating a new favourite thing in an existing
        position shifts others of the same category by the same user downwards.
        """
        third_favourite_thing = create_favourite_thing(
            {
                'title': 'Favourite thing Third',
                'description': 'this is the third one',
                'user_id': self.user.id,
                'category_id': self.category.id,
                'ranking': 1
            }
        )

        self.refresh_all_columns()
        self.assertEquals(third_favourite_thing.ranking, 1)
        self.assertEquals(self.second_favourite_thing.ranking, 3)
        self.assertEquals(self.favourite_thing.ranking, 2)

    def test_thing_is_added_in_least_rank_if_no_ranking(self):
        """
        Verify Favourite thing is added in least position.

        Test that favourite thing is added at the least rank
        when ranking is not specified in the input.
        """
        third_favourite_thing = create_favourite_thing(
            {
                'title': 'Favourite thing Third',
                'description': 'this is the third one',
                'user_id': self.user.id,
                'category_id': self.category.id
            }
        )
        self.assertEquals(third_favourite_thing.ranking, 3)

    def test_favourite_thing_updates_ranking_and_reorders(self):
        """Favourite thing should reorder when ranking is updated."""
        update_favourite_thing(self.second_favourite_thing, {'ranking': 1})
        self.second_favourite_thing.save()
        self.refresh_all_columns()
        self.assertEquals(self.second_favourite_thing.ranking, 1)
        self.assertEquals(self.favourite_thing.ranking, 2)
