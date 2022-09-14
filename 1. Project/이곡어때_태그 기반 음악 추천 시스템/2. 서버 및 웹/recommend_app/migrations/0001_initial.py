# Generated by Django 3.2.5 on 2022-08-24 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100)),
                ('satisfaction', models.PositiveSmallIntegerField()),
                ('postdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
