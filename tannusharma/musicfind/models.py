from django.db import models

class Music(models.Model):
    song=models.CharField()
    artist=models.CharField()
    album=models.CharField()
    year=models.IntegerField()
    def __str__(self):
        return self.song