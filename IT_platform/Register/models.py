from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE
from Events.models import Event, Category


class Profile(models.Model):
    username = models.OneToOneField(User, max_length=100, primary_key=True, on_delete=CASCADE)
    name = models.CharField(max_length=80)
    second_name = models.CharField(max_length=80)
    surname = models.CharField(max_length=80)
    birth = models.DateField(auto_now_add=True)
    is_organizer = models.BooleanField(default=False, help_text="Я организатор")
    category = models.ForeignKey(Category, max_length=100, on_delete=models.SET_NULL, null=True)
    special = models.CharField(max_length=100)
    github = models.URLField()
    portfolio = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='image/event/', null=True)

    def __str__(self):
        return self.username

