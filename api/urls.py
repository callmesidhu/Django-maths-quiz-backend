from django.urls import path # type: ignore
from leaderboard.views import leaderboard_data
from questions.views import question_data

urlpatterns = [
    path("leaderboard/", leaderboard_data),
    path("questions/", question_data)
]
