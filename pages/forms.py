from django.forms import ModelForm
from .models import Volunteer, RSVP, Event, EmailSignup


class VolunteerSignUpForm(ModelForm):
    class Meta:
        model = Volunteer
        exclude = ['contacted', 'notes']


class RSVPForm(ModelForm):
    class Meta:
        model = RSVP
        exclude = ['contacted', 'notes']


class EmailForm(ModelForm):
    class Meta:
        model = EmailSignup
        exclude = []
