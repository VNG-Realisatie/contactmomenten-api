# Generated by Django 2.2.11 on 2020-05-19 10:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_better_admin_arrayfield.models.fields
import uuid
import vng_api_common.fields
import vng_api_common.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ContactMoment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        help_text="Unieke resource identifier (UUID4)",
                        unique=True,
                    ),
                ),
                (
                    "bronorganisatie",
                    vng_api_common.fields.RSINField(
                        help_text="Het RSIN van de Niet-natuurlijk persoon zijnde de organisatie die de klantinteractie heeft gecreeerd. Dit moet een geldig RSIN zijn van 9 nummers en voldoen aan https://nl.wikipedia.org/wiki/Burgerservicenummer#11-proef",
                        max_length=9,
                    ),
                ),
                (
                    "klant",
                    models.URLField(
                        blank=True,
                        help_text="URL-referentie naar een KLANT (in Klanten API)",
                        max_length=1000,
                    ),
                ),
                (
                    "interactiedatum",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        help_text="De datum en het tijdstip waarop de klantinteractie heeft plaatsgevonden.",
                    ),
                ),
                (
                    "tekst",
                    models.TextField(
                        blank=True,
                        help_text="Een toelichting die inhoudelijk de klantinteractie van de klant beschrijft.",
                    ),
                ),
                (
                    "voorkeurskanaal",
                    models.CharField(
                        blank=True,
                        help_text="Het communicatiekanaal dat voor opvolging van de klantinteractie de voorkeur heeft van de KLANT.",
                        max_length=50,
                    ),
                ),
                (
                    "kanaal",
                    models.CharField(
                        blank=True,
                        help_text="Het communicatiekanaal waarlangs het CONTACTMOMENT gevoerd wordt",
                        max_length=50,
                    ),
                ),
                (
                    "initiatiefnemer",
                    models.CharField(
                        blank=True,
                        choices=[("gemeente", "gemeente"), ("klant", "klant")],
                        help_text="De partij die het contact heeft geïnitieerd.",
                        max_length=20,
                    ),
                ),
                (
                    "medewerker",
                    models.URLField(
                        blank=True,
                        help_text="URL-referentie naar een medewerker",
                        max_length=1000,
                    ),
                ),
                (
                    "onderwerp_links",
                    django_better_admin_arrayfield.models.fields.ArrayField(
                        base_field=models.URLField(
                            help_text="URL naar een product, webpagina of andere entiteit zodat contactmomenten gegroepeerd kunnen worden.",
                            max_length=1000,
                            verbose_name="onderwerp link",
                        ),
                        blank=True,
                        default=list,
                        help_text="Eén of meerdere links naar een product, webpagina of andere entiteit zodat contactmomenten gegroepeerd kunnen worden op onderwerp.",
                        size=None,
                    ),
                ),
            ],
            options={
                "verbose_name": "contactmoment",
                "verbose_name_plural": "contactmomenten",
            },
            bases=(vng_api_common.models.APIMixin, models.Model),
        ),
        migrations.CreateModel(
            name="Medewerker",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "identificatie",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        help_text="Een korte unieke aanduiding van de MEDEWERKER.",
                        max_length=24,
                    ),
                ),
                (
                    "achternaam",
                    models.CharField(
                        blank=True,
                        help_text="De achternaam zoals de MEDEWERKER die in het dagelijkse verkeer gebruikt.",
                        max_length=200,
                    ),
                ),
                (
                    "voorletters",
                    models.CharField(
                        blank=True,
                        help_text="De verzameling letters die gevormd wordt door de eerste letter van alle in volgorde voorkomende voornamen.",
                        max_length=20,
                    ),
                ),
                (
                    "voorvoegsel_achternaam",
                    models.CharField(
                        blank=True,
                        help_text="Dat deel van de geslachtsnaam dat voorkomt in Tabel 36 (GBA), voorvoegseltabel, en door een spatie van de geslachtsnaam is",
                        max_length=10,
                    ),
                ),
                (
                    "contactmoment",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="medewerker_identificatie",
                        to="datamodel.ContactMoment",
                    ),
                ),
            ],
            options={"verbose_name": "medewerker",},
        ),
        migrations.CreateModel(
            name="ObjectContactMoment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        help_text="Unieke resource identifier (UUID4)",
                        unique=True,
                    ),
                ),
                (
                    "object",
                    models.URLField(
                        help_text="URL-referentie naar het gerelateerde OBJECT (in een andere API)."
                    ),
                ),
                (
                    "object_type",
                    models.CharField(
                        choices=[("zaak", "Zaak")],
                        help_text="Het type van het gerelateerde OBJECT.",
                        max_length=100,
                        verbose_name="objecttype",
                    ),
                ),
                (
                    "contactmoment",
                    models.ForeignKey(
                        help_text="URL-referentie naar het CONTACTMOMENT.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="datamodel.ContactMoment",
                    ),
                ),
            ],
            options={
                "verbose_name": "object-contactmoment",
                "verbose_name_plural": "object-contactmomenten",
                "unique_together": {("contactmoment", "object")},
            },
            bases=(vng_api_common.models.APIMixin, models.Model),
        ),
    ]
