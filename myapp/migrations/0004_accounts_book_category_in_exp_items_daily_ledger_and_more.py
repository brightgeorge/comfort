# Generated by Django 4.1.7 on 2023-08-09 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_background_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='accounts_book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accounts_book_name', models.CharField(max_length=200)),
                ('created_by', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
                ('enter_by', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='in_exp_items_daily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('particulars', models.CharField(max_length=200)),
                ('amount', models.FloatField()),
                ('ledger', models.CharField(max_length=200)),
                ('accounts_book_name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('day', models.CharField(max_length=200)),
                ('month', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=200)),
                ('enter_by', models.CharField(max_length=200)),
                ('flag', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ledger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ledger_name', models.CharField(max_length=200)),
                ('contact_person_name', models.CharField(max_length=200)),
                ('contact_person_mob', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('created_by', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='opening_balance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_no', models.CharField(max_length=200)),
                ('month_name', models.CharField(max_length=200)),
                ('month_amount', models.FloatField()),
                ('date', models.CharField(max_length=200)),
                ('enter_by', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='table1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('item_category', models.CharField(max_length=200)),
                ('created_by', models.CharField(max_length=200)),
            ],
        ),
    ]
