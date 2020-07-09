from django.utils.translation import ugettext_lazy as _

from vng_api_common.filters import URLModelChoiceFilter
from vng_api_common.filtersets import FilterSet

from contactmomenten.datamodel.constants import Rol
from contactmomenten.datamodel.models import (
    ContactMoment,
    KlantContactMoment,
    ObjectContactMoment,
)


class ObjectContactMomentFilter(FilterSet):
    class Meta:
        model = ObjectContactMoment
        fields = ("object", "contactmoment")


class ContactMomentFilter(FilterSet):
    class Meta:
        model = ContactMoment
        fields = ("voorkeurstaal", "vorig_contactmoment", "volgend_contactmoment")

    @classmethod
    def filter_for_field(cls, f, name, lookup_expr):
        # Needed because `volgend_contactmoment` is a reverse OneToOne rel
        if f.name == "volgend_contactmoment":
            filter = URLModelChoiceFilter()
            filter.field_name = "volgend_contactmoment"
            filter.extra["help_text"] = _(
                "URL-referentie naar het volgende CONTACTMOMENT."
            )
            filter.queryset = ContactMoment.objects.all()
        else:
            filter = super().filter_for_field(f, name, lookup_expr)
        return filter


class KlantContactMomentFilter(FilterSet):
    class Meta:
        model = KlantContactMoment
        fields = ("contactmoment", "klant", "rol")
