# Generated by Django 4.2.3 on 2023-07-31 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akademi', '0022_rename_blog_blog_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='akadem1_model',
            name='category',
            field=models.CharField(choices=[('duz', 'Düz'), ('damask', 'Damask'), ('cizgili', 'Çizgili'), ('tas_desen', 'Taş Desen'), ('cocuk', 'Çocuk'), ('cicek_desen', 'Çiçek Desen'), ('kircilli', 'Kırçıllı'), ('3d_poster', '3D Poster')], max_length=20),
        ),
        migrations.AlterField(
            model_name='akadem1_model',
            name='price',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='akadem1_model',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='akadem2_model',
            name='category',
            field=models.CharField(choices=[('duz', 'Düz'), ('damask', 'Damask'), ('cizgili', 'Çizgili'), ('tas_desen', 'Taş Desen'), ('cocuk', 'Çocuk'), ('cicek_desen', 'Çiçek Desen'), ('kircilli', 'Kırçıllı'), ('3d_poster', '3D Poster')], max_length=20),
        ),
        migrations.AlterField(
            model_name='akadem3_model',
            name='category',
            field=models.CharField(choices=[('duz', 'Düz'), ('damask', 'Damask'), ('cizgili', 'Çizgili'), ('tas_desen', 'Taş Desen'), ('cocuk', 'Çocuk'), ('cicek_desen', 'Çiçek Desen'), ('kircilli', 'Kırçıllı'), ('3d_poster', '3D Poster')], max_length=20),
        ),
        migrations.AlterField(
            model_name='akadem4_model',
            name='category',
            field=models.CharField(choices=[('duz', 'Düz'), ('damask', 'Damask'), ('cizgili', 'Çizgili'), ('tas_desen', 'Taş Desen'), ('cocuk', 'Çocuk'), ('cicek_desen', 'Çiçek Desen'), ('kircilli', 'Kırçıllı'), ('3d_poster', '3D Poster')], max_length=20),
        ),
    ]
