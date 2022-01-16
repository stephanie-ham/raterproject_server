from django.db import models

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
    rating = models.IntegerField(
        min_value=0,
        max_value=5
    )