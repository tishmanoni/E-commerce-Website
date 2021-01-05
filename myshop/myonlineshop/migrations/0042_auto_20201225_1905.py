# Generated by Django 3.1.1 on 2020-12-25 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myonlineshop', '0041_delete_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='body',
        ),
        migrations.RemoveField(
            model_name='review',
            name='email',
        ),
        migrations.RemoveField(
            model_name='review',
            name='name',
        ),
        migrations.AddField(
            model_name='review',
            name='comment',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='review',
            name='subject',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]