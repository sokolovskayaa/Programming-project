# Generated by Django 3.2.5 on 2022-05-20 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='TaskFolder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('tags', models.ManyToManyField(to='tasks.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('text', models.TextField()),
                ('deadline', models.DateTimeField()),
                ('finished', models.BooleanField(default=False)),
                ('folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.taskfolder')),
                ('tags', models.ManyToManyField(to='tasks.Tag')),
            ],
        ),
    ]