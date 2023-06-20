from rest_framework import APIView

class BaseAPI(APIView):

    def get_serializer_class(self):
        