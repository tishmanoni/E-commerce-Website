# Generated by Django 3.1.1 on 2020-10-19 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myonlineshop', '0033_remove_product_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
    ]
