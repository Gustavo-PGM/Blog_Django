# Generated by Django 5.1 on 2024-08-10 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_postagem_imagens'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postagem',
            name='imagens',
            field=models.ImageField(blank=True, default=1, upload_to='imagens/'),
            preserve_default=False,
        ),
    ]