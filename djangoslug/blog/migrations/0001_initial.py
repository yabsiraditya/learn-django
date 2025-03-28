# Generated by Django 5.1.1 on 2024-10-04 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artikel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=255)),
                ('isi', models.TextField()),
                ('kategori', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('pubdate', models.TimeField(auto_now=True)),
                ('update', models.TimeField(auto_now=True)),
            ],
        ),
    ]
