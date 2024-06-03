from django.db import models
from django.utils.translation import gettext_lazy as _


class Location(models.Model):
    """An abstract class for all geographical locations"""

    class Meta:
        abstract = True
        verbose_name = _("Location")
        verbose_name_plural = _("Locations")

    # TODO: Make it possible to translate this user-supplied name dynamically.
    # see this StackOverflow answer: https://stackoverflow.com/a/26276164
    name = models.TextField(
        _("name"),
        help_text=_("The usual, English name of the location"),
    )
    native_name = models.TextField(
        _("native_name"),
        help_text=_(
            "The location name in the native language, if different from the name."
        ),
        blank=True,
    )

    wiki = models.URLField(_("Wikipedia URL"), blank=True)

    latitude = models.DecimalField(
        _("latitude"),
        max_digits=7,
        decimal_places=4,
        null=True,
        blank=True,
    )
    longitude = models.DecimalField(
        _("longitude"),
        max_digits=7,
        decimal_places=4,
        null=True,
        blank=True,
    )


class Country(Location):
    """A Distinct part of the world, such as a state, nation or other political entity."""

    class Meta(Location.Meta):
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")

    image_flag = models.URLField(_("image_flag"), blank=True)


class Region(Location):
    """The principal administrative division of a country"""

    class Meta(Location.Meta):
        verbose_name = _("Region")
        verbose_name_plural = _("Regions")

    region_type = models.CharField(
        _("region type"),
        help_text=_("State, province, oblast, etc."),
        default="region",
        max_length=32,
        blank=True,
    )

    country = models.ForeignKey(Country, on_delete=models.CASCADE)


class SubRegion(Location):
    """The second-tier administrative division of a country

    Attributes:
        subregion_type: The subregion type (county, district, etc.)
        region: The subregion's region
    """

    class Meta(Location.Meta):
        verbose_name = _("SubRegion")
        verbose_name_plural = _("SubRegions")

    subregion_type = models.CharField(
        _("subregion type"),
        help_text=_("County, district, etc."),
        default="subregion",
        max_length=32,
        blank=True,
    )

    region = models.ForeignKey(Region, on_delete=models.CASCADE)


class Settlement(Location):
    """A municipality, village, city, etc. in a country"""

    class Meta(Location.Meta):
        verbose_name = _("Municipality")
        verbose_name_plural = _("Municipalities")

    settlement_type = models.CharField(
        _("settlement type"),
        help_text=_("City, town, village, hamlet, municipality, reservation, etc."),
        default="settlement",
        max_length=32,
        blank=True,
    )

    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True)
    subregion = models.ForeignKey(
        SubRegion, on_delete=models.CASCADE, null=True, blank=True
    )


class Place(Location):
    """Any physical location with a name that is not country-specific."""

    class Meta(Location.Meta):
        verbose_name = _("Place")
        verbose_name_plural = _("Places")

    place_type = models.CharField(
        _("place type"),
        max_length=70,
        help_text=_(
            "Can be a natural place like a forest, a body of water, a mountain, etc.;"
            "or a man-made place like a landmark, a monument, a historic site, a building, etc."
        ),
        blank=True,
    )

    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
    subregion = models.ForeignKey(SubRegion, on_delete=models.CASCADE, null=True)
    settlement = models.ForeignKey(Settlement, on_delete=models.CASCADE, null=True)
