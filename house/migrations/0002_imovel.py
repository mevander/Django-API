# Generated by Django 3.2.4 on 2021-06-04 18:56

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('endereco', models.CharField(max_length=255)),
                ('descricao', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[(0, 'Ativo'), (1, 'Inativo')], max_length=1)),
                ('caracteristicas', models.CharField(max_length=255)),
                ('tipo', models.CharField(choices=[(0, 'Apartamento'), (1, 'Casa')], max_length=1)),
                ('finalidade', models.CharField(choices=[(0, 'Residencial'), (1, 'Comercial')], max_length=1)),
                ('imobiliaria', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='house.imobiliaria')),
            ],
        ),
    ]
