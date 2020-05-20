import logging

from rest_framework import mixins, viewsets
from rest_framework.serializers import ValidationError
from rest_framework.settings import api_settings
from vng_api_common.audittrails.viewsets import (
    AuditTrailViewSet,
    AuditTrailViewsetMixin,
)
from vng_api_common.notifications.viewsets import NotificationViewSetMixin
from vng_api_common.permissions import AuthScopesRequired
from vng_api_common.viewsets import CheckQueryParamsMixin

from contactmomenten.datamodel.models import ContactMoment, ObjectContactMoment

from .audits import AUDIT_CONTACTMOMENTEN
from .filters import ObjectContactMomentFilter
from .kanalen import KANAAL_CONTACTMOMENTEN
from .scopes import (
    SCOPE_KLANTEN_AANMAKEN,
    SCOPE_KLANTEN_ALLES_LEZEN,
    SCOPE_KLANTEN_ALLES_VERWIJDEREN,
    SCOPE_KLANTEN_BIJWERKEN,
)
from .serializers import ContactMomentSerializer, ObjectContactMomentSerializer
from .validators import ObjectContactMomentDestroyValidator

logger = logging.getLogger(__name__)


class ContactMomentViewSet(
    NotificationViewSetMixin, AuditTrailViewsetMixin, viewsets.ModelViewSet
):
    """
    Opvragen en bewerken van CONTACTMOMENTen.

    create:
    Maak een CONTACTMOMENT aan.

    Maak een CONTACTMOMENT aan.

    list:
    Alle CONTACTMOMENTen opvragen.

    Alle CONTACTMOMENTen opvragen.

    retrieve:
    Een specifiek CONTACTMOMENT opvragen.

    Een specifiek CONTACTMOMENT opvragen.

    update:
    Werk een CONTACTMOMENT in zijn geheel bij.

    Werk een CONTACTMOMENT in zijn geheel bij.

    partial_update:
    Werk een CONTACTMOMENT deels bij.

    Werk een CONTACTMOMENT deels bij.

    destroy:
    Verwijder een CONTACTMOMENT.

    Verwijder een CONTACTMOMENT.
    """

    queryset = ContactMoment.objects.all()
    serializer_class = ContactMomentSerializer
    lookup_field = "uuid"
    permission_classes = (AuthScopesRequired,)
    required_scopes = {
        "list": SCOPE_KLANTEN_ALLES_LEZEN,
        "retrieve": SCOPE_KLANTEN_ALLES_LEZEN,
        "create": SCOPE_KLANTEN_AANMAKEN,
        "update": SCOPE_KLANTEN_BIJWERKEN,
        "partial_update": SCOPE_KLANTEN_BIJWERKEN,
        "destroy": SCOPE_KLANTEN_ALLES_VERWIJDEREN,
    }
    notifications_kanaal = KANAAL_CONTACTMOMENTEN
    audit = AUDIT_CONTACTMOMENTEN


class ObjectContactMomentViewSet(
    CheckQueryParamsMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.ReadOnlyModelViewSet,
):
    """
    Opvragen en verwijderen van OBJECT-CONTACTMOMENT relaties.

    Het betreft een relatie tussen een willekeurig OBJECT, bijvoorbeeld een
    ZAAK in de Zaken API, en een CONTACTMOMENT.

    create:
    Maak een OBJECT-CONTACTMOMENT relatie aan.

    Maak een OBJECT-CONTACTMOMENT relatie aan.

    **LET OP: Dit endpoint hoor je als consumer niet zelf aan te spreken.**

    Andere API's, zoals de Zaken API, gebruiken dit
    endpoint bij het synchroniseren van relaties.

    list:
    Alle OBJECT-CONTACTMOMENT relaties opvragen.

    Alle OBJECT-CONTACTMOMENT relaties opvragen.

    retrieve:
    Een specifiek OBJECT-CONTACTMOMENT relatie opvragen.

    Een specifiek OBJECT-CONTACTMOMENT relatie opvragen.

    destroy:
    Verwijder een OBJECT-CONTACTMOMENT relatie.

    Verwijder een OBJECT-CONTACTMOMENT relatie.

    **LET OP: Dit endpoint hoor je als consumer niet zelf aan te spreken.**

    Andere API's, zoals de Zaken API, gebruiken dit
    endpoint bij het synchroniseren van relaties.
    """

    queryset = ObjectContactMoment.objects.all()
    serializer_class = ObjectContactMomentSerializer
    filterset_class = ObjectContactMomentFilter
    lookup_field = "uuid"
    permission_classes = (AuthScopesRequired,)
    required_scopes = {
        "list": SCOPE_KLANTEN_ALLES_LEZEN,
        "retrieve": SCOPE_KLANTEN_ALLES_LEZEN,
        "create": SCOPE_KLANTEN_AANMAKEN,
        "destroy": SCOPE_KLANTEN_ALLES_VERWIJDEREN,
    }

    def perform_destroy(self, instance):
        # destroy is only allowed if the remote relation does no longer exist, so check for that
        validator = ObjectContactMomentDestroyValidator()

        try:
            validator(instance)
        except ValidationError as exc:
            raise ValidationError(
                {api_settings.NON_FIELD_ERRORS_KEY: exc}, code=exc.detail[0].code
            )
        else:
            super().perform_destroy(instance)


class ContactMomentAuditTrailViewSet(AuditTrailViewSet):
    """
    Opvragen van de audit trail regels.

    list:
    Alle audit trail regels behorend bij de CONTACTMOMENT.

    Alle audit trail regels behorend bij de CONTACTMOMENT.

    retrieve:
    Een specifieke audit trail regel opvragen.

    Een specifieke audit trail regel opvragen.
    """

    main_resource_lookup_field = "contactmoment_uuid"
