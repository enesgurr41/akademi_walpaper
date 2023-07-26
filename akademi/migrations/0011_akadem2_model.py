# Generated by Django 4.2.3 on 2023-07-26 12:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("akademi", "0010_akadem1_model_delete_akadem1"),
    ]

    operations = [
        migrations.CreateModel(
            name="akadem2_Model",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="akadem2_photo/")),
                (
                    "category",
                    models.CharField(
                        choices=[
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
                ("price", models.CharField(max_length=10)),
                ("title", models.CharField(max_length=100)),
            ],
        ),
    ]