# Generated by Django 4.2.5 on 2023-09-28 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adiblar', '0002_bookscategorymodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='booksmodel',
            name='description',
            field=models.TextField(default=' '),
        ),
    ]
