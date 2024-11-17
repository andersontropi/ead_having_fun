# Generated by Django 5.1.3 on 2024-11-16 21:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aula', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gravacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('video', models.URLField()),
                ('aula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gravacoes', to='aula.aula')),
            ],
        ),
        migrations.DeleteModel(
            name='Episodio',
        ),
    ]
