# Generated by Django 3.1.1 on 2020-10-14 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0019_auto_20201014_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='paid',
            field=models.BooleanField(choices=[('Pending Payment', 'Pending Payment'), ('Paid', 'Paid')], default='Pending Payment'),
        ),
    ]
