# Generated by Django 3.1.1 on 2020-09-15 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200915_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filiado',
            name='ID_Filiado',
            field=models.IntegerField(verbose_name=5),
        ),
    ]
