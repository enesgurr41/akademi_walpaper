# Generated by Django 4.2.3 on 2023-08-04 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akademi', '0042_alter_citalama_dekor_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citalama_dekor',
            name='price',
            field=models.CharField(blank=True, default=1, max_length=100),
            preserve_default=False,
        ),
    ]