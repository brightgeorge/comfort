# Generated by Django 4.1.7 on 2023-07-15 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch4app', '0003_pg1_new_guest_april_dis_amt_and_more'),
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
