# Generated by Django 4.2.10 on 2024-08-29 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_userdata_unique_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationphase',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=20, null=True),
        ),
    ]
