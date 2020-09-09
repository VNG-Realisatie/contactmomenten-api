from django.test import TestCase

from freezegun import freeze_time

from .factories import ContactMomentFactory

KLANT = "http://some.klanten.nl/api/v1/klanten/951e4660-3835-4643-8f9c-e523e364a30f"
ZAAK = "http://some.zrc.nl/api/v1/zaken/ffb1a466-fdad-4898-87fa-dae026df38c0"


@freeze_time("2020-01-01")
class UniqueRepresentationTests(TestCase):
    def test_contactmoment(self):
        contactmoment = ContactMomentFactory.create(
            bronorganisatie="423182687",
            klant=KLANT,
            kanaal="telephone",
        )
        self.assertEqual(
            contactmoment.unique_representation(),
            "423182687 951e4660-3835-4643-8f9c-e523e364a30f at 2020-01-01 00:00:00+00:00 via telephone",
        )

    def test_contactmoment_empty_klant(self):
        contactmoment = ContactMomentFactory.create(
            bronorganisatie="423182687",
            kanaal="telephone",
            klant="",
        )
        self.assertEqual(
            contactmoment.unique_representation(),
            "423182687  at 2020-01-01 00:00:00+00:00 via telephone",
        )
