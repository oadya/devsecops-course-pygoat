# Generated by Django 3.0.6 on 2021-04-13 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAANG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=200)),
                ('ceo', models.CharField(max_length=200)),
                ('about', models.CharField(max_length=200)),
            ],
        ),
    ]
