# Generated by Django 2.0.7 on 2018-10-06 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
