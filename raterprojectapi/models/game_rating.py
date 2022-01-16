from django.db import models

from raterprojectapi.models.game import Game
from raterprojectapi.models.gamer import Gamer

class Game_Rating(models.Model):
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name='ratings'
    )
    rater = models.ForeignKey(
        Gamer,
        on_delete=models.CASCADE,
        related_name='rater'
    )
    rating = models.IntegerField()
    
    # come back and make this a RatingField