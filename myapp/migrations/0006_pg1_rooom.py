# Generated by Django 4.1.7 on 2023-03-30 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_pg1_regform_self_mob_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='pg1_rooom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roon_no', models.IntegerField()),
                ('created_by', models.CharField(max_length=100)),
            ],
        ),
    ]
