from django.urls import path
from .views import *

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("about/", about, name="about"),
    path("area-5/", Area5.as_view(), name="area-5"),
    path("news-room/", NewsRoom.as_view(), name="news-room"),
    path("news-room/<slug:slug>", ArticleDetail.as_view(), name="article-detail"),
    path("support-pam/", SupportPam.as_view(), name="support-pam"),
    path("support-pam/thanks/", support_thanks_view, name="support-thanks"),
    path("contribute/", contribute, name="contribute"),
    path("rsvp/<int:pk>", RSVPView.as_view(), name="rsvp"),
    path("rsvp/thanks/", rsvp_thanks_view, name="rsvp-thanks")
]
