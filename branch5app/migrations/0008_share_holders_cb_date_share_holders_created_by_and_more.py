# Generated by Django 4.1.7 on 2023-10-01 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch5app', '0007_share_holders_share_holders_amt'),
    ]

    operations = [
        migrations.AddField(
            model_name='share_holders',
            name='cb_date',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='share_holders',
            name='created_by',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='share_holders',
            name='db_date',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='share_holders',
            name='deleted_by',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='share_holders',
            name='flag',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='share_holders',
            name='ub_date',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='share_holders',
            name='ub_flag',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='share_holders',
            name='updated_by',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]