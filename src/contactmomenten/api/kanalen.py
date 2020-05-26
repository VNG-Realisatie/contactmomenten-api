from django.conf import settings

from vng_api_common.notifications.kanalen import Kanaal

from contactmomenten.datamodel.models import ContactMoment

KANAAL_CONTACTMOMENTEN = Kanaal(
    settings.NOTIFICATIONS_KANAAL,
    main_resource=ContactMoment,
    kenmerken=("bronorganisatie", "kanaal"),
)
