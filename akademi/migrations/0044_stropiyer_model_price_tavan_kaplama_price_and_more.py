# Generated by Django 4.2.3 on 2023-08-04 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akademi', '0043_alter_citalama_dekor_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='stropiyer_model',
            name='price',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='tavan_kaplama',
            name='price',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='aka_kids',
            name='price',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='akadem1_model',
            name='price',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='akadem2_model',
            name='price',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='akadem3_model',
            name='price',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='akadem4_model',
            name='price',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='duvar_paneli',
            name='price',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='poster_model',
            name='price',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='serisonu_model',
            name='price',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]