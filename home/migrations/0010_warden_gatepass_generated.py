# Generated by Django 4.1.4 on 2023-04-04 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_remove_visitors_qr_code_visitors_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='warden',
            name='gatepass_generated',
            field=models.BooleanField(default=False),
        ),
    ]
