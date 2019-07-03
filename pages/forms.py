from django.forms import ModelForm
from .models import Volunteer, RSVP, Event


class VolunteerSignUpForm(ModelForm):
    class Meta:
        model = Volunteer
        exclude = ['contacted', 'notes']


class RSVPForm(ModelForm):
    class Meta:
        model = RSVP
        exclude = ['contacted', 'notes']
