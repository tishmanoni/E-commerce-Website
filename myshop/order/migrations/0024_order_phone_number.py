# Generated by Django 3.1.1 on 2020-10-25 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0023_auto_20201024_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone_number',
            field=models.IntegerField(default=1, max_length=11),
            preserve_default=False,
        ),
    ]
