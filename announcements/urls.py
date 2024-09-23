from django.urls import path

from . import views

urlpatterns = [
    path("", views.AnnouncementListView.as_view(), name='announcements'),
    path("<int:id>/", views.AnnouncementView.as_view(), name='announcement'),
    path("new/", views.CreateAnnouncement.as_view(), name='new announcement'),
    path("<int:id>/edit/", views.EditAnnouncement.as_view(), name='edit announcement')
]

