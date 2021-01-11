===================
Contactmomenten API
===================

:Version: master
:Source: https://github.com/VNG-Realisatie/contactmomenten-api
:Keywords: zaken, zaakgericht werken, GEMMA


Introductie
===========

API voor opslag en ontsluiting van contactmomenten en daarbij behorende metadata.

Deze API ondersteunt het verwerken van gegevens van contactmomenten inclusief de relatie met eventuele za(a)k(en), klant(en) en/of verzoek(en).

API specificaties
=================

|lint-oas| |generate-sdks| |generate-postman-collection|

==========  ==============  ====================================================================================================================================================================================================  =======================================================================================================================  =================================================================================================================================
Versie      Release datum   API specificatie                                                                                                                                                                                      Autorisaties                                                                                                             Notificaties
==========  ==============  ====================================================================================================================================================================================================  =======================================================================================================================  =================================================================================================================================
master      n.v.t.          `ReDoc <https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/VNG-Realisatie/contactmomenten-api/master/src/openapi.yaml>`_,                                                         `Scopes <https://github.com/VNG-Realisatie/contactmomenten-api/blob/master/src/autorisaties.md>`_                        `Berichtkenmerken <https://github.com/VNG-Realisatie/contactmomenten-api/blob/master/src/notificaties.md>`_
                            `Swagger <https://petstore.swagger.io/?url=https://raw.githubusercontent.com/VNG-Realisatie/contactmomenten-api/master/src/openapi.yaml>`_
1.0.0       n.v.t.          `ReDoc <https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/VNG-Realisatie/contactmomenten-api/1.0.0/src/openapi.yaml>`_,                                                          `Scopes <https://github.com/VNG-Realisatie/contactmomenten-api/blob/1.0.0/src/autorisaties.md>`_                         `Berichtkenmerken <https://github.com/VNG-Realisatie/contactmomenten-api/blob/1.0.0/src/notificaties.md>`_
                            `Swagger <https://petstore.swagger.io/?url=https://raw.githubusercontent.com/VNG-Realisatie/contactmomenten-api/1.0.0/src/openapi.yaml>`_
==========  ==============  ====================================================================================================================================================================================================  =======================================================================================================================  =================================================================================================================================

Zie ook: `Alle versies en wijzigingen <https://github.com/VNG-Realisatie/contactmomenten-api/blob/master/CHANGELOG.rst>`_

Ondersteuning
-------------

==========  ==============  ==========================  =================
Versie      Release datum   Einddatum ondersteuning     Documentatie
==========  ==============  ==========================  =================
==========  ==============  ==========================  =================

Referentie implementatie
========================

|build-status| |coverage| |docker| |black| |python-versions|

Referentieimplementatie van de Contactmomenten API. Ook wel
contactmomentencomponent (CMC) genoemd.

Ontwikkeld door `Maykin Media B.V. <https://www.maykinmedia.nl>`_ in opdracht
van VNG Realisatie.

Deze referentieimplementatie toont aan dat de API specificatie voor de
Zaken API implementeerbaar is, en vormt een voorbeeld voor andere
implementaties indien ergens twijfel bestaat.

Deze component heeft ook een `demo omgeving`_ waar leveranciers tegenaan kunnen
testen.

Links
=====

* Deze API is onderdeel van de `VNG standaard "API's voor Zaakgericht werken" <https://github.com/VNG-Realisatie/gemma-zaken>`_.
* Lees de `functionele specificatie <https://vng-realisatie.github.io/gemma-zaken/standaard/contactmomenten/index>`_ bij de API specificatie.
* Bekijk de `demo omgeving`_ met de laatst gepubliceerde versie.
* Bekijk de `test omgeving <https://contactmomenten-api.test.vng.cloud/>`_ met de laatste ontwikkel versie.
* Rapporteer `issues <https://github.com/VNG-Realisatie/gemma-zaken/issues>`_ bij vragen, fouten of wensen.
* Bekijk de `code <https://github.com/VNG-Realisatie/contactmomenten-api/>`_ van de referentie implementatie.

.. _`demo omgeving`: https://contactmomenten-api.vng.cloud/

Licentie
========

Copyright © VNG Realisatie 2018 - 2020

Licensed under the EUPL_

.. _EUPL: LICENCE.md

.. |build-status| image:: https://github.com/VNG-Realisatie/contactmomenten-api/workflows/ci-build/badge.svg
    :alt: Build status
    :target: https://github.com/VNG-Realisatie/contactmomenten-api/actions?query=workflow%3Aci-build

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

.. |lint-oas| image:: https://github.com/VNG-Realisatie/contactmomenten-api/workflows/lint-oas/badge.svg
    :alt: Lint OAS
    :target: https://github.com/VNG-Realisatie/contactmomenten-api/actions?query=workflow%3Alint-oas

.. |generate-sdks| image:: https://github.com/VNG-Realisatie/contactmomenten-api/workflows/generate-sdks/badge.svg
    :alt: Generate SDKs
    :target: https://github.com/VNG-Realisatie/contactmomenten-api/actions?query=workflow%3Agenerate-sdks

.. |generate-postman-collection| image:: https://github.com/VNG-Realisatie/contactmomenten-api/workflows/generate-postman-collection/badge.svg
    :alt: Generate Postman collection
    :target: https://github.com/VNG-Realisatie/contactmomenten-api/actions?query=workflow%3Agenerate-postman-collection
.. _testomgeving: https://contactmomenten-api.vng.cloud

.. |requirements| image:: https://requires.io/github/VNG-Realisatie/contactmomenten-api/requirements.svg?branch=master
     :target: https://requires.io/github/VNG-Realisatie/contactmomenten-api/requirements/?branch=master
     :alt: Requirements status

.. |coverage| image:: https://codecov.io/github/VNG-Realisatie/contactmomenten-api/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage
    :target: https://codecov.io/gh/VNG-Realisatie/contactmomenten-api

.. |docker| image:: https://img.shields.io/badge/docker-latest-blue.svg
    :alt: Docker image
    :target: https://hub.docker.com/r/vngr/contactmomenten-api/

.. |python-versions| image:: https://img.shields.io/badge/python-3.7%2B-blue.svg
    :alt: Supported Python version
    :target: https://hub.docker.com/r/vngr/contactmomenten-api/






Referentieimplementatie van de Contactmomenten API.

Inleiding
=========

Deze referentieimplementatie toont aan dat de API specificatie voor
Contactmomenten implementeerbaar is, en vormt een voorbeeld voor andere
implementaties indien ergens twijfel bestaat.

Deze component heeft ook een `testomgeving`_ waar leveranciers tegenaan kunnen
testen.

Documentatie
============

Zie ``INSTALL.rst`` voor installatieinstructies, beschikbare instellingen en
commando's.

Indien je actief gaat ontwikkelen aan deze component raden we aan om niet van
Docker gebruik te maken. Indien je deze component als black-box wil gebruiken,
raden we aan om net wel van Docker gebruik te maken.

Handige links
=============

* `Issues <https://github.com/VNG-Realisatie/contactmomenten-api/issues>`_
* `Code <https://github.com/VNG-Realisatie/contactmomenten-api>`_

Licentie
========

Copyright © VNG Realisatie 2020

Licensed under the EUPL_

.. _EUPL: LICENCE.md

.. |build-status| image:: https://travis-ci.com/VNG-Realisatie/contactmomenten-api.svg?branch=master
    :alt: Build status
    :target: https://travis-ci.com/VNG-Realisatie/contactmomenten-api

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

.. |lint-oas| image:: https://github.com/VNG-Realisatie/contactmomenten-api/workflows/lint-oas/badge.svg
    :alt: Lint OAS
    :target: https://github.com/VNG-Realisatie/contactmomenten-api/actions?query=workflow%3Alint-oas

.. |generate-sdks| image:: https://github.com/VNG-Realisatie/contactmomenten-api/workflows/generate-sdks/badge.svg
    :alt: Generate SDKs
    :target: https://github.com/VNG-Realisatie/contactmomenten-api/actions?query=workflow%3Agenerate-sdks

.. |generate-postman-collection| image:: https://github.com/VNG-Realisatie/contactmomenten-api/workflows/generate-postman-collection/badge.svg
    :alt: Generate Postman collection
    :target: https://github.com/VNG-Realisatie/contactmomenten-api/actions?query=workflow%3Agenerate-postman-collection
.. _testomgeving: https://contactmomenten-api.vng.cloud
