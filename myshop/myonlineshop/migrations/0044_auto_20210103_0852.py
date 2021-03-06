# Generated by Django 3.1.1 on 2021-01-03 13:52

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myonlineshop', '0043_review_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='variant_product',
            new_name='variant',
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
