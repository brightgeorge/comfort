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

    total_jan_tc=[]
    total_jan_adv=[]
    total_jan_dis=[]
    total_jan_ren=[]

    jan_tc=[]
    jan_adv=[]
    jan_dis=[]
    jan_ren=[]

    for i in range(len(branch)):
        total_collection_br1 = branch[i].models.pg1_new_guest.objects.all().filter(flag=2,jan_rent_flag__gt=99)
        for i in total_collection_br1:
            if i.monthly_rent !='':
                jan_tc.append(float(i.monthly_rent))
            if i.jan_advance != '':
                jan_adv.append(float(i.jan_advance))
            if i.jan_dis_amt != '':
                jan_dis.append(float(i.jan_dis_amt))
            if i.jan_rent != '':
                jan_ren.append(float(i.jan_rent))

        total_jan_tc.append(sum(jan_tc))
        total_jan_adv.append(sum(jan_adv))
        total_jan_dis.append(sum(jan_dis))
        total_jan_ren.append(sum(jan_ren))
        jan_tc.clear()
        jan_adv.clear()
        jan_dis.clear()
        jan_ren.clear()

    total_receivable_amt=[]
    rlen=len(total_jan_tc)
    for i in range(rlen):
        total_receivable_amt.append(total_jan_tc[i] + total_jan_adv[i] - total_jan_dis[i] )

    balance_amt = []
    ba = len(total_jan_tc)
    for i in range(ba):
        balance_amt.append(total_receivable_amt[i] - total_jan_ren[i] )

##########################

    total_feb_tc = []
    total_feb_adv = []
    total_feb_dis = []
    total_feb_ren = []

    feb_tc = []
    feb_adv = []
    feb_dis = []
    feb_ren = []

    for i in range(len(branch)):
        total_collection_br1 = branch[i].models.pg1_new_guest.objects.all().filter(flag=2, feb_rent_flag__gt=99)
        for i in total_collection_br1:
            if i.monthly_rent != '':
                feb_tc.append(float(i.monthly_rent))
            if i.feb_advance != '':
                feb_adv.append(float(i.feb_advance))
            if i.feb_dis_amt != '':
                feb_dis.append(float(i.feb_dis_amt))
            if i.feb_rent != '':
                feb_ren.append(float(i.feb_rent))

        total_feb_tc.append(sum(feb_tc))
        total_feb_adv.append(sum(feb_adv))
        total_feb_dis.append(sum(feb_dis))
        total_feb_ren.append(sum(feb_ren))
        feb_tc.clear()
        feb_adv.clear()
        feb_dis.clear()
        feb_ren.clear()

    total_receivable_amt = []
    rlen = len(total_feb_tc)
    for i in range(rlen):
        total_receivable_amt.append(total_feb_tc[i] + total_feb_adv[i] - total_feb_dis[i])

    balance_amt = []
    ba = len(total_feb_tc)
    for i in range(ba):
        balance_amt.append(total_receivable_amt[i] - total_feb_ren[i])

#########################

    total_march_tc = []
    total_march_adv = []
    total_march_dis = []
    total_march_ren = []

    march_tc = []
    march_adv = []
    march_dis = []
    march_ren = []

    for i in range(len(branch)):
        total_collection_br1 = branch[i].models.pg1_new_guest.objects.all().filter(flag=2, march_rent_flag__gt=99)
        for i in total_collection_br1:
            if i.monthly_rent != '':
                march_tc.append(float(i.monthly_rent))
            if i.march_advance != '':
                march_adv.append(float(i.march_advance))
            if i.march_dis_amt != '':
                march_dis.append(float(i.march_dis_amt))
            if i.march_rent != '':
                march_ren.append(float(i.march_rent))

        total_march_tc.append(sum(march_tc))
        total_march_adv.append(sum(march_adv))
        total_march_dis.append(sum(march_dis))
        total_march_ren.append(sum(march_ren))
        march_tc.clear()
        march_adv.clear()
        march_dis.clear()
        march_ren.clear()

    total_receivable_amt = []
    rlen = len(total_march_tc)
    for i in range(rlen):
        total_receivable_amt.append(total_march_tc[i] + total_march_adv[i] - total_march_dis[i])

    balance_amt = []
    ba = len(total_march_tc)
    for i in range(ba):
        balance_amt.append(total_receivable_amt[i] - total_march_ren[i])

##############################

    total_april_tc = []
    total_april_adv = []
    total_april_dis = []
    total_april_ren = []

    april_tc = []
    april_adv = []
    april_dis = []
    april_ren = []

    for i in range(len(branch)):
        total_collection_br1 = branch[i].models.pg1_new_guest.objects.all().filter(flag=2, april_rent_flag__gt=99)
        for i in total_collection_br1:
            if i.monthly_rent != '':
                april_tc.append(float(i.monthly_rent))
            if i.april_advance != '':
                april_adv.append(float(i.april_advance))
            if i.april_dis_amt != '':
                april_dis.append(float(i.april_dis_amt))
            if i.april_rent != '':
                april_ren.append(float(i.april_rent))

        total_april_tc.append(sum(april_tc))
        total_april_adv.append(sum(april_adv))
        total_april_dis.append(sum(april_dis))
        total_april_ren.append(sum(april_ren))
        april_tc.clear()
        april_adv.clear()
        april_dis.clear()
        april_ren.clear()

    total_receivable_amt = []
    rlen = len(total_april_tc)
    for i in range(rlen):
        total_receivable_amt.append(total_april_tc[i] + total_april_adv[i] - total_april_dis[i])

    balance_amt = []
    ba = len(total_april_tc)
    for i in range(ba):
        balance_amt.append(total_receivable_amt[i] - total_april_ren[i])

############################

    total_may_tc = []
    total_may_adv = []
    total_may_dis = []
    total_may_ren = []

    may_tc = []
    may_adv = []
    may_dis = []
    may_ren = []

    for i in range(len(branch)):
        total_collection_br1 = branch[i].models.pg1_new_guest.objects.all().filter(flag=2, may_rent_flag__gt=99)
        for i in total_collection_br1:
            if i.monthly_rent != '':
                may_tc.append(float(i.monthly_rent))
            if i.may_advance != '':
                may_adv.append(float(i.may_advance))
            if i.may_dis_amt != '':
                may_dis.append(float(i.may_dis_amt))
            if i.may_rent != '':
                may_ren.append(float(i.may_rent))

        total_may_tc.append(sum(may_tc))
        total_may_adv.append(sum(may_adv))
        total_may_dis.append(sum(may_dis))
        total_may_ren.append(sum(may_ren))
        may_tc.clear()
        may_adv.clear()
        may_dis.clear()
        may_ren.clear()

    total_receivable_amt = []
    rlen = len(total_may_tc)
    for i in range(rlen):
        total_receivable_amt.append(total_may_tc[i] + total_may_adv[i] - total_may_dis[i])

    balance_amt = []
    ba = len(total_may_tc)
    for i in range(ba):
        balance_amt.append(total_receivable_amt[i] - total_may_ren[i])

################################3

    total_june_tc = []
    total_june_adv = []
    total_june_dis = []
    total_june_ren = []

    june_tc = []
    june_adv = []
    june_dis = []
    june_ren = []

    for i in range(len(branch)):
        total_collection_br1 = branch[i].models.pg1_new_guest.objects.all().filter(flag=2, june_rent_flag__gt=99)
        for i in total_collection_br1:
            if i.monthly_rent != '':
                june_tc.append(float(i.monthly_rent))
            if i.june_advance != '':
                june_adv.append(float(i.june_advance))
            if i.june_dis_amt != '':
                june_dis.append(float(i.june_dis_amt))
            if i.june_rent != '':
                june_ren.append(float(i.june_rent))

        total_june_tc.append(sum(june_tc))
        total_june_adv.append(sum(june_adv))
        total_june_dis.append(sum(june_dis))
        total_june_ren.append(sum(june_ren))
        june_tc.clear()
        june_adv.clear()
        june_dis.clear()
        june_ren.clear()

    total_receivable_amt = []
    rlen = len(total_june_tc)
    for i in range(rlen):
        total_receivable_amt.append(total_june_tc[i] + total_june_adv[i] - total_june_dis[i])

    balance_amt = []
    ba = len(total_june_tc)
    for i in range(ba):
        balance_amt.append(total_receivable_amt[i] - total_june_ren[i])

##############################

    total_july_tc = []
    total_july_adv = []
    total_july_dis = []
    total_july_ren = []

    july_tc = []
    july_adv = []
    july_dis = []
    july_ren = []

    for i in range(len(branch)):
        total_collection_br1 = branch[i].models.pg1_new_guest.objects.all().filter(flag=2, july_rent_flag__gt=99)
        for i in total_collection_br1:
            if i.monthly_rent != '':
                july_tc.append(float(i.monthly_rent))
            if i.july_advance != '':
                july_adv.append(float(i.july_advance))
            if i.july_dis_amt != '':
                july_dis.append(float(i.july_dis_amt))
            if i.july_rent != '':
                july_ren.append(float(i.july_rent))

        total_july_tc.append(sum(july_tc))
        total_july_adv.append(sum(july_adv))
        total_july_dis.append(sum(july_dis))
        total_july_ren.append(sum(july_ren))
        july_tc.clear()
        july_adv.clear()
        july_dis.clear()
        july_ren.clear()

    total_receivable_amt = []
    rlen = len(total_july_tc)
    for i in range(rlen):
        total_receivable_amt.append(total_july_tc[i] + total_july_adv[i] - total_july_dis[i])

    balance_amt = []
    ba = len(total_july_tc)
    for i in range(ba):
        balance_amt.append(total_receivable_amt[i] - total_july_ren[i])

#############################

    total_auguest_tc = []
    total_auguest_adv = []
    total_auguest_dis = []
    total_auguest_ren = []

    auguest_tc = []
    auguest_adv = []
    auguest_dis = []
    auguest_ren = []

    for i in range(len(branch)):
        total_collection_br1 = branch[i].models.pg1_new_guest.objects.all().filter(flag=2, auguest_rent_flag__gt=99)
        for i in total_collection_br1:
            if i.monthly_rent != '':
                auguest_tc.append(float(i.monthly_rent))
            if i.auguest_advance != '':
                auguest_adv.append(float(i.auguest_advance))
            if i.auguest_dis_amt != '':
                auguest_dis.append(float(i.auguest_dis_amt))
            if i.auguest_rent != '':
                auguest_ren.append(float(i.auguest_rent))

        total_auguest_tc.append(sum(auguest_tc))
        total_auguest_adv.append(sum(auguest_adv))
        total_auguest_dis.append(sum(auguest_dis))
        total_auguest_ren.append(sum(auguest_ren))
        auguest_tc.clear()
        auguest_adv.clear()
        auguest_dis.clear()
        auguest_ren.clear()

    total_receivable_amt = []
    rlen = len(total_auguest_tc)
    for i in range(rlen):
        total_receivable_amt.append(total_auguest_tc[i] + total_auguest_adv[i] - total_auguest_dis[i])

    balance_amt = []
    ba = len(total_auguest_tc)
    for i in range(ba):
        balance_amt.append(total_receivable_amt[i] - total_auguest_ren[i])

#############################

    total_sept_tc = []
    total_sept_adv = []
    total_sept_dis = []
    total_sept_ren = []

    sept_tc = []
    sept_adv = []
    sept_dis = []
    sept_ren = []

    for i in range(len(branch)):
        total_collection_br1 = branch[i].models.pg1_new_guest.objects.all().filter(flag=2, sept_rent_flag__gt=99)
        for i in total_collection_br1:
            if i.monthly_rent != '':
                sept_tc.append(float(i.monthly_rent))
            if i.sept_advance != '':
                sept_adv.append(float(i.sept_advance))
            if i.sept_dis_amt != '':
                sept_dis.append(float(i.sept_dis_amt))
            if i.sept_rent != '':
                sept_ren.append(float(i.sept_rent))

        total_sept_tc.append(sum(sept_tc))
        total_sept_adv.append(sum(sept_adv))
        total_sept_dis.append(sum(sept_dis))
        total_sept_ren.append(sum(sept_ren))
        sept_tc.clear()
        sept_adv.clear()
        sept_dis.clear()
        sept_ren.clear()

    total_receivable_amt = []
    rlen = len(total_sept_tc)
    for i in range(rlen):
        total_receivable_amt.append(total_sept_tc[i] + total_sept_adv[i] - total_sept_dis[i])

    balance_amt = []
    ba = len(total_sept_tc)
    for i in range(ba):
        balance_amt.append(total_receivable_amt[i] - total_sept_ren[i])

##########################

    total_october_tc = []
    total_october_adv = []
    total_october_dis = []
    total_october_ren = []

    october_tc = []
    october_adv = []
    october_dis = []
    october_ren = []

    for i in range(len(branch)):
        total_collection_br1 = branch[i].models.pg1_new_guest.objects.all().filter(flag=2, october_rent_flag__gt=99)
        for i in total_collection_br1:
            if i.monthly_rent != '':
                october_tc.append(float(i.monthly_rent))
            if i.october_advance != '':
                october_adv.append(float(i.october_advance))
            if i.october_dis_amt != '':
                october_dis.append(float(i.october_dis_amt))
            if i.october_rent != '':
                october_ren.append(float(i.october_rent))

        total_october_tc.append(sum(october_tc))
        total_october_adv.append(sum(october_adv))
        total_october_dis.append(sum(october_dis))
        total_october_ren.append(sum(october_ren))
        october_tc.clear()
        october_adv.clear()
        october_dis.clear()
        october_ren.clear()

    total_receivable_amt = []
    rlen = len(total_october_tc)
    for i in range(rlen):
        total_receivable_amt.append(total_october_tc[i] + total_october_adv[i] - total_october_dis[i])

    balance_amt = []
    ba = len(total_october_tc)
    for i in range(ba):
        balance_amt.append(total_receivable_amt[i] - total_october_ren[i])

##########################

    total_nov_tc = []
    total_nov_adv = []
    total_nov_dis = []
    total_nov_ren = []

    nov_tc = []
    nov_adv = []
    nov_dis = []
    nov_ren = []

    for i in range(len(branch)):
        total_collection_br1 = branch[i].models.pg1_new_guest.objects.all().filter(flag=2, nov_rent_flag__gt=99)
        for i in total_collection_br1:
            if i.monthly_rent != '':
                nov_tc.append(float(i.monthly_rent))
            if i.nov_advance != '':
                nov_adv.append(float(i.nov_advance))
            if i.nov_dis_amt != '':
                nov_dis.append(float(i.nov_dis_amt))
            if i.nov_rent != '':
                nov_ren.append(float(i.nov_rent))

        total_nov_tc.append(sum(nov_tc))
        total_nov_adv.append(sum(nov_adv))
        total_nov_dis.append(sum(nov_dis))
        total_nov_ren.append(sum(nov_ren))
        nov_tc.clear()
        nov_adv.clear()
        nov_dis.clear()
        nov_ren.clear()

    total_receivable_amt = []
    rlen = len(total_nov_tc)
    for i in range(rlen):
        total_receivable_amt.append(total_nov_tc[i] + total_nov_adv[i] - total_nov_dis[i])

    balance_amt = []
    ba = len(total_nov_tc)
    for i in range(ba):
        balance_amt.append(total_receivable_amt[i] - total_nov_ren[i])

############################3

    total_dec_tc = []
    total_dec_adv = []
    total_dec_dis = []
    total_dec_ren = []

    dec_tc = []
    dec_adv = []
    dec_dis = []
    dec_ren = []

    for i in range(len(branch)):
        total_collection_br1 = branch[i].models.pg1_new_guest.objects.all().filter(flag=2, dec_rent_flag__gt=99)
        for i in total_collection_br1:
            if i.monthly_rent != '':
                dec_tc.append(float(i.monthly_rent))
            if i.dec_advance != '':
                dec_adv.append(float(i.dec_advance))
            if i.dec_dis_amt != '':
                dec_dis.append(float(i.dec_dis_amt))
            if i.dec_rent != '':
                dec_ren.append(float(i.dec_rent))

        total_dec_tc.append(sum(dec_tc))
        total_dec_adv.append(sum(dec_adv))
        total_dec_dis.append(sum(dec_dis))
        total_dec_ren.append(sum(dec_ren))
        dec_tc.clear()
        dec_adv.clear()
        dec_dis.clear()
        dec_ren.clear()

    total_receivable_amt = []
    rlen = len(total_dec_tc)
    for i in range(rlen):
        total_receivable_amt.append(total_dec_tc[i] + total_dec_adv[i] - total_dec_dis[i])

    balance_amt = []
    ba = len(total_dec_tc)
    for i in range(ba):
        balance_amt.append(total_receivable_amt[i] - total_dec_ren[i])

######################################

    context={
        'total_jan_tc' : sum(total_jan_tc),
        'total_jan_adv' : sum(total_jan_adv),
        'total_jan_dis': sum(total_jan_dis),
        'total_receivable_amt' : sum(total_receivable_amt),
        'total_jan_ren' : sum(total_jan_ren),
        'balance_amt' : sum(balance_amt),

        'total_feb_tc': sum(total_feb_tc),
        'total_feb_adv': sum(total_feb_adv),
        'total_feb_dis': sum(total_feb_dis),
        'total_receivable_amt': sum(total_receivable_amt),
        'total_feb_ren': sum(total_feb_ren),
        'balance_amt': sum(balance_amt),

        'total_march_tc': sum(total_march_tc),
        'total_march_adv': sum(total_march_adv),
        'total_march_dis': sum(total_march_dis),
        'total_receivable_amt': sum(total_receivable_amt),
        'total_march_ren': sum(total_march_ren),
        'balance_amt': sum(balance_amt),

        'total_april_tc': sum(total_april_tc),
        'total_april_adv': sum(total_april_adv),
        'total_april_dis': sum(total_april_dis),
        'total_receivable_amt': sum(total_receivable_amt),
        'total_april_ren': sum(total_april_ren),
        'balance_amt': sum(balance_amt),

        'total_may_tc': sum(total_may_tc),
        'total_may_adv': sum(total_may_adv),
        'total_may_dis': sum(total_may_dis),
        'total_receivable_amt': sum(total_receivable_amt),
        'total_may_ren': sum(total_may_ren),
        'balance_amt': sum(balance_amt),

        'total_june_tc': sum(total_june_tc),
        'total_june_adv': sum(total_june_adv),
        'total_june_dis': sum(total_june_dis),
        'total_receivable_amt': sum(total_receivable_amt),
        'total_june_ren': sum(total_june_ren),
        'balance_amt': sum(balance_amt),

        'total_july_tc': sum(total_july_tc),
        'total_july_adv': sum(total_july_adv),
        'total_july_dis': sum(total_july_dis),
        'total_receivable_amt': sum(total_receivable_amt),
        'total_july_ren': sum(total_july_ren),
        'balance_amt': sum(balance_amt),

        'total_auguest_tc': sum(total_auguest_tc),
        'total_auguest_adv': sum(total_auguest_adv),
        'total_auguest_dis': sum(total_auguest_dis),
        'total_receivable_amt': sum(total_receivable_amt),
        'total_auguest_ren': sum(total_auguest_ren),
        'balance_amt': sum(balance_amt),

        'total_sept_tc': sum(total_sept_tc),
        'total_sept_adv': sum(total_sept_adv),
        'total_sept_dis': sum(total_sept_dis),
        'total_receivable_amt': sum(total_receivable_amt),
        'total_sept_ren': sum(total_sept_ren),
        'balance_amt': sum(balance_amt),

        'total_october_tc': sum(total_october_tc),
        'total_october_adv': sum(total_october_adv),
        'total_october_dis': sum(total_october_dis),
        'total_receivable_amt': sum(total_receivable_amt),
        'total_october_ren': sum(total_october_ren),
        'balance_amt': sum(balance_amt),

        'total_nov_tc': sum(total_nov_tc),
        'total_nov_adv': sum(total_nov_adv),
        'total_nov_dis': sum(total_nov_dis),
        'total_receivable_amt': sum(total_receivable_amt),
        'total_nov_ren': sum(total_nov_ren),
        'balance_amt': sum(balance_amt),

        'total_dec_tc': sum(total_dec_tc),
        'total_dec_adv': sum(total_dec_adv),
        'total_dec_dis': sum(total_dec_dis),
        'total_receivable_amt': sum(total_receivable_amt),
        'total_dec_ren': sum(total_dec_ren),
        'balance_amt': sum(balance_amt),

    }

    return render (request,'admindashboard/admin_dashboard_reports/total_monthly_branch_wise_collection_report.html',context)

