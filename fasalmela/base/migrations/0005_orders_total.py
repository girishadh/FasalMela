# Generated by Django 5.1.2 on 2024-10-17 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_profile_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='total',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
