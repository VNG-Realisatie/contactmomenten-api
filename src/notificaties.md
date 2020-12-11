## Notificaties
## Berichtkenmerken voor Contactmomenten API

Kanalen worden typisch per component gedefinieerd. Producers versturen berichten op bepaalde kanalen,
consumers ontvangen deze. Consumers abonneren zich via een notificatiecomponent (zoals <a href="https://notificaties-api.vng.cloud/api/v1/schema/" rel="nofollow">https://notificaties-api.vng.cloud/api/v1/schema/</a>) op berichten.

Hieronder staan de kanalen beschreven die door deze component gebruikt worden, met de kenmerken bij elk bericht.

De architectuur van de notificaties staat beschreven op <a href="https://github.com/VNG-Realisatie/notificaties-api" rel="nofollow">https://github.com/VNG-Realisatie/notificaties-api</a>.


### contactmomenten

**Kanaal**
`contactmomenten`

**Main resource**

`contactmoment`



**Kenmerken**

* `bronorganisatie`: Het RSIN van de Niet-natuurlijk persoon zijnde de organisatie die de klantinteractie heeft gecreeerd. Dit moet een geldig RSIN zijn van 9 nummers en voldoen aan <a href="https://nl.wikipedia.org/wiki/Burgerservicenummer#11-proef" rel="nofollow">https://nl.wikipedia.org/wiki/Burgerservicenummer#11-proef</a>
* `kanaal`: Het communicatiekanaal waarlangs het CONTACTMOMENT gevoerd wordt

**Resources en acties**


* <code>contactmoment</code>: create, update, destroy


