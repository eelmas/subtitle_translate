# Generated by Django 2.0.6 on 2018-06-26 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subtitle_app', '0004_auto_20180626_2033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='dscription',
            new_name='description',
        ),
    ]