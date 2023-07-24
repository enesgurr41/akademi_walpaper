# Generated by Django 4.2.3 on 2023-07-21 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akademi', '0005_rename_portfolio_duvar_kagidi'),
    ]

    operations = [
        migrations.AddField(
            model_name='duvar_paneli',
            name='category',
            field=models.CharField(choices=[('naber', 'naber'), ('nasilsin', 'nasilsin'), ('iyi', 'iyi'), ('baybay', 'baybay'), ('uza', 'uza'), ('aynen', 'aynen')], default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='duvar_paneli',
            name='price',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='salon_citasi',
            name='category',
            field=models.CharField(choices=[('duafdgz', 'Düafgz'), ('dafagmask', 'Damafask'), ('cizfgili', 'Çiagzgili'), ('tas_agagdesen', 'Taş agDesen'), ('cocaguk', 'Çoafcuk'), ('cicek_afdgdesen', 'Çiçekag Desen')], default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='salon_citasi',
            name='price',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stropiyer',
            name='category',
            field=models.CharField(choices=[('dufghfgz', 'Düfghz'), ('dafghmask', 'Dafghmask'), ('csfghizgili', 'Çizgfghili'), ('tas_sfghdesen', 'Taş gfhDesen'), ('cocgsdfuk', 'Çofgscuk'), ('cicek_sdfgdesen', 'Çiçek sdfgDesen')], default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stropiyer',
            name='price',
            field=models.CharField(default=2, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tavan_kaplama',
            name='category',
            field=models.CharField(choices=[('ddsfgz', 'Dsdfgüz'), ('damsdfgask', 'Damsfgask'), ('cizggsili', 'Çizgsgili'), ('tas_gdesen', 'Taşsfg Desen'), ('cocsguk', 'Çocusgk'), ('cicekfg_desen', 'Çiçekag Desen')], default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tavan_kaplama',
            name='price',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='duvar_paneli',
            name='image',
            field=models.ImageField(upload_to='duvar_panelleri/'),
        ),
        migrations.AlterField(
            model_name='salon_citasi',
            name='image',
            field=models.ImageField(upload_to='salon_citalari/'),
        ),
        migrations.AlterField(
            model_name='stropiyer',
            name='image',
            field=models.ImageField(upload_to='stropiyerler/'),
        ),
        migrations.AlterField(
            model_name='tavan_kaplama',
            name='image',
            field=models.ImageField(upload_to='tavan_kaplamalari/'),
        ),
    ]
