from django.db import models
from .rater import Rater
from .game import Game


class Rating(models.Model):

    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    rater = models.ForeignKey("Rater", on_delete=models.CASCADE)
    rating = models.IntegerField()