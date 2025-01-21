from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def question_data(request):
    question_details = {
        1:'35+65',
        2: '26+98',
    }
    return Response(question_details)