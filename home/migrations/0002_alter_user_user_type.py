# Generated by Django 4.1.4 on 2023-03-30 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'parent'), (2, 'hod'), (3, 'warden')], default=1),
        ),
    ]