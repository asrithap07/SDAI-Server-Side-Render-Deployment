# Generated by Django 5.0.7 on 2024-07-20 16:18

import detection.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("authtoken", "0004_alter_tokenproxy_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="UploadAlert",
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
                (
                    "image",
                    models.ImageField(
                        upload_to=detection.models.scramble_uploaded_filename,
                        verbose_name="Uploaded image",
                    ),
                ),
                ("alert_receiver", models.CharField(max_length=200)),
                ("location", models.CharField(max_length=200)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                (
                    "user_ID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="authtoken.token",
                    ),
                ),
            ],
        ),
    ]
