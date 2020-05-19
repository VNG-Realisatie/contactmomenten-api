from django.utils.translation import ugettext_lazy as _

from djchoices import ChoiceItem, DjangoChoices


class InitiatiefNemer(DjangoChoices):
    gemeente = ChoiceItem("gemeente", _("gemeente"))
    klant = ChoiceItem("klant", _("klant"))


class ObjectTypes(DjangoChoices):
    zaak = ChoiceItem("zaak", _("Zaak"))
