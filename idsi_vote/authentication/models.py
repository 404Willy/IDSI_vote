from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    NOM = 'Nom'
    PRENOMS = 'Prénoms'
    MATRICULE = 'Matricule'
    EMAIL = 'Email'
   
