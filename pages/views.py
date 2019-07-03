from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, CreateView
from .models import Event
from .forms import VolunteerSignUpForm, RSVPForm
from datetime import datetime


def index(request):
    return render(request, "pages/index.html")


def about(request):
    return render(request, "pages/about.html")


class Area5(TemplateView):
    template_name = "pages/area-5.html"

    def get_context_data(self, **kwargs):
        context = super(Area5, self).get_context_data(**kwargs)
        events = Event.objects.all()
        context['upcoming_events'] = events.filter(date_end__gt=datetime.now())
        context['past_events'] = events.filter(date_end__lt=datetime.now())
        return context


def news_room(request):
    return render(request, "pages/news-room.html")


class SupportPam(CreateView):
    template_name = "pages/support-pam.html"
    form_class = VolunteerSignUpForm
    success_url = "/support-pam/thanks/"


def support_thanks_view(request):
    return render(request, "pages/support_thanks.html")


def contribute(request):
    return render(request, "pages/contribute.html")


class RSVPView(CreateView):
    template_name = "pages/rsvp.html"
    form_class = RSVPForm
    success_url = "/rsvp/thanks/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event'] = Event.objects.get(pk=self.kwargs['pk'])
        return context


def rsvp_thanks_view(request):
    return render(request, "pages/rsvp_thanks.html")