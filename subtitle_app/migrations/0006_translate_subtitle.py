# Generated by Django 2.0.6 on 2018-06-26 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subtitle_app', '0005_auto_20180626_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='translate',
            name='subtitle',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
