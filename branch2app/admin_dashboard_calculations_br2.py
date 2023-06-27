#admin_dashboard_calculations_br2

from django.shortcuts import render
from django.contrib import messages
import branch2app

def total_count_active_guests():
    tvr = branch2app.models.pg1_new_beds.objects.all().filter(flag=2)
    l=[]
    for i in tvr:
        l.append(i.roon_no)
    print('total_count_active_guests',l)
    return len(l)

def total_count_vaccant_rooms():
    tvr = branch2app.models.pg1_new_beds.objects.all().exclude(flag=2).order_by('roon_no')
    l=[]
    for i in tvr:
        l.append(i.roon_no)
    print('total_count_vaccant_rooms',l)
    return len(l)

def total_collection_june():
    total_mthly_rent = []
    total_advance_amt = []
    total_due_amt = []
    total_guest_br2 = branch2app.models.pg1_new_guest.objects.all().filter(flag=2)
    for i in total_guest_br2:
        total_mthly_rent.append(int(i.monthly_rent))
        total_advance_amt.append(int(i.june_advance))
        total_due_amt.append(int(i.may_due_amt))

    tm=sum(total_mthly_rent)
    ta=sum(total_advance_amt)
    td=sum(total_due_amt)

    total_discout_amt = []
    pg1_new_beds = branch2app.models.pg1_new_guest.objects.all().filter(flag=2)
    for i in pg1_new_beds:
        total_discout_amt.append(int(i.june_dis_amt))

    tdis=sum(total_discout_amt)

    total_collection_amt = tm+ta+td-tdis
    return total_collection_amt

def total_received_june():
    total_collection=[]
    total_guest_br2 = branch2app.models.pg1_new_guest.objects.all().filter(flag=2)
    for i in total_guest_br2:
        total_collection.append(int(i.june_rent))
    print(total_collection)

    tc=sum(total_collection)

    total_collection_amt = tc
    return total_collection_amt

def total_received_june_list():
    total_collection=[]
    total_guest_br2 = branch2app.models.pg1_new_guest.objects.all().filter(flag=2)
    for i in total_guest_br2:
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
    total_guest_br2 = branch2app.models.pg1_new_guest.objects.all().filter(flag=2)
    for i in total_guest_br2:
        total_mthly_rent.append(int(i.monthly_rent))
        total_collection.append(int(i.june_rent))
        total_advance_amt.append(int(i.june_advance))
        total_due_amt.append(int(i.may_due_amt))

    tm=sum(total_mthly_rent)
    tc=sum(total_collection)
    ta=sum(total_advance_amt)
    td=sum(total_due_amt)

    total_discout_amt = []
    pg1_new_beds = branch2app.models.pg1_new_guest.objects.all().filter(flag=2)
    for i in pg1_new_beds:
        total_discout_amt.append(int(i.june_dis_amt))

    tdis = sum(total_discout_amt)

    total_collection_amt = tm+ta+td-tc-tdis
    return total_collection_amt

def total_collection_monthly_june():
    total_mthly_rent = []

    total_guest_br2 = branch2app.models.pg1_new_guest.objects.all().filter(flag=2)
    for i in total_guest_br2:
        total_mthly_rent.append(int(i.monthly_rent))

    tm=sum(total_mthly_rent)

    total_collection_amt = tm
    return total_collection_amt

def total_collection_advance_june():

    total_advance_amt = []

    total_guest_br2 = branch2app.models.pg1_new_guest.objects.all().filter(flag=2)
    for i in total_guest_br2:
        total_advance_amt.append(int(i.june_advance))

    ta=sum(total_advance_amt)

    total_collection_amt = ta
    return total_collection_amt

def total_collection_due_june():
    total_due_amt = []
    total_guest_br2 = branch2app.models.pg1_new_guest.objects.all().filter(flag=2)
    for i in total_guest_br2:
        total_due_amt.append(int(i.may_due_amt))

    td=sum(total_due_amt)

    total_collection_amt = td
    return total_collection_amt

def total_collection_discount_june():
    total_discout_amt = []
    pg1_new_beds = branch2app.models.pg1_new_guest.objects.all().filter(flag=2)
    for i in pg1_new_beds:
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

