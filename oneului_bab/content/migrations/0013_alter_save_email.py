# Generated by Django 4.1.6 on 2023-03-29 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0012_save_question_email_question_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='save',
            name='email',
            field=models.EmailField(default='', max_length=254, unique=True, verbose_name='email address'),
        ),
    ]