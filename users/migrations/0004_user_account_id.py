# Generated by Django 2.2.5 on 2021-01-15 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210114_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='account_id',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
