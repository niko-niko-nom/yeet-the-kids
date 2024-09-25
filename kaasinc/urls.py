from django.urls import path
from . import views

urlpatterns = [
    path("", views.kaas, name="kaas"),
    path("vote/", views.stem_van_de_week, name="kaas-vote"),
]
