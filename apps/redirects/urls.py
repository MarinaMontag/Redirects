from rest_framework.routers import DefaultRouter

from apps.redirects.views.redirect_rule_retrieve_list import RedirectRuleViewSet

app_name = 'redirects'

router = DefaultRouter()
router.register('', RedirectRuleViewSet, basename='redirect_rules')

urlpatterns = [] + router.urls
