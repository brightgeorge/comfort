# Generated by Django 4.1.7 on 2023-06-12 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch5app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pg1_new_beds',
            name='april_dis_amt',
            field=models.CharField(default='0', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pg1_new_beds',
            name='auguest_dis_amt',
            field=models.CharField(default='0', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pg1_new_beds',
            name='dec_dis_amt',
            field=models.CharField(default='0', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pg1_new_beds',
            name='feb_dis_amt',
            field=models.CharField(default='0', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pg1_new_beds',
            name='jan_dis_amt',
            field=models.CharField(default='0', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pg1_new_beds',
            name='july_dis_amt',
            field=models.CharField(default='0', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pg1_new_beds',
            name='june_dis_amt',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pg1_new_beds',
            name='march_dis_amt',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pg1_new_beds',
            name='may_dis_amt',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pg1_new_beds',
            name='nov_dis_amt',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pg1_new_beds',
            name='october_dis_amt',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pg1_new_beds',
            name='sept_dis_amt',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]