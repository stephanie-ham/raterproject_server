from django.db import models

from raterprojectapi.models.gamer import Gamer
from raterprojectapi.models.category import Category

class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    designer = models.CharField(max_length=100)
    year_released = models.IntegerField()
    number_of_players = models.IntegerField()
    play_time = models.IntegerField()
    age_range_start = models.IntegerField()
    age_range_end = models.IntegerField()
    gamer = models.ForeignKey(
        Gamer,
        on_delete=models.CASCADE,
        related_name='games'
    )
    categories = models.ManyToManyField(Category)