# Generated by Django 4.1.2 on 2022-11-01 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='caption',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
