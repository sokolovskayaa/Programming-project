# Generated by Django 3.2.5 on 2022-05-20 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20220521_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(default=None, to='tasks.Tag'),
        ),
        migrations.AlterField(
            model_name='taskfolder',
            name='tags',
            field=models.ManyToManyField(default=None, to='tasks.Tag'),
        ),
    ]
