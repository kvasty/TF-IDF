# Generated by Django 2.2.19 on 2024-03-27 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_file', models.CharField(max_length=100)),
                ('word', models.CharField(max_length=50)),
                ('tf', models.FloatField()),
                ('idf', models.FloatField()),
            ],
        ),
    ]
