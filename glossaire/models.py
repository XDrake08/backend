from asyncio.windows_events import NULL
from django.db import models

# Create your models here.


class Glossary(models.Model):
  id = models.AutoField(primary_key=True)
  French = models.CharField(max_length=100)
  English = models.CharField(max_length=100)
  Arabic = models.CharField(max_length=100)
  ArabicDesc = models.CharField(max_length=1000,default=' ')
  FrenchDesc = models.CharField(max_length=1000,default=' ')
  EnglishDesc = models.CharField(max_length=1000,default=' ')

  def __str__(self):
        return self.name