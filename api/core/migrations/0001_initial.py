# Generated by Django 5.0.6 on 2024-06-10 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="StockData",
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
                ("date", models.DateField()),
                ("trade_code", models.CharField(max_length=20)),
                ("high", models.DecimalField(decimal_places=2, max_digits=10)),
                ("low", models.DecimalField(decimal_places=2, max_digits=10)),
                ("open", models.DecimalField(decimal_places=2, max_digits=10)),
                ("close", models.DecimalField(decimal_places=2, max_digits=10)),
                ("volume", models.PositiveIntegerField()),
            ],
        ),
    ]
