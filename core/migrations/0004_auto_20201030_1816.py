# Generated by Django 3.1.1 on 2020-10-30 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20201024_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='RegistroCBJ',
            field=models.AutoField(editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]