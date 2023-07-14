#admin_dashboard_calculations_br5
import lib2to3.pgen2.token
import locale

from django.shortcuts import render
from django.contrib import messages
import branch9app

def total_count_active_guests():
    tvr = branch9app.models.pg1_new_beds.objects.all().filter(flag=2)
    l=[]
    for i in tvr:
        l.append(i.roon_no)
    print('total_count_active_guests',l)
    return len(l)

def total_count_vaccant_rooms():
    tvr = branch9app.models.pg1_new_beds.objects.all().exclude(flag=2).order_by('roon_no')
    l=[]
    for i in tvr:
        l.append(i.roon_no)
    print('total_count_vaccant_rooms',l)
    return len(l)

def grand_total_collection():
    jan_tc=[]
    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2,jan_rent_flag__gt=99)
    for i in total_guest_br5:
        if i.monthly_rent !='':
            jan_tc.append(int(i.monthly_rent))

    feb_tc=[]
    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2,feb_rent_flag__gt=99)
    for i in total_guest_br5:
        if i.monthly_rent !='':
            feb_tc.append(int(i.monthly_rent))

    mar_tc=[]
    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2,march_rent_flag__gt=99)
    for i in total_guest_br5:
        if i.monthly_rent !='':
            mar_tc.append(int(i.monthly_rent))

    apr_tc=[]
    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2,april_rent_flag__gt=99)
    for i in total_guest_br5:
        if i.monthly_rent !='':
            apr_tc.append(int(i.monthly_rent))

    may_tc=[]
    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2,may_rent_flag__gt=99)
    for i in total_guest_br5:
        if i.monthly_rent !='':
            may_tc.append(int(i.monthly_rent))

    jun_tc=[]
    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2,june_rent_flag__gt=99)
    for i in total_guest_br5:
        if i.monthly_rent !='':
            jun_tc.append(int(i.monthly_rent))

    jul_tc=[]
    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2,july_rent_flag__gt=99)
    for i in total_guest_br5:
        if i.monthly_rent !='':
            jul_tc.append(int(i.monthly_rent))

    aug_tc=[]
    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2,auguest_rent_flag__gt=99)
    for i in total_guest_br5:
        if i.monthly_rent !='':
            aug_tc.append(int(i.monthly_rent))

    sep_tc=[]
    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2,sept_rent_flag__gt=99)
    for i in total_guest_br5:
        if i.monthly_rent !='':
            sep_tc.append(int(i.monthly_rent))

    oct_tc=[]
    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2,october_rent_flag__gt=99)
    for i in total_guest_br5:
        if i.monthly_rent !='':
            oct_tc.append(int(i.monthly_rent))

    nov_tc=[]
    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2,nov_rent_flag__gt=99)
    for i in total_guest_br5:
        if i.monthly_rent !='':
            nov_tc.append(int(i.monthly_rent))

    dec_tc=[]
    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2,dec_rent_flag__gt=99)
    for i in total_guest_br5:
        if i.monthly_rent !='':
            dec_tc.append(int(i.monthly_rent))

    l=[]
    l.append(sum(jan_tc))
    l.append(sum(feb_tc))
    l.append(sum(mar_tc))
    l.append(sum(apr_tc))
    l.append(sum(may_tc))
    l.append(sum(jun_tc))
    l.append(sum(jul_tc))
    l.append(sum(aug_tc))
    l.append(sum(sep_tc))
    l.append(sum(oct_tc))
    l.append(sum(nov_tc))
    l.append(sum(dec_tc))

    t=l
    return t

def grand_total():
    jul_tc=[]
    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2,july_rent_flag__gt=99)
    for i in total_guest_br5:
        if i.monthly_rent !='':
            jul_tc.append(int(i.monthly_rent))
    return jul_tc


def total_collection_advance():
    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2)
    jan_advance = []
    for i in total_guest_br5:
        if i.jan_advance != '':
            jan_advance.append(int(i.jan_advance))

    feb_advance = []
    for i in total_guest_br5:
        if i.feb_advance != '':
            feb_advance.append(int(i.feb_advance))

    mar_advance = []
    for i in total_guest_br5:
        if i.march_advance != '':
            mar_advance.append(int(i.march_advance))

    apr_advance = []
    for i in total_guest_br5:
        if i.april_advance != '':
            apr_advance.append(int(i.april_advance))

    may_advance = []
    for i in total_guest_br5:
        if i.may_advance != '':
            may_advance.append(int(i.may_advance))

    jun_advance = []
    for i in total_guest_br5:
        if i.june_advance != '':
            jun_advance.append(int(i.june_advance))

    jul_advance = []
    for i in total_guest_br5:
        if i.july_advance != '':
            jul_advance.append(int(i.july_advance))

    aug_advance = []
    for i in total_guest_br5:
        if i.auguest_advance != '':
            aug_advance.append(int(i.auguest_advance))

    sep_advance = []
    for i in total_guest_br5:
        if i.sept_advance != '':
            sep_advance.append(int(i.sept_advance))

    oct_advance = []
    for i in total_guest_br5:
        if i.october_advance != '':
            oct_advance.append(int(i.october_advance))

    nov_advance = []
    for i in total_guest_br5:
        if i.nov_advance != '':
            nov_advance.append(int(i.nov_advance))

    dec_advance = []
    for i in total_guest_br5:
        if i.dec_advance != '':
            dec_advance.append(int(i.dec_advance))

    total_advance_amt = []

    total_advance_amt.append(jan_advance)
    total_advance_amt.append(feb_advance)
    total_advance_amt.append(mar_advance)
    total_advance_amt.append(apr_advance)
    total_advance_amt.append(may_advance)
    total_advance_amt.append(jun_advance)
    total_advance_amt.append(jul_advance)
    total_advance_amt.append(aug_advance)
    total_advance_amt.append(sep_advance)
    total_advance_amt.append(oct_advance)
    total_advance_amt.append(nov_advance)
    total_advance_amt.append(dec_advance)

    from datetime import datetime
    cmm = datetime.now().month
    cm=cmm-1

    tam=total_advance_amt[cm]
    ta=sum(tam)

    total_collection_amt = ta
    return total_collection_amt


def total_discount():
    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2)
    jan_dis_amt = []
    for i in total_guest_br5:
        if i.jan_dis_amt != '':
            jan_dis_amt.append(int(i.jan_dis_amt))

    feb_dis_amt = []
    for i in total_guest_br5:
        if i.feb_dis_amt != '':
            feb_dis_amt.append(int(i.feb_dis_amt))

    mar_dis_amt = []
    for i in total_guest_br5:
        if i.march_dis_amt != '':
            mar_dis_amt.append(int(i.march_dis_amt))

    apr_dis_amt = []
    for i in total_guest_br5:
        if i.april_dis_amt != '':
            apr_dis_amt.append(int(i.april_dis_amt))

    may_dis_amt = []
    for i in total_guest_br5:
        if i.may_dis_amt != '':
            may_dis_amt.append(int(i.may_dis_amt))

    jun_dis_amt = []
    for i in total_guest_br5:
        if i.june_dis_amt != '':
            jun_dis_amt.append(int(i.june_dis_amt))

    jul_dis_amt = []
    for i in total_guest_br5:
        if i.july_dis_amt != '':
            jul_dis_amt.append(int(i.july_dis_amt))

    aug_dis_amt = []
    for i in total_guest_br5:
        if i.auguest_dis_amt != '':
            aug_dis_amt.append(int(i.auguest_dis_amt))

    sep_dis_amt = []
    for i in total_guest_br5:
        if i.sept_dis_amt != '':
            sep_dis_amt.append(int(i.sept_dis_amt))

    oct_dis_amt = []
    for i in total_guest_br5:
        if i.october_dis_amt != '':
            oct_dis_amt.append(int(i.october_dis_amt))

    nov_dis_amt = []
    for i in total_guest_br5:
        if i.nov_dis_amt != '':
            nov_dis_amt.append(int(i.nov_dis_amt))

    dec_dis_amt = []
    for i in total_guest_br5:
        if i.dec_dis_amt != '':
            dec_dis_amt.append(int(i.dec_dis_amt))

    total_due_amount = []

    total_due_amount.append(jan_dis_amt)
    total_due_amount.append(feb_dis_amt)
    total_due_amount.append(mar_dis_amt)
    total_due_amount.append(apr_dis_amt)
    total_due_amount.append(may_dis_amt)
    total_due_amount.append(jun_dis_amt)
    total_due_amount.append(jul_dis_amt)
    total_due_amount.append(aug_dis_amt)
    total_due_amount.append(sep_dis_amt)
    total_due_amount.append(oct_dis_amt)
    total_due_amount.append(nov_dis_amt)
    total_due_amount.append(dec_dis_amt)

    from datetime import datetime
    cmm = datetime.now().month
    cm=cmm-1
    tam=total_due_amount[cm]
    total_due=(sum(tam))
    return total_due

def total_colatable_amount():
    x=grand_total_collection()
    from datetime import datetime
    cmm = datetime.now().month
    cm=cmm-1
    a=x[cm]
    b=total_collection_advance()
    c=total_discount()
    ans=a+b-c
    return ans


def total_collected_amount():
    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2)
    jan_rent = []
    for i in total_guest_br5:
        if i.jan_rent != '':
            jan_rent.append(int(i.jan_rent))

    feb_rent = []
    for i in total_guest_br5:
        if i.feb_rent != '':
            feb_rent.append(int(i.feb_rent))

    mar_rent = []
    for i in total_guest_br5:
        if i.march_rent != '':
            mar_rent.append(int(i.march_rent))

    apr_rent = []
    for i in total_guest_br5:
        if i.april_rent != '':
            apr_rent.append(int(i.april_rent))

    may_rent = []
    for i in total_guest_br5:
        if i.may_rent != '':
            may_rent.append(int(i.may_rent))

    jun_rent = []
    for i in total_guest_br5:
        if i.june_rent != '':
            jun_rent.append(int(i.june_rent))

    jul_rent = []
    for i in total_guest_br5:
        if i.july_rent != '':
            jul_rent.append(int(i.july_rent))

    aug_rent = []
    for i in total_guest_br5:
        if i.auguest_rent != '':
            aug_rent.append(int(i.auguest_rent))

    sep_rent = []
    for i in total_guest_br5:
        if i.sept_rent != '':
            sep_rent.append(int(i.sept_rent))

    oct_rent = []
    for i in total_guest_br5:
        if i.october_rent != '':
            oct_rent.append(int(i.october_rent))

    nov_rent = []
    for i in total_guest_br5:
        if i.nov_rent != '':
            nov_rent.append(int(i.nov_rent))

    dec_rent = []
    for i in total_guest_br5:
        if i.dec_rent != '':
            dec_rent.append(int(i.dec_rent))

    total_collection_monthly = []

    total_collection_monthly.append(jan_rent)
    total_collection_monthly.append(feb_rent)
    total_collection_monthly.append(mar_rent)
    total_collection_monthly.append(apr_rent)
    total_collection_monthly.append(may_rent)
    total_collection_monthly.append(jun_rent)
    total_collection_monthly.append(jul_rent)
    total_collection_monthly.append(aug_rent)
    total_collection_monthly.append(sep_rent)
    total_collection_monthly.append(oct_rent)
    total_collection_monthly.append(nov_rent)
    total_collection_monthly.append(dec_rent)

    from datetime import datetime
    cmm = datetime.now().month
    cm=cmm-1
    tam=total_collection_monthly[cm]
    monthly_rent=(sum(tam))
    return monthly_rent

def total_due():
    a=total_colatable_amount()
    b=total_collected_amount()
    c=a-b
    return c


def bar_chart():
    l=[]
    #l.append(total_collection_june())
    #l.append(total_received_june())
    #l.append(total_due_june())
    #l.append(total_collection_discount_june())
    return l







def monthly_details_due9(request):
    jan_tc = []
    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2, jan_rent_flag__gt=99)
    for i in total_guest_br5:
        if i.monthly_rent != '':
            jan_tc.append(int(i.monthly_rent))

    feb_tc = []
    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2, feb_rent_flag__gt=99)
    for i in total_guest_br5:
        if i.monthly_rent != '':
            feb_tc.append(int(i.monthly_rent))

    mar_tc = []
    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2, march_rent_flag__gt=99)
    for i in total_guest_br5:
        if i.monthly_rent != '':
            mar_tc.append(int(i.monthly_rent))

    apr_tc = []
    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2, april_rent_flag__gt=99)
    for i in total_guest_br5:
        if i.monthly_rent != '':
            apr_tc.append(int(i.monthly_rent))

    may_tc = []
    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2, may_rent_flag__gt=99)
    for i in total_guest_br5:
        if i.monthly_rent != '':
            may_tc.append(int(i.monthly_rent))

    jun_tc = []
    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2, june_rent_flag__gt=99)
    for i in total_guest_br5:
        if i.monthly_rent != '':
            jun_tc.append(int(i.monthly_rent))

    jul_tc = []
    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2, july_rent_flag__gt=99)
    for i in total_guest_br5:
        if i.monthly_rent != '':
            jul_tc.append(int(i.monthly_rent))

    aug_tc = []
    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2, auguest_rent_flag__gt=99)
    for i in total_guest_br5:
        if i.monthly_rent != '':
            aug_tc.append(int(i.monthly_rent))

    sep_tc = []
    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2, sept_rent_flag__gt=99)
    for i in total_guest_br5:
        if i.monthly_rent != '':
            sep_tc.append(int(i.monthly_rent))

    oct_tc = []
    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2, october_rent_flag__gt=99)
    for i in total_guest_br5:
        if i.monthly_rent != '':
            oct_tc.append(int(i.monthly_rent))

    nov_tc = []
    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2, nov_rent_flag__gt=99)
    for i in total_guest_br5:
        if i.monthly_rent != '':
            nov_tc.append(int(i.monthly_rent))

    dec_tc = []
    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2, dec_rent_flag__gt=99)
    for i in total_guest_br5:
        if i.monthly_rent != '':
            dec_tc.append(int(i.monthly_rent))

    l=[]
    l.append(sum(jan_tc))
    l.append(sum(feb_tc))
    l.append(sum(mar_tc))
    l.append(sum(apr_tc))
    l.append(sum(may_tc))
    l.append(sum(jun_tc))
    l.append(sum(jul_tc))
    l.append(sum(aug_tc))
    l.append(sum(sep_tc))
    l.append(sum(oct_tc))
    l.append(sum(nov_tc))
    l.append(sum(dec_tc))

    t = l

    #advance start here

    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2)

    jan_advance = []
    for i in total_guest_br5:
        if i.jan_advance != '':
            jan_advance.append(int(i.jan_advance))

    feb_advance = []
    for i in total_guest_br5:
        if i.feb_advance != '':
            feb_advance.append(int(i.feb_advance))

    mar_advance = []
    for i in total_guest_br5:
        if i.march_advance != '':
            mar_advance.append(int(i.march_advance))

    apr_advance = []
    for i in total_guest_br5:
        if i.april_advance != '':
            apr_advance.append(int(i.april_advance))

    may_advance = []
    for i in total_guest_br5:
        if i.may_advance != '':
            may_advance.append(int(i.may_advance))

    jun_advance = []
    for i in total_guest_br5:
        if i.june_advance != '':
            jun_advance.append(int(i.june_advance))

    jul_advance = []
    for i in total_guest_br5:
        if i.july_advance != '':
            jul_advance.append(int(i.july_advance))

    aug_advance = []
    for i in total_guest_br5:
        if i.auguest_advance != '':
            aug_advance.append(int(i.auguest_advance))

    sep_advance = []
    for i in total_guest_br5:
        if i.sept_advance != '':
            sep_advance.append(int(i.sept_advance))

    oct_advance = []
    for i in total_guest_br5:
        if i.october_advance != '':
            oct_advance.append(int(i.october_advance))

    nov_advance = []
    for i in total_guest_br5:
        if i.nov_advance != '':
            nov_advance.append(int(i.nov_advance))

    dec_advance = []
    for i in total_guest_br5:
        if i.dec_advance != '':
            dec_advance.append(int(i.dec_advance))

    total_advance_amt = []

    total_advance_amt.append(sum(jan_advance))
    total_advance_amt.append(sum(feb_advance))
    total_advance_amt.append(sum(mar_advance))
    total_advance_amt.append(sum(apr_advance))
    total_advance_amt.append(sum(may_advance))
    total_advance_amt.append(sum(jun_advance))
    total_advance_amt.append(sum(jul_advance))
    total_advance_amt.append(sum(aug_advance))
    total_advance_amt.append(sum(sep_advance))
    total_advance_amt.append(sum(oct_advance))
    total_advance_amt.append(sum(nov_advance))
    total_advance_amt.append(sum(dec_advance))

    #advance end here
    #discount start here

    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2)
    jan_dis_amt = []
    for i in total_guest_br5:
        if i.jan_dis_amt != '':
            jan_dis_amt.append(int(i.jan_dis_amt))

    feb_dis_amt = []
    for i in total_guest_br5:
        if i.feb_dis_amt != '':
            feb_dis_amt.append(int(i.feb_dis_amt))

    mar_dis_amt = []
    for i in total_guest_br5:
        if i.march_dis_amt != '':
            mar_dis_amt.append(int(i.march_dis_amt))

    apr_dis_amt = []
    for i in total_guest_br5:
        if i.april_dis_amt != '':
            apr_dis_amt.append(int(i.april_dis_amt))

    may_dis_amt = []
    for i in total_guest_br5:
        if i.may_dis_amt != '':
            may_dis_amt.append(int(i.may_dis_amt))

    jun_dis_amt = []
    for i in total_guest_br5:
        if i.june_dis_amt != '':
            jun_dis_amt.append(int(i.june_dis_amt))

    jul_dis_amt = []
    for i in total_guest_br5:
        if i.july_dis_amt != '':
            jul_dis_amt.append(int(i.july_dis_amt))

    aug_dis_amt = []
    for i in total_guest_br5:
        if i.auguest_dis_amt != '':
            aug_dis_amt.append(int(i.auguest_dis_amt))

    sep_dis_amt = []
    for i in total_guest_br5:
        if i.sept_dis_amt != '':
            sep_dis_amt.append(int(i.sept_dis_amt))

    oct_dis_amt = []
    for i in total_guest_br5:
        if i.october_dis_amt != '':
            oct_dis_amt.append(int(i.october_dis_amt))

    nov_dis_amt = []
    for i in total_guest_br5:
        if i.nov_dis_amt != '':
            nov_dis_amt.append(int(i.nov_dis_amt))

    dec_dis_amt = []
    for i in total_guest_br5:
        if i.dec_dis_amt != '':
            dec_dis_amt.append(int(i.dec_dis_amt))

    total_dis_amount = []

    total_dis_amount.append(sum(jan_dis_amt))
    total_dis_amount.append(sum(feb_dis_amt))
    total_dis_amount.append(sum(mar_dis_amt))
    total_dis_amount.append(sum(apr_dis_amt))
    total_dis_amount.append(sum(may_dis_amt))
    total_dis_amount.append(sum(jun_dis_amt))
    total_dis_amount.append(sum(jul_dis_amt))
    total_dis_amount.append(sum(aug_dis_amt))
    total_dis_amount.append(sum(sep_dis_amt))
    total_dis_amount.append(sum(oct_dis_amt))
    total_dis_amount.append(sum(nov_dis_amt))
    total_dis_amount.append(sum(dec_dis_amt))

    #discount end here

    #total collected amount start here

    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2)
    jan_rent = []
    for i in total_guest_br5:
        if i.jan_rent != '':
            jan_rent.append(int(i.jan_rent))

    feb_rent = []
    for i in total_guest_br5:
        if i.feb_rent != '':
            feb_rent.append(int(i.feb_rent))

    mar_rent = []
    for i in total_guest_br5:
        if i.march_rent != '':
            mar_rent.append(int(i.march_rent))

    apr_rent = []
    for i in total_guest_br5:
        if i.april_rent != '':
            apr_rent.append(int(i.april_rent))

    may_rent = []
    for i in total_guest_br5:
        if i.may_rent != '':
            may_rent.append(int(i.may_rent))

    jun_rent = []
    for i in total_guest_br5:
        if i.june_rent != '':
            jun_rent.append(int(i.june_rent))

    jul_rent = []
    for i in total_guest_br5:
        if i.july_rent != '':
            jul_rent.append(int(i.july_rent))

    aug_rent = []
    for i in total_guest_br5:
        if i.auguest_rent != '':
            aug_rent.append(int(i.auguest_rent))

    sep_rent = []
    for i in total_guest_br5:
        if i.sept_rent != '':
            sep_rent.append(int(i.sept_rent))

    oct_rent = []
    for i in total_guest_br5:
        if i.october_rent != '':
            oct_rent.append(int(i.october_rent))

    nov_rent = []
    for i in total_guest_br5:
        if i.nov_rent != '':
            nov_rent.append(int(i.nov_rent))

    dec_rent = []
    for i in total_guest_br5:
        if i.dec_rent != '':
            dec_rent.append(int(i.dec_rent))

    total_collection_monthly = []

    total_collection_monthly.append(sum(jan_rent))
    total_collection_monthly.append(sum(feb_rent))
    total_collection_monthly.append(sum(mar_rent))
    total_collection_monthly.append(sum(apr_rent))
    total_collection_monthly.append(sum(may_rent))
    total_collection_monthly.append(sum(jun_rent))
    total_collection_monthly.append(sum(jul_rent))
    total_collection_monthly.append(sum(aug_rent))
    total_collection_monthly.append(sum(sep_rent))
    total_collection_monthly.append(sum(oct_rent))
    total_collection_monthly.append(sum(nov_rent))
    total_collection_monthly.append(sum(dec_rent))

    #total collected amount end here
    #total collatable amount start here

    total_collatable_amount=[]

    total_collatable_amount.append(t[0]+total_advance_amt[0]-total_dis_amount[0])
    total_collatable_amount.append(t[1]+total_advance_amt[1]-total_dis_amount[1])
    total_collatable_amount.append(t[2]+total_advance_amt[2]-total_dis_amount[2])
    total_collatable_amount.append(t[3]+total_advance_amt[3]-total_dis_amount[3])
    total_collatable_amount.append(t[4]+total_advance_amt[4]-total_dis_amount[4])
    total_collatable_amount.append(t[5]+total_advance_amt[5]-total_dis_amount[5])
    total_collatable_amount.append(t[6]+total_advance_amt[6]-total_dis_amount[6])
    total_collatable_amount.append(t[7]+total_advance_amt[7]-total_dis_amount[7])
    total_collatable_amount.append(t[8]+total_advance_amt[8]-total_dis_amount[8])
    total_collatable_amount.append(t[9]+total_advance_amt[9]-total_dis_amount[9])
    total_collatable_amount.append(t[10]+total_advance_amt[10]-total_dis_amount[10])
    total_collatable_amount.append(t[11]+total_advance_amt[11]-total_dis_amount[11])

    #total collatable amount end here
    #total due amount start here

    total_due_amt=[]

    total_due_amt.append(total_collatable_amount[0]-total_collection_monthly[0])
    total_due_amt.append(total_collatable_amount[1]-total_collection_monthly[1])
    total_due_amt.append(total_collatable_amount[2]-total_collection_monthly[2])
    total_due_amt.append(total_collatable_amount[3]-total_collection_monthly[3])
    total_due_amt.append(total_collatable_amount[4]-total_collection_monthly[4])
    total_due_amt.append(total_collatable_amount[5]-total_collection_monthly[5])
    total_due_amt.append(total_collatable_amount[6]-total_collection_monthly[6])
    total_due_amt.append(total_collatable_amount[7]-total_collection_monthly[7])
    total_due_amt.append(total_collatable_amount[8]-total_collection_monthly[8])
    total_due_amt.append(total_collatable_amount[9]-total_collection_monthly[9])
    total_due_amt.append(total_collatable_amount[10]-total_collection_monthly[10])
    total_due_amt.append(total_collatable_amount[11]-total_collection_monthly[11])

    #total due amount end here


    context={
        'grand_total_collection':t,
        'total_advance_amt':total_advance_amt,
        'total_dis_amount':total_dis_amount,
        'total_collection_monthly':total_collection_monthly,
        'total_collatable_amount':total_collatable_amount,
        'total_due_amt':total_due_amt,
    }

    return render(request,'branches/branch9/reports/dashboard_reports/due_amount/monthly_details.html',context)

def monthly_collection_details9(request):
    jan_tc = []
    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2, jan_rent_flag__gt=99)
    for i in total_guest_br5:
        if i.monthly_rent != '':
            jan_tc.append(int(i.monthly_rent))

    feb_tc = []
    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2, feb_rent_flag__gt=99)
    for i in total_guest_br5:
        if i.monthly_rent != '':
            feb_tc.append(int(i.monthly_rent))

    mar_tc = []
    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2, march_rent_flag__gt=99)
    for i in total_guest_br5:
        if i.monthly_rent != '':
            mar_tc.append(int(i.monthly_rent))

    apr_tc = []
    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2, april_rent_flag__gt=99)
    for i in total_guest_br5:
        if i.monthly_rent != '':
            apr_tc.append(int(i.monthly_rent))

    may_tc = []
    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2, may_rent_flag__gt=99)
    for i in total_guest_br5:
        if i.monthly_rent != '':
            may_tc.append(int(i.monthly_rent))

    jun_tc = []
    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2, june_rent_flag__gt=99)
    for i in total_guest_br5:
        if i.monthly_rent != '':
            jun_tc.append(int(i.monthly_rent))

    jul_tc = []
    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2, july_rent_flag__gt=99)
    for i in total_guest_br5:
        if i.monthly_rent != '':
            jul_tc.append(int(i.monthly_rent))

    aug_tc = []
    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2, auguest_rent_flag__gt=99)
    for i in total_guest_br5:
        if i.monthly_rent != '':
            aug_tc.append(int(i.monthly_rent))

    sep_tc = []
    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2, sept_rent_flag__gt=99)
    for i in total_guest_br5:
        if i.monthly_rent != '':
            sep_tc.append(int(i.monthly_rent))

    oct_tc = []
    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2, october_rent_flag__gt=99)
    for i in total_guest_br5:
        if i.monthly_rent != '':
            oct_tc.append(int(i.monthly_rent))

    nov_tc = []
    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2, nov_rent_flag__gt=99)
    for i in total_guest_br5:
        if i.monthly_rent != '':
            nov_tc.append(int(i.monthly_rent))

    dec_tc = []
    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2, dec_rent_flag__gt=99)
    for i in total_guest_br5:
        if i.monthly_rent != '':
            dec_tc.append(int(i.monthly_rent))

    l=[]
    l.append(sum(jan_tc))
    l.append(sum(feb_tc))
    l.append(sum(mar_tc))
    l.append(sum(apr_tc))
    l.append(sum(may_tc))
    l.append(sum(jun_tc))
    l.append(sum(jul_tc))
    l.append(sum(aug_tc))
    l.append(sum(sep_tc))
    l.append(sum(oct_tc))
    l.append(sum(nov_tc))
    l.append(sum(dec_tc))

    t = l

    #advance start here

    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2)

    jan_advance = []
    for i in total_guest_br5:
        if i.jan_advance != '':
            jan_advance.append(int(i.jan_advance))

    feb_advance = []
    for i in total_guest_br5:
        if i.feb_advance != '':
            feb_advance.append(int(i.feb_advance))

    mar_advance = []
    for i in total_guest_br5:
        if i.march_advance != '':
            mar_advance.append(int(i.march_advance))

    apr_advance = []
    for i in total_guest_br5:
        if i.april_advance != '':
            apr_advance.append(int(i.april_advance))

    may_advance = []
    for i in total_guest_br5:
        if i.may_advance != '':
            may_advance.append(int(i.may_advance))

    jun_advance = []
    for i in total_guest_br5:
        if i.june_advance != '':
            jun_advance.append(int(i.june_advance))

    jul_advance = []
    for i in total_guest_br5:
        if i.july_advance != '':
            jul_advance.append(int(i.july_advance))

    aug_advance = []
    for i in total_guest_br5:
        if i.auguest_advance != '':
            aug_advance.append(int(i.auguest_advance))

    sep_advance = []
    for i in total_guest_br5:
        if i.sept_advance != '':
            sep_advance.append(int(i.sept_advance))

    oct_advance = []
    for i in total_guest_br5:
        if i.october_advance != '':
            oct_advance.append(int(i.october_advance))

    nov_advance = []
    for i in total_guest_br5:
        if i.nov_advance != '':
            nov_advance.append(int(i.nov_advance))

    dec_advance = []
    for i in total_guest_br5:
        if i.dec_advance != '':
            dec_advance.append(int(i.dec_advance))

    total_advance_amt = []

    total_advance_amt.append(sum(jan_advance))
    total_advance_amt.append(sum(feb_advance))
    total_advance_amt.append(sum(mar_advance))
    total_advance_amt.append(sum(apr_advance))
    total_advance_amt.append(sum(may_advance))
    total_advance_amt.append(sum(jun_advance))
    total_advance_amt.append(sum(jul_advance))
    total_advance_amt.append(sum(aug_advance))
    total_advance_amt.append(sum(sep_advance))
    total_advance_amt.append(sum(oct_advance))
    total_advance_amt.append(sum(nov_advance))
    total_advance_amt.append(sum(dec_advance))

    #advance end here
    #discount start here

    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2)
    jan_dis_amt = []
    for i in total_guest_br5:
        if i.jan_dis_amt != '':
            jan_dis_amt.append(int(i.jan_dis_amt))

    feb_dis_amt = []
    for i in total_guest_br5:
        if i.feb_dis_amt != '':
            feb_dis_amt.append(int(i.feb_dis_amt))

    mar_dis_amt = []
    for i in total_guest_br5:
        if i.march_dis_amt != '':
            mar_dis_amt.append(int(i.march_dis_amt))

    apr_dis_amt = []
    for i in total_guest_br5:
        if i.april_dis_amt != '':
            apr_dis_amt.append(int(i.april_dis_amt))

    may_dis_amt = []
    for i in total_guest_br5:
        if i.may_dis_amt != '':
            may_dis_amt.append(int(i.may_dis_amt))

    jun_dis_amt = []
    for i in total_guest_br5:
        if i.june_dis_amt != '':
            jun_dis_amt.append(int(i.june_dis_amt))

    jul_dis_amt = []
    for i in total_guest_br5:
        if i.july_dis_amt != '':
            jul_dis_amt.append(int(i.july_dis_amt))

    aug_dis_amt = []
    for i in total_guest_br5:
        if i.auguest_dis_amt != '':
            aug_dis_amt.append(int(i.auguest_dis_amt))

    sep_dis_amt = []
    for i in total_guest_br5:
        if i.sept_dis_amt != '':
            sep_dis_amt.append(int(i.sept_dis_amt))

    oct_dis_amt = []
    for i in total_guest_br5:
        if i.october_dis_amt != '':
            oct_dis_amt.append(int(i.october_dis_amt))

    nov_dis_amt = []
    for i in total_guest_br5:
        if i.nov_dis_amt != '':
            nov_dis_amt.append(int(i.nov_dis_amt))

    dec_dis_amt = []
    for i in total_guest_br5:
        if i.dec_dis_amt != '':
            dec_dis_amt.append(int(i.dec_dis_amt))

    total_dis_amount = []

    total_dis_amount.append(sum(jan_dis_amt))
    total_dis_amount.append(sum(feb_dis_amt))
    total_dis_amount.append(sum(mar_dis_amt))
    total_dis_amount.append(sum(apr_dis_amt))
    total_dis_amount.append(sum(may_dis_amt))
    total_dis_amount.append(sum(jun_dis_amt))
    total_dis_amount.append(sum(jul_dis_amt))
    total_dis_amount.append(sum(aug_dis_amt))
    total_dis_amount.append(sum(sep_dis_amt))
    total_dis_amount.append(sum(oct_dis_amt))
    total_dis_amount.append(sum(nov_dis_amt))
    total_dis_amount.append(sum(dec_dis_amt))

    #discount end here

    #total collected amount start here

    total_guest_br5 = branch9app.models.pg1_new_guest.objects.all().filter(flag=2)
    jan_rent = []
    for i in total_guest_br5:
        if i.jan_rent != '':
            jan_rent.append(int(i.jan_rent))

    feb_rent = []
    for i in total_guest_br5:
        if i.feb_rent != '':
            feb_rent.append(int(i.feb_rent))

    mar_rent = []
    for i in total_guest_br5:
        if i.march_rent != '':
            mar_rent.append(int(i.march_rent))

    apr_rent = []
    for i in total_guest_br5:
        if i.april_rent != '':
            apr_rent.append(int(i.april_rent))

    may_rent = []
    for i in total_guest_br5:
        if i.may_rent != '':
            may_rent.append(int(i.may_rent))

    jun_rent = []
    for i in total_guest_br5:
        if i.june_rent != '':
            jun_rent.append(int(i.june_rent))

    jul_rent = []
    for i in total_guest_br5:
        if i.july_rent != '':
            jul_rent.append(int(i.july_rent))

    aug_rent = []
    for i in total_guest_br5:
        if i.auguest_rent != '':
            aug_rent.append(int(i.auguest_rent))

    sep_rent = []
    for i in total_guest_br5:
        if i.sept_rent != '':
            sep_rent.append(int(i.sept_rent))

    oct_rent = []
    for i in total_guest_br5:
        if i.october_rent != '':
            oct_rent.append(int(i.october_rent))

    nov_rent = []
    for i in total_guest_br5:
        if i.nov_rent != '':
            nov_rent.append(int(i.nov_rent))

    dec_rent = []
    for i in total_guest_br5:
        if i.dec_rent != '':
            dec_rent.append(int(i.dec_rent))

    total_collection_monthly = []

    total_collection_monthly.append(sum(jan_rent))
    total_collection_monthly.append(sum(feb_rent))
    total_collection_monthly.append(sum(mar_rent))
    total_collection_monthly.append(sum(apr_rent))
    total_collection_monthly.append(sum(may_rent))
    total_collection_monthly.append(sum(jun_rent))
    total_collection_monthly.append(sum(jul_rent))
    total_collection_monthly.append(sum(aug_rent))
    total_collection_monthly.append(sum(sep_rent))
    total_collection_monthly.append(sum(oct_rent))
    total_collection_monthly.append(sum(nov_rent))
    total_collection_monthly.append(sum(dec_rent))

    #total collected amount end here
    #total collatable amount start here

    total_collatable_amount=[]

    total_collatable_amount.append(t[0]+total_advance_amt[0]-total_dis_amount[0])
    total_collatable_amount.append(t[1]+total_advance_amt[1]-total_dis_amount[1])
    total_collatable_amount.append(t[2]+total_advance_amt[2]-total_dis_amount[2])
    total_collatable_amount.append(t[3]+total_advance_amt[3]-total_dis_amount[3])
    total_collatable_amount.append(t[4]+total_advance_amt[4]-total_dis_amount[4])
    total_collatable_amount.append(t[5]+total_advance_amt[5]-total_dis_amount[5])
    total_collatable_amount.append(t[6]+total_advance_amt[6]-total_dis_amount[6])
    total_collatable_amount.append(t[7]+total_advance_amt[7]-total_dis_amount[7])
    total_collatable_amount.append(t[8]+total_advance_amt[8]-total_dis_amount[8])
    total_collatable_amount.append(t[9]+total_advance_amt[9]-total_dis_amount[9])
    total_collatable_amount.append(t[10]+total_advance_amt[10]-total_dis_amount[10])
    total_collatable_amount.append(t[11]+total_advance_amt[11]-total_dis_amount[11])

    #total collatable amount end here
    #total due amount start here

    total_due_amt=[]

    total_due_amt.append(total_collatable_amount[0]-total_collection_monthly[0])
    total_due_amt.append(total_collatable_amount[1]-total_collection_monthly[1])
    total_due_amt.append(total_collatable_amount[2]-total_collection_monthly[2])
    total_due_amt.append(total_collatable_amount[3]-total_collection_monthly[3])
    total_due_amt.append(total_collatable_amount[4]-total_collection_monthly[4])
    total_due_amt.append(total_collatable_amount[5]-total_collection_monthly[5])
    total_due_amt.append(total_collatable_amount[6]-total_collection_monthly[6])
    total_due_amt.append(total_collatable_amount[7]-total_collection_monthly[7])
    total_due_amt.append(total_collatable_amount[8]-total_collection_monthly[8])
    total_due_amt.append(total_collatable_amount[9]-total_collection_monthly[9])
    total_due_amt.append(total_collatable_amount[10]-total_collection_monthly[10])
    total_due_amt.append(total_collatable_amount[11]-total_collection_monthly[11])

    #total due amount end here


    context={
        'grand_total_collection':t,
        'total_advance_amt':total_advance_amt,
        'total_dis_amount':total_dis_amount,
        'total_collection_monthly':total_collection_monthly,
        'total_collatable_amount':total_collatable_amount,
        'total_due_amt':total_due_amt,
    }

    return render(request,'branches/branch9/reports/dashboard_reports/due_amount/monthly_collection_details.html',context)


def bar_chart():
    a=total_colatable_amount()
    b=total_collected_amount()
    c=total_due()
    d=total_collection_advance()

    t=[]
    t.append(a)
    t.append(b)
    t.append(c)
    t.append(d)
    return t