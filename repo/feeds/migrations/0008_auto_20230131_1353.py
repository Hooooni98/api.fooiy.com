# Generated by Django 3.1.5 on 2023-01-31 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0007_feedcomment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedcomment',
            old_name='comment',
            new_name='content',
        ),
    ]