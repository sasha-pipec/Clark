from rest_framework import serializers

from api.serializers.user.serializers import UserMessageSerializer
from models_app.models import Message


class MessageSerializer(serializers.ModelSerializer):
    author = UserMessageSerializer()

    class Meta:
        model = Message
        fields = (
            'id',
            'author',
            'created_at',
            'text'
        )
