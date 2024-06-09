from django.db import models
from datetime import datetime, time

# Database
class Destinations(models.Model):

    nama = models.CharField(max_length=20)
    kategori = models.CharField(max_length=20, default="")
    suka = models.PositiveIntegerField(default=0)
    image_file_name = models.CharField(max_length=50, default="")
    timeOpen= models.TimeField(default=datetime.strptime('06:00', '%H:%M').time())
    timeClose= models.TimeField(default=datetime.strptime('18:00', '%H:%M').time())
    location = models.CharField(max_length=100,default="")


class Fasility(models.Model):
    destination = models.ForeignKey(Destinations, on_delete=models.CASCADE)  # ForeignKey
    nama_fasilitas = models.CharField(max_length=20)
    logo_file_name = models.CharField(max_length=50, default="")

    def __str__(self) -> str:
        return self.nama_fasilitas
    

class Profile(models.Model):
    textInfografis = models.TextField()
    kodePos = models.CharField(max_length=20)
    Wilayah = models.CharField(max_length=20)
    Penduduk = models.CharField(max_length=20)
    Kepadatan = models.CharField(max_length=20)

