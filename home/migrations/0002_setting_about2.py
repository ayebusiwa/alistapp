# Generated by Django 3.2.3 on 2021-05-14 13:59

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='about2',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='About'),
        ),
    ]
