# Generated by Django 4.2.3 on 2023-08-02 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akademi', '0029_remove_stropiyer_model_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='akadem2_model',
            name='category',
            field=models.CharField(choices=[('duz', 'Düz'), ('damask', 'Damask'), ('cizgili', 'Çizgili'), ('cicek_desen', 'Çiçek Desen'), ('kircilli', 'Kırçıllı')], max_length=20),
        ),
    ]
