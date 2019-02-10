from rest_framework.views import APIView
from rest_framework.response import Response



class UpdatePosition(APIView):
    
    def get_pos_object(uid):
        try:
            return Position.objects.get(user_id=uid)
        except:
            return False
    
    
    def app_key_valid(key):
        #implement application key validation
        return True

    def post(self, request, format=None):

        app_key = request.data['app_key']

        if !app_key_valid(app_key): #check validity of the application key
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

        uid = request.data['data']['user_id']
        pos_object = get_pos_object(uid)
        serializer = PositionSerializer(request.data['data'])

        if !serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if pos_object: #if the user is already registered
            serializer.save(pos_object)
            
        else:
            serializer.save()
       
        #create JSON of coordinates of incidents
        #return Response
        return Response("SUCCESS")


