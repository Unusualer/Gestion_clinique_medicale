# Generated by Django 5.0.1 on 2024-01-14 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_rename_appoiment_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='Maladie',
            field=models.TextField(null=True),
        ),
    ]
