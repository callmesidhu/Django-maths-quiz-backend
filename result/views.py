from rest_framework.decorators import api_view  # type: ignore
from rest_framework.response import Response    # type: ignore
from rest_framework import status # type: ignore
from players.models import Players

@api_view(['POST'])
def updated_result(request):
    if request.method == 'POST':
        # Extract the data
        player_name = request.data.get('name')  # Assuming 'name' is used as a unique identifier
        time = request.data.get('time')
        point = request.data.get('point')

        try:
            # Fetch the player using the unique 'name'
            player = Players.objects.get(name=player_name)

            # Update the fields
            player.time = time
            player.point = point

            # Save the updated player
            player.save()

            return Response(
                {"message": "Player result updated successfully!"},
                status=status.HTTP_200_OK
            )

        except Players.DoesNotExist:
            return Response(
                {"message": "Player not found!"},
                status=status.HTTP_404_NOT_FOUND
            )
