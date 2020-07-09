import logging

from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from vng_api_common.serializers import add_choice_values_help_text
from vng_api_common.validators import IsImmutableValidator

from contactmomenten.datamodel.constants import ObjectTypes
from contactmomenten.datamodel.models import (
    ContactMoment,
    KlantContactMoment,
    Medewerker,
    ObjectContactMoment,
)

from .validators import ObjectContactMomentCreateValidator

logger = logging.getLogger(__name__)


class MedewerkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medewerker
        fields = (
            "identificatie",
            "achternaam",
            "voorletters",
            "voorvoegsel_achternaam",
        )


class ContactMomentSerializer(serializers.HyperlinkedModelSerializer):
    medewerker_identificatie = MedewerkerSerializer(required=False, allow_null=True)

    class Meta:
        model = ContactMoment
        fields = (
            "url",
            "vorig_contactmoment",
            "volgend_contactmoment",
            "bronorganisatie",
            "klant",
            "interactiedatum",
            "kanaal",
            "voorkeurskanaal",
            "voorkeurstaal",
            "tekst",
            "onderwerp_links",
            "initiatiefnemer",
            "medewerker",
            "medewerker_identificatie",
        )
        extra_kwargs = {
            "url": {"lookup_field": "uuid"},
            "vorig_contactmoment": {"lookup_field": "uuid"},
            "volgend_contactmoment": {
                "lookup_field": "uuid",
                "read_only": True,
                "allow_null": True,
                "help_text": _("URL-referentie naar het volgende CONTACTMOMENT."),
            },
        }

    def validate(self, attrs):
        validated_attrs = super().validate(attrs)

        medewerker = validated_attrs.get("medewerker", None)
        medewerker_identificatie = validated_attrs.get("medewerker_identificatie", None)

        if self.instance:
            medewerker = medewerker or self.instance.medewerker
            medewerker_identificatie = medewerker_identificatie or getattr(
                self.instance, "medewerker_identificatie", None
            )

        if not medewerker and not medewerker_identificatie:
            raise serializers.ValidationError(
                _("medewerker or medewerkerIdentificatie must be provided"),
                code="invalid-medewerker",
            )

        return validated_attrs

    def create(self, validated_data):
        medewerker_identificatie_data = validated_data.pop(
            "medewerker_identificatie", None
        )
        contactmoment = super().create(validated_data)

        if medewerker_identificatie_data:
            medewerker_identificatie_data["contactmoment"] = contactmoment
            MedewerkerSerializer().create(medewerker_identificatie_data)

        return contactmoment

    def update(self, instance, validated_data):
        medewerker_identificatie_data = validated_data.pop(
            "medewerker_identificatie", None
        )
        contactmoment = super().update(instance, validated_data)

        if medewerker_identificatie_data:
            if hasattr(contactmoment, "medewerker_identificatie"):
                MedewerkerSerializer().update(
                    contactmoment.medewerker_identificatie,
                    medewerker_identificatie_data,
                )
            else:
                medewerker_identificatie_data["contactmoment"] = contactmoment
                MedewerkerSerializer().create(medewerker_identificatie_data)

        return contactmoment


class ObjectContactMomentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ObjectContactMoment
        fields = ("url", "contactmoment", "object", "object_type")
        extra_kwargs = {
            "url": {"lookup_field": "uuid"},
            "contactmoment": {
                "lookup_field": "uuid",
                "validators": [IsImmutableValidator()],
            },
            "object": {"validators": [IsImmutableValidator()],},
            "object_type": {"validators": [IsImmutableValidator()]},
        }
        validators = [ObjectContactMomentCreateValidator()]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        value_display_mapping = add_choice_values_help_text(ObjectTypes)
        self.fields["object_type"].help_text += f"\n\n{value_display_mapping}"

        if not hasattr(self, "initial_data"):
            return


class KlantContactMomentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = KlantContactMoment
        fields = (
            "url",
            "contactmoment",
            "klant",
            "rol",
        )
        extra_kwargs = {
            "url": {"lookup_field": "uuid"},
            "contactmoment": {"lookup_field": "uuid"},
        }
