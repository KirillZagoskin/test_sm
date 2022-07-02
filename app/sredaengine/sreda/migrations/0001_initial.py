# Generated by Django 4.0.4 on 2022-06-30 20:33

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(db_index=True)),
            ],
            options={
                'verbose_name_plural': '3. Ответы',
            },
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
                ('pic', models.ImageField(max_length=300, upload_to='images/')),
            ],
            options={
                'verbose_name_plural': '5. Сообщества',
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('on_main', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_image', models.ImageField(blank=True, max_length=300, null=True, upload_to='images/')),
                ('title', models.CharField(max_length=250)),
                ('subtitle', models.CharField(max_length=250)),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('body', ckeditor.fields.RichTextField(blank=True, db_index=True)),
                ('slug', models.SlugField(blank=True, max_length=250, unique=True)),
                ('on_main', models.BooleanField(default=False)),
                ('rating', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': '1. Посты',
                'ordering': ['-rating'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('profile_pic', models.ImageField(max_length=300, upload_to='images/')),
            ],
            options={
                'verbose_name_plural': '7. Профиль',
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_image', models.ImageField(blank=True, max_length=300, null=True, upload_to='images/')),
                ('title', models.CharField(max_length=140)),
            ],
            options={
                'verbose_name_plural': '2. Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name_plural': '4. Рубрики',
            },
        ),
        migrations.CreateModel(
            name='TypeContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': '6. Тип контента',
            },
        ),
    ]