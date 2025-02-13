import factory

from apps.redirects.models import RedirectRule


class RedirectRuleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = RedirectRule

    user = factory.SubFactory('apps.accounts.tests.factories.UserFactory')
    redirect_url = 'https://vivat.com.ua/category/knyhy/'
