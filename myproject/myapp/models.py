from django.db import models

# Create your models here.
class pictures(models.Model):
    pic=models.FileField(upload_to='images/',default='set.jpg')

class videos(models.Model):
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

class Song(models.Model):
    songname= models.CharField(max_length=500)
    audiofile=models.FileField(upload_to='musics/')

