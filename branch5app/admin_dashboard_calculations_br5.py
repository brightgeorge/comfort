#admin_dashboard_calculations_br5

from django.shortcuts import render
from django.contrib import messages
import branch5app

def total_collection_june():
    total_mthly_rent = []
    total_advance_amt = []
    total_due_amt = []
    total_guest_br5 = branch5app.models.pg1_new_guest.objects.all().filter(flag=2)
    for i in total_guest_br5:
        total_mthly_rent.append(int(i.monthly_rent))
        total_advance_amt.append(int(i.june_advance))
        total_due_amt.append(int(i.may_due_amt))

    tm=sum(total_mthly_rent)
    ta=sum(total_advance_amt)
    td=sum(total_due_amt)

    total_discout_amt = []
    pg1_new_beds = branch5app.models.pg1_new_beds.objects.all().filter(flag=2)
    for i in pg1_new_beds:
        total_discout_amt.append(int(i.june_rent))

    tdis=sum(total_discout_amt)

    total_collection_amt = tm+ta+td-tdis
    return total_collection_amt

def total_received_june():
    total_collection=[]
    total_guest_br5 = branch5app.models.pg1_new_guest.objects.all().filter(flag=2)
    for i in total_guest_br5:
        total_collection.append(int(i.june_rent))

    tc=sum(total_collection)

    total_collection_amt = tc
    return total_collection_amt

def total_due_june():
    total_mthly_rent = []
    total_collection=[]
    total_advance_amt = []
    total_due_amt = []
    total_guest_br5 = branch5app.models.pg1_new_guest.objects.all().filter(flag=2)
    for i in total_guest_br5:
        total_mthly_rent.append(int(i.monthly_rent))
        total_collection.append(int(i.june_rent))
        total_advance_amt.append(int(i.june_advance))
        total_due_amt.append(int(i.may_due_amt))

    tm=sum(total_mthly_rent)
    tc=sum(total_collection)
    ta=sum(total_advance_amt)
    td=sum(total_due_amt)

    total_discout_amt = []
    pg1_new_beds = branch5app.models.pg1_new_beds.objects.all().filter(flag=2)
    for i in pg1_new_beds:
        total_discout_amt.append(int(i.june_rent))

    tdis = sum(total_discout_amt)

    total_collection_amt = tm+ta+td-tc-tdis
    return total_collection_amt

def total_collection_monthly_june():
    total_mthly_rent = []

    total_guest_br5 = branch5app.models.pg1_new_guest.objects.all().filter(flag=2)
    for i in total_guest_br5:
        total_mthly_rent.append(int(i.monthly_rent))

    tm=sum(total_mthly_rent)

    total_collection_amt = tm
    return total_collection_amt