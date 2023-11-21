from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:character_id>/", views.detail, name="detail"),
    path("<int:character_id>/results/", views.results, name = "results"),
    path("<int:character_id>/vote/", views.vote, name="Vote"),
    path("q/<int:question_id/", views.survey, name="Question")
]