# Generated by Django 5.1 on 2024-08-18 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reynolds_cookbook', '0002_alter_recipe_author_alter_recipe_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='author',
            field=models.CharField(max_length=255),
        ),
    ]
