# Generated by Django 2.2.2 on 2019-07-02 17:03

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20190628_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='description_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
