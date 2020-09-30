# Generated by Django 3.1.1 on 2020-09-20 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myonlineshop', '0005_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='post',
        ),
        migrations.AddField(
            model_name='review',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review', to='myonlineshop.product'),
        ),
    ]
