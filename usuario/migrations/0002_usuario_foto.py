# Generated by Django 5.2 on 2025-04-20 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='usuario/img'),
        ),
    ]
