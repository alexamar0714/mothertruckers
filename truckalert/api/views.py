from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from api.serializers import PositionSerializer
from api.models import Position



class UpdatePosition(APIView):
    
    def get_pos_object(self, uid):
        try:
            return Position.objects.get(user_id=uid)
        except:
            return False
    
    
    def app_key_valid(self, key):
        #implement application key validation
        return True

    def post(self, request, format=None):

        app_key = request.data['app_key']

        if not self.app_key_valid(app_key): #check validity of the application key
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

        uid = request.data['data']['user_id']
        pos_object = self.get_pos_object(uid)
        serializer = PositionSerializer(data=request.data['data'])

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if pos_object: #if the user is already registered
            serializer2 = PositionSerializer(pos_object, data=request.data['data'])
            if not serializer2.is_valid():
                return Response(seiralizer2.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            serializer2.save()
            
        else:
            serializer.save()
       
        #create JSON of coordinates of incidents
        #return Response
        return Response("SUCCESS")

    
    def get(self, request, format=None):
        return Response("TEST SUCCESSFUL")
