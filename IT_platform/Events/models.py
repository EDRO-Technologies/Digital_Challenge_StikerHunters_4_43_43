from django.db import models
from django.db.migrations import CreateModel
from django.db.models import Model, CASCADE


class Organizer(models.Model):
    title = models.CharField(max_length=80, primary_key=True)
    contact = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="image/organizator", null = True)

    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey("Category",max_length=50, on_delete=models.SET_NULL, null=True)
    special = models.CharField(max_length=100)
    place = models.TextField()
    description = models.TextField()
    date = models.DateField(blank=True, null=True)
    organizer = models.CharField(max_length=50)
    partners = models.ForeignKey(Organizer, max_length=150, null=True, on_delete=models.PROTECT, blank=True)
    image = models.ImageField(upload_to='image/avatar/', null=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name