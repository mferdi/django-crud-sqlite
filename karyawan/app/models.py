from django.db import models
from django.urls import reverse

# Create your models here.
class Karyawan(models.Model):
    name = models.CharField(max_length=200, null=False)
    nip = models.CharField(max_length=200, null=False)
    alamat = models.CharField(max_length=200, null=True)
    divisi = models.CharField(max_length=200, null=True)
    jeniskelamin = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.name
    
    # The absolute path to get the url then reverse into 'karyawan_edit' with keyword arguments (kwargs) primary key
    def get_absolute_url(self):
        return reverse('karyawan_edit', kwargs={'pk': self.pk})