# Generated by Django 5.0.6 on 2024-05-30 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Qpelada', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='peladas_bd',
            old_name='preco',
            new_name='preço',
        ),
    ]
