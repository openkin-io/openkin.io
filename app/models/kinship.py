from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q, F
from django.utils.translation import gettext_lazy as _


class Filiation(models.Model):
    """Filial relation between parent and child. Does not imply genetic relation."""

    child = models.ForeignKey("Person", on_delete=models.CASCADE)
    parent = models.ForeignKey(
        "Person", related_name="children", on_delete=models.CASCADE
    )

    is_adoption = models.BooleanField(null=True)
    date_of_adoption = models.DateField(null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["parent", "child"], name="parent_child_unique"
            ),
            models.CheckConstraint(
                check=~Q(parent=F("child")),
                name="parent_and_child_cannot_be_the_same_person",
            ),
        ]

    def clean(self):
        # Ensure is_adoption if date_of_adoption is set
        if self.date_of_adoption is not None and not self.is_adoption:
            self.is_adoption = True

        return super().clean()


class Siblingship(models.Model):
    """Sibling relation between two persons. Does not imply genetic relation."""

    person = models.ForeignKey("Person", on_delete=models.CASCADE)
    sibling = models.ForeignKey(
        "Person", related_name="siblingships", on_delete=models.CASCADE
    )
    became_siblings_at = models.DateField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["person", "sibling"], name="unique_siblingship"
            ),
            models.CheckConstraint(
                check=~Q(person=F("sibling")),
                name="siblings_cannot_be_the_same_person",
            ),
        ]
        ordering = ["person", "sibling"]

    def save(self, *args, **kwargs):
        if self.person.id > self.sibling.id:
            self.person, self.sibling = self.sibling, self.person
        super().save(*args, **kwargs)


class Partnership(models.Model):
    """Some form of long-term partnership between two persons."""

    person = models.ForeignKey("Person", on_delete=models.CASCADE)
    partner = models.ForeignKey(
        "Person", related_name="partnerships", on_delete=models.CASCADE
    )
    date_of_union = models.DateField(null=True)
    partnership_type = models.CharField(
        _("partnership type"),
        help_text=_("partnership, marriage, etc."),
        max_length=255,
        blank=True,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["person", "partner"], name="unique_partnership"
            ),
            models.CheckConstraint(
                check=~Q(person=F("partner")), name="partners_cannot_be_the_same_person"
            ),
        ]
        ordering = ["person", "partner"]

    def clean(self):
        if self.person == self.partner:
            raise ValidationError("Partners cannot be the same person.")

    def save(self, *args, **kwargs):
        if self.person.id > self.partner.id:
            self.person, self.partner = self.partner, self.person
        super().save(*args, **kwargs)
