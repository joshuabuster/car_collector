from django.forms import ModelForm
from .models import ServicesCompleted

class ServicesForm(ModelForm):
  class Meta:
    model = ServicesCompleted
    fields = ['date', 'service']