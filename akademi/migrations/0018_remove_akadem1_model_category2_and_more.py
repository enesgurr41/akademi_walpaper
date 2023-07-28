# Generated by Django 4.2.3 on 2023-07-28 12:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("akademi", "0017_akadem1_model_category2"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="akadem1_model",
            name="category2",
        ),
        migrations.AlterField(
            model_name="akadem1_model",
            name="category",
            field=models.CharField(
                choices=[
                    ("gold", "Akadem1 Gold"),
                    ("for", "Akadem1 For"),
                    ("black", "Akadem1 Black"),
                    ("duz", "Düz"),
                    ("damask", "Damask"),
                    ("cizgili", "Çizgili"),
                    ("tas_desen", "Taş Desen"),
                    ("cocuk", "Çocuk"),
                    ("cicek_desen", "Çiçek Desen"),
                    ("kircilli", "Kırçıllı"),
                ],
                max_length=20,
            ),
        ),
    ]