# Generated by Django 3.0.8 on 2020-08-06 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myonlineshop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='myUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('phone_number', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_joined', models.DateField(auto_now_add=True)),
            ],
        ),
    ]