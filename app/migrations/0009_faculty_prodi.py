# Generated by Django 4.2.15 on 2024-09-03 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_registrationphase_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nama Fakultas ')),
            ],
        ),
        migrations.CreateModel(
            name='Prodi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nama Prodi ')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.faculty', verbose_name='Fakultas ')),
            ],
        ),
    ]
