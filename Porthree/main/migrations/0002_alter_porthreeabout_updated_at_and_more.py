# Generated by Django 4.2.7 on 2023-11-21 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='porthreeabout',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='porthreefaq',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
