# Generated by Django 5.1.2 on 2024-10-29 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0008_campaign_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="campaign",
            name="points",
            field=models.IntegerField(default=0),
        ),
    ]
