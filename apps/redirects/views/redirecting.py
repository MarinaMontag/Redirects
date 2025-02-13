from django.shortcuts import get_object_or_404, redirect
from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView

from apps.redirects.models import RedirectRule


@extend_schema(
    responses={
        status.HTTP_302_FOUND: OpenApiResponse(description='Successfully redirected'),
        status.HTTP_404_NOT_FOUND: OpenApiResponse(description='Redirect not found'),
    },
)
class PublicRedirectView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, redirect_identifier):
        redirect_rule = get_object_or_404(RedirectRule, redirect_identifier=redirect_identifier, is_private=False)

        return redirect(redirect_rule.redirect_url)


@extend_schema(
    responses={
        status.HTTP_302_FOUND: OpenApiResponse(description='Successfully redirected'),
        status.HTTP_401_UNAUTHORIZED: OpenApiResponse(description='User is not authenticated'),
        status.HTTP_404_NOT_FOUND: OpenApiResponse(description='Redirect not found'),
    },
)
class PrivateRedirectView(APIView):
    permission_classes = [IsAuthenticated]


    def get(self, request, redirect_identifier):
        redirect_rule = get_object_or_404(RedirectRule, redirect_identifier=redirect_identifier, is_private=True)

        return redirect(redirect_rule.redirect_url)

