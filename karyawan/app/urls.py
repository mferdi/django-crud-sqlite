from django.urls import path
from . import views

urlpatterns = [
    path('', views.KaryawanList.as_view(), name='karyawan_list'),
    path('view/<int:pk>', views.KaryawanDetail.as_view(), name='karyawan_detail'),
    path('new', views.KaryawanCreate.as_view(), name='karyawan_new'),
    path('edit/<int:pk>', views.KaryawanUpdate.as_view(), name='karyawan_edit'),
    path('delete/<int:pk>', views.KaryawanDelete.as_view(), name='karyawan_delete'),
]