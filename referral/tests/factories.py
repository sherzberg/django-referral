import factory

from referral.models import Campaign, Referrer


class CampaignFactory(factory.Factory):
    FACTORY_FOR = Campaign

    name = factory.Sequence(lambda n: "Test Campaign %s" % n)
    description = "Some long test description"

class ReferrerFactory(factory.Factory):
    FACTORY_FOR = Referrer

    name = factory.Sequence(lambda n: "Test Referrer %s" % n)
    description = "Some long test description"
