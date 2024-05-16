from django.core.exceptions import ValidationError
from typing_extensions import override
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from .kinship import Filiation, Partnership, Siblingship
from .world import Country, Region, SubRegion, Settlement, Place


class AbstractPerson(models.Model):
    """The AbstractPerson class is the base class for all person models. It contains all the fields that are common to all person models."""

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
    given_name = models.CharField(
        _("given name"),
        help_text=_("Also called first name or forename."),
        max_length=100,
        blank=True,
    )
    birth_name = models.CharField(
        _("birth name"),
        help_text=_(
            "Name at birth, also known as maiden name; only use if different from name"
        ),
        max_length=750,
        blank=True,
    )
    other_names = models.TextField(_("other names"), blank=True)
    native_name = models.CharField(
        _("native name"),
        help_text=_("The person's name in their own language, if different."),
        max_length=750,
        blank=True,
    )
    native_name_lang = models.CharField(
        _("language of native name"),
        choices=settings.LANGUAGES,
        max_length=7,
        blank=True,
    )
    pronunciation = models.CharField(
        _("pronunciation of native name"),
        help_text=_("The phonetic pronunciation of the native name."),
        max_length=100,
        blank=True,
    )
    other_names = models.TextField(
        _("other names"),
        help_text=_(
            "Other notable names for the person, if different from name and birth name."
            "This can include stage names, nicknames, criminal aliases, etc."
        ),
        blank=True,
    )
    honorific_prefix = models.CharField(
        _("honorific prefix"),
        help_text=_(
            "This is for honorifics of serious significance that are attached to"
            'the name in formal address, such as knighthoods, "The Honourable", '
            'and "His/Her Excellency"; do not use it for routine things like "Dr.'
            '" or "Ms."'
        ),
        max_length=100,
        blank=True,
    )
    honorific_suffix = models.CharField(
        _("honorific suffix"),
        help_text=_(
            "Similar to honorific prefix, this is for honorifics of serious significance."
        ),
        max_length=100,
        blank=True,
    )

    #
    # Media
    #
    image = models.URLField(
        _("image url"), help_text=_("A person's image"), blank=True
    )

    #
    # Dates & Places
    #
    birth_date = models.DateField(_("date of birth"), null=True, blank=True)
    birth_place_content_type = models.ForeignKey(
        ContentType,
        limit_choices_to={
            "model__in": [Country, Region, SubRegion, Settlement, Place]
        },
        on_delete=models.SET_NULL,
        null=True,
        related_name='natives',
    )
    birth_place_object_id = models.PositiveIntegerField()
    birth_place = GenericForeignKey(
        "birth_place_content_type", "birth_place_object_id"
    )

    disappearance_date = models.DateField(
        _("date of disappearance"),
        help_text=_("(For missing persons)"),
        null=True,
        blank=True,
    )
    disappearance_place_content_type = models.ForeignKey(
        ContentType,
        limit_choices_to={
            "model__in": [Country, Region, SubRegion, Settlement, Place]
        },
        on_delete=models.SET_NULL,
        null=True,
        related_name='gone_missing',
    )
    disappearance_place_object_id = models.PositiveIntegerField()
    disappearance_place = GenericForeignKey(
        "disappearance_place_content_type", "disappearance_place_object_id"
    )

    death_date = models.DateField(_("date of death"), null=True, blank=True)
    death_place_content_type = models.ForeignKey(
        ContentType,
        limit_choices_to={
            "model__in": [Country, Region, SubRegion, Settlement, Place]
        },
        on_delete=models.SET_NULL,
        null=True,
        related_name='deceased'
    )
    death_place_object_id = models.PositiveIntegerField()
    death_place = GenericForeignKey(
        "death_place_content_type", "death_place_object_id"
    )

    death_cause = models.TextField(_("cause of death"), blank=True)

    resting_place_content_type = models.ForeignKey(
        ContentType,
        limit_choices_to={
            "model__in": [Country, Region, SubRegion, Settlement, Place]
        },
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
    education = models.TextField(
        _("education"),
        help_text=_(
            "e.g., degree, institution and graduation year, if relevant. If very"
            "little information is available or relevant, the alma mater parameter"
            "may be more appropriate. "
        ),
        blank=True,
    )
    alma_mater = models.TextField(
        _("alma mater"),
        help_text=_("e.g. college, university, etc."),
        blank=True,
    )
    nationality = models.CharField(
        _("nationality"),
        help_text=_(
            "Synonymous with citizenship. Do not put religion or ethnicity in this field."
        ),
        max_length=100,
        blank=True,
    )
    occupation = models.TextField(_("occupation"), blank=True)
    title = models.CharField(
        _("title"),
        help_text=_("e.g. Mayor of the city of New York"),
        max_length=100,
        blank=True,
    )
    notes = models.TextField(_("notes"), blank=True)

    def __str__(self) -> str:
        return self.get_full_name()

    def get_full_name(self) -> str:
        if self.surname and self.given_name:
            # TODO: make locale-aware (e.g. surname before given name)
            return f"{self.given_name} {self.surname}"
        return str(self.name)


class Person(AbstractPerson):
    """The base person model
    Inherits all metatdata and biographical information fields from AbstractPerson.
    This class includes two categories of first-degree relational fields to other Person instances:
        - Genetic relations
        - Kinship relations (may or may not coincide with genetic relations)
    Second-, third-, nth-degree relations are not specified directly in the model, but are inferred
    from the first-degree relations at runtime.
    """

    class Meta(AbstractPerson.Meta):
        verbose_name = _("person")
        verbose_name_plural = _("persons")

    #
    # First-degree genetic relations
    #
    genetic_mother = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True,
    )
    genetic_father = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True,
    )

    @property
    def genetic_siblings(self):
        """Returns the set of people who share the same genetic parents as this person."""
        return Person.objects.filter(
            genetic_mother=self.genetic_mother,
            genetic_father=self.genetic_father,
        )

    #
    # First-degree Kinship relations
    #
    parents = models.ManyToManyField("self", through=Filiation)
    siblings = models.ManyToManyField("self", through=Siblingship)
    partners = models.ManyToManyField("self", through=Partnership)

    @override
    def clean(self) -> None:
        if self.genetic_mother == self.genetic_father:
            raise ValidationError(
                _(
                    "Genetic mothers and genetic fathers cannot be the same person."
                )
            )
        if self.genetic_mother == self or self.genetic_father == self:
            raise ValidationError(
                _("A person cannot be their own genetic mother or father.")
            )

        return super().clean()
