# Generated by Django 5.2 on 2025-04-21 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_alter_usuario_foto_alter_usuario_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='CPF',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
