# Generated by Django 4.2.3 on 2023-07-21 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akademi', '0003_portfolio_delete_duvar_kagidi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(upload_to='duvar_kagitlari/'),
        ),
    ]
