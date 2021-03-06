# Generated by Django 3.2.8 on 2021-10-20 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=None)),
                ('deleted_at', models.DateTimeField(default=None)),
                ('name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=20, null=True)),
                ('birthdate', models.DateField(null=True)),
            ],
            options={
                'db_table': 'authors',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=None)),
                ('deleted_at', models.DateTimeField(default=None)),
                ('main_name', models.CharField(max_length=100)),
                ('sub_name', models.CharField(max_length=100, null=True)),
                ('translator', models.CharField(max_length=20, null=True)),
                ('price', models.IntegerField()),
                ('trailer', models.CharField(max_length=600, null=True)),
                ('rent_discount', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('sale_discount', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
            ],
            options={
                'db_table': 'books',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=None)),
                ('deleted_at', models.DateTimeField(default=None)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'menus',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=None)),
                ('deleted_at', models.DateTimeField(default=None)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'publishers',
            },
        ),
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=None)),
                ('deleted_at', models.DateTimeField(default=None)),
                ('image_url', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'thumbnails',
            },
        ),
        migrations.CreateModel(
            name='ViewCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=None)),
                ('deleted_at', models.DateTimeField(default=None)),
                ('hit', models.IntegerField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.book')),
            ],
            options={
                'db_table': 'hits',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=None)),
                ('deleted_at', models.DateTimeField(default=None)),
                ('rating', models.IntegerField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'ratings',
            },
        ),
        migrations.CreateModel(
            name='Preview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=None)),
                ('deleted_at', models.DateTimeField(default=None)),
                ('image', models.CharField(max_length=500)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.book')),
            ],
            options={
                'db_table': 'previews',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=None)),
                ('deleted_at', models.DateTimeField(default=None)),
                ('name', models.CharField(max_length=20)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.menu')),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='BookAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=None)),
                ('deleted_at', models.DateTimeField(default=None)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.author')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.book')),
            ],
            options={
                'db_table': 'books_authors',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(related_name='book_author', through='products.BookAuthor', to='products.Author'),
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category'),
        ),
        migrations.AddField(
            model_name='book',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.menu'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.publisher'),
        ),
        migrations.AddField(
            model_name='book',
            name='thumbnail',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.thumbnail'),
        ),
    ]
