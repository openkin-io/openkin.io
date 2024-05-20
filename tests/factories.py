import factory

from app.models.person import Post

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    name = "x"
    surname = "x"
    given_name = "x"
    birth_name = "x"
    other_names = "x"
    native_name = "x"
    pronunciation = "x"
    other_names = "x"
    honorific_prefix = "x"
    honorific_suffix = "x"
    image = "x"
    birth_date = "x"
    birth_place_content_type = "x"
    birth_place_object_id = "x"
    birth_place = "x"
    disappearance_date = "x"
    disappearance_place_content_type = "x"
    disappearance_place_object_id = "x"
    disappearance_place = "x"
    death_date = "x"
    death_place_content_type = "x"
    death_place_object_id = "x"
    death_place = "x"
    death_cause = "x"
    resting_place_content_type = "x"
    resting_place_object_id = "x"
    resting_place = "x"
    education = "x"
    alma_mater = "x"
    nationality = "x"
    occupation = "x"
    title = "x"
    notes = "x"
