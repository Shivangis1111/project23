# Generated by Django 4.1.4 on 2023-04-04 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_visitors_qr_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitors',
            name='qr_code',
        ),
        migrations.AddField(
            model_name='visitors',
            name='code',
            field=models.ImageField(blank=True, upload_to='code'),
        ),
    ]
