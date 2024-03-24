from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from typing_extensions import override


class Filiation(models.Model):
    """Filial relation between parent and child. Does not imply genetic relation.

    Attributes:
        parent (ForeignKey to Person)
        child (ForeignKey to Person)
        is_adoption (BooleanField): optional
        date_of_adoption (DateField): optional
    """

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
            )
        ]

    @override
    def clean(self):
        if self.parent == self.child:
            raise ValidationError(
                "A person cannot be their own parent or child."
            )

        # Ensure is_adoption if date_of_adoption is set
        if self.date_of_adoption is not None and not self.is_adoption:
            self.is_adoption = True

        return super().clean()


class Siblingship(models.Model):
    """Sibling relation between two persons. Does not imply genetic relation.

    Attributes:
        sibling_a (ForeignKey to Person)
        sibling_b (ForeignKey to Person)
        sibling_since (DateField): optional
    """

    sibling_a = models.ForeignKey(
        "Person", related_name="sibling", on_delete=models.CASCADE
    )
    sibling_b = models.ForeignKey(
        "Person", related_name="sibling", on_delete=models.CASCADE
    )
    sibling_since = models.DateField(null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["sibling_a", "sibling_b"],
                name="sibling_a_sibling_b_unique",
            ),
        ]

    @override
    def clean(self):
        if self.sibling_a == self.sibling_b:
            raise ValidationError("A person cannot be their own sibling.")


class Partnership(models.Model):
    """Some form of long-term partnership between two persons.

    Attributes:
        partner_a (ForeignKey to Person)
        partner_b (ForeignKey to Person)
        date_of_union (DateField): optional
        partnership_type (CharField): optional
    """

    partner_a = models.ForeignKey(
        "Person", related_name="partner", on_delete=models.CASCADE
    )
    partner_b = models.ForeignKey(
        "Person", related_name="partner", on_delete=models.CASCADE
    )
    date_of_union = models.DateField(null=True)
    partnership_type = models.CharField(
        _("partnership type"),
        help_text=_("partnership, marriage, etc."),
        max_length=255,
        blank=True,
    )
