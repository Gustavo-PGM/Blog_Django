# Generated by Django 5.1 on 2024-08-10 18:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_postagem_imagens'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('comentario', models.TextField()),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('postagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.postagem')),
            ],
        ),
    ]
