# Generated by Django 3.2.4 on 2021-06-09 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hamburgame', '0002_auto_20210609_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='Nombre'),
        ),
    ]