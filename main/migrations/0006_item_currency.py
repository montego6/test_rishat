# Generated by Django 4.1.7 on 2023-02-18 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_tax'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='currency',
            field=models.CharField(default='USD', max_length=200),
        ),
    ]
