# Generated by Django 4.2.4 on 2023-08-14 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empolyee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('school', models.CharField(max_length=50, unique=True)),
                ('certificate', models.ImageField(upload_to='')),
                ('schoolCode', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('subscribeCode', models.CharField(max_length=50)),
                ('grade', models.PositiveIntegerField()),
                ('classNumber', models.PositiveIntegerField()),
                ('number', models.PositiveIntegerField()),
                ('isAllowed', models.BooleanField(default=False)),
            ],
        ),
    ]