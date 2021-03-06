# Generated by Django 2.1.5 on 2019-01-26 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0001_initial'),
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='askanswer',
            name='author',
        ),
        migrations.RemoveField(
            model_name='askanswer',
            name='id',
        ),
        migrations.RemoveField(
            model_name='askanswer',
            name='is_posted',
        ),
        migrations.RemoveField(
            model_name='askanswer',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='askanswer',
            name='text',
        ),
        migrations.RemoveField(
            model_name='askpost',
            name='author',
        ),
        migrations.RemoveField(
            model_name='askpost',
            name='id',
        ),
        migrations.RemoveField(
            model_name='askpost',
            name='is_posted',
        ),
        migrations.RemoveField(
            model_name='askpost',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='askpost',
            name='text',
        ),
        migrations.AddField(
            model_name='askanswer',
            name='textpost_ptr',
            field=models.OneToOneField(auto_created=True, default=0, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='utils.TextPost'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='askpost',
            name='question_answer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.AskAnswer'),
        ),
        migrations.AddField(
            model_name='askpost',
            name='textpost_ptr',
            field=models.OneToOneField(auto_created=True, default=0, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='utils.TextPost'),
            preserve_default=False,
        ),
    ]
