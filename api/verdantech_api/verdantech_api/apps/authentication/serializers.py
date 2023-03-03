from dj_rest_auth.serializers import LoginSerializer as RestAuthLoginSerializer
from rest_framework import serializers


class CSRFTokenSerializer(serializers.Serializer):
    csrftoken = serializers.CharField()


# Overriding default dj-rest-auth behavior, in order
# to not consider username and require email
class LoginSerializer(RestAuthLoginSerializer):

    username = None
    email = serializers.EmailField(required=True)
