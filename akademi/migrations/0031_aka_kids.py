# Generated by Django 4.2.3 on 2023-08-03 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akademi', '0030_alter_akadem2_model_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='aka_Kids',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='akakids_photo/')),
                ('price', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]
