# Generated by Django 4.1.7 on 2023-07-27 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch9app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='background_color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme_name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('flag', models.CharField(max_length=200)),
            ],
        ),
    ]
