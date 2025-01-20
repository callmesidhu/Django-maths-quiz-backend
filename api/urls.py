from django.urls import path # type: ignore
from leaderboard.views import leaderboard_data

urlpatterns = [
    path("leaderboard/", leaderboard_data),
]
