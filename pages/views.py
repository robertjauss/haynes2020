from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Event, NewsArticle
from .forms import VolunteerSignUpForm, RSVPForm
from datetime import datetime
from django.utils.timezone import now


def index(request):
    return render(request, "pages/index.html")


class Index(TemplateView):
    template_name = "pages/index.html"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['article'] = NewsArticle.objects.order_by('-publish_date')[0]
        context['event'] = Event.objects.order_by('date_start').filter(date_start__gte=now())[0]
        return context


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


class NewsRoom(ListView):
    model = NewsArticle
    template_name = "pages/news-room.html"
    ordering = ['-publish_date']


class ArticleDetail(DetailView):
    model = NewsArticle
    template_name = "pages/news-article.html"


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
