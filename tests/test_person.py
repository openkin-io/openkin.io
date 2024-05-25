from django.test import TestCase

from app.models import Person


class PersonTestCase(TestCase):
    def test_siblings(self):
        a = Person.objects.create(name="A")
        b = Person.objects.create(name="B")

        a.siblings.add(b)

        self.assertEqual(a.siblings.count(), 1)
