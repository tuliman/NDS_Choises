# Generated by Django 3.1.6 on 2021-02-03 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Objects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=250)),
                ('nds', models.BooleanField(blank=True, default=False)),
                ('nds_value', models.IntegerField(blank=True, default=20)),
            ],
        ),
    ]
