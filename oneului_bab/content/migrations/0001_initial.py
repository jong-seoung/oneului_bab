# Generated by Django 4.1.6 on 2023-04-05 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='이름')),
                ('image', models.TextField(default='food_basic_img')),
                ('main', models.CharField(choices=[('noodle', '면'), ('rice', '밥'), ('bread', '빵')], max_length=10, verbose_name='메인분류')),
                ('soup', models.CharField(choices=[('yes', '국물 있음'), ('little', '국물 쪼금'), ('no', '국물 없음')], max_length=10, verbose_name='국물')),
                ('Spicy', models.CharField(choices=[('spicy', '매움'), ('normal', '보통'), ('mild', '순함')], max_length=10, verbose_name='맵기')),
                ('temperature', models.CharField(choices=[('cool', '차갑게'), ('warm', '적당히 따뜻하게'), ('hot', '뜨거울 정도로')], max_length=10, verbose_name='온도')),
                ('weight', models.CharField(choices=[('heavy', '무거움'), ('light', '가벼움')], max_length=10, verbose_name='무게')),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='', max_length=254)),
                ('nickname', models.CharField(default='', max_length=30, verbose_name='nickname')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('answer', models.TextField(default='아직 답변이 없습니다. 빠른 시일내에 답변해 드리겠습니다.')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Save',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_id', models.IntegerField(default=0)),
                ('email', models.EmailField(default='', max_length=254)),
                ('is_save', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Save_memo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='', max_length=254)),
                ('memo', models.CharField(default='', max_length=255)),
                ('food_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memo_set', to='content.foodlist')),
            ],
        ),
    ]
