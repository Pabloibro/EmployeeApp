# Generated by Django 4.2 on 2023-04-05 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("EmployeeApp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Employee",
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
                ("full_name", models.CharField(max_length=200)),
                ("email", models.CharField(max_length=100)),
                ("contact", models.CharField(max_length=20)),
                ("address", models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name="Department",
        ),
        migrations.DeleteModel(
            name="Employees",
        ),
    ]