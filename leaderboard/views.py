from rest_framework.decorators import api_view #type: ignore
from rest_framework.response import Response #type: ignore
from players.models import Players
from players.serializer import PlayerSerializer  # Import the serializer

@api_view(['GET'])
def leaderboard_data(request):
    # Query all players from the Players table
    players = Players.objects.all()

    # Serialize the data using the PlayerSerializer
    serializer = PlayerSerializer(players, many=True)

    # Return the serialized data in the response
    return Response(serializer.data)
