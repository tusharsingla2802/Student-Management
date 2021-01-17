# Generated by Django 3.0.5 on 2020-08-25 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c1', models.CharField(max_length=10)),
                ('c2', models.CharField(max_length=10)),
                ('c3', models.CharField(max_length=10)),
                ('c4', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'Course',
            },
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Login',
            },
        ),
    ]