import datetime as datetime
from django.shortcuts import render
from django.contrib import messages

# from myapp.models import *
from branch5app.models import *
import datetime

database_name = 'cpg'
database_password = '#123.com#'
database_user = 'root'
database_host = 'localhost'

import pymysql as py
import pymysql.cursors

def detailed_report_choose_months5(request):
    if 'username' in request.session:
        return render(request, 'branches/branch5/live_print_report/detailed_report_choose_months.html')
    return render(request, 'index.html')


def may_print_live5(request):
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
            'brname': 'BRANCH 3 Room Creation Form',
            # 'br': pg1_new_beds.objects.all().filter(roon_no=101).order_by('roon_no'),
            'rn1': l[0],
            'table_height': '50px',

            'rs113': ll[0],
            '113_data': pg1_new_beds.objects.all().filter(roon_no=113),
            'rs114': ll[1],
            '114_data': pg1_new_beds.objects.all().filter(roon_no=114),
            'rs115': ll[2],
            '115_data': pg1_new_beds.objects.all().filter(roon_no=115),
            'rs116': ll[3],
            '116_data': pg1_new_beds.objects.all().filter(roon_no=116),
            'rs117': ll[4],
            '117_data': pg1_new_beds.objects.all().filter(roon_no=117),

            # 'g1_data':g1_data,
            'rs213': ll[5],
            '213_data': pg1_new_beds.objects.all().filter(roon_no=213),
            'rs214': ll[6],
            '214_data': pg1_new_beds.objects.all().filter(roon_no=214),
            'rs215': ll[7],
            '215_data': pg1_new_beds.objects.all().filter(roon_no=215),
            'rs216': ll[8],
            '216_data': pg1_new_beds.objects.all().filter(roon_no=216),
            'rs217': ll[9],
            '217_data': pg1_new_beds.objects.all().filter(roon_no=217),

            'rs313': ll[10],
            '313_data': pg1_new_beds.objects.all().filter(roon_no=313),
            'rs314': ll[11],
            '314_data': pg1_new_beds.objects.all().filter(roon_no=314),
            'rs315': ll[12],
            '315_data': pg1_new_beds.objects.all().filter(roon_no=315),
            'rs316': ll[13],
            '316_data': pg1_new_beds.objects.all().filter(roon_no=316),
            'rs317': ll[14],
            '317_data': pg1_new_beds.objects.all().filter(roon_no=317),
            'rs318': ll[15],
            '318_data': pg1_new_beds.objects.all().filter(roon_no=318),

        }
        return render(request, 'branches/branch5/live_print_report/may_print_live.html', context)
    return render(request, 'index.html')

def june_print_live5(request):
    if 'username' in request.session:
        ll = []
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        context = {
            'table_height': '50px',

            'rs113': ll[0],
            '113_data': pg1_new_beds.objects.all().filter(roon_no=113),
            'rs114': ll[1],
            '114_data': pg1_new_beds.objects.all().filter(roon_no=114),
            'rs115': ll[2],
            '115_data': pg1_new_beds.objects.all().filter(roon_no=115),
            'rs116': ll[3],
            '116_data': pg1_new_beds.objects.all().filter(roon_no=116),
            'rs117': ll[4],
            '117_data': pg1_new_beds.objects.all().filter(roon_no=117),

            # 'g1_data':g1_data,
            'rs213': ll[5],
            '213_data': pg1_new_beds.objects.all().filter(roon_no=213),
            'rs214': ll[6],
            '214_data': pg1_new_beds.objects.all().filter(roon_no=214),
            'rs215': ll[7],
            '215_data': pg1_new_beds.objects.all().filter(roon_no=215),
            'rs216': ll[8],
            '216_data': pg1_new_beds.objects.all().filter(roon_no=216),
            'rs217': ll[9],
            '217_data': pg1_new_beds.objects.all().filter(roon_no=217),

            'rs313': ll[10],
            '313_data': pg1_new_beds.objects.all().filter(roon_no=313),
            'rs314': ll[11],
            '314_data': pg1_new_beds.objects.all().filter(roon_no=314),
            'rs315': ll[12],
            '315_data': pg1_new_beds.objects.all().filter(roon_no=315),
            'rs316': ll[13],
            '316_data': pg1_new_beds.objects.all().filter(roon_no=316),
            'rs317': ll[14],
            '317_data': pg1_new_beds.objects.all().filter(roon_no=317),
            'rs318': ll[15],
            '318_data': pg1_new_beds.objects.all().filter(roon_no=318),

        }
        return render(request, 'branches/branch5/live_print_report/june_print_live.html', context)
    return render(request, 'index.html')

def june_dtails_live5(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch5/live_print_report/live_monthly_details/june/june_dtails_live.html', context)
    return render(request, 'index.html')


def viewall_vaccant_room5(request):
    context = {
        'vr': pg1_new_beds.objects.all().exclude(flag=2).order_by('roon_no')
    }
    return render(request, 'branches/branch5/reports/vaccant_room/viewall_vaccant_room.html', context)

def full_paid_guest5(request):
    context = {
        'fpr': pg1_new_guest.objects.all().filter(flag=2,june_due_amt='0',june_rent_flag=200).order_by('roon_no')
    }
    return render(request, 'branches/branch5/reports/paid_rent/full_paid_guest.html', context)

