# Generated by Django 3.1.1 on 2020-10-25 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0026_auto_20201025_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(max_length=14),
        ),
    ]
