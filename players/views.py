from rest_framework.decorators import api_view  # type: ignore
from rest_framework.response import Response  # type: ignore
from rest_framework import status  # type: ignore
from .models import Players
from .serializer import PlayerSerializer

@api_view(['POST'])
def save_player(request):
    if request.method == 'POST':
        # Log the input data from the frontend
        print("Input data from frontend:", request.data)

        # Extract data to check for duplicates (replace 'name' with the unique field in your model)
        player_data = request.data
        unique_field_value = player_data.get('name')  # Ensure 'name' exists in the data

        # Check if a player with this unique field already exists
        if Players.objects.filter(name=unique_field_value).exists():
            return Response(
                {"message": "Player already exists, no new data added."},
                status=status.HTTP_200_OK
            )

        # Deserialize the data
        serializer = PlayerSerializer(data=player_data)
        if serializer.is_valid():
            # Save the data to the database
            serializer.save()
            return Response(
                {"message": "Player saved successfully!"},
                status=status.HTTP_201_CREATED
            )
        else:
            # Return validation errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
