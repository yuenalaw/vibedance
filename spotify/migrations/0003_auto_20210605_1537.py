# Generated by Django 3.1.4 on 2021-06-05 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0002_auto_20210605_1533'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spotifytoken',
            old_name='token_Type',
            new_name='token_type',
        ),
    ]
