# Generated by Django 2.1.1 on 2018-10-04 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0008_auto_20181003_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='is_posted',
            field=models.BooleanField(default=False),
        ),
    ]
