from rest_framework import serializers

from apps.redirects.models import RedirectRule


class RedirectRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedirectRule
        fields = "__all__"
        read_only_fields = ['id', 'created_at', 'updated_at', 'user', 'redirect_identifier']
        