"""Helper that runs all the operations on the favourite things."""
from thingsApi.models import FavouriteThing


def create_favourite_thing(payload):
    """Create Favourite thing."""
    if payload.get('ranking') in [None, '']:
        # Get Last ranking (Largest ranking in category by user)
        least_ranking_thing = FavouriteThing.objects.filter(
            category_id=payload['category_id'],
            user_id=payload['user_id']
        ).order_by('-ranking').first()

        # determine ranking because user did not specify
        if least_ranking_thing:
            new_least_ranking = least_ranking_thing.ranking + 1
        else:
            new_least_ranking = 1

        payload['ranking'] = new_least_ranking
    # User set ranking and we should use that
    else:
        reorder_rankings(
            payload['ranking'],
            payload['category_id'],
            payload['user_id']
        )
    return FavouriteThing.objects.create(**payload)


def update_favourite_thing(instance, payload):
    """Update favourite things."""
    if payload.get('ranking') not in [instance.ranking, None]:
        category_id = payload['category_id'] if (
            payload.get('category_id')
        ) else instance.category_id
        reorder_rankings(
            payload['ranking'],
            instance.user_id,
            category_id,
            instance.id
        )

    # this block will never execute if for some reason the above fails
    for field in payload:
        instance.__setattr__(field, payload.get(field))
    instance.save()
    return instance


def reorder_rankings(
    intended_ranking,
    category_id,
    user_id,
        favourite_thing_id=None):
        """Update the rankings of other favourite things."""
        # check for items in positions below the intended position
        subsequent_positions = FavouriteThing.objects.filter(
            ranking__gte=intended_ranking,
            category_id=category_id,
            user_id=user_id
        )

        # if updating, exclude current favourite thing from query set
        if favourite_thing_id is not None:
            subsequent_positions = subsequent_positions.exclude(
                id=favourite_thing_id
            )

        # shift other ranks accordingly
        count = 1
        for favourite_thing in subsequent_positions:
            increment_ranking(favourite_thing, intended_ranking + count)
            count += 1

        # check if increment worked
        integrity_check = FavouriteThing.objects.filter(
            ranking=intended_ranking,
            category_id=category_id,
            user_id=user_id
        )

        # There are no other objects in this position therefore, empty set
        if len(integrity_check) == 0:
            return True
        else:
            raise Exception('An Error Occurred, rankings were not updated')


def increment_ranking(favourite_thing, new_ranking):
    """Increment ranking of favourite thing."""
    favourite_thing.ranking = new_ranking
    favourite_thing.save()
    return favourite_thing
