# Generated by Django 4.0.4 on 2022-06-30 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tg_id',
            field=models.PositiveIntegerField(null=True),
        ),
    ]