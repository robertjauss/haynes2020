from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Event, NewsArticle, CarouselImage, Speech
from .forms import VolunteerSignUpForm, RSVPForm
from datetime import datetime
from django.utils.timezone import now


class Index(TemplateView):
    template_name = "pages/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['article'] = NewsArticle.objects.order_by('-publish_date')[0]
        except IndexError:
            context['article'] = None
        try:
            context['event'] = Event.objects.order_by('date_start').filter(date_start__gte=now())[0]
        except IndexError:
            context['event'] = None
        return context


def about(request):
    return render(request, "pages/about.html")


class About(TemplateView):
    template_name = "pages/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        carousel_images = CarouselImage.objects.filter(active=True)
        context['carousel_images'] = carousel_images
        return context


def area5(request):
    return render(request, "pages/area-5.html")


class Events(TemplateView):
    template_name = "pages/events.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        events = Event.objects.order_by('-date_start')
        context['upcoming_events'] = events.filter(date_end__gt=datetime.now())
        context['past_events'] = events.filter(date_end__lt=datetime.now())
        return context


class Articles(ListView):
    model = NewsArticle
    template_name = "pages/news-room.html"
    ordering = ['-publish_date']


class ArticleDetail(DetailView):
    model = NewsArticle
    template_name = "pages/news-article.html"


class Speeches(ListView):
    model = Speech
    template_name = "pages/speeches.html"
    ordering = ['-publish_date']


class SpeechDetail(DetailView):
    model = Speech
    template_name = "pages/speech-detail.html"


class PhotoAlbum(TemplateView):
    template_name = "pages/photo-album.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photos'] = CarouselImage.objects.all()
        return context


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
