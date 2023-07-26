from django.db import models

# Create your models here.

class br2test(models.Model):
    br2test_name = models.CharField(max_length=10)


class room_pg1(models.Model):
    roon_no = models.IntegerField()
    room_name = models.CharField(max_length=100)
    share_type = models.IntegerField()
    created_by = models.CharField(max_length=100)

class pg1_new_beds(models.Model):
    roon_no = models.IntegerField()
    room_name = models.CharField(max_length=100)
    bed_no = models.IntegerField()
    created_by = models.CharField(max_length=100)

    bed_code = models.IntegerField()
    guest_code = models.IntegerField()
    guest_join_date = models.CharField(max_length=50)
    guest_join_month = models.CharField(max_length=50)
    guest_vacated_date = models.CharField(max_length=50)
    #guest_vacate_month = models.IntegerField()
    guest_vacate_month = models.CharField(max_length=50)

    share_type = models.IntegerField()
    name = models.CharField(max_length=150)
    advance = models.CharField(max_length=15)
    monthly_rent = models.CharField(max_length=12)
    self_mob = models.CharField(max_length=12)
    age = models.IntegerField(null=True)
    remark = models.CharField(max_length=100)
    narration = models.CharField(max_length=250)

    parent_name = models.CharField(max_length=200)
    parent_mob = models.BigIntegerField(null=True)
    permanent_address = models.TextField()

    jan_rent = models.FloatField(null=True)
    jan_advance = models.CharField(max_length=200)
    jan_due_amt = models.CharField(max_length=200)
    jan_dis_amt = models.CharField(max_length=200)
    jan_rent_rec_date = models.CharField(max_length=200)
    jan_rent_flag = models.IntegerField()

    feb_rent = models.FloatField()
    feb_advance = models.CharField(max_length=200)
    feb_due_amt = models.CharField(max_length=200)
    feb_dis_amt = models.CharField(max_length=200)
    feb_rent_rec_date = models.CharField(max_length=200)
    feb_rent_flag = models.IntegerField()

    march_rent = models.FloatField()
    march_advance = models.CharField(max_length=200)
    march_due_amt = models.CharField(max_length=200)
    march_dis_amt = models.CharField(max_length=200)
    march_rent_rec_date = models.CharField(max_length=200)
    march_rent_flag = models.IntegerField()

    april_rent = models.FloatField()
    april_advance = models.CharField(max_length=200)
    april_due_amt = models.CharField(max_length=200)
    april_dis_amt = models.CharField(max_length=200)
    april_rent_rec_date = models.CharField(max_length=200)
    april_rent_flag = models.IntegerField()

    may_rent = models.FloatField()
    may_advance = models.CharField(max_length=200)
    may_due_amt = models.CharField(max_length=200)
    may_dis_amt = models.CharField(max_length=200)
    may_rent_rec_date = models.CharField(max_length=200)
    may_rent_flag = models.IntegerField()

    june_rent = models.FloatField()
    june_advance = models.CharField(max_length=200)
    june_due_amt = models.CharField(max_length=200)
    june_dis_amt = models.CharField(max_length=200)
    june_rent_rec_date = models.CharField(max_length=200)
    june_rent_flag = models.IntegerField()

    july_rent = models.FloatField()
    july_advance = models.CharField(max_length=200)
    july_due_amt = models.CharField(max_length=200)
    july_dis_amt = models.CharField(max_length=200)
    july_rent_rec_date = models.CharField(max_length=200)
    july_rent_flag = models.IntegerField()

    auguest_rent = models.FloatField()
    auguest_advance = models.CharField(max_length=200)
    auguest_due_amt = models.CharField(max_length=200)
    auguest_dis_amt = models.CharField(max_length=200)
    auguest_rent_rec_date = models.CharField(max_length=200)
    auguest_rent_flag = models.IntegerField()

    sept_rent = models.FloatField()
    sept_advance = models.CharField(max_length=200)
    sept_due_amt = models.CharField(max_length=200)
    sept_dis_amt = models.CharField(max_length=200)
    sept_rent_rec_date = models.CharField(max_length=200)
    sept_rent_flag = models.IntegerField()

    october_rent = models.FloatField()
    october_advance = models.CharField(max_length=200)
    october_due_amt = models.CharField(max_length=200)
    october_dis_amt = models.CharField(max_length=200)
    october_rent_rec_date = models.CharField(max_length=200)
    october_rent_flag = models.IntegerField()

    nov_rent = models.FloatField()
    nov_advance = models.CharField(max_length=200)
    nov_due_amt = models.CharField(max_length=200)
    nov_dis_amt = models.CharField(max_length=200)
    nov_rent_rec_date = models.CharField(max_length=200)
    nov_rent_flag = models.IntegerField()

    dec_rent = models.FloatField()
    dec_advance = models.CharField(max_length=200)
    dec_due_amt = models.CharField(max_length=200)
    dec_dis_amt = models.CharField(max_length=200)
    dec_rent_rec_date = models.CharField(max_length=200)
    dec_rent_flag = models.IntegerField()

    #total_due = models.CharField(max_length=200)

    flag = models.IntegerField()


    def get_total_due_feb(self):
        rno = pg1_new_guest.objects.all().filter(guest_code = self.guest_code)
        lr = []
        for i in rno:
            lr.append(str(i.guest_code))
        gc = ''.join(lr)
        print('lllrr', lr)

        l=[]

        for i in rno:

            if i.jan_rent_flag >= 99:
                if i.jan_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.jan_advance)
                    c = int(i.jan_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.jan_rent_flag == 200:
                    l.append(int(i.jan_due_amt))

        ll = []
        for i in l:
            if i != '':
                ll.append(int(i))
        print('my lll',l)

        return sum(ll)


    def get_total_due_march(self):
        rno = pg1_new_guest.objects.all().filter(guest_code = self.guest_code)
        lr = []
        for i in rno:
            lr.append(str(i.guest_code))
        gc = ''.join(lr)
        print('lllrr', lr)

        l=[]

        for i in rno:

            if i.jan_rent_flag >= 99:
                if i.jan_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.jan_advance)
                    c = int(i.jan_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.jan_rent_flag == 200:
                    l.append(int(i.jan_due_amt))

            if i.feb_rent_flag >= 99:
                if i.feb_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.feb_advance)
                    c = int(i.feb_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.feb_rent_flag == 200:
                    l.append(int(i.feb_due_amt))

        ll = []
        for i in l:
            if i != '':
                ll.append(int(i))
        print('my lll',l)

        return sum(ll)


    def get_total_due_april(self):
        rno = pg1_new_guest.objects.all().filter(guest_code = self.guest_code)
        lr = []
        for i in rno:
            lr.append(str(i.guest_code))
        gc = ''.join(lr)
        print('lllrr', lr)

        l=[]

        for i in rno:

            if i.jan_rent_flag >= 99:
                if i.jan_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.jan_advance)
                    c = int(i.jan_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.jan_rent_flag == 200:
                    l.append(int(i.jan_due_amt))

            if i.feb_rent_flag >= 99:
                if i.feb_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.feb_advance)
                    c = int(i.feb_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.feb_rent_flag == 200:
                    l.append(int(i.feb_due_amt))

            if i.march_rent_flag >= 99:
                if i.march_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.march_advance)
                    c = int(i.march_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.march_rent_flag == 200:
                    l.append(int(i.march_due_amt))

        ll = []
        for i in l:
            if i != '':
                ll.append(int(i))
        print('my lll',l)

        return sum(ll)


    def get_total_due_may(self):
        rno = pg1_new_guest.objects.all().filter(guest_code = self.guest_code)
        lr = []
        for i in rno:
            lr.append(str(i.guest_code))
        gc = ''.join(lr)
        print('lllrr', lr)

        l=[]

        for i in rno:

            if i.jan_rent_flag >= 99:
                if i.jan_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.jan_advance)
                    c = int(i.jan_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.jan_rent_flag == 200:
                    l.append(int(i.jan_due_amt))

            if i.feb_rent_flag >= 99:
                if i.feb_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.feb_advance)
                    c = int(i.feb_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.feb_rent_flag == 200:
                    l.append(int(i.feb_due_amt))

            if i.march_rent_flag >= 99:
                if i.march_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.march_advance)
                    c = int(i.march_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.march_rent_flag == 200:
                    l.append(int(i.march_due_amt))

            if i.april_rent_flag >= 99:
                if i.april_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.april_advance)
                    c = int(i.april_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.april_rent_flag == 200:
                    l.append(int(i.april_due_amt))

        ll = []
        for i in l:
            if i != '':
                ll.append(int(i))
        print('my lll',l)

        return sum(ll)


    def get_total_due_june(self):
        rno = pg1_new_guest.objects.all().filter(guest_code = self.guest_code)
        lr = []
        for i in rno:
            lr.append(str(i.guest_code))
        gc = ''.join(lr)
        print('lllrr', lr)

        l=[]


        for i in rno:

            if i.jan_rent_flag >= 99:
                if i.jan_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.jan_advance)
                    c = int(i.jan_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.jan_rent_flag == 200:
                    l.append(int(i.jan_due_amt))

            if i.feb_rent_flag >= 99:
                if i.feb_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.feb_advance)
                    c = int(i.feb_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.feb_rent_flag == 200:
                    l.append(int(i.feb_due_amt))

            if i.march_rent_flag >= 99:
                if i.march_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.march_advance)
                    c = int(i.march_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.march_rent_flag == 200:
                    l.append(int(i.march_due_amt))

            if i.april_rent_flag >= 99:
                if i.april_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.april_advance)
                    c = int(i.april_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.april_rent_flag == 200:
                    l.append(int(i.april_due_amt))

            if i.may_rent_flag >= 99:
                if i.may_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.may_advance)
                    c = int(i.may_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.may_rent_flag == 200:
                    l.append(int(i.may_due_amt))

        ll = []
        for i in l:
            if i != '':
                ll.append(int(i))
        print('my lll',l)

        return sum(ll)


    def get_total_due_july(self):
        rno = pg1_new_guest.objects.all().filter(guest_code = self.guest_code)
        lr = []
        for i in rno:
            lr.append(str(i.guest_code))
        gc = ''.join(lr)
        print('lllrr', lr)

        l=[]


        for i in rno:

            if i.jan_rent_flag >= 99:
                if i.jan_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.jan_advance)
                    c = int(i.jan_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.jan_rent_flag == 200:
                    l.append(int(i.jan_due_amt))

            if i.feb_rent_flag >= 99:
                if i.feb_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.feb_advance)
                    c = int(i.feb_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.feb_rent_flag == 200:
                    l.append(int(i.feb_due_amt))

            if i.march_rent_flag >= 99:
                if i.march_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.march_advance)
                    c = int(i.march_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.march_rent_flag == 200:
                    l.append(int(i.march_due_amt))

            if i.april_rent_flag >= 99:
                if i.april_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.april_advance)
                    c = int(i.april_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.april_rent_flag == 200:
                    l.append(int(i.april_due_amt))

            if i.may_rent_flag >= 99:
                if i.may_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.may_advance)
                    c = int(i.may_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.may_rent_flag == 200:
                    l.append(int(i.may_due_amt))

            if i.june_rent_flag >= 99:
                if i.june_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.june_advance)
                    c = int(i.june_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.june_rent_flag == 200:
                    l.append(int(i.june_due_amt))

        ll = []
        for i in l:
            if i != '':
                ll.append(int(i))
        print('my lll',l)

        return sum(ll)


    def get_total_due_auguest(self):
        rno = pg1_new_guest.objects.all().filter(guest_code = self.guest_code)
        lr = []
        for i in rno:
            lr.append(str(i.guest_code))
        gc = ''.join(lr)
        print('lllrr', lr)

        l=[]

        for i in rno:

            if i.jan_rent_flag >= 99:
                if i.jan_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.jan_advance)
                    c = int(i.jan_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.jan_rent_flag == 200:
                    l.append(int(i.jan_due_amt))

            if i.feb_rent_flag >= 99:
                if i.feb_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.feb_advance)
                    c = int(i.feb_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.feb_rent_flag == 200:
                    l.append(int(i.feb_due_amt))

            if i.march_rent_flag >= 99:
                if i.march_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.march_advance)
                    c = int(i.march_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.march_rent_flag == 200:
                    l.append(int(i.march_due_amt))

            if i.april_rent_flag >= 99:
                if i.april_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.april_advance)
                    c = int(i.april_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.april_rent_flag == 200:
                    l.append(int(i.april_due_amt))

            if i.may_rent_flag >= 99:
                if i.may_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.may_advance)
                    c = int(i.may_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.may_rent_flag == 200:
                    l.append(int(i.may_due_amt))

            if i.june_rent_flag >= 99:
                if i.june_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.june_advance)
                    c = int(i.june_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.june_rent_flag == 200:
                    l.append(int(i.june_due_amt))

            if i.july_rent_flag >= 99:
                if i.july_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.july_advance)
                    c = int(i.july_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.july_rent_flag == 200:
                    l.append(int(i.july_due_amt))

        ll = []
        for i in l:
            if i != '':
                ll.append(int(i))
        print('my lll',l)

        return sum(ll)


    def get_total_due_sept(self):
        rno = pg1_new_guest.objects.all().filter(guest_code = self.guest_code)
        lr = []
        for i in rno:
            lr.append(str(i.guest_code))
        gc = ''.join(lr)
        print('lllrr', lr)

        l=[]

        for i in rno:

            if i.jan_rent_flag >= 99:
                if i.jan_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.jan_advance)
                    c = int(i.jan_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.jan_rent_flag == 200:
                    l.append(int(i.jan_due_amt))

            if i.feb_rent_flag >= 99:
                if i.feb_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.feb_advance)
                    c = int(i.feb_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.feb_rent_flag == 200:
                    l.append(int(i.feb_due_amt))

            if i.march_rent_flag >= 99:
                if i.march_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.march_advance)
                    c = int(i.march_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.march_rent_flag == 200:
                    l.append(int(i.march_due_amt))

            if i.april_rent_flag >= 99:
                if i.april_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.april_advance)
                    c = int(i.april_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.april_rent_flag == 200:
                    l.append(int(i.april_due_amt))

            if i.may_rent_flag >= 99:
                if i.may_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.may_advance)
                    c = int(i.may_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.may_rent_flag == 200:
                    l.append(int(i.may_due_amt))

            if i.june_rent_flag >= 99:
                if i.june_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.june_advance)
                    c = int(i.june_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.june_rent_flag == 200:
                    l.append(int(i.june_due_amt))

            if i.july_rent_flag >= 99:
                if i.july_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.july_advance)
                    c = int(i.july_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.july_rent_flag == 200:
                    l.append(int(i.july_due_amt))

            if i.auguest_rent_flag >= 99:
                if i.auguest_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.auguest_advance)
                    c = int(i.auguest_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.auguest_rent_flag == 200:
                    l.append(int(i.auguest_due_amt))

        ll = []
        for i in l:
            if i != '':
                ll.append(int(i))
        print('my lll',l)

        return sum(ll)

    def get_total_due_october(self):
        rno = pg1_new_guest.objects.all().filter(guest_code = self.guest_code)
        lr = []
        for i in rno:
            lr.append(str(i.guest_code))
        gc = ''.join(lr)
        print('lllrr', lr)

        l=[]

        for i in rno:

            if i.jan_rent_flag >= 99:
                if i.jan_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.jan_advance)
                    c = int(i.jan_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.jan_rent_flag == 200:
                    l.append(int(i.jan_due_amt))

            if i.feb_rent_flag >= 99:
                if i.feb_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.feb_advance)
                    c = int(i.feb_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.feb_rent_flag == 200:
                    l.append(int(i.feb_due_amt))

            if i.march_rent_flag >= 99:
                if i.march_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.march_advance)
                    c = int(i.march_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.march_rent_flag == 200:
                    l.append(int(i.march_due_amt))

            if i.april_rent_flag >= 99:
                if i.april_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.april_advance)
                    c = int(i.april_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.april_rent_flag == 200:
                    l.append(int(i.april_due_amt))

            if i.may_rent_flag >= 99:
                if i.may_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.may_advance)
                    c = int(i.may_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.may_rent_flag == 200:
                    l.append(int(i.may_due_amt))

            if i.june_rent_flag >= 99:
                if i.june_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.june_advance)
                    c = int(i.june_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.june_rent_flag == 200:
                    l.append(int(i.june_due_amt))

            if i.july_rent_flag >= 99:
                if i.july_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.july_advance)
                    c = int(i.july_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.july_rent_flag == 200:
                    l.append(int(i.july_due_amt))

            if i.auguest_rent_flag >= 99:
                if i.auguest_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.auguest_advance)
                    c = int(i.auguest_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.auguest_rent_flag == 200:
                    l.append(int(i.auguest_due_amt))

            if i.sept_rent_flag >= 99:
                if i.sept_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.sept_advance)
                    c = int(i.sept_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.sept_rent_flag == 200:
                    l.append(int(i.sept_due_amt))

        ll = []
        for i in l:
            if i != '':
                ll.append(int(i))
        print('my lll',l)

        return sum(ll)

    def get_total_due_nov(self):
        rno = pg1_new_guest.objects.all().filter(guest_code=self.guest_code)
        lr = []
        for i in rno:
            lr.append(str(i.guest_code))
        gc = ''.join(lr)
        print('lllrr', lr)

        l = []

        for i in rno:

            if i.jan_rent_flag >= 99:
                if i.jan_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.jan_advance)
                    c = int(i.jan_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.jan_rent_flag == 200:
                    l.append(int(i.jan_due_amt))

            if i.feb_rent_flag >= 99:
                if i.feb_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.feb_advance)
                    c = int(i.feb_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.feb_rent_flag == 200:
                    l.append(int(i.feb_due_amt))

            if i.march_rent_flag >= 99:
                if i.march_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.march_advance)
                    c = int(i.march_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.march_rent_flag == 200:
                    l.append(int(i.march_due_amt))

            if i.april_rent_flag >= 99:
                if i.april_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.april_advance)
                    c = int(i.april_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.april_rent_flag == 200:
                    l.append(int(i.april_due_amt))

            if i.may_rent_flag >= 99:
                if i.may_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.may_advance)
                    c = int(i.may_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.may_rent_flag == 200:
                    l.append(int(i.may_due_amt))

            if i.june_rent_flag >= 99:
                if i.june_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.june_advance)
                    c = int(i.june_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.june_rent_flag == 200:
                    l.append(int(i.june_due_amt))

            if i.july_rent_flag >= 99:
                if i.july_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.july_advance)
                    c = int(i.july_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.july_rent_flag == 200:
                    l.append(int(i.july_due_amt))

            if i.auguest_rent_flag >= 99:
                if i.auguest_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.auguest_advance)
                    c = int(i.auguest_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.auguest_rent_flag == 200:
                    l.append(int(i.auguest_due_amt))

            if i.sept_rent_flag >= 99:
                if i.sept_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.sept_advance)
                    c = int(i.sept_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.sept_rent_flag == 200:
                    l.append(int(i.sept_due_amt))

            if i.october_rent_flag >= 99:
                if i.october_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.october_advance)
                    c = int(i.october_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.october_rent_flag == 200:
                    l.append(int(i.october_due_amt))

        ll = []
        for i in l:
            if i != '':
                ll.append(int(i))
        print('my lll', l)

        return sum(ll)


    def get_total_due_dec(self):
        rno = pg1_new_guest.objects.all().filter(guest_code=self.guest_code)
        lr = []
        for i in rno:
            lr.append(str(i.guest_code))
        gc = ''.join(lr)
        print('lllrr', lr)

        l = []


        for i in rno:

            if i.jan_rent_flag >= 99:
                if i.jan_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.jan_advance)
                    c = int(i.jan_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.jan_rent_flag == 200:
                    l.append(int(i.jan_due_amt))

            if i.feb_rent_flag >= 99:
                if i.feb_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.feb_advance)
                    c = int(i.feb_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.feb_rent_flag == 200:
                    l.append(int(i.feb_due_amt))

            if i.march_rent_flag >= 99:
                if i.march_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.march_advance)
                    c = int(i.march_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.march_rent_flag == 200:
                    l.append(int(i.march_due_amt))

            if i.april_rent_flag >= 99:
                if i.april_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.april_advance)
                    c = int(i.april_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.april_rent_flag == 200:
                    l.append(int(i.april_due_amt))

            if i.may_rent_flag >= 99:
                if i.may_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.may_advance)
                    c = int(i.may_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.may_rent_flag == 200:
                    l.append(int(i.may_due_amt))

            if i.june_rent_flag >= 99:
                if i.june_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.june_advance)
                    c = int(i.june_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.june_rent_flag == 200:
                    l.append(int(i.june_due_amt))

            if i.july_rent_flag >= 99:
                if i.july_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.july_advance)
                    c = int(i.july_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.july_rent_flag == 200:
                    l.append(int(i.july_due_amt))

            if i.auguest_rent_flag >= 99:
                if i.auguest_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.auguest_advance)
                    c = int(i.auguest_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.auguest_rent_flag == 200:
                    l.append(int(i.auguest_due_amt))

            if i.sept_rent_flag >= 99:
                if i.sept_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.sept_advance)
                    c = int(i.sept_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.sept_rent_flag == 200:
                    l.append(int(i.sept_due_amt))

            if i.october_rent_flag >= 99:
                if i.october_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.october_advance)
                    c = int(i.october_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.october_rent_flag == 200:
                    l.append(int(i.october_due_amt))

            if i.nov_rent_flag >= 99:
                if i.nov_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.nov_advance)
                    c = int(i.nov_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.nov_rent_flag == 200:
                    l.append(int(i.nov_due_amt))

        ll = []
        for i in l:
            if i != '':
                ll.append(int(i))
        print('my lll', l)

        return sum(ll)





class pg1_new_guest(models.Model):
    roon_no = models.IntegerField()
    room_name = models.CharField(max_length=100)
    bed_no = models.IntegerField()
    created_by = models.CharField(max_length=100)

    bed_code = models.IntegerField()
    guest_code = models.IntegerField()
    guest_join_date = models.CharField(max_length=50)
    guest_join_month = models.CharField(max_length=50)
    guest_vacated_date = models.CharField(max_length=50)
    #guest_vacate_month = models.IntegerField()
    guest_vacate_month = models.CharField(max_length=50)

    share_type = models.IntegerField()
    name = models.CharField(max_length=150)
    advance = models.CharField(max_length=15)
    monthly_rent = models.CharField(max_length=12)
    self_mob = models.CharField(max_length=12)
    age = models.IntegerField(null=True)
    remark = models.CharField(max_length=100)
    narration = models.CharField(max_length=250)

    parent_name = models.CharField(max_length=200)
    parent_mob = models.BigIntegerField(null=True)
    permanent_address = models.TextField()

    jan_rent = models.FloatField()
    jan_advance = models.CharField(max_length=200)
    jan_due_amt = models.CharField(max_length=200)
    jan_dis_amt = models.CharField(max_length=200)
    jan_rent_rec_date = models.CharField(max_length=200)
    jan_rent_flag = models.IntegerField()

    feb_rent = models.FloatField()
    feb_advance = models.CharField(max_length=200)
    feb_due_amt = models.CharField(max_length=200)
    feb_dis_amt = models.CharField(max_length=200)
    feb_rent_rec_date = models.CharField(max_length=200)
    feb_rent_flag = models.IntegerField()

    march_rent = models.FloatField()
    march_advance = models.CharField(max_length=200)
    march_due_amt = models.CharField(max_length=200)
    march_dis_amt = models.CharField(max_length=200)
    march_rent_rec_date = models.CharField(max_length=200)
    march_rent_flag = models.IntegerField()

    april_rent = models.FloatField()
    april_advance = models.CharField(max_length=200)
    april_due_amt = models.CharField(max_length=200)
    april_dis_amt = models.CharField(max_length=200)
    april_rent_rec_date = models.CharField(max_length=200)
    april_rent_flag = models.IntegerField()

    may_rent = models.FloatField()
    may_advance = models.CharField(max_length=200)
    may_due_amt = models.CharField(max_length=200)
    may_dis_amt = models.CharField(max_length=200)
    may_rent_rec_date = models.CharField(max_length=200)
    may_rent_flag = models.IntegerField()

    june_rent = models.FloatField()
    june_advance = models.CharField(max_length=200)
    june_due_amt = models.CharField(max_length=200)
    june_dis_amt = models.CharField(max_length=200)
    june_rent_rec_date = models.CharField(max_length=200)
    june_rent_flag = models.IntegerField()

    july_rent = models.FloatField()
    july_advance = models.CharField(max_length=200)
    july_due_amt = models.CharField(max_length=200)
    july_dis_amt = models.CharField(max_length=200)
    july_rent_rec_date = models.CharField(max_length=200)
    july_rent_flag = models.IntegerField()

    auguest_rent = models.FloatField()
    auguest_advance = models.CharField(max_length=200)
    auguest_due_amt = models.CharField(max_length=200)
    auguest_dis_amt = models.CharField(max_length=200)
    auguest_rent_rec_date = models.CharField(max_length=200)
    auguest_rent_flag = models.IntegerField()

    sept_rent = models.FloatField()
    sept_advance = models.CharField(max_length=200)
    sept_due_amt = models.CharField(max_length=200)
    sept_dis_amt = models.CharField(max_length=200)
    sept_rent_rec_date = models.CharField(max_length=200)
    sept_rent_flag = models.IntegerField()

    october_rent = models.FloatField()
    october_advance = models.CharField(max_length=200)
    october_due_amt = models.CharField(max_length=200)
    october_dis_amt = models.CharField(max_length=200)
    october_rent_rec_date = models.CharField(max_length=200)
    october_rent_flag = models.IntegerField()

    nov_rent = models.FloatField()
    nov_advance = models.CharField(max_length=200)
    nov_due_amt = models.CharField(max_length=200)
    nov_dis_amt = models.CharField(max_length=200)
    nov_rent_rec_date = models.CharField(max_length=200)
    nov_rent_flag = models.IntegerField()

    dec_rent = models.FloatField()
    dec_advance = models.CharField(max_length=200)
    dec_due_amt = models.CharField(max_length=200)
    dec_dis_amt = models.CharField(max_length=200)
    dec_rent_rec_date = models.CharField(max_length=200)
    dec_rent_flag = models.IntegerField()

    flag = models.IntegerField()




    def get_total_due_feb(self):
        rno = pg1_new_guest.objects.all().filter(guest_code = self.guest_code)
        lr = []
        for i in rno:
            lr.append(str(i.guest_code))
        gc = ''.join(lr)
        print('lllrr', lr)

        l=[]

        for i in rno:

            if i.jan_rent_flag >= 99:
                if i.jan_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.jan_advance)
                    c = int(i.jan_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.jan_rent_flag == 200:
                    l.append(int(i.jan_due_amt))

        ll = []
        for i in l:
            if i != '':
                ll.append(int(i))
        print('my lll',l)

        return sum(ll)


    def get_total_due_march(self):
        rno = pg1_new_guest.objects.all().filter(guest_code = self.guest_code)
        lr = []
        for i in rno:
            lr.append(str(i.guest_code))
        gc = ''.join(lr)
        print('lllrr', lr)

        l=[]

        for i in rno:

            if i.jan_rent_flag >= 99:
                if i.jan_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.jan_advance)
                    c = int(i.jan_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.jan_rent_flag == 200:
                    l.append(int(i.jan_due_amt))

            if i.feb_rent_flag >= 99:
                if i.feb_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.feb_advance)
                    c = int(i.feb_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.feb_rent_flag == 200:
                    l.append(int(i.feb_due_amt))

        ll = []
        for i in l:
            if i != '':
                ll.append(int(i))
        print('my lll',l)

        return sum(ll)


    def get_total_due_april(self):
        rno = pg1_new_guest.objects.all().filter(guest_code = self.guest_code)
        lr = []
        for i in rno:
            lr.append(str(i.guest_code))
        gc = ''.join(lr)
        print('lllrr', lr)

        l=[]

        for i in rno:

            if i.jan_rent_flag >= 99:
                if i.jan_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.jan_advance)
                    c = int(i.jan_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.jan_rent_flag == 200:
                    l.append(int(i.jan_due_amt))

            if i.feb_rent_flag >= 99:
                if i.feb_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.feb_advance)
                    c = int(i.feb_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.feb_rent_flag == 200:
                    l.append(int(i.feb_due_amt))

            if i.march_rent_flag >= 99:
                if i.march_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.march_advance)
                    c = int(i.march_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.march_rent_flag == 200:
                    l.append(int(i.march_due_amt))

        ll = []
        for i in l:
            if i != '':
                ll.append(int(i))
        print('my lll',l)

        return sum(ll)


    def get_total_due_may(self):
        rno = pg1_new_guest.objects.all().filter(guest_code = self.guest_code)
        lr = []
        for i in rno:
            lr.append(str(i.guest_code))
        gc = ''.join(lr)
        print('lllrr', lr)

        l=[]

        for i in rno:

            if i.jan_rent_flag >= 99:
                if i.jan_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.jan_advance)
                    c = int(i.jan_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.jan_rent_flag == 200:
                    l.append(int(i.jan_due_amt))

            if i.feb_rent_flag >= 99:
                if i.feb_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.feb_advance)
                    c = int(i.feb_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.feb_rent_flag == 200:
                    l.append(int(i.feb_due_amt))

            if i.march_rent_flag >= 99:
                if i.march_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.march_advance)
                    c = int(i.march_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.march_rent_flag == 200:
                    l.append(int(i.march_due_amt))

            if i.april_rent_flag >= 99:
                if i.april_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.april_advance)
                    c = int(i.april_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.april_rent_flag == 200:
                    l.append(int(i.april_due_amt))

        ll = []
        for i in l:
            if i != '':
                ll.append(int(i))
        print('my lll',l)

        return sum(ll)


    def get_total_due_june(self):
        rno = pg1_new_guest.objects.all().filter(guest_code = self.guest_code)
        lr = []
        for i in rno:
            lr.append(str(i.guest_code))
        gc = ''.join(lr)
        print('lllrr', lr)

        l=[]


        for i in rno:

            if i.jan_rent_flag >= 99:
                if i.jan_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.jan_advance)
                    c = int(i.jan_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.jan_rent_flag == 200:
                    l.append(int(i.jan_due_amt))

            if i.feb_rent_flag >= 99:
                if i.feb_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.feb_advance)
                    c = int(i.feb_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.feb_rent_flag == 200:
                    l.append(int(i.feb_due_amt))

            if i.march_rent_flag >= 99:
                if i.march_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.march_advance)
                    c = int(i.march_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.march_rent_flag == 200:
                    l.append(int(i.march_due_amt))

            if i.april_rent_flag >= 99:
                if i.april_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.april_advance)
                    c = int(i.april_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.april_rent_flag == 200:
                    l.append(int(i.april_due_amt))

            if i.may_rent_flag >= 99:
                if i.may_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.may_advance)
                    c = int(i.may_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.may_rent_flag == 200:
                    l.append(int(i.may_due_amt))

        ll = []
        for i in l:
            if i != '':
                ll.append(int(i))
        print('my lll',l)

        return sum(ll)


    def get_total_due_july(self):
        rno = pg1_new_guest.objects.all().filter(guest_code = self.guest_code)
        lr = []
        for i in rno:
            lr.append(str(i.guest_code))
        gc = ''.join(lr)
        print('lllrr', lr)

        l=[]


        for i in rno:

            if i.jan_rent_flag >= 99:
                if i.jan_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.jan_advance)
                    c = int(i.jan_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.jan_rent_flag == 200:
                    l.append(int(i.jan_due_amt))

            if i.feb_rent_flag >= 99:
                if i.feb_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.feb_advance)
                    c = int(i.feb_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.feb_rent_flag == 200:
                    l.append(int(i.feb_due_amt))

            if i.march_rent_flag >= 99:
                if i.march_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.march_advance)
                    c = int(i.march_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.march_rent_flag == 200:
                    l.append(int(i.march_due_amt))

            if i.april_rent_flag >= 99:
                if i.april_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.april_advance)
                    c = int(i.april_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.april_rent_flag == 200:
                    l.append(int(i.april_due_amt))

            if i.may_rent_flag >= 99:
                if i.may_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.may_advance)
                    c = int(i.may_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.may_rent_flag == 200:
                    l.append(int(i.may_due_amt))

            if i.june_rent_flag >= 99:
                if i.june_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.june_advance)
                    c = int(i.june_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.june_rent_flag == 200:
                    l.append(int(i.june_due_amt))

        ll = []
        for i in l:
            if i != '':
                ll.append(int(i))
        print('my lll',l)

        return sum(ll)


    def get_total_due_auguest(self):
        rno = pg1_new_guest.objects.all().filter(guest_code = self.guest_code)
        lr = []
        for i in rno:
            lr.append(str(i.guest_code))
        gc = ''.join(lr)
        print('lllrr', lr)

        l=[]

        for i in rno:

            if i.jan_rent_flag >= 99:
                if i.jan_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.jan_advance)
                    c = int(i.jan_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.jan_rent_flag == 200:
                    l.append(int(i.jan_due_amt))

            if i.feb_rent_flag >= 99:
                if i.feb_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.feb_advance)
                    c = int(i.feb_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.feb_rent_flag == 200:
                    l.append(int(i.feb_due_amt))

            if i.march_rent_flag >= 99:
                if i.march_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.march_advance)
                    c = int(i.march_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.march_rent_flag == 200:
                    l.append(int(i.march_due_amt))

            if i.april_rent_flag >= 99:
                if i.april_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.april_advance)
                    c = int(i.april_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.april_rent_flag == 200:
                    l.append(int(i.april_due_amt))

            if i.may_rent_flag >= 99:
                if i.may_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.may_advance)
                    c = int(i.may_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.may_rent_flag == 200:
                    l.append(int(i.may_due_amt))

            if i.june_rent_flag >= 99:
                if i.june_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.june_advance)
                    c = int(i.june_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.june_rent_flag == 200:
                    l.append(int(i.june_due_amt))

            if i.july_rent_flag >= 99:
                if i.july_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.july_advance)
                    c = int(i.july_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.july_rent_flag == 200:
                    l.append(int(i.july_due_amt))

        ll = []
        for i in l:
            if i != '':
                ll.append(int(i))
        print('my lll',l)

        return sum(ll)


    def get_total_due_sept(self):
        rno = pg1_new_guest.objects.all().filter(guest_code = self.guest_code)
        lr = []
        for i in rno:
            lr.append(str(i.guest_code))
        gc = ''.join(lr)
        print('lllrr', lr)

        l=[]

        for i in rno:

            if i.jan_rent_flag >= 99:
                if i.jan_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.jan_advance)
                    c = int(i.jan_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.jan_rent_flag == 200:
                    l.append(int(i.jan_due_amt))

            if i.feb_rent_flag >= 99:
                if i.feb_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.feb_advance)
                    c = int(i.feb_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.feb_rent_flag == 200:
                    l.append(int(i.feb_due_amt))

            if i.march_rent_flag >= 99:
                if i.march_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.march_advance)
                    c = int(i.march_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.march_rent_flag == 200:
                    l.append(int(i.march_due_amt))

            if i.april_rent_flag >= 99:
                if i.april_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.april_advance)
                    c = int(i.april_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.april_rent_flag == 200:
                    l.append(int(i.april_due_amt))

            if i.may_rent_flag >= 99:
                if i.may_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.may_advance)
                    c = int(i.may_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.may_rent_flag == 200:
                    l.append(int(i.may_due_amt))

            if i.june_rent_flag >= 99:
                if i.june_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.june_advance)
                    c = int(i.june_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.june_rent_flag == 200:
                    l.append(int(i.june_due_amt))

            if i.july_rent_flag >= 99:
                if i.july_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.july_advance)
                    c = int(i.july_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.july_rent_flag == 200:
                    l.append(int(i.july_due_amt))

            if i.auguest_rent_flag >= 99:
                if i.auguest_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.auguest_advance)
                    c = int(i.auguest_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.auguest_rent_flag == 200:
                    l.append(int(i.auguest_due_amt))

        ll = []
        for i in l:
            if i != '':
                ll.append(int(i))
        print('my lll',l)

        return sum(ll)

    def get_total_due_october(self):
        rno = pg1_new_guest.objects.all().filter(guest_code = self.guest_code)
        lr = []
        for i in rno:
            lr.append(str(i.guest_code))
        gc = ''.join(lr)
        print('lllrr', lr)

        l=[]

        for i in rno:

            if i.jan_rent_flag >= 99:
                if i.jan_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.jan_advance)
                    c = int(i.jan_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.jan_rent_flag == 200:
                    l.append(int(i.jan_due_amt))

            if i.feb_rent_flag >= 99:
                if i.feb_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.feb_advance)
                    c = int(i.feb_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.feb_rent_flag == 200:
                    l.append(int(i.feb_due_amt))

            if i.march_rent_flag >= 99:
                if i.march_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.march_advance)
                    c = int(i.march_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.march_rent_flag == 200:
                    l.append(int(i.march_due_amt))

            if i.april_rent_flag >= 99:
                if i.april_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.april_advance)
                    c = int(i.april_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.april_rent_flag == 200:
                    l.append(int(i.april_due_amt))

            if i.may_rent_flag >= 99:
                if i.may_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.may_advance)
                    c = int(i.may_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.may_rent_flag == 200:
                    l.append(int(i.may_due_amt))

            if i.june_rent_flag >= 99:
                if i.june_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.june_advance)
                    c = int(i.june_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.june_rent_flag == 200:
                    l.append(int(i.june_due_amt))

            if i.july_rent_flag >= 99:
                if i.july_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.july_advance)
                    c = int(i.july_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.july_rent_flag == 200:
                    l.append(int(i.july_due_amt))

            if i.auguest_rent_flag >= 99:
                if i.auguest_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.auguest_advance)
                    c = int(i.auguest_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.auguest_rent_flag == 200:
                    l.append(int(i.auguest_due_amt))

            if i.sept_rent_flag >= 99:
                if i.sept_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.sept_advance)
                    c = int(i.sept_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.sept_rent_flag == 200:
                    l.append(int(i.sept_due_amt))

        ll = []
        for i in l:
            if i != '':
                ll.append(int(i))
        print('my lll',l)

        return sum(ll)

    def get_total_due_nov(self):
        rno = pg1_new_guest.objects.all().filter(guest_code=self.guest_code)
        lr = []
        for i in rno:
            lr.append(str(i.guest_code))
        gc = ''.join(lr)
        print('lllrr', lr)

        l = []

        for i in rno:

            if i.jan_rent_flag >= 99:
                if i.jan_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.jan_advance)
                    c = int(i.jan_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.jan_rent_flag == 200:
                    l.append(int(i.jan_due_amt))

            if i.feb_rent_flag >= 99:
                if i.feb_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.feb_advance)
                    c = int(i.feb_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.feb_rent_flag == 200:
                    l.append(int(i.feb_due_amt))

            if i.march_rent_flag >= 99:
                if i.march_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.march_advance)
                    c = int(i.march_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.march_rent_flag == 200:
                    l.append(int(i.march_due_amt))

            if i.april_rent_flag >= 99:
                if i.april_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.april_advance)
                    c = int(i.april_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.april_rent_flag == 200:
                    l.append(int(i.april_due_amt))

            if i.may_rent_flag >= 99:
                if i.may_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.may_advance)
                    c = int(i.may_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.may_rent_flag == 200:
                    l.append(int(i.may_due_amt))

            if i.june_rent_flag >= 99:
                if i.june_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.june_advance)
                    c = int(i.june_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.june_rent_flag == 200:
                    l.append(int(i.june_due_amt))

            if i.july_rent_flag >= 99:
                if i.july_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.july_advance)
                    c = int(i.july_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.july_rent_flag == 200:
                    l.append(int(i.july_due_amt))

            if i.auguest_rent_flag >= 99:
                if i.auguest_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.auguest_advance)
                    c = int(i.auguest_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.auguest_rent_flag == 200:
                    l.append(int(i.auguest_due_amt))

            if i.sept_rent_flag >= 99:
                if i.sept_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.sept_advance)
                    c = int(i.sept_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.sept_rent_flag == 200:
                    l.append(int(i.sept_due_amt))

            if i.october_rent_flag >= 99:
                if i.october_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.october_advance)
                    c = int(i.october_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.october_rent_flag == 200:
                    l.append(int(i.october_due_amt))

        ll = []
        for i in l:
            if i != '':
                ll.append(int(i))
        print('my lll', l)

        return sum(ll)


    def get_total_due_dec(self):
        rno = pg1_new_guest.objects.all().filter(guest_code=self.guest_code)
        lr = []
        for i in rno:
            lr.append(str(i.guest_code))
        gc = ''.join(lr)
        print('lllrr', lr)

        l = []


        for i in rno:

            if i.jan_rent_flag >= 99:
                if i.jan_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.jan_advance)
                    c = int(i.jan_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.jan_rent_flag == 200:
                    l.append(int(i.jan_due_amt))

            if i.feb_rent_flag >= 99:
                if i.feb_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.feb_advance)
                    c = int(i.feb_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.feb_rent_flag == 200:
                    l.append(int(i.feb_due_amt))

            if i.march_rent_flag >= 99:
                if i.march_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.march_advance)
                    c = int(i.march_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.march_rent_flag == 200:
                    l.append(int(i.march_due_amt))

            if i.april_rent_flag >= 99:
                if i.april_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.april_advance)
                    c = int(i.april_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.april_rent_flag == 200:
                    l.append(int(i.april_due_amt))

            if i.may_rent_flag >= 99:
                if i.may_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.may_advance)
                    c = int(i.may_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.may_rent_flag == 200:
                    l.append(int(i.may_due_amt))

            if i.june_rent_flag >= 99:
                if i.june_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.june_advance)
                    c = int(i.june_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.june_rent_flag == 200:
                    l.append(int(i.june_due_amt))

            if i.july_rent_flag >= 99:
                if i.july_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.july_advance)
                    c = int(i.july_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.july_rent_flag == 200:
                    l.append(int(i.july_due_amt))

            if i.auguest_rent_flag >= 99:
                if i.auguest_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.auguest_advance)
                    c = int(i.auguest_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.auguest_rent_flag == 200:
                    l.append(int(i.auguest_due_amt))

            if i.sept_rent_flag >= 99:
                if i.sept_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.sept_advance)
                    c = int(i.sept_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.sept_rent_flag == 200:
                    l.append(int(i.sept_due_amt))

            if i.october_rent_flag >= 99:
                if i.october_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.october_advance)
                    c = int(i.october_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.october_rent_flag == 200:
                    l.append(int(i.october_due_amt))

            if i.nov_rent_flag >= 99:
                if i.nov_rent_flag == 100:
                    a = int(i.monthly_rent)
                    b = int(i.nov_advance)
                    c = int(i.nov_dis_amt)

                    x = a + b - c
                    l.append(x)
                elif i.nov_rent_flag == 200:
                    l.append(int(i.nov_due_amt))

        ll = []
        for i in l:
            if i != '':
                ll.append(int(i))
        print('my lll', l)

        return sum(ll)


    def vcated_guest(self):
        rno = pg1_new_guest.objects.all().filter(guest_code=self.guest_code,flag=3)
        lr = []
        for i in rno:
            lr.append(str(i.guest_code))
        gc = ''.join(lr)
        print('lllrr', lr)

        from datetime import datetime
        cmm = datetime.now().month
        cm = cmm

        l = []


        for i in rno:

            if i.jan_rent_flag >= 99:
                a= int(i.guest_vacate_month)
                ml=[]
                ml.append(a)
                if 1 <= ml[0]:
                    if i.jan_rent_flag == 100:
                        a = int(i.monthly_rent)
                        b = int(i.jan_advance)
                        c = int(i.jan_dis_amt)

                        x = a + b - c
                        l.append(x)
                    elif i.jan_rent_flag == 200:
                        l.append(int(i.jan_due_amt))

            if i.feb_rent_flag >= 99:
                a= int(i.guest_vacate_month)
                ml=[]
                ml.append(a)
                if 2 <= ml[0]:
                    if i.feb_rent_flag == 100:
                        a = int(i.monthly_rent)
                        b = int(i.feb_advance)
                        c = int(i.feb_dis_amt)

                        x = a + b - c
                        l.append(x)
                    elif i.feb_rent_flag == 200:
                        l.append(int(i.feb_due_amt))

            if i.march_rent_flag >= 99:
                a= int(i.guest_vacate_month)
                ml=[]
                ml.append(a)
                if 3 <= ml[0]:
                    if i.march_rent_flag == 100:
                        a = int(i.monthly_rent)
                        b = int(i.march_advance)
                        c = int(i.march_dis_amt)

                        x = a + b - c
                        l.append(x)
                    elif i.march_rent_flag == 200:
                        l.append(int(i.march_due_amt))

            if i.april_rent_flag >= 99:
                a= int(i.guest_vacate_month)
                ml=[]
                ml.append(a)
                if 4 <= ml[0]:
                    if i.april_rent_flag == 100:
                        a = int(i.monthly_rent)
                        b = int(i.april_advance)
                        c = int(i.april_dis_amt)

                        x = a + b - c
                        l.append(x)
                    elif i.april_rent_flag == 200:
                        l.append(int(i.april_due_amt))

            if i.may_rent_flag >= 99:
                a= int(i.guest_vacate_month)
                ml=[]
                ml.append(a)
                if 5 <= ml[0]:
                    if i.may_rent_flag == 100:
                        a = int(i.monthly_rent)
                        b = int(i.may_advance)
                        c = int(i.may_dis_amt)

                        x = a + b - c
                        l.append(x)
                    elif i.may_rent_flag == 200:
                        l.append(int(i.may_due_amt))

            if i.june_rent_flag >= 99:
                a= int(i.guest_vacate_month)
                ml=[]
                ml.append(a)
                if 6 <= ml[0]:
                    if i.june_rent_flag == 100:
                        a = int(i.monthly_rent)
                        b = int(i.june_advance)
                        c = int(i.june_dis_amt)

                        x = a + b - c
                        l.append(x)
                    elif i.june_rent_flag == 200:
                        l.append(int(i.june_due_amt))

            if i.july_rent_flag >= 99:
                a= int(i.guest_vacate_month)
                ml=[]
                ml.append(a)
                if 7 <= ml[0]:
                    if i.july_rent_flag == 100:
                        a = int(i.monthly_rent)
                        b = int(i.july_advance)
                        c = int(i.july_dis_amt)

                        x = a + b - c
                        l.append(x)
                    elif i.july_rent_flag == 200:
                        l.append(int(i.july_due_amt))

            if i.auguest_rent_flag >= 99:
                a= int(i.guest_vacate_month)
                ml=[]
                ml.append(a)
                if 8 <= ml[0]:
                    if i.auguest_rent_flag == 100:
                        a = int(i.monthly_rent)
                        b = int(i.auguest_advance)
                        c = int(i.auguest_dis_amt)

                        x = a + b - c
                        l.append(x)
                    elif i.auguest_rent_flag == 200:
                        l.append(int(i.auguest_due_amt))

            if i.sept_rent_flag >= 99:
                a= int(i.guest_vacate_month)
                ml=[]
                ml.append(a)
                if 9 <= ml[0]:
                    if i.sept_rent_flag == 100:
                        a = int(i.monthly_rent)
                        b = int(i.sept_advance)
                        c = int(i.sept_dis_amt)

                        x = a + b - c
                        l.append(x)
                    elif i.sept_rent_flag == 200:
                        l.append(int(i.sept_due_amt))

            if i.october_rent_flag >= 99:
                a= int(i.guest_vacate_month)
                ml=[]
                ml.append(a)
                if 10 <= ml[0]:
                    if i.october_rent_flag == 100:
                        a = int(i.monthly_rent)
                        b = int(i.october_advance)
                        c = int(i.october_dis_amt)

                        x = a + b - c
                        l.append(x)
                    elif i.october_rent_flag == 200:
                        l.append(int(i.october_due_amt))

            if i.nov_rent_flag >= 99:
                a= int(i.guest_vacate_month)
                ml=[]
                ml.append(a)
                if 11 <= ml[0]:
                    if i.nov_rent_flag == 100:
                        a = int(i.monthly_rent)
                        b = int(i.nov_advance)
                        c = int(i.nov_dis_amt)

                        x = a + b - c
                        l.append(x)
                    elif i.nov_rent_flag == 200:
                        l.append(int(i.nov_due_amt))

            if i.dec_rent_flag >= 99:
                a= int(i.guest_vacate_month)
                ml=[]
                ml.append(a)
                if 12 <= ml[0]:
                    if i.dec_rent_flag == 100:
                        a = int(i.monthly_rent)
                        b = int(i.dec_advance)
                        c = int(i.dec_dis_amt)

                        x = a + b - c
                        l.append(x)
                    elif i.dec_rent_flag == 200:
                        l.append(int(i.dec_due_amt))


        ll = []
        for i in l:
            if i != '':
                ll.append(int(i))
        print('my lll', l)

        return sum(ll)






class branch_closing(models.Model):
    branch_name = models.CharField(max_length=200)

    jan = models.CharField(max_length=200)
    feb = models.CharField(max_length=200)
    mar = models.CharField(max_length=200)
    apr = models.CharField(max_length=200)
    may = models.CharField(max_length=200)
    jun = models.CharField(max_length=200)

    jul = models.CharField(max_length=200)
    aug = models.CharField(max_length=200)
    sep = models.CharField(max_length=200)
    oct = models.CharField(max_length=200)
    nov = models.CharField(max_length=200)
    dec = models.CharField(max_length=200)

    flag = models.CharField(max_length=200)

class background_color(models.Model):
    theme_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    flag = models.CharField(max_length=200)
