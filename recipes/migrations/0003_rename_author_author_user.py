# Generated by Django 3.2.20 on 2023-08-20 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_comment_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='author',
            new_name='user',
        ),
    ]
