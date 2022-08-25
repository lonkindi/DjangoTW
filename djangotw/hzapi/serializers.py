from rest_framework import serializers

from hzapi.models import Anket


class AnketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anket
        fields = ('external_id', 'state', 'content',)
        read_only_fields = ('id',)
