import uuid

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from django_better_admin_arrayfield.models.fields import ArrayField
from vng_api_common.fields import RSINField
from vng_api_common.models import APIMixin
from vng_api_common.utils import get_uuid_from_path

from .constants import InitiatiefNemer, ObjectTypes


class ContactMoment(APIMixin, models.Model):
    uuid = models.UUIDField(
        unique=True, default=uuid.uuid4, help_text="Unieke resource identifier (UUID4)"
    )
    bronorganisatie = RSINField(
        help_text="Het RSIN van de Niet-natuurlijk persoon zijnde de "
        "organisatie die de klantinteractie heeft gecreeerd. Dit moet een "
        "geldig RSIN zijn van 9 nummers en voldoen aan "
        "https://nl.wikipedia.org/wiki/Burgerservicenummer#11-proef"
    )
    klant = models.URLField(
        max_length=1000,
        blank=True,
        help_text=_(
            "URL-referentie naar een KLANT (in Klanten API) indien de klantinteractie niet anoniem is."
        ),
    )
    interactiedatum = models.DateTimeField(
        default=timezone.now,
        help_text=_(
            "De datum en het tijdstip waarop de klantinteractie heeft plaatsgevonden."
        ),
    )
    tekst = models.TextField(
        blank=True,
        help_text=_(
            "Een toelichting die inhoudelijk de klantinteractie van de klant beschrijft."
        ),
    )
    voorkeurskanaal = models.CharField(
        max_length=50,
        blank=True,
        help_text=_(
            "Het communicatiekanaal dat voor opvolging van de klantinteractie de voorkeur heeft van de KLANT."
        ),
    )
    kanaal = models.CharField(
        blank=True,
        max_length=50,
        help_text=_("Het communicatiekanaal waarlangs het CONTACTMOMENT gevoerd wordt"),
    )
    initiatiefnemer = models.CharField(
        max_length=20,
        blank=True,
        choices=InitiatiefNemer.choices,
        help_text=_("De partij die het contact heeft geïnitieerd."),
    )
    medewerker = models.URLField(
        help_text="URL-referentie naar een medewerker", max_length=1000, blank=True
    )
    onderwerp_links = ArrayField(
        models.URLField(
            _("onderwerp link"),
            max_length=1000,
            help_text=_(
                "URL naar een product, webpagina of andere entiteit zodat contactmomenten gegroepeerd kunnen worden."
            ),
        ),
        help_text=_(
            "Eén of meerdere links naar een product, webpagina of andere entiteit "
            "zodat contactmomenten gegroepeerd kunnen worden op onderwerp."
        ),
        blank=True,
        default=list,
    )

    class Meta:
        verbose_name = "contactmoment"
        verbose_name_plural = "contactmomenten"

    def save(self, *args, **kwargs):
        # workaround for https://github.com/gradam/django-better-admin-arrayfield/issues/17
        if self.onderwerp_links is None:
            self.onderwerp_links = []
        super().save(*args, **kwargs)

    def unique_representation(self):
        klant_path = self.klant
        if klant_path.endswith("/"):
            klant_path = klant_path.rstrip("/")
        klant_id = klant_path.rsplit("/")[-1]
        return f"{self.bronorganisatie} {klant_id} at {self.interactiedatum} via {self.kanaal}"


class ObjectContactMoment(APIMixin, models.Model):
    """
    Modelleer een CONTACTMOMENT horend bij een OBJECT.
    """

    uuid = models.UUIDField(
        unique=True, default=uuid.uuid4, help_text="Unieke resource identifier (UUID4)"
    )
    object = models.URLField(
        help_text="URL-referentie naar het gerelateerde OBJECT (in een andere API)."
    )
    object_type = models.CharField(
        "objecttype",
        max_length=100,
        choices=ObjectTypes.choices,
        help_text="Het type van het gerelateerde OBJECT.",
    )
    contactmoment = models.ForeignKey(
        "datamodel.ContactMoment",
        on_delete=models.CASCADE,
        help_text="URL-referentie naar het CONTACTMOMENT.",
    )

    class Meta:
        verbose_name = "object-contactmoment"
        verbose_name_plural = "object-contactmomenten"
        unique_together = ("contactmoment", "object")


class Medewerker(models.Model):
    contactmoment = models.OneToOneField(
        "datamodel.ContactMoment",
        on_delete=models.CASCADE,
        related_name="medewerker_identificatie",
    )
    identificatie = models.CharField(
        max_length=24,
        blank=True,
        help_text="Een korte unieke aanduiding van de MEDEWERKER.",
        db_index=True,
    )
    achternaam = models.CharField(
        max_length=200,
        blank=True,
        help_text="De achternaam zoals de MEDEWERKER die in het dagelijkse verkeer gebruikt.",
    )
    voorletters = models.CharField(
        max_length=20,
        blank=True,
        help_text="De verzameling letters die gevormd wordt door de eerste letter van "
        "alle in volgorde voorkomende voornamen.",
    )
    voorvoegsel_achternaam = models.CharField(
        max_length=10,
        blank=True,
        help_text="Dat deel van de geslachtsnaam dat voorkomt in Tabel 36 (GBA), "
        "voorvoegseltabel, en door een spatie van de geslachtsnaam is",
    )

    class Meta:
        verbose_name = "medewerker"
