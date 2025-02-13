from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from apps.redirects.models import RedirectRule
from apps.redirects.serializers.redirect_rule import RedirectRuleSerializer


@extend_schema_view(
    create=extend_schema(
        description='Create a redirect rule',
        responses={
            status.HTTP_201_CREATED: RedirectRuleSerializer,
            status.HTTP_400_BAD_REQUEST: 'Invalid input data.',
            status.HTTP_401_UNAUTHORIZED: 'User is not authenticated.',
            status.HTTP_404_NOT_FOUND: 'Redirect rule wasn\'t found.',
        },
    ),
    partial_update=extend_schema(
        description='Update the redirect rule',
        responses={
            status.HTTP_200_OK: RedirectRuleSerializer,
            status.HTTP_400_BAD_REQUEST: 'Invalid input data.',
            status.HTTP_401_UNAUTHORIZED: 'User is not authenticated.',
            status.HTTP_404_NOT_FOUND: 'Redirect rule wasn\'t found.',
        },
    ),
    destroy=extend_schema(
        description='Remove the redirect rule',
        responses={
            status.HTTP_204_NO_CONTENT: 'Redirect rule was successfully deleted.',
            status.HTTP_401_UNAUTHORIZED: 'User is not authenticated.',
            status.HTTP_404_NOT_FOUND: 'Redirect rule wasn\'t found.',
        },
    ),
)
class RedirectRuleModifyViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    serializer_class = RedirectRuleSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'redirect_identifier'
    lookup_field = 'redirect_identifier'

    def get_queryset(self):
        return RedirectRule.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
