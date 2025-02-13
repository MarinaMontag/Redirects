from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient

from apps.accounts.tests.factories import UserFactory
from apps.redirects.tests.factories import RedirectRuleFactory


class RedirectRuleTestCase(APITestCase):
    maxDiff = None
    client: APIClient

    def test_public_redirect__success(self):
        redirect_rule = RedirectRuleFactory()
        response = self.client.get(
            reverse(
                'redirects:public_redirect',
                kwargs={'redirect_identifier': redirect_rule.redirect_identifier},
            ),
            follow=False,
        )

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response["Location"], redirect_rule.redirect_url)

    def test_private_redirect__success(self):
        redirect_rule = RedirectRuleFactory(is_private=True)
        user = UserFactory()
        self.client.force_authenticate(user=user)
        response = self.client.get(
            reverse(
                'redirects:private_redirect',
                kwargs={'redirect_identifier': redirect_rule.redirect_identifier},
            ),
            follow=False,
        )

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response["Location"], redirect_rule.redirect_url)

    def test_private_redirect__not_authorized(self):
        redirect_rule = RedirectRuleFactory(is_private=True)
        response = self.client.get(
            reverse(
                'redirects:private_redirect',
                kwargs={'redirect_identifier': redirect_rule.redirect_identifier},
            ),
            follow=False,
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)