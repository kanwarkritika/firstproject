# Generated by Django 5.0.1 on 2024-01-13 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=200)),
                ('Last_Name', models.CharField(max_length=200)),
                ('Email', models.EmailField(max_length=200)),
                ('Company', models.CharField(max_length=200)),
                ('Contact', models.BigIntegerField()),
                ('Reason', models.CharField(max_length=250)),
                ('Message', models.TextField()),
            ],
            options={
                'db_table': 'contact',
            },
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Description', models.TextField()),
                ('CompanyName', models.CharField(max_length=200)),
                ('Price', models.BigIntegerField()),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]
