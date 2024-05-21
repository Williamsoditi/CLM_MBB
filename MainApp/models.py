from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class League(models.Model):
    title = models.CharField(max_length=200)
    league_logo = CloudinaryField("League Logo" ,null=True, blank=True)

    class Meta:
        verbose_name_plural="League"

    def __str__(self):
        return self.title

class Player(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveSmallIntegerField()
    height = models.DecimalField(decimal_places=2, max_digits=6)
    nationality = models.CharField(max_length=50)
    position = models.CharField(max_length=200)
    player_image = CloudinaryField("Player Image", null=True, blank=True)  
    league_in = models.ForeignKey(League, on_delete=models.CASCADE, null=True)         

    class Meta:
        verbose_name_plural="Athlete_bio"


    def __str__(self):
        return self.name
    

class Schedule(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE, null=True)  
    venue = models.CharField(max_length=255)
    date = models.DateTimeField()  
    home_team = models.CharField(max_length=255)
    away_team = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural='Schedule'

    def __str__(self):
        return f'  {self.league} => {self.home_team} vs {self.away_team} at {self.venue} {self.date}'
    