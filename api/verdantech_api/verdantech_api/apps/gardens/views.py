from rest_framework import serializers

# from rest_framework.response import Response
from rest_framework.views import APIView


class GardenCreateView(APIView):
    class InputSerializer(serializers.Serializer):
        name = serializers.CharField()
        # creator_id = serial.primarykey
        visibility = serializers.CharField()
        # admin_invitees
        # editor_invitees
        # viewer_invitees
        # timezone

    # class OutputSerializer():
