# Generated by Django 4.1.7 on 2023-10-02 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch8app', '0003_accounts_book_category_in_exp_items_daily_ledger_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='share_holders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share_holders_name', models.CharField(max_length=200)),
                ('share_holders_percentage', models.CharField(max_length=200)),
                ('share_holders_amt', models.CharField(max_length=200)),
                ('created_by', models.CharField(max_length=200)),
                ('cb_date', models.CharField(max_length=200)),
                ('updated_by', models.CharField(max_length=200)),
                ('ub_date', models.CharField(max_length=200)),
                ('deleted_by', models.CharField(max_length=200)),
                ('db_date', models.CharField(max_length=200)),
                ('ub_flag', models.IntegerField()),
                ('flag', models.IntegerField()),
            ],
        ),
    ]
