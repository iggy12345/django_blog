# Generated by Django 2.1.2 on 2018-10-16 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0015_auto_20181010_0913'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailSubscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SiteNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='is_posted',
            field=models.BooleanField(default=True),
        ),
    ]
