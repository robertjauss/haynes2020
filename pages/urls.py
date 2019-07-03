from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("area-5/", Area5.as_view(), name="area-5"),
    path("news-room/", news_room, name="news-room"),
    path("support-pam/", SupportPam.as_view(), name="support-pam"),
    path("support-pam/thanks/", support_thanks_view, name="support-thanks"),
    path("contribute/", contribute, name="contribute"),
    path("rsvp/<int:pk>", RSVPView.as_view(), name="rsvp"),
    path("rsvp/thanks/", rsvp_thanks_view, name="rsvp-thanks")
]
