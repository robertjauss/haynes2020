from django.urls import path
from .views import *

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("about/", About.as_view(), name="about"),
    path("area-5/", area5, name="area-5"),
    path("events/", Events.as_view(), name="events"),
    path("articles/", Articles.as_view(), name="articles"),
    path("articles/<slug:slug>/", ArticleDetail.as_view(), name="article-detail"),
    path("speeches/", Speeches.as_view(), name="speeches"),
    path("speeches/<slug:slug>/", SpeechDetail.as_view(), name="speech-detail"),
    path("photo-album", PhotoAlbum.as_view(), name="photo-album"),
    path("support-pam/", SupportPam.as_view(), name="support-pam"),
    path("support-pam/thanks/", support_thanks_view, name="support-thanks"),
    path("contribute/", contribute, name="contribute"),
    path("rsvp/<int:pk>", RSVPView.as_view(), name="rsvp"),
    path("rsvp/thanks/", rsvp_thanks_view, name="rsvp-thanks"),
    path("emailsignup/", email_signup, name="email_signup")
]
