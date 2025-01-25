from django.urls import path # type: ignore
from leaderboard.views import leaderboard_data
from result.views import updated_result
from players.views import save_player

urlpatterns = [
    path("leaderboard/", leaderboard_data),
    path("result/", updated_result),
    path("players/", save_player),
]
