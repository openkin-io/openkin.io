from django.db import IntegrityError, transaction
from django.test import TestCase

from app.models import Person


class SiblingTestCase(TestCase):
    def test_sibling_add(self):
        a = Person.objects.create(name="A")
        b = Person.objects.create(name="B")

        a.siblings.add(b)

        self.assertEqual(a.siblings.count(), 1)
        self.assertEqual(b.siblings.count(), 1)

    def test_sibling_add_multiple(self):
        a = Person.objects.create(name="A")
        b = Person.objects.create(name="B")
        c = Person.objects.create(name="C")

        a.siblings.add(b, c)

        self.assertEqual(a.siblings.count(), 2)
        self.assertEqual(b.siblings.count(), 1)
        self.assertEqual(c.siblings.count(), 1)

    def test_sibling_remove(self):
        a = Person.objects.create(name="A")
        b = Person.objects.create(name="B")

        a.siblings.add(b)
        a.siblings.remove(b)

        self.assertEqual(a.siblings.count(), 0)
        self.assertEqual(b.siblings.count(), 0)

    def test_sibling_not_self(self):
        a = Person.objects.create(name="A")

        # the transaction wrapper is needed so that the test transaction
        # isn't rolled back and we can query after the exception is raised
        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                a.siblings.add(a)

        self.assertEqual(a.siblings.count(), 0)

    def test_common_genetic_mother(self):
        mother = Person.objects.create(name="mom")
        father = Person.objects.create(name="dad")
        a = Person.objects.create(
            name="A", genetic_mother=mother, genetic_father=father
        )
        sibling = Person.objects.create(name="B", genetic_mother=mother)

        self.assertEqual(a.genetic_siblings.count(), 1)
        self.assertTrue(a.genetic_siblings.contains(sibling))

    def test_common_genetic_father(self):
        mother = Person.objects.create(name="mom")
        father = Person.objects.create(name="dad")
        a = Person.objects.create(
            name="A", genetic_mother=mother, genetic_father=father
        )
        sibling = Person.objects.create(name="C", genetic_father=father)

        self.assertEqual(a.genetic_siblings.count(), 1)
        self.assertTrue(a.genetic_siblings.contains(sibling))

    def test_common_genetic_parents(self):
        mother = Person.objects.create(name="mom")
        father = Person.objects.create(name="dad")
        a = Person.objects.create(
            name="A", genetic_mother=mother, genetic_father=father
        )
        sibling = Person.objects.create(
            name="E", genetic_mother=mother, genetic_father=father
        )

        self.assertEqual(a.genetic_siblings.count(), 1)
        self.assertTrue(a.genetic_siblings.contains(sibling))

    def test_extended_siblings(self):
        mother = Person.objects.create(name="mom")
        a = Person.objects.create(name="A", genetic_mother=mother)
        genetic_sibling = Person.objects.create(name="B", genetic_mother=mother)
        sibling = Person.objects.create(name="C")
        a.siblings.add(sibling)

        self.assertEqual(a.extended_siblings.count(), 2)
        self.assertEqual(genetic_sibling.extended_siblings.count(), 1)
        self.assertEqual(sibling.extended_siblings.count(), 1)
