# Generated by Django 2.1.5 on 2019-01-16 05:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0020_auto_20190116_0544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitenews',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 16, 5, 46, 43, 255925, tzinfo=utc), verbose_name='date published'),
        ),
    ]
