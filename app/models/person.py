from django.core.exceptions import ValidationError
from typing_extensions import override
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from . import world


class AbstractPerson(models.Model):
    class Meta:
        abstract = True

    #
    # Names
    #
    surname = models.CharField(
        _("surname"),
        help_text=_("Also called last name, second name or family name."),
        max_length=750,  # https://www.guinnessworldrecords.com/world-records/67285-longest-personal-name
    )
    firstname = models.CharField(_("first name"), max_length=100, blank=True)
    birth_name = models.CharField(_("birth name"), max_length=750, blank=True)
    other_names = models.TextField(_("other names"), blank=True)
    native_name = models.CharField(_("native name"), max_length=750, blank=True)
    native_name_lang = models.CharField(
        _("native name language"),
        choices=settings.LANGUAGES,
        max_length=5,
        blank=True,
    )
    pronunciation = models.CharField(
        _("pronunciation"),
        help_text=_("The phonetic pronunciation."),
        max_length=100,
        blank=True,
    )

    #
    # Media
    #
    image = models.URLField(_("image url"), blank=True)

    #
    # Dates & Places
    #
    birth_date = models.DateField(blank=True, null=True)
    birth_place_content_type = models.ForeignKey(
        ContentType,
        limit_choices_to={"model__in": world},
        on_delete=models.SET_NULL,
        null=True,
    )
    birth_place_object_id = models.PositiveIntegerField()
    birth_place = GenericForeignKey(
        "birth_place_content_type", "birth_place_object_id"
    )

    disappearance_date = models.DateField(blank=True, null=True)
    disappearance_place_content_type = models.ForeignKey(
        ContentType,
        limit_choices_to={"model__in": world},
        on_delete=models.SET_NULL,
        null=True,
    )
    disappearance_place_object_id = models.PositiveIntegerField()
    disappearance_place = GenericForeignKey(
        "appearance_place_content_type", "disappearance_place_object_id"
    )

    death_date = models.DateField(blank=True, null=True)
    death_place_content_type = models.ForeignKey(
        ContentType,
        limit_choices_to={"model__in": world},
        on_delete=models.SET_NULL,
        null=True,
    )
    death_place_object_id = models.PositiveIntegerField()
    death_place = GenericForeignKey(
        "death_place_content_type", "death_place_object_id"
    )

    death_cause = models.TextField(_("death cause"), blank=True)

    resting_place_content_type = models.ForeignKey(
        ContentType,
        limit_choices_to={"model__in": world},
        on_delete=models.SET_NULL,
        null=True,
    )
    resting_place_object_id = models.PositiveIntegerField()
    resting_place = GenericForeignKey(
        "resting_place_content_type", "resting_place_object_id"
    )

    #
    # Extra Biographical Information
    #
    nationality = models.CharField(_("nationality"), max_length=100, blank=True)
    occupation = models.TextField(_("occupation"), blank=True)
    notes = models.TextField(_("notes"), blank=True)


class Person(AbstractPerson):
    class Meta(AbstractPerson.Meta):
        verbose_name = _("person")
        verbose_name_plural = _("persons")

    mother = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True, related_name="children"
    )
    father = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True, related_name="children"
    )

    @override
    def clean(self) -> None:
        if self.mother == self.father:
            raise ValidationError(
                _("Mother and father cannot be the same person")
            )
        if self.mother == self or self.father == self:
            raise ValidationError(
                _("A person cannot be their own mother or father")
            )
        return super().clean()

    @property
    def siblings(self):
        return Person.objects.filter(mother=self.mother, father=self.father)
