# Generated by Django 2.1.5 on 2019-01-26 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0001_initial'),
        ('email_manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailbody',
            name='author',
        ),
        migrations.RemoveField(
            model_name='emailbody',
            name='id',
        ),
        migrations.RemoveField(
            model_name='emailbody',
            name='is_posted',
        ),
        migrations.RemoveField(
            model_name='emailbody',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='emailbody',
            name='text',
        ),
        migrations.AddField(
            model_name='emailbody',
            name='textpost_ptr',
            field=models.OneToOneField(auto_created=True, default=0, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='utils.TextPost'),
            preserve_default=False,
        ),
    ]
