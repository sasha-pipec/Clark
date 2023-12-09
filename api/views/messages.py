from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from service_objects.services import ServiceOutcome

from api.serializers.message.serializers import MessageSerializer
from api.services.messages.create import MessageCreateService
from api.services.messages.list_to_user import MessageListToUserService


class MessageListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        outcome = ServiceOutcome(MessageListToUserService, request.query_params)
        return Response({
            'messages': MessageSerializer(outcome.result, many=True).data
        })

    def post(self, request):
        outcome = ServiceOutcome(MessageCreateService, request.data | {'author': request.user})
        return Response(MessageSerializer(outcome.result).data)
