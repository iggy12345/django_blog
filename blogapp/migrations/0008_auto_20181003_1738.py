# Generated by Django 2.1.1 on 2018-10-03 17:38

import blogapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0007_auto_20181003_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posttopic',
            name='articles',
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='topic',
            field=models.ManyToManyField(default=blogapp.models.BlogPost.defaultTag, to='blogapp.PostTopic'),
        ),
    ]
