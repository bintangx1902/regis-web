# Generated by Django 4.2.10 on 2024-08-24 17:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_alter_scorelist_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationPhase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nama Gelombang : ')),
                ('open_on', models.DateTimeField(verbose_name='Tanggal Buka Gelombang : ')),
                ('closed_on', models.DateTimeField(verbose_name='Tanggal Penutupan Gelombang : ')),
            ],
        ),
        migrations.AlterField(
            model_name='scorelist',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='score', related_query_name='score', to=settings.AUTH_USER_MODEL),
        ),
    ]
