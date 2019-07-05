from django.db import models
from django.utils.timezone import now


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    address_1 = models.CharField(max_length=100, null=True, blank=True)
    address_2 = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    zip = models.CharField(max_length=5, null=True, blank=True)
    image = models.ImageField(upload_to="events", null=True, blank=True)
    date_start = models.DateTimeField(null=True, blank=True)
    date_end = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class RSVP(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    contacted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.last_name}, {self.first_name} - {self.event}"


class Volunteer(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=5)
    mobile = models.CharField(max_length=10, blank=True, null=True)
    host_attend_events = models.BooleanField(default=False)
    knock_on_doors = models.BooleanField(default=False)
    make_calls = models.BooleanField(default=False)
    send_texts = models.BooleanField(default=False)
    donate_skills = models.BooleanField(default=False)
    pledge_to_donate = models.BooleanField(default=False)
    contacted = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    article = models.TextField()
    image = models.ImageField(upload_to="news", blank=True, null=True)
    publish_date = models.DateField(default=now)
    slug = models.SlugField()


class CarouselImage(models.Model):
    image = models.ImageField(upload_to="carousel")
    active = models.BooleanField(default=True)
