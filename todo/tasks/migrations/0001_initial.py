# Generated by Django 3.1.2 on 2021-01-08 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('complete', models.BooleanField(default=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
