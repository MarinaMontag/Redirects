from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient

from apps.accounts.tests.factories import UserFactory
from apps.redirects.models import RedirectRule
from apps.redirects.tests.factories import RedirectRuleFactory


class RedirectRuleDeleteTestCase(APITestCase):
    maxDiff = None
    client: APIClient

    def test_delete_redirect_rule__success(self):
        redirect_rule = RedirectRuleFactory()
        user = redirect_rule.user
        self.client.force_authenticate(user)

        response = self.client.delete(
            reverse(
                'redirects:modify_redirect_rules',
                kwargs={'redirect_identifier': redirect_rule.redirect_identifier},
            ),
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(RedirectRule.objects.filter(user_id=user.pk).exists())

    def test_delete_redirect_rule__not_authorized(self):
        redirect_rule = RedirectRuleFactory()
        response = self.client.delete(
            reverse(
                'redirects:modify_redirect_rules',
                kwargs={'redirect_identifier': redirect_rule.redirect_identifier},
            ),
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_redirect_rule__not_found(self):
        redirect_rule = RedirectRuleFactory()
        user = UserFactory()
        self.client.force_authenticate(user)
        response = self.client.patch(
            reverse(
                'redirects:modify_redirect_rules',
                kwargs={'redirect_identifier': redirect_rule.redirect_identifier},
            ),
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)