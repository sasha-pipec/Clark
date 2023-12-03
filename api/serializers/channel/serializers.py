from rest_framework import serializers

from models_app.models import Channel


class ChannelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Channel
        fields = (
            'name',
        )