# Generated by Django 5.1 on 2024-08-10 12:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_categoria_postagem_subtitulo_postagem_usuario_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='postagem',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.categoria'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='postagem',
            name='imagens',
            field=models.ImageField(blank=True, default=1, upload_to='imagens/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='postagem',
            name='subtitulo',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='postagem',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]