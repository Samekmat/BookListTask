# Generated by Django 3.2.7 on 2021-10-01 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=120)),
                ('publish_date', models.DateField()),
                ('ISBN', models.CharField(max_length=13)),
                ('num_of_pages', models.IntegerField()),
                ('cover_link', models.URLField()),
                ('publish_lang', models.CharField(max_length=100)),
            ],
        ),
    ]