# Generated by Django 5.1 on 2024-08-10 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_data_categoria_criada_em_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='atualizacao',
            new_name='atualizada_em',
        ),
        migrations.RenameField(
            model_name='postagem',
            old_name='atualizacao',
            new_name='atualizada_em',
        ),
    ]