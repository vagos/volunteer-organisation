from django.urls import path

from . import views

app_name = "volunteer"

urlpatterns = [
    path('', views.index, name = "index"),

    path("join", views.join, name="join"),

    path("join", views.join, name="join"),
    path("profile/<int:volunteer_id>/", views.profile, name="profile"),
    path("team/<str:team_name>/", views.team, name="team"),
    path("team_join/<str:team_name>/", views.team_join, name="team_join"),
    path("team_leave/<str:team_name>/", views.team_leave, name="team_leave"),

    path("task/<int:task_id>/", views.task, name="task"),
    path("task_done/<int:task_id>", views.task_done, name="task_done"),
]
