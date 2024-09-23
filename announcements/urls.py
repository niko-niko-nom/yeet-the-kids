from django.urls import path

from . import views

urlpatterns = [
    path("", views.AnnouncementListView.as_view(), name='announcements'),
    path("<str:id>/", views.AnnouncementView.as_view(), name='announcement',),
]


