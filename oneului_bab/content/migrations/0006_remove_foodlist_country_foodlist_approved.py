# Generated by Django 4.1.6 on 2023-02-22 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_remove_foodlist_chocie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodlist',
            name='country',
        ),
        migrations.AddField(
            model_name='foodlist',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
