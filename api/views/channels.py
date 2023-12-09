from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from service_objects.services import ServiceOutcome

from api.serializers.channel.serializers import ChannelSerializer
from api.services.channels.list_to_user import ChannelListToUserService


class ChannelsListToUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        outcome = ServiceOutcome(ChannelListToUserService, {
            'workspace_id': id,
            'user': request.user
        })
        return Response({
            'channels': ChannelSerializer(outcome.result, many=True).data
        })
