# Generated by Django 5.1 on 2024-09-05 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_blog', '0002_blogpost_delete_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
