# Generated by Django 4.2.3 on 2023-07-20 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akademi', '0002_duvar_kagidi_kategori_alter_duvar_kagidi_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img/duvar_kagitlari/')),
                ('category', models.CharField(choices=[('duz', 'Düz'), ('damask', 'Damask'), ('cizgili', 'Çizgili'), ('tas_desen', 'Taş Desen'), ('cocuk', 'Çocuk'), ('cicek_desen', 'Çiçek Desen')], max_length=20)),
                ('price', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='duvar_kagidi',
        ),
    ]
