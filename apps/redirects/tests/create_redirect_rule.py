from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient

from apps.accounts.tests.factories import UserFactory
from apps.redirects.models import RedirectRule


class RedirectRuleCreateTestCase(APITestCase):
    maxDiff = None
    client: APIClient

    def setUp(self):
        self.data = {"redirect_url": "https://google.com"}

    def test_create_redirect_rule__success(self):
        self.user = UserFactory()
        self.client.force_authenticate(self.user)

        response = self.client.post(
            reverse('redirects:create_redirect_rules'),
            data=self.data,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(RedirectRule.objects.filter(user_id=self.user.pk, **self.data).exists())

    def test_create_redirect_rule__not_authorized(self):
        response = self.client.post(
            reverse('redirects:create_redirect_rules'),
            data=self.data,
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)