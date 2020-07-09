from datetime import datetime

from django.utils.timezone import make_aware

from rest_framework import status
from rest_framework.test import APITestCase
from vng_api_common.tests import JWTAuthMixin, get_validation_errors, reverse

from contactmomenten.datamodel.constants import InitiatiefNemer, Rol
from contactmomenten.datamodel.models import ContactMoment, KlantContactMoment
from contactmomenten.datamodel.tests.factories import (
    ContactMomentFactory,
    KlantContactMomentFactory,
)


class KlantContactMomentTests(JWTAuthMixin, APITestCase):
    heeft_alle_autorisaties = True

    def test_list_klantcontactmomenten(self):
        list_url = reverse(KlantContactMoment)
        KlantContactMomentFactory.create_batch(2)

        response = self.client.get(list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        self.assertEqual(len(data), 2)

    def test_read_klantcontactmoment(self):
        cmc = ContactMomentFactory.create(
            interactiedatum=make_aware(datetime(2019, 1, 1)),
            initiatiefnemer=InitiatiefNemer.gemeente,
        )
        cmc_url = reverse(cmc)
        klantcontactmoment = KlantContactMomentFactory.create(
            contactmoment=cmc, rol=Rol.belanghebbende,
        )
        detail_url = reverse(klantcontactmoment)

        response = self.client.get(detail_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()

        self.assertEqual(
            data,
            {
                "url": f"http://testserver{detail_url}",
                "klant": klantcontactmoment.klant,
                "contactmoment": f"http://testserver{cmc_url}",
                "rol": Rol.belanghebbende,
            },
        )

    def test_create_klantcontactmoment(self):
        cmc = ContactMomentFactory.create(
            interactiedatum=make_aware(datetime(2019, 1, 1)),
            initiatiefnemer=InitiatiefNemer.gemeente,
        )
        cmc_url = reverse(cmc)

        list_url = reverse(KlantContactMoment)
        data = {
            "klant": "http://testserver.com/klant/1",
            "contactmoment": f"http://testserver{cmc_url}",
            "rol": Rol.gesprekspartner,
        }

        response = self.client.post(list_url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        klantcontactmoment = KlantContactMoment.objects.get()

        self.assertEqual(klantcontactmoment.klant, "http://testserver.com/klant/1")
        self.assertEqual(klantcontactmoment.contactmoment, cmc)
        self.assertEqual(klantcontactmoment.rol, Rol.gesprekspartner)

    def test_destroy_klantcontactmoment(self):
        klantcontactmoment = KlantContactMomentFactory.create()
        detail_url = reverse(klantcontactmoment)

        response = self.client.delete(detail_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(KlantContactMoment.objects.count(), 0)


class KlantContactMomentFilterTests(JWTAuthMixin, APITestCase):
    heeft_alle_autorisaties = True
    list_url = reverse(KlantContactMoment)

    def test_filter_klant(self):
        klantcontactmoment = KlantContactMomentFactory.create(
            klant="https://testserver.com/klant/1"
        )
        KlantContactMomentFactory.create()

        response = self.client.get(
            self.list_url,
            {"klant": "https://testserver.com/klant/1"},
            HTTP_HOST="testserver.com",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["klant"], "https://testserver.com/klant/1")

    def test_filter_contactmoment(self):
        klantcontactmoment = KlantContactMomentFactory.create()
        KlantContactMomentFactory.create()
        cmc_url = reverse(klantcontactmoment.contactmoment)

        response = self.client.get(
            self.list_url,
            {"contactmoment": f"http://testserver.com{cmc_url}"},
            HTTP_HOST="testserver.com",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(
            response.data[0]["contactmoment"], f"http://testserver.com{cmc_url}"
        )

    def test_filter_rol(self):
        klantcontactmoment = KlantContactMomentFactory.create(rol=Rol.belanghebbende,)
        KlantContactMomentFactory.create(rol=Rol.gesprekspartner,)

        response = self.client.get(self.list_url, {"rol": klantcontactmoment.rol},)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["rol"], klantcontactmoment.rol)
