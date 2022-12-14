# Generated by Django 4.0.6 on 2022-07-20 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AudioFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('image', models.ImageField(upload_to='audio/')),
                ('song_file', models.FileField(upload_to=' songs/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('email', models.CharField(max_length=200)),
                ('phone_number', models.BigIntegerField(default=9989)),
                ('theme', models.CharField(max_length=500)),
                ('message', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('full_name', models.CharField(max_length=500)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('job_title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='team/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('img', models.ImageField(upload_to='post/')),
                ('caption', models.CharField(max_length=250)),
                ('text', models.TextField()),
                ('views', models.BigIntegerField(default=0)),
                ('is_main', models.BooleanField(default=False)),
                ('is_editor_choice', models.BooleanField(default=False)),
                ('is_trend', models.BooleanField(default=False)),
                ('is_interview', models.BooleanField(default=False)),
                ('is_investigation', models.BooleanField(default=False)),
                ('is_article', models.BooleanField(default=False)),
                ('is_business', models.BooleanField(default=False)),
                ('is_videonews', models.BooleanField(default=False)),
                ('is_photonews', models.BooleanField(default=False)),
                ('is_adviced', models.BooleanField(default=False)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='post.category')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='post.region')),
                ('tags', models.ManyToManyField(blank=True, to='post.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
