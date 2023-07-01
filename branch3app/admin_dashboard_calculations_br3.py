#admin_dashboard_calculations_br3

from django.shortcuts import render
from django.contrib import messages
import branch3app

def total_count_active_guests():
    tvr = branch3app.models.pg1_new_beds.objects.all().filter(flag=2)
    l=[]
    for i in tvr:
        l.append(i.roon_no)
    print('total_count_active_guests',l)
    return len(l)

def total_count_vaccant_rooms():
    tvr = branch3app.models.pg1_new_beds.objects.all().exclude(flag=2).order_by('roon_no')
    l=[]
    for i in tvr:
        l.append(i.roon_no)
    print('total_count_vaccant_rooms',l)
    return len(l)

def total_collection_june():
    total_mthly_rent = []
    total_advance_amt = []
    total_due_amt = []
    total_guest_br3 = branch3app.models.pg1_new_guest.objects.all().filter(flag=2)
    for i in total_guest_br3:
        a=0
        b=type(a)
        print('this is b',b)
        x=int(i.monthly_rent)
        y=int(i.june_advance)
        z=int(i.june_dis_amt)
        j=type(x)
        k=type(y)
        l=type(z)
        if b == j:
            total_mthly_rent.append(int(i.monthly_rent))
        if b == k:
            total_advance_amt.append(int(i.june_advance))
        if b == l:
            total_due_amt.append(int(i.may_due_amt))

    tm=sum(total_mthly_rent)
    ta=sum(total_advance_amt)
    td=sum(total_due_amt)

    total_discout_amt = []
    pg1_new_beds = branch3app.models.pg1_new_guest.objects.all().filter(flag=2)
    for i in pg1_new_beds:
        a = 0
        b = type(a)
        m=int(i.june_dis_amt)
        n=type(m)
        if b == n:
            total_discout_amt.append(int(i.june_dis_amt))

    tdis=sum(total_discout_amt)

    total_collection_amt = tm+ta+td-tdis
    return total_collection_amt

def total_received_june():
    total_collection=[]
    total_guest_br3 = branch3app.models.pg1_new_guest.objects.all().filter(flag=2)
    for i in total_guest_br3:
        a=0
        b=type(a)
        x=int(i.june_rent)
        j=type(x)
        if b == j:
            total_collection.append(int(i.june_rent))
    print(total_collection)

    tc=sum(total_collection)

    total_collection_amt = tc
    return total_collection_amt

def total_received_june_list():
    total_collection=[]
    total_guest_br3 = branch3app.models.pg1_new_guest.objects.all().filter(flag=2)
    for i in total_guest_br3:
        a = 0
        b = type(a)
        x = int(i.june_rent)
        j = type(x)
        if b == j:
            total_collection.append(int(i.june_rent))
    print(total_collection)

    tc=sum(total_collection)

    total_collection_amt = tc
    return total_collection

def total_due_june():
    total_mthly_rent = []
    total_collection=[]
    total_advance_amt = []
    total_due_amt = []
    total_guest_br3 = branch3app.models.pg1_new_guest.objects.all().filter(flag=2)
    for i in total_guest_br3:
        a=10
        b=type(a)
        q=int(i.monthly_rent)
        x=int(i.june_rent)
        y=int(i.june_advance)
        z=int(i.june_dis_amt)
        j=type(x)
        k=type(y)
        l=type(z)
        m=type(q)
        if b == m:
            total_mthly_rent.append(int(i.monthly_rent))
        if b == j:
            total_collection.append(int(i.june_rent))
        if b == k:
            total_advance_amt.append(int(i.june_advance))
        if b == l:
            total_due_amt.append(int(i.may_due_amt))

    tm=sum(total_mthly_rent)
    tc=sum(total_collection)
    ta=sum(total_advance_amt)
    td=sum(total_due_amt)

    total_discout_amt = []
    pg1_new_beds = branch3app.models.pg1_new_guest.objects.all().filter(flag=2)
    for i in pg1_new_beds:
        a = 0
        b = type(a)
        if i.june_dis_amt == b:
            total_discout_amt.append(int(i.june_dis_amt))

    tdis = sum(total_discout_amt)

    total_collection_amt = tm+ta+td-tc-tdis
    return total_collection_amt

def total_collection_monthly_june():
    total_mthly_rent = []

    total_guest_br3 = branch3app.models.pg1_new_guest.objects.all().filter(flag=2)
    for i in total_guest_br3:
        a=0
        b=type(a)
        if i.monthly_rent == b:
            total_mthly_rent.append(int(i.monthly_rent))

    tm=sum(total_mthly_rent)

    total_collection_amt = tm
    return total_collection_amt

def total_collection_advance_june():

    total_advance_amt = []

    total_guest_br3 = branch3app.models.pg1_new_guest.objects.all().filter(flag=2)
    for i in total_guest_br3:
        a=0
        b=type(a)
        if i.june_advance == b:
            total_advance_amt.append(int(i.june_advance))

    ta=sum(total_advance_amt)

    total_collection_amt = ta
    return total_collection_amt

def total_collection_due_june():
    total_due_amt = []
    total_guest_br3 = branch3app.models.pg1_new_guest.objects.all().filter(flag=2)
    for i in total_guest_br3:
        a=0
        b=type(a)
        if i.may_due_amt == b:
            total_due_amt.append(int(i.may_due_amt))

    td=sum(total_due_amt)

    total_collection_amt = td
    return total_collection_amt

def total_collection_discount_june():
    total_discout_amt = []
    pg1_new_beds = branch3app.models.pg1_new_guest.objects.all().filter(flag=2)
    for i in pg1_new_beds:
        a=0
        b=type(a)
        if i.june_dis_amt == b:
            total_discout_amt.append(int(i.june_dis_amt))

    tdis=sum(total_discout_amt)

    total_collection_amt = tdis
    return total_collection_amt

def bar_chart():
    l=[]
    l.append(total_collection_june())
    l.append(total_received_june())
    l.append(total_due_june())
    l.append(total_collection_discount_june())
    return l

