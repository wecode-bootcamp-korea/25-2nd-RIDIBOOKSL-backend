# Generated by Django 3.2.8 on 2021-10-20 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialPlatform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=None)),
                ('deleted_at', models.DateTimeField(default=None)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'social_platforms',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=None)),
                ('deleted_at', models.DateTimeField(default=None)),
                ('nickname', models.CharField(max_length=40)),
                ('profile_image', models.CharField(max_length=500, null=True)),
                ('email', models.CharField(max_length=40)),
                ('social_platform', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.socialplatform')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
