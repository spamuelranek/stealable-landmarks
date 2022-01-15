from random import choices
from django.db import models
from django.contrib.auth import get_user_model

class Landmark(models.Model):
  class Stealability(models.TextChoices):
    zero = 'zero', ('American President Nuclear Football')
    one = 'one', ('Face off of Mt. Rushmore')
    two = 'two', ('Part of the Daytona Track During a Race')
    three = 'three', ('The Top of the "Effifel" tower in Las Vegas')
    four = 'four', ('Items from Walmart')
    five = 'five', ('Views of the Grand Canyon')

  class EvilCorp(models.TextChoices):
    aim = 'aim',('Advanced Idea Mechanics AIM')
    cobra = 'cobra', ('Criminal Organization of Bloodiness, Revenge and Assassination COBRA')
    hydra = 'HYDRA', ('HYDRA')
    skool = 'skool', ('Secert Knowledge of Organized Lawbreakers SKOOL')
    vile = 'vile', ('The Villians International League of Evil VILE')



  title = models.CharField(max_length=64)
  poster = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  rating_of_stealablity = models.CharField(max_length = 5, choices=Stealability.choices,default= Stealability.five)
  member_of_which_evil_organization = models.CharField(max_length=5, choices=EvilCorp.choices )
  location = models.CharField(max_length=128) 