# Generated by Django 3.2.7 on 2021-10-03 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_book_publish_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='num_of_pages',
            field=models.IntegerField(null=True),
        ),
    ]
