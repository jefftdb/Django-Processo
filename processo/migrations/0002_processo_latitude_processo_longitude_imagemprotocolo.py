# Generated by Django 5.2 on 2025-04-21 20:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='processo',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='processo',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='ImagemProtocolo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='processo/img/')),
                ('processo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagens', to='processo.processo')),
            ],
        ),
    ]
