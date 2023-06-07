from rest_framework import serializers
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Garden
from .selectors import garden_detail, garden_list, garden_members
from .services import garden_create, garden_create_parse_invitees, garden_update


class GardenListView(APIView):
    authentication_classes = [SessionAuthentication]

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        hashid = serializers.CharField()
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
    authentication_classes = [SessionAuthentication]

    class InputSerializer(serializers.Serializer):
        name = serializers.CharField()
        invitees = serializers.ListField(child=serializers.DictField(), required=False)

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        hashid = serializers.CharField()
        name = serializers.CharField()
        invitations_sent = serializers.ListField(child=serializers.DictField())

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        name = serializer.validated_data["name"]
        invitees = serializer.validated_data.get("invitees", None)
        invitees = garden_create_parse_invitees(invitees)

        garden, invitations_sent = garden_create(
            name=name, creator=request.user, invitees=invitees
        )

        data = {
            "id": garden.id,
            "hashid": garden.hashid,
            "name": garden.name,
            "invitations_sent": invitations_sent,
        }
        data = self.OutputSerializer(data).data

        return Response(data)


class GardenDetailView(APIView):
    authentication_classes = [SessionAuthentication]

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        hashid = serializers.CharField()
        name = serializers.CharField()
        visibility = serializers.ChoiceField(choices=Garden.VisibilityChoices.choices)
        members = serializers.ListField(child=serializers.DictField())

    def get(self, request, hashid):

        garden = garden_detail(fetched_by=request.user, hashid=hashid)
        members = garden_members(garden)

        data = {
            "id": garden.id,
            "hashid": garden.hashid,
            "name": garden.name,
            "visibility": garden.visibility,
            "members": members,
        }
        data = self.OutputSerializer(data).data

        return Response(data)


class GardenUpdateView(APIView):
    authentication_classes = [SessionAuthentication]

    class InputSerializer(serializers.Serializer):
        name = serializers.CharField(required=False)
        visibility = serializers.ChoiceField(
            choices=Garden.VisibilityChoices.choices, required=False
        )

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        hashid = serializers.CharField()
        name = serializers.CharField()
        visibility = serializers.ChoiceField(choices=Garden.VisibilityChoices.choices)

    def post(self, request, hashid):

        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        name = serializer.validated_data["name"] or None
        visibility = serializer.validated_data["visibility"] or None

        garden = garden_update(
            user=request.user, hashid=hashid, name=name, visibility=visibility
        )

        data = self.OutputSerializer(garden).data

        return Response(data)


class GardenMembershipCreateView(APIView):
    authentication_classes = [SessionAuthentication]

    class InputSerializer(serializers.Serializer):
        pass

    class OutputSerializer(serializers.Serializer):
        pass


class GardenMembershipAcceptView(APIView):
    authentication_classes = [SessionAuthentication]

    class InputSerializer(serializers.Serializer):
        pass


class GardenMembershipUpdateView(APIView):
    authentication_classes = [SessionAuthentication]

    class InputSerializer(serializers.Serializer):
        pass


class GardenMemberhipDeleteView(APIView):
    authentication_classes = [SessionAuthentication]

    class InputSerializer(serializers.Serializer):
        pass
