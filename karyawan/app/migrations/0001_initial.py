# Generated by Django 4.0.6 on 2022-07-18 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Karyawan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('nip', models.CharField(max_length=200)),
                ('alamat', models.CharField(max_length=200, null=True)),
                ('divisi', models.CharField(max_length=200, null=True)),
                ('jeniskelamin', models.CharField(max_length=200)),
            ],
        ),
    ]