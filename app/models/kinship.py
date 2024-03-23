from django.db import models

from app.models.person import Person

# Abbreviations for genealogical relationships
#
# The genealogical terminology used in many genealogical charts describes
# relatives of the subject in question. Using the abbreviations below,
# genealogical relationships may be distinguished by single or compound
# relationships, such as BC for a brother's children, MBD for a mother's
# brother's daughter, and so forth.
#
# B = Brother
# C = Child(ren)
# D = Daughter
# F = Father
# GC = Grandchild(ren)
# GP = Grandparent(s)
# H = Husband
# LA = In-law
# M = Mother
# P = Parent
# S = Son
# SI = Siblings
# SP = Spouse
# W = Wife
# Z = Sister


class Filiation(models.Model):
    parent = models.ForeignKey(
        Person, related_name="children", on_delete=models.CASCADE
    )
    child = models.ForeignKey(
        Person, related_name="parents", on_delete=models.CASCADE
    )

    date_of_adoption = models.DateField(null=True)


class Sibling(models.Model):
    sibling = models.ForeignKey(
        Person, related_name="siblings", on_delete=models.CASCADE
    )
    sibling_since = models.DateField(null=True)
