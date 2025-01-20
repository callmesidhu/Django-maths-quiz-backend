from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def leaderboard_data(request):
    leaderboard_details = {
        'name':'Sidharth',
        'mark':13,
        'time':35.2315,
        'rank':4,
    }
    return Response(leaderboard_details)