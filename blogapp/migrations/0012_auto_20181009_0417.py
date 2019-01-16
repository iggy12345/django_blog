# Generated by Django 2.1.1 on 2018-10-09 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0011_auto_20181009_0305'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForumComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, max_length=50, null=True)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('text', models.TextField()),
                ('comment_target', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blogapp.ForumComment')),
                ('question_target', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='blogapp.AskPost')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='askanswer',
            name='question_target',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blogapp.AskPost'),
        ),
    ]