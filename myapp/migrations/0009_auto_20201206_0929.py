# Generated by Django 3.1.3 on 2020-12-06 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20201206_0922'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog_post',
            old_name='post_author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='blog_post',
            old_name='post_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='blog_post',
            old_name='post_img',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='blog_post',
            old_name='post_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='blog_post',
            old_name='post_title',
            new_name='title',
        ),
    ]
