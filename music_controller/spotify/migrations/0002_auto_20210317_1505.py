# Generated by Django 3.1.7 on 2021-03-17 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spotifytoken',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
