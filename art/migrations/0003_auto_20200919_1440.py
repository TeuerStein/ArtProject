# Generated by Django 3.0.8 on 2020-09-19 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0002_auto_20200911_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Name'),
        ),
    ]
