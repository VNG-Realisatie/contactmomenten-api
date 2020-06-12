from vng_api_common.filtersets import FilterSet

from contactmomenten.datamodel.models import ContactMoment, ObjectContactMoment


class ObjectContactMomentFilter(FilterSet):
    class Meta:
        model = ObjectContactMoment
        fields = ("object", "contactmoment")


class ContactMomentFilter(FilterSet):
    class Meta:
        model = ContactMoment
        fields = ("voorkeurstaal",)
