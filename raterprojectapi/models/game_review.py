from django.db import models

from raterprojectapi.models.game import Game
from raterprojectapi.models.gamer import Gamer

class Game_Review(models.Model):
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    reviewer= models.ForeignKey(
        Gamer,
        on_delete=models.CASCADE,
        related_name='reviewer'
    )
    review = models.CharField(max_length=300)