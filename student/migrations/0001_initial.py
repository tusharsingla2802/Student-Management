# Generated by Django 3.0.5 on 2020-07-09 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=20)),
                ('Contact', models.CharField(max_length=20)),
                ('Qualification', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Student',
            },
        ),
    ]
