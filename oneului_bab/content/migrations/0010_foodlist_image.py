# Generated by Django 4.1.6 on 2023-03-14 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_question_answer_delete_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodlist',
            name='image',
            field=models.TextField(default='food_basic_img'),
        ),
    ]
