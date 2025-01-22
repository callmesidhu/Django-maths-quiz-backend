from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def check_player(request):
    question_details = {
        1:'Sidharth'
    }
    return Response(question_details)