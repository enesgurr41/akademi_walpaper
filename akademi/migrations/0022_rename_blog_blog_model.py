# Generated by Django 4.2.3 on 2023-07-31 12:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("akademi", "0021_blog"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="blog",
            new_name="blog_Model",
        ),
    ]