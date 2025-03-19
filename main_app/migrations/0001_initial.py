# Generated by Django 5.0.6 on 2025-02-27 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('description', models.CharField(default='', max_length=300)),
                ('fees', models.IntegerField(default=0)),
                ('teacher', models.CharField(default='', max_length=100)),
                ('timings', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
