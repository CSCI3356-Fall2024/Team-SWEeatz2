# Generated by Django 5.1.2 on 2024-11-19 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_completedaction_campaign'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='completed_by',
            field=models.JSONField(default=list, help_text='List of users who have completed the campaign'),
        ),
    ]
