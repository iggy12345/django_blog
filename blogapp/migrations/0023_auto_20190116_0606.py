# Generated by Django 2.1.5 on 2019-01-16 06:06

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0022_auto_20190116_0549'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='status_changed',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status', verbose_name='status changed'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='status',
            field=model_utils.fields.StatusField(choices=[(0, 'dummy')], default='draft', max_length=100, no_check_for_status=True, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='sitenews',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 16, 6, 6, 30, 584826, tzinfo=utc), verbose_name='date published'),
        ),
    ]
