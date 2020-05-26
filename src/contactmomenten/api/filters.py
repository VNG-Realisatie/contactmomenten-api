from vng_api_common.filtersets import FilterSet

from contactmomenten.datamodel.models import ObjectContactMoment


class ObjectContactMomentFilter(FilterSet):
    class Meta:
        model = ObjectContactMoment
        fields = ("object", "contactmoment")
