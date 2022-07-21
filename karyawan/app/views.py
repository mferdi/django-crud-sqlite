from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Karyawan

# Create your views here.

class KaryawanList(ListView):
    model = Karyawan

class KaryawanDetail(DetailView):
    model = Karyawan

class KaryawanCreate(CreateView):
    model = Karyawan
    # Field must be same as the model attribute
    fields = ['name', 'nip', 'alamat', 'divisi', 'jeniskelamin']
    success_url = reverse_lazy('karyawan_list')

class KaryawanUpdate(UpdateView):
    model = Karyawan
    # Field must be same as the model attribute
    fields = ['name', 'nip', 'alamat', 'divisi', 'jeniskelamin']
    success_url = reverse_lazy('karyawan_list')

class KaryawanDelete(DeleteView):
    model = Karyawan
    success_url = reverse_lazy('karyawan_list')