from django.db import models
from .rater import Rater
from .game import Game


class Review(models.Model):

    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    rater = models.ForeignKey("Rater", on_delete=models.CASCADE)
    content = models.CharField(max_length=255)