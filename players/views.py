# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Player
from .serializer import PlayerSerializer

@api_view(['POST'])
def save_player(request):
    if request.method == 'POST':
        # Log the input data from the frontend
        print("Input data from frontend:", request.data)
        
        # Create Player objects and serialize them
        objPlayers = Player.objects.all()
        serializer = PlayerSerializer(objPlayers, many=True)
        
        # Return the serialized data as a response
        return Response(serializer.data, status=status.HTTP_200_OK)
