from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.redirects.views.redirect_rule_create_update_delete import RedirectRuleModifyViewSet
from apps.redirects.views.redirect_rule_retrieve_list import RedirectRuleGetViewSet

app_name = 'redirects'

router = DefaultRouter()
router.register('', RedirectRuleGetViewSet, basename='get_redirect_rules')

urlpatterns = [
    path(
        'modify/',
        RedirectRuleModifyViewSet.as_view({'post': 'create'}),
        name='create_redirect_rules',
    ),
    path(
        'modify/<str:redirect_identifier>/',
        RedirectRuleModifyViewSet.as_view({'patch': 'partial_update', 'delete': 'destroy'}),
        name='modify_redirect_rules',
    ),
] + router.urls
