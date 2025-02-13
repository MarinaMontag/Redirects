from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient, APITestCase

from apps.accounts.tests.factories import UserFactory
from apps.redirects.tests.factories import RedirectRuleFactory


class RedirectRuleUpdateTestCase(APITestCase):
    maxDiff = None
    client: APIClient

    def setUp(self):
        self.data = {"is_private": True}

    def test_update_redirect_rule__success(self):
        redirect_rule = RedirectRuleFactory()
        self.client.force_authenticate(redirect_rule.user)

        response = self.client.patch(
            reverse(
                'redirects:modify_redirect_rules',
                kwargs={'redirect_identifier': redirect_rule.redirect_identifier},
            ),
            data=self.data,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        redirect_rule.refresh_from_db()
        self.assertTrue(redirect_rule.is_private)

    def test_update_redirect_rule__not_authorized(self):
        redirect_rule = RedirectRuleFactory()
        response = self.client.patch(
            reverse(
                'redirects:modify_redirect_rules',
                kwargs={'redirect_identifier': redirect_rule.redirect_identifier},
            ),
            data=self.data,
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_redirect_rule__not_found(self):
        redirect_rule = RedirectRuleFactory()
        user = UserFactory()
        self.client.force_authenticate(user)
        response = self.client.patch(
            reverse(
                'redirects:modify_redirect_rules',
                kwargs={'redirect_identifier': redirect_rule.redirect_identifier},
            ),
            data=self.data,
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)