#admin_dashboard_calculations_br5
import lib2to3.pgen2.token
import locale

from django.shortcuts import render
from django.contrib import messages
import myapp
import branch2app
import branch3app
import branch4app
import branch5app
import branch6app
import branch7app
import branch8app
import branch9app
import branch10app
import branch11app
import branch12app
import branch13app
import branch14app


def total_monthly_branch_wise_collection_report(request):

    branch=[myapp,branch2app,branch3app,branch4app,branch5app,branch6app,branch7app,branch8app,branch9app,
            branch10app,branch11app,branch12app,branch13app,branch14app]
    jan_tc=[]
    for i in range(len(branch)):
        total_collection_br1 = branch[i].models.pg1_new_guest.objects.all().filter(flag=2,jan_rent_flag__gt=99)
        for i in total_collection_br1:
            if i.monthly_rent !='':
                jan_tc.append(int(i.monthly_rent))

    feb_tc=[]
    for i in range(len(branch)):
        total_collection_br1 = branch[i].models.pg1_new_guest.objects.all().filter(flag=2,feb_rent_flag__gt=99)
        for i in total_collection_br1:
            if i.monthly_rent !='':
                feb_tc.append(int(i.monthly_rent))

    mar_tc=[]
    for i in range(len(branch)):
        total_collection_br1 = branch[i].models.pg1_new_guest.objects.all().filter(flag=2,march_rent_flag__gt=99)
        for i in total_collection_br1:
            if i.monthly_rent !='':
                mar_tc.append(int(i.monthly_rent))

    print('jan_tc',jan_tc)
    print(sum(jan_tc))

    context={
        'grand_total_collection' : jan_tc,
    }

    return render (request,'admindashboard/admin_dashboard_reports/total_monthly_branch_wise_collection_report.html',context)

