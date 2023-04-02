from django.db import models

# Create your models here.
class login(models.Model):
    emp_id = models.CharField(max_length=100)
    emp_name = models.CharField(max_length=250)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=20)
    emp_branch = models.CharField(max_length=200)
    emp_description = models.TextField()
    user_flage = models.IntegerField()

class pg1_regform(models.Model):
    room_no = models.CharField(max_length=20)
    name = models.CharField(max_length=250)
    room_type = models.CharField(max_length=20)
    monthly_rent = models.FloatField()
    advance = models.FloatField()
    age = models.IntegerField()
    dob = models.DateField()
    edu_qualification = models.CharField(max_length=200)
    mail_id = models.CharField(max_length=200)
    self_mob_no = models.BigIntegerField()
    id_proof_type = models.CharField(max_length=50)
    id_proof_no = models.CharField(max_length=50)

    prsnt_employee = models.CharField(max_length=200)
    prsnt_emp_contact_no = models.IntegerField()
    prsnt_emp_address = models.CharField(max_length=250)

    fname = models.CharField(max_length=100)
    fmob_no = models.IntegerField()
    emg_contact_no = models.IntegerField()
    relationship = models.CharField(max_length=100)

    permanent_address = models.TextField()
    join_date = models.DateField()

    jan_rent = models.FloatField()
    jan_rent_flag = models.IntegerField()
    feb_rent = models.FloatField()
    feb_rent_flag = models.IntegerField()
    march_rent = models.FloatField()
    march_rent_flag = models.IntegerField()
    april_rent = models.FloatField()
    april_rent_flag = models.IntegerField()

    may_rent = models.FloatField()
    may_rent_flag = models.IntegerField()
    june_rent = models.FloatField()
    june_rent_flag = models.IntegerField()
    july_rent = models.FloatField()
    july_rent_flag = models.IntegerField()
    aug_rent = models.FloatField()
    aug_rent_flag = models.IntegerField()

    sept_rent = models.FloatField()
    sept_rent_flag = models.IntegerField()
    oct_rent = models.FloatField()
    oct_rent_flag = models.IntegerField()
    nov_rent = models.FloatField()
    nov_rent_flag = models.IntegerField()
    dec_rent = models.FloatField()
    dec_rent_flag = models.IntegerField()

    year = models.CharField(max_length=20)
    month = models.CharField(max_length=20)
    branch_name = models.CharField(max_length=100)
    flag = models.IntegerField()

class pg1_rooom(models.Model):
    roon_no = models.CharField(max_length=20)
    created_by = models.CharField(max_length=100)

class pg2_rooom(models.Model):
    roon_no = models.CharField(max_length=20)
    created_by = models.CharField(max_length=100)


class pg2_regform(models.Model):
    room_no = models.CharField(max_length=20)
    name = models.CharField(max_length=250)
    room_type = models.CharField(max_length=20)
    monthly_rent = models.FloatField()
    advance = models.FloatField()
    age = models.IntegerField()
    dob = models.DateField()
    edu_qualification = models.CharField(max_length=200)
    mail_id = models.CharField(max_length=200)
    self_mob_no = models.BigIntegerField()
    id_proof_type = models.CharField(max_length=50)
    id_proof_no = models.CharField(max_length=50)

    prsnt_employee = models.CharField(max_length=200)
    prsnt_emp_contact_no = models.IntegerField()
    prsnt_emp_address = models.CharField(max_length=250)

    fname = models.CharField(max_length=100)
    fmob_no = models.IntegerField()
    emg_contact_no = models.IntegerField()
    relationship = models.CharField(max_length=100)

    permanent_address = models.TextField()
    join_date = models.DateField()

    jan_rent = models.FloatField()
    jan_rent_flag = models.IntegerField()
    feb_rent = models.FloatField()
    feb_rent_flag = models.IntegerField()
    march_rent = models.FloatField()
    march_rent_flag = models.IntegerField()
    april_rent = models.FloatField()
    april_rent_flag = models.IntegerField()

    may_rent = models.FloatField()
    may_rent_flag = models.IntegerField()
    june_rent = models.FloatField()
    june_rent_flag = models.IntegerField()
    july_rent = models.FloatField()
    july_rent_flag = models.IntegerField()
    aug_rent = models.FloatField()
    aug_rent_flag = models.IntegerField()

    sept_rent = models.FloatField()
    sept_rent_flag = models.IntegerField()
    oct_rent = models.FloatField()
    oct_rent_flag = models.IntegerField()
    nov_rent = models.FloatField()
    nov_rent_flag = models.IntegerField()
    dec_rent = models.FloatField()
    dec_rent_flag = models.IntegerField()

    year = models.CharField(max_length=20)
    month = models.CharField(max_length=20)
    branch_name = models.CharField(max_length=100)
    flag = models.IntegerField()

#PG THEREE START HERE
class pg3_rooom(models.Model):
    roon_no = models.CharField(max_length=20)
    created_by = models.CharField(max_length=100)


class pg3_regform(models.Model):
    room_no = models.CharField(max_length=20)
    name = models.CharField(max_length=250)
    room_type = models.CharField(max_length=20)
    monthly_rent = models.FloatField()
    advance = models.FloatField()
    age = models.IntegerField()
    dob = models.DateField()
    edu_qualification = models.CharField(max_length=200)
    mail_id = models.CharField(max_length=200)
    self_mob_no = models.BigIntegerField()
    id_proof_type = models.CharField(max_length=50)
    id_proof_no = models.CharField(max_length=50)

    prsnt_employee = models.CharField(max_length=200)
    prsnt_emp_contact_no = models.IntegerField()
    prsnt_emp_address = models.CharField(max_length=250)

    fname = models.CharField(max_length=100)
    fmob_no = models.IntegerField()
    emg_contact_no = models.IntegerField()
    relationship = models.CharField(max_length=100)

    permanent_address = models.TextField()
    join_date = models.DateField()

    jan_rent = models.FloatField()
    jan_rent_flag = models.IntegerField()
    feb_rent = models.FloatField()
    feb_rent_flag = models.IntegerField()
    march_rent = models.FloatField()
    march_rent_flag = models.IntegerField()
    april_rent = models.FloatField()
    april_rent_flag = models.IntegerField()

    may_rent = models.FloatField()
    may_rent_flag = models.IntegerField()
    june_rent = models.FloatField()
    june_rent_flag = models.IntegerField()
    july_rent = models.FloatField()
    july_rent_flag = models.IntegerField()
    aug_rent = models.FloatField()
    aug_rent_flag = models.IntegerField()

    sept_rent = models.FloatField()
    sept_rent_flag = models.IntegerField()
    oct_rent = models.FloatField()
    oct_rent_flag = models.IntegerField()
    nov_rent = models.FloatField()
    nov_rent_flag = models.IntegerField()
    dec_rent = models.FloatField()
    dec_rent_flag = models.IntegerField()

    year = models.CharField(max_length=20)
    month = models.CharField(max_length=20)
    branch_name = models.CharField(max_length=100)
    flag = models.IntegerField()






