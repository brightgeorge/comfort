# Generated by Django 4.1.7 on 2023-03-30 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_pg2_rooom'),
    ]

    operations = [
        migrations.CreateModel(
            name='pg2_regform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=250)),
                ('room_type', models.CharField(max_length=20)),
                ('monthly_rent', models.FloatField()),
                ('advance', models.FloatField()),
                ('age', models.IntegerField()),
                ('dob', models.DateField()),
                ('edu_qualification', models.CharField(max_length=200)),
                ('mail_id', models.CharField(max_length=200)),
                ('self_mob_no', models.BigIntegerField()),
                ('id_proof_type', models.CharField(max_length=50)),
                ('id_proof_no', models.CharField(max_length=50)),
                ('prsnt_employee', models.CharField(max_length=200)),
                ('prsnt_emp_contact_no', models.IntegerField()),
                ('prsnt_emp_address', models.CharField(max_length=250)),
                ('fname', models.CharField(max_length=100)),
                ('fmob_no', models.IntegerField()),
                ('emg_contact_no', models.IntegerField()),
                ('relationship', models.CharField(max_length=100)),
                ('permanent_address', models.TextField()),
                ('join_date', models.DateField()),
                ('jan_rent', models.FloatField()),
                ('jan_rent_flag', models.IntegerField()),
                ('feb_rent', models.FloatField()),
                ('feb_rent_flag', models.IntegerField()),
                ('march_rent', models.FloatField()),
                ('march_rent_flag', models.IntegerField()),
                ('april_rent', models.FloatField()),
                ('april_rent_flag', models.IntegerField()),
                ('may_rent', models.FloatField()),
                ('may_rent_flag', models.IntegerField()),
                ('june_rent', models.FloatField()),
                ('june_rent_flag', models.IntegerField()),
                ('july_rent', models.FloatField()),
                ('july_rent_flag', models.IntegerField()),
                ('aug_rent', models.FloatField()),
                ('aug_rent_flag', models.IntegerField()),
                ('sept_rent', models.FloatField()),
                ('sept_rent_flag', models.IntegerField()),
                ('oct_rent', models.FloatField()),
                ('oct_rent_flag', models.IntegerField()),
                ('nov_rent', models.FloatField()),
                ('nov_rent_flag', models.IntegerField()),
                ('dec_rent', models.FloatField()),
                ('dec_rent_flag', models.IntegerField()),
                ('year', models.CharField(max_length=20)),
                ('month', models.CharField(max_length=20)),
                ('branch_name', models.CharField(max_length=100)),
                ('flag', models.IntegerField()),
            ],
        ),
    ]
