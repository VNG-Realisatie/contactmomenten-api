from vng_api_common.filtersets import FilterSet

from contactmomenten.datamodel.constants import Rol
from contactmomenten.datamodel.models import ContactMoment, KlantContactMoment, ObjectContactMoment


class ObjectContactMomentFilter(FilterSet):
    class Meta:
        model = ObjectContactMoment
        fields = ("object", "contactmoment")


class ContactMomentFilter(FilterSet):
    class Meta:
        model = ContactMoment
        fields = ("voorkeurstaal",)


class KlantContactMomentFilter(FilterSet):
    class Meta:
        model = KlantContactMoment
        fields = ("contactmoment", "klant", "rol")
