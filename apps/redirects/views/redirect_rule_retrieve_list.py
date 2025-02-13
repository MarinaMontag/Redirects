from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiResponse
from rest_framework import mixins, status
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from apps.common.paginations import PageNumberPagination
from apps.redirects.models import RedirectRule
from apps.redirects.serializers.redirect_rule import RedirectRuleSerializer


@extend_schema_view(
    list=extend_schema(
        description='List all redirect rules',
        responses={status.HTTP_200_OK: RedirectRuleSerializer,},
    ),
    retrieve=extend_schema(
        description='Retrieve a redirect rule',
        responses={status.HTTP_200_OK: RedirectRuleSerializer,},
    ),
)
class RedirectRuleGetViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    serializer_class = RedirectRuleSerializer
    permission_classes = [AllowAny]
    queryset = RedirectRule.objects.all()
    lookup_url_kwarg = 'redirect_identifier'
    lookup_field = 'redirect_identifier'
    pagination_class = PageNumberPagination

