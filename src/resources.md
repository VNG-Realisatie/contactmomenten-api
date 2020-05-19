# Resources

Dit document beschrijft de (RGBZ-)objecttypen die als resources ontsloten
worden met de beschikbare attributen.


## Medewerker

Objecttype op [GEMMA Online](https://www.gemmaonline.nl/index.php/Rgbz_1.0/doc/objecttype/medewerker)

| Attribuut | Omschrijving | Type | Verplicht | CRUD* |
| --- | --- | --- | --- | --- |
| identificatie | Een korte unieke aanduiding van de MEDEWERKER. | string | nee | C​R​U​D |
| achternaam | De achternaam zoals de MEDEWERKER die in het dagelijkse verkeer gebruikt. | string | nee | C​R​U​D |
| voorletters | De verzameling letters die gevormd wordt door de eerste letter van alle in volgorde voorkomende voornamen. | string | nee | C​R​U​D |
| voorvoegselAchternaam | Dat deel van de geslachtsnaam dat voorkomt in Tabel 36 (GBA), voorvoegseltabel, en door een spatie van de geslachtsnaam is | string | nee | C​R​U​D |

## ContactMoment

Objecttype op [GEMMA Online](https://www.gemmaonline.nl/index.php/Rgbz_1.0/doc/objecttype/contactmoment)

| Attribuut | Omschrijving | Type | Verplicht | CRUD* |
| --- | --- | --- | --- | --- |
| url | URL-referentie naar dit object. Dit is de unieke identificatie en locatie van dit object. | string | nee | ~~C~~​R​~~U~~​~~D~~ |
| bronorganisatie | Het RSIN van de Niet-natuurlijk persoon zijnde de organisatie die de klantinteractie heeft gecreeerd. Dit moet een geldig RSIN zijn van 9 nummers en voldoen aan https://nl.wikipedia.org/wiki/Burgerservicenummer#11-proef | string | ja | C​R​U​D |
| klant | URL-referentie naar een KLANT (in Klanten API) | string | nee | C​R​U​D |
| interactiedatum | De datum en het tijdstip waarop de klantinteractie heeft plaatsgevonden. | string | nee | C​R​U​D |
| kanaal | Het communicatiekanaal waarlangs het CONTACTMOMENT gevoerd wordt | string | nee | C​R​U​D |
| voorkeurskanaal | Het communicatiekanaal dat voor opvolging van de klantinteractie de voorkeur heeft van de KLANT. | string | nee | C​R​U​D |
| tekst | Een toelichting die inhoudelijk de klantinteractie van de klant beschrijft. | string | nee | C​R​U​D |
| onderwerpLinks | Eén of meerdere links naar een product, webpagina of andere entiteit zodat contactmomenten gegroepeerd kunnen worden op onderwerp. | array | nee | C​R​U​D |
| initiatiefnemer | De partij die het contact heeft geïnitieerd. | string | nee | C​R​U​D |
| medewerker | URL-referentie naar een medewerker | string | nee | C​R​U​D |

## ObjectContactMoment

Objecttype op [GEMMA Online](https://www.gemmaonline.nl/index.php/Rgbz_1.0/doc/objecttype/objectcontactmoment)

| Attribuut | Omschrijving | Type | Verplicht | CRUD* |
| --- | --- | --- | --- | --- |
| url | URL-referentie naar dit object. Dit is de unieke identificatie en locatie van dit object. | string | nee | ~~C~~​R​~~U~~​~~D~~ |
| contactmoment | URL-referentie naar het CONTACTMOMENT. | string | ja | C​R​U​D |
| object | URL-referentie naar het gerelateerde OBJECT (in een andere API). | string | ja | C​R​U​D |
| objectType | Het type van het gerelateerde OBJECT.

Uitleg bij mogelijke waarden:

* `zaak` - Zaak | string | ja | C​R​U​D |


* Create, Read, Update, Delete
