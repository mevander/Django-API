# Generated by Django 3.2.4 on 2021-06-04 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0002_imovel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imobiliaria',
            options={'ordering': ['nome']},
        ),
        migrations.AlterModelOptions(
            name='imovel',
            options={'ordering': ['nome']},
        ),
    ]