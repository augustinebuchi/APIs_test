# Generated by Django 4.1.1 on 2022-10-01 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('GovtApprovedID', models.IntegerField(max_length=200)),
                ('ExpiryDate', models.DateField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=25)),
                ('Password', models.SlugField(max_length=500)),
                ('address', models.CharField(max_length=70)),
            ],
        ),
    ]
