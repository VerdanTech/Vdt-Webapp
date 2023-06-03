from rest_framework import serializers
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from .selectors import garden_list


class GardenListView(APIView):

    authentication_classes = [SessionAuthentication]

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField()
        creator_username = serializers.SerializerMethodField()

        def get_creator_username(self, garden):
            creator = garden.creator
            if creator is not None:
                return creator.username
            else:
                return ""

    def get(self, request):

        gardens = garden_list(fetched_by=request.user)
        data = self.OutputSerializer(gardens, many=True).data

        return Response(data)


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
