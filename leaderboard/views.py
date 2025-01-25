from rest_framework.decorators import api_view # type: ignore
from rest_framework.response import Response   # type: ignore
from players.models import Players
from players.serializer import PlayerSerializer

@api_view(['GET'])
def leaderboard_data(request):
    # Query all players from the Players table and order them by points (descending) and time (ascending)
    players = Players.objects.all().order_by('-point', 'time')

    # Serialize the data using the PlayerSerializer
    serializer = PlayerSerializer(players, many=True)

    # Return the serialized data in the response
    return Response(serializer.data)
