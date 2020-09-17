from django.db import models
from django.urls import reverse
from datetime import date

SERVICES =   (
    ('O', 'Oil Service'),
    ('T', 'Tire Service'),
    ('X', 'Other Service')
)

class Show(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('show_detail', kwargs={'pk': self.id})

# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    shows = models.ManyToManyField(Show)

    def __str__(self):
        return self.model

    # Add this method to redirect to cat that was just created
    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})

class ServicesCompleted(models.Model):
    date = models.DateField('Service Date')
    service = models.CharField(max_length=1, choices=SERVICES, default=SERVICES[2][0])

    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_service_display()} on {self.date}" 

    class Meta:
        ordering = ['-date']   