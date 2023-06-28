import datetime as datetime
from django.shortcuts import render
from django.contrib import messages

# from myapp.models import *
from branch2app.models import *
import datetime

database_name = 'cpg'
database_password = '#123.com#'
database_user = 'root'
database_host = 'localhost'

import pymysql as py
import pymysql.cursors

def detailed_report_choose_months2(request):
    if 'username' in request.session:
        return render(request, 'branches/branch2/live_print_report/detailed_report_choose_months.html')
    return render(request, 'index.html')


def may_print_live2(request):
    if 'username' in request.session:
        l = []
        data = pg1_new_beds.objects.all()
        for i in data:
            l.append(i.share_type)

        ll = []
        # rsdata = room_pg1.objects.all().order_by('roon_no')1,
        # a
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        g1_data = pg1_new_beds.objects.all().filter(roon_no=1),
        print('room share type of branch22', ll)
        print('room share type of branchl0', ll[0])
        print('room share type of branchl1', ll[1])

        context = {
            'brname': 'BRANCH 2 Room Creation Form',
            'br': pg1_new_beds.objects.all().filter(roon_no=101).order_by('roon_no'),
            'rn1': l[0],
            'table_height': '40px',

            'rs101': ll[0],
            '101_data': pg1_new_beds.objects.all().filter(roon_no=101),
            # 'g1_data':g1_data,
            'rs102': ll[1],
            '102_data': pg1_new_beds.objects.all().filter(roon_no=102),
            'rs103': ll[2],
            '103_data': pg1_new_beds.objects.all().filter(roon_no=103),
            # 'g1_data':g1_data,
            'rs104': ll[3],
            '104_data': pg1_new_beds.objects.all().filter(roon_no=104),
            'rs106': ll[4],
            '106_data': pg1_new_beds.objects.all().filter(roon_no=106),
            # 'g1_data':g1_data,
            'rs107': ll[5],
            '107_data': pg1_new_beds.objects.all().filter(roon_no=107),
            'rs108': ll[6],
            '108_data': pg1_new_beds.objects.all().filter(roon_no=108),
            # 'g1_data':g1_data,
            'rs109': ll[7],
            '109_data': pg1_new_beds.objects.all().filter(roon_no=109),

            'rs201': ll[8],
            '201_data': pg1_new_beds.objects.all().filter(roon_no=201),
            # 'g1_data':g1_data,
            'rs202': ll[9],
            '202_data': pg1_new_beds.objects.all().filter(roon_no=202),
            'rs203': ll[10],
            '203_data': pg1_new_beds.objects.all().filter(roon_no=203),
            # 'g1_data':g1_data,
            'rs204': ll[11],
            '204_data': pg1_new_beds.objects.all().filter(roon_no=204),
            'rs205': ll[12],
            '205_data': pg1_new_beds.objects.all().filter(roon_no=205),
            'rs206': ll[13],
            '206_data': pg1_new_beds.objects.all().filter(roon_no=206),
            # 'g1_data':g1_data,
            'rs207': ll[14],
            '207_data': pg1_new_beds.objects.all().filter(roon_no=207),
            'rs208': ll[15],
            '208_data': pg1_new_beds.objects.all().filter(roon_no=208),
            # 'g1_data':g1_data,
            'rs209': ll[16],
            '209_data': pg1_new_beds.objects.all().filter(roon_no=209),

            'rs210': ll[17],
            '210_data': pg1_new_beds.objects.all().filter(roon_no=210),
            'rs211': ll[18],
            '211_data': pg1_new_beds.objects.all().filter(roon_no=211),
            'rs212': ll[19],
            '212_data': pg1_new_beds.objects.all().filter(roon_no=212),
            # 'g1_data':g1_data,
            'rs213': ll[20],
            '213_data': pg1_new_beds.objects.all().filter(roon_no=213),
            'rs214': ll[21],
            '214_data': pg1_new_beds.objects.all().filter(roon_no=214),
            # 'g1_data':g1_data,
            'rs215': ll[22],
            '215_data': pg1_new_beds.objects.all().filter(roon_no=215),

            'rs301': ll[23],
            '301_data': pg1_new_beds.objects.all().filter(roon_no=301),
            # 'g1_data':g1_data,
            'rs302': ll[24],
            '302_data': pg1_new_beds.objects.all().filter(roon_no=302),
            'rs303': ll[25],
            '303_data': pg1_new_beds.objects.all().filter(roon_no=303),
            # 'g1_data':g1_data,
            'rs304': ll[26],
            '304_data': pg1_new_beds.objects.all().filter(roon_no=304),
            'rs305': ll[27],
            '305_data': pg1_new_beds.objects.all().filter(roon_no=305),
            'rs306': ll[28],
            '306_data': pg1_new_beds.objects.all().filter(roon_no=306),
            # 'g1_data':g1_data,
            'rs307': ll[29],
            '307_data': pg1_new_beds.objects.all().filter(roon_no=307),
            'rs308': ll[30],
            '308_data': pg1_new_beds.objects.all().filter(roon_no=308),
            # 'g1_data':g1_data,
            'rs309': ll[31],
            '309_data': pg1_new_beds.objects.all().filter(roon_no=309),

            'rs310': ll[32],
            '310_data': pg1_new_beds.objects.all().filter(roon_no=310),
            'rs311': ll[33],
            '311_data': pg1_new_beds.objects.all().filter(roon_no=311),
            'rs312': ll[34],
            '312_data': pg1_new_beds.objects.all().filter(roon_no=312),
            # 'g1_data':g1_data,
            'rs313': ll[35],
            '313_data': pg1_new_beds.objects.all().filter(roon_no=313),
            'rs314': ll[36],
            '314_data': pg1_new_beds.objects.all().filter(roon_no=314),
            # 'g1_data':g1_data,
            'rs315': ll[37],
            '315_data': pg1_new_beds.objects.all().filter(roon_no=315),

            'rs401': ll[38],
            '401_data': pg1_new_beds.objects.all().filter(roon_no=401),
            # 'g1_data':g1_data,
            'rs402': ll[39],
            '402_data': pg1_new_beds.objects.all().filter(roon_no=402),
            'rs403': ll[40],
            '403_data': pg1_new_beds.objects.all().filter(roon_no=403),
            # 'g1_data':g1_data,
            'rs404': ll[41],
            '404_data': pg1_new_beds.objects.all().filter(roon_no=404),
            'rs405': ll[42],
            '405_data': pg1_new_beds.objects.all().filter(roon_no=405),
            'rs406': ll[43],
            '406_data': pg1_new_beds.objects.all().filter(roon_no=406),
            # 'g1_data':g1_data,
            'rs407': ll[44],
            '407_data': pg1_new_beds.objects.all().filter(roon_no=407),
            'rs408': ll[45],
            '408_data': pg1_new_beds.objects.all().filter(roon_no=408),
            # 'g1_data':g1_data,
            'rs409': ll[46],
            '409_data': pg1_new_beds.objects.all().filter(roon_no=409),

            'rs410': ll[47],
            '410_data': pg1_new_beds.objects.all().filter(roon_no=410),
            'rs411': ll[48],
            '411_data': pg1_new_beds.objects.all().filter(roon_no=411),
            'rs412': ll[49],
            '412_data': pg1_new_beds.objects.all().filter(roon_no=412),
            # 'g1_data':g1_data,
            'rs413': ll[50],
            '413_data': pg1_new_beds.objects.all().filter(roon_no=413),
            'rs414': ll[51],
            '414_data': pg1_new_beds.objects.all().filter(roon_no=414),
            # 'g1_data':g1_data,
            'rs415': ll[52],
            '415_data': pg1_new_beds.objects.all().filter(roon_no=415),

        }
        return render(request, 'branches/branch2/live_print_report/may_print_live.html', context)
    return render(request, 'index.html')

def june_print_live2(request):
    if 'username' in request.session:
        ll = []
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        context = {
            'brname': 'BRANCH 2 Room Creation Form',
            'br': pg1_new_beds.objects.all().filter(roon_no=101).order_by('roon_no'),
            'rn1': l[0],
            'table_height': '40px',

            'rs101': ll[0],
            '101_data': pg1_new_beds.objects.all().filter(roon_no=101),
            # 'g1_data':g1_data,
            'rs102': ll[1],
            '102_data': pg1_new_beds.objects.all().filter(roon_no=102),
            'rs103': ll[2],
            '103_data': pg1_new_beds.objects.all().filter(roon_no=103),
            # 'g1_data':g1_data,
            'rs104': ll[3],
            '104_data': pg1_new_beds.objects.all().filter(roon_no=104),
            'rs106': ll[4],
            '106_data': pg1_new_beds.objects.all().filter(roon_no=106),
            # 'g1_data':g1_data,
            'rs107': ll[5],
            '107_data': pg1_new_beds.objects.all().filter(roon_no=107),
            'rs108': ll[6],
            '108_data': pg1_new_beds.objects.all().filter(roon_no=108),
            # 'g1_data':g1_data,
            'rs109': ll[7],
            '109_data': pg1_new_beds.objects.all().filter(roon_no=109),

            'rs201': ll[8],
            '201_data': pg1_new_beds.objects.all().filter(roon_no=201),
            # 'g1_data':g1_data,
            'rs202': ll[9],
            '202_data': pg1_new_beds.objects.all().filter(roon_no=202),
            'rs203': ll[10],
            '203_data': pg1_new_beds.objects.all().filter(roon_no=203),
            # 'g1_data':g1_data,
            'rs204': ll[11],
            '204_data': pg1_new_beds.objects.all().filter(roon_no=204),
            'rs205': ll[12],
            '205_data': pg1_new_beds.objects.all().filter(roon_no=205),
            'rs206': ll[13],
            '206_data': pg1_new_beds.objects.all().filter(roon_no=206),
            # 'g1_data':g1_data,
            'rs207': ll[14],
            '207_data': pg1_new_beds.objects.all().filter(roon_no=207),
            'rs208': ll[15],
            '208_data': pg1_new_beds.objects.all().filter(roon_no=208),
            # 'g1_data':g1_data,
            'rs209': ll[16],
            '209_data': pg1_new_beds.objects.all().filter(roon_no=209),

            'rs210': ll[17],
            '210_data': pg1_new_beds.objects.all().filter(roon_no=210),
            'rs211': ll[18],
            '211_data': pg1_new_beds.objects.all().filter(roon_no=211),
            'rs212': ll[19],
            '212_data': pg1_new_beds.objects.all().filter(roon_no=212),
            # 'g1_data':g1_data,
            'rs213': ll[20],
            '213_data': pg1_new_beds.objects.all().filter(roon_no=213),
            'rs214': ll[21],
            '214_data': pg1_new_beds.objects.all().filter(roon_no=214),
            # 'g1_data':g1_data,
            'rs215': ll[22],
            '215_data': pg1_new_beds.objects.all().filter(roon_no=215),

            'rs301': ll[23],
            '301_data': pg1_new_beds.objects.all().filter(roon_no=301),
            # 'g1_data':g1_data,
            'rs302': ll[24],
            '302_data': pg1_new_beds.objects.all().filter(roon_no=302),
            'rs303': ll[25],
            '303_data': pg1_new_beds.objects.all().filter(roon_no=303),
            # 'g1_data':g1_data,
            'rs304': ll[26],
            '304_data': pg1_new_beds.objects.all().filter(roon_no=304),
            'rs305': ll[27],
            '305_data': pg1_new_beds.objects.all().filter(roon_no=305),
            'rs306': ll[28],
            '306_data': pg1_new_beds.objects.all().filter(roon_no=306),
            # 'g1_data':g1_data,
            'rs307': ll[29],
            '307_data': pg1_new_beds.objects.all().filter(roon_no=307),
            'rs308': ll[30],
            '308_data': pg1_new_beds.objects.all().filter(roon_no=308),
            # 'g1_data':g1_data,
            'rs309': ll[31],
            '309_data': pg1_new_beds.objects.all().filter(roon_no=309),

            'rs310': ll[32],
            '310_data': pg1_new_beds.objects.all().filter(roon_no=310),
            'rs311': ll[33],
            '311_data': pg1_new_beds.objects.all().filter(roon_no=311),
            'rs312': ll[34],
            '312_data': pg1_new_beds.objects.all().filter(roon_no=312),
            # 'g1_data':g1_data,
            'rs313': ll[35],
            '313_data': pg1_new_beds.objects.all().filter(roon_no=313),
            'rs314': ll[36],
            '314_data': pg1_new_beds.objects.all().filter(roon_no=314),
            # 'g1_data':g1_data,
            'rs315': ll[37],
            '315_data': pg1_new_beds.objects.all().filter(roon_no=315),

            'rs401': ll[38],
            '401_data': pg1_new_beds.objects.all().filter(roon_no=401),
            # 'g1_data':g1_data,
            'rs402': ll[39],
            '402_data': pg1_new_beds.objects.all().filter(roon_no=402),
            'rs403': ll[40],
            '403_data': pg1_new_beds.objects.all().filter(roon_no=403),
            # 'g1_data':g1_data,
            'rs404': ll[41],
            '404_data': pg1_new_beds.objects.all().filter(roon_no=404),
            'rs405': ll[42],
            '405_data': pg1_new_beds.objects.all().filter(roon_no=405),
            'rs406': ll[43],
            '406_data': pg1_new_beds.objects.all().filter(roon_no=406),
            # 'g1_data':g1_data,
            'rs407': ll[44],
            '407_data': pg1_new_beds.objects.all().filter(roon_no=407),
            'rs408': ll[45],
            '408_data': pg1_new_beds.objects.all().filter(roon_no=408),
            # 'g1_data':g1_data,
            'rs409': ll[46],
            '409_data': pg1_new_beds.objects.all().filter(roon_no=409),

            'rs410': ll[47],
            '410_data': pg1_new_beds.objects.all().filter(roon_no=410),
            'rs411': ll[48],
            '411_data': pg1_new_beds.objects.all().filter(roon_no=411),
            'rs412': ll[49],
            '412_data': pg1_new_beds.objects.all().filter(roon_no=412),
            # 'g1_data':g1_data,
            'rs413': ll[50],
            '413_data': pg1_new_beds.objects.all().filter(roon_no=413),
            'rs414': ll[51],
            '414_data': pg1_new_beds.objects.all().filter(roon_no=414),
            # 'g1_data':g1_data,
            'rs415': ll[52],
            '415_data': pg1_new_beds.objects.all().filter(roon_no=415),

        }
        return render(request, 'branches/branch2/live_print_report/june_print_live.html', context)
    return render(request, 'index.html')

def june_dtails_live2(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch2/live_print_report/live_monthly_details/june/june_dtails_live.html', context)
    return render(request, 'index.html')


def viewall_vaccant_room2(request):
    context = {
        'vr': pg1_new_beds.objects.all().exclude(flag=2).order_by('roon_no')
    }
    return render(request, 'branches/branch2/reports/vaccant_room/viewall_vaccant_room.html', context)

#########FULL PAID GUEST START HERE ############

def full_paid_guest2(request):
    context = {
        'fpr': pg1_new_guest.objects.all().filter(flag=2,june_due_amt=0,june_rent_flag=200).order_by('roon_no')
    }
    return render(request, 'branches/branch2/reports/paid_rent/full_paid_guest.html', context)

def may_full_paid_guest2(request):
    context = {
        'fpr': pg1_new_guest.objects.all().filter(flag=2,may_due_amt=0,may_rent_flag=200).order_by('roon_no')
    }
    return render(request, 'branches/branch2/reports/paid_rent/paid_monthly_reports/may/may_full_paid_guest.html', context)

def june_full_paid_guest2(request):
    context = {
        'fpr': pg1_new_guest.objects.all().filter(flag=2,june_due_amt=0,june_rent_flag=200).order_by('roon_no')
    }
    return render(request, 'branches/branch2/reports/paid_rent/paid_monthly_reports/jun/june_full_paid_guest.html', context)

def july_full_paid_guest2(request):
    context = {
        'fpr': pg1_new_guest.objects.all().filter(flag=2,july_due_amt=0,july_rent_flag=200).order_by('roon_no')
    }
    return render(request, 'branches/branch2/reports/paid_rent/paid_monthly_reports/jul/july_full_paid_guest.html', context)

def aug_full_paid_guest2(request):
    context = {
        'fpr': pg1_new_guest.objects.all().filter(flag=2,auguest_due_amt=0,auguest_rent_flag=200).order_by('roon_no')
    }
    return render(request, 'branches/branch2/reports/paid_rent/paid_monthly_reports/aug/aug_full_paid_guest.html', context)
#

#########FULL PAID GUEST END HERE ############

#########PARTIALLY PAID GUEST START HERE ############

def partially_paid_guest_choose_months2(request):
    if 'username' in request.session:
        return render(request, 'branches/branch2/reports/paid_rent/partially_paid_guest_choose_months.html')

def may_partially_paid_guest2(request):
    context = {
        'ppr': pg1_new_guest.objects.all().filter(flag=2,may_rent_flag=200).exclude(may_due_amt='0').order_by('roon_no')
    }
    return render(request, 'branches/branch2/reports/paid_rent/paid_monthly_reports/may/may_partially_paid_guest.html', context)
def table_may_partially_paid_guest2(request):
    context = {
        'ppr': pg1_new_guest.objects.all().filter(flag=2,may_rent_flag=200).exclude(may_due_amt='0').order_by('roon_no'),
    }
    return render(request, 'branches/branch2/reports/paid_rent/paid_monthly_reports/may/table_may_partially_paid_guest.html', context)

def june_partially_paid_guest2(request):
    context = {
        'ppr': pg1_new_guest.objects.all().filter(flag=2,june_rent_flag=200).exclude(june_due_amt='0').order_by('roon_no')
    }
    return render(request, 'branches/branch2/reports/paid_rent/paid_monthly_reports/jun/june_partially_paid_guest.html', context)
def table_june_partially_paid_guest2(request):
    context = {
        'ppr': pg1_new_guest.objects.all().filter(flag=2,june_rent_flag=200).exclude(june_due_amt='0').order_by('roon_no'),
    }
    return render(request, 'branches/branch2/reports/paid_rent/paid_monthly_reports/jun/table_june_partially_paid_guest.html', context)

def july_partially_paid_guest2(request):
    context = {
        'ppr': pg1_new_guest.objects.all().filter(flag=2,july_rent_flag=200).exclude(july_due_amt='0').order_by('roon_no')
    }
    return render(request, 'branches/branch2/reports/paid_rent/paid_monthly_reports/jul/july_partially_paid_guest.html', context)
def table_july_partially_paid_guest2(request):
    context = {
        'ppr': pg1_new_guest.objects.all().filter(flag=2,july_rent_flag=200).exclude(july_due_amt='0').order_by('roon_no'),
    }
    return render(request, 'branches/branch2/reports/paid_rent/paid_monthly_reports/jul/table_july_partially_paid_guest.html', context)



#########PARTIALLY PAID GUEST START HERE ############

