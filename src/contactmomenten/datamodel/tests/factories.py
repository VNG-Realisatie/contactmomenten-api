import factory.fuzzy

from ..constants import InitiatiefNemer, ObjectTypes


class ContactMomentFactory(factory.django.DjangoModelFactory):
    bronorganisatie = factory.Faker("ssn", locale="nl_NL")
    kanaal = factory.Faker("word")
    initiatiefnemer = factory.fuzzy.FuzzyChoice(InitiatiefNemer.values)
    medewerker = factory.Faker("url")

    class Meta:
        model = "datamodel.ContactMoment"


class ObjectContactMomentFactory(factory.django.DjangoModelFactory):
    contactmoment = factory.SubFactory(ContactMomentFactory)
    object_type = factory.fuzzy.FuzzyChoice(ObjectTypes.values)
    object = factory.Faker("url")

    class Meta:
        model = "datamodel.ObjectContactMoment"


class MedewerkerFactory(factory.django.DjangoModelFactory):
    contactmoment = factory.SubFactory(ContactMomentFactory)
    identificatie = factory.Sequence(lambda n: f"{n}")
    achternaam = factory.Faker("last_name")

    class Meta:
        model = "datamodel.Medewerker"


class KlantContactMomentFactory(factory.django.DjangoModelFactory):
    contactmoment = factory.SubFactory(ContactMomentFactory)
    klant = factory.Faker("url")

    class Meta:
        model = "datamodel.KlantContactMoment"
