from django.core.exceptions import ValidationError
from typing_extensions import override
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from app.models.kinship import Filiation, Sibling
from app.models import world


class AbstractPerson(models.Model):
    class Meta:
        abstract = True

    #
    # Names
    #
    name = models.CharField(_("name"), max_length=750)
    surname = models.CharField(
        _("surname"),
        help_text=_("Also called last name, second name or family name."),
        max_length=750,  # https://www.guinnessworldrecords.com/world-records/67285-longest-personal-name
        blank=True,
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

    def __str__(self) -> str:
        return self.get_full_name()

    def get_full_name(self) -> str:
        if self.surname and self.firstname:
            return f"{self.firstname} {self.surname}"
        return str(self.name)


class Person(AbstractPerson):
    """The base person model.
    Inherits all metatdata and biographical information fields from AbstractPerson.
    Defines `genetic_mother` and `genetic_father` foreign keys to other Person models.
    All other kinship relations can be derived from these.

    Attributes:
        mother: The person's mother (another Person) (optional)
        father: The person's father (another Person) (optional)
    """

    class Meta(AbstractPerson.Meta):
        verbose_name = _("person")
        verbose_name_plural = _("persons")

    genetic_mother = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        related_name="children",
        null=True,
    )
    genetic_father = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        related_name="children",
        null=True,
    )

    parents = models.ManyToManyField("self", through=Filiation)
    siblings = models.ManyToManyField("self", through=Sibling)

    @override
    def clean(self) -> None:
        if self.genetic_mother == self.genetic_father:
            raise ValidationError(
                _("Mother and father cannot be the same person")
            )
        if self.genetic_mother == self or self.genetic_father == self:
            raise ValidationError(
                _("A person cannot be their own mother or father")
            )

        return super().clean()
