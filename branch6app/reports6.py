import datetime as datetime
from django.shortcuts import render
from django.contrib import messages

# from myapp.models import *
from branch6app.models import *
import datetime

database_name = 'cpg'
database_password = '#123.com#'
database_user = 'root'
database_host = 'localhost'

import pymysql as py
import pymysql.cursors

def detailed_report_choose_months6(request):
    if 'username' in request.session:
        return render(request, 'branches/branch6/live_print_report/detailed_report_choose_months.html')
    return render(request, 'index.html')


def jan_details_live6(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch6/live_print_report/live_monthly_details/jan/jan_details_live.html', context)
    return render(request, 'index.html')

def jan_print_live6(request):
    if 'username' in request.session:
        ll = []
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        context = {
            'brname': 'BRANCH 6 Room Creation Form',
            'table_height': '60px',

            'rs1': ll[0],
            'rm1_data': pg1_new_beds.objects.all().filter(roon_no=1),
            # 'g1_data':g1_data,
            'rs2': ll[1],
            'rm2_data': pg1_new_beds.objects.all().filter(roon_no=2),
            'rs3': ll[2],
            'rm3_data': pg1_new_beds.objects.all().filter(roon_no=3),
            'rs4': ll[3],
            'rm4_data': pg1_new_beds.objects.all().filter(roon_no=4),
            'rs5': ll[4],
            'rm5_data': pg1_new_beds.objects.all().filter(roon_no=5),
            'rs6': ll[5],
            'rm6_data': pg1_new_beds.objects.all().filter(roon_no=6),
            'rs7': ll[6],
            'rm7_data': pg1_new_beds.objects.all().filter(roon_no=7),
            'rs8': ll[7],
            'rm8_data': pg1_new_beds.objects.all().filter(roon_no=8),
            'rs9': ll[8],
            'rm9_data': pg1_new_beds.objects.all().filter(roon_no=9),
            'rs10': ll[9],
            'rm10_data': pg1_new_beds.objects.all().filter(roon_no=10),
            'rs11': ll[10],
            'rm11_data': pg1_new_beds.objects.all().filter(roon_no=11),
            'rs12': ll[11],
            'rm12_data': pg1_new_beds.objects.all().filter(roon_no=12),
            'rs13': ll[12],
            'rm13_data': pg1_new_beds.objects.all().filter(roon_no=13),
            'rs14': ll[13],
            'rm14_data': pg1_new_beds.objects.all().filter(roon_no=14),
            'rs15': ll[14],
            'rm15_data': pg1_new_beds.objects.all().filter(roon_no=15),
            'rs16': ll[15],
            'rm16_data': pg1_new_beds.objects.all().filter(roon_no=16),
            'rs17': ll[16],
            'rm17_data': pg1_new_beds.objects.all().filter(roon_no=17),
            'rs18': ll[17],
            'rm18_data': pg1_new_beds.objects.all().filter(roon_no=18),
            'rs19': ll[18],
            'rm19_data': pg1_new_beds.objects.all().filter(roon_no=19),
            'rs20': ll[19],
            'rm20_data': pg1_new_beds.objects.all().filter(roon_no=20),
            'rs21': ll[20],
            'rm21_data': pg1_new_beds.objects.all().filter(roon_no=21),
            'rs22': ll[21],
            'rm22_data': pg1_new_beds.objects.all().filter(roon_no=22),

        }
        return render(request, 'branches/branch6/live_print_report/live_monthly_details/jan/jan_print_live.html', context)
    return render(request, 'index.html')


def feb_details_live6(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch6/live_print_report/live_monthly_details/feb/feb_details_live.html', context)
    return render(request, 'index.html')

def feb_print_live6(request):
    if 'username' in request.session:
        ll = []
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        context = {
            'brname': 'BRANCH 6 Room Creation Form',
            'table_height': '60px',

            'rs1': ll[0],
            'rm1_data': pg1_new_beds.objects.all().filter(roon_no=1),
            # 'g1_data':g1_data,
            'rs2': ll[1],
            'rm2_data': pg1_new_beds.objects.all().filter(roon_no=2),
            'rs3': ll[2],
            'rm3_data': pg1_new_beds.objects.all().filter(roon_no=3),
            'rs4': ll[3],
            'rm4_data': pg1_new_beds.objects.all().filter(roon_no=4),
            'rs5': ll[4],
            'rm5_data': pg1_new_beds.objects.all().filter(roon_no=5),
            'rs6': ll[5],
            'rm6_data': pg1_new_beds.objects.all().filter(roon_no=6),
            'rs7': ll[6],
            'rm7_data': pg1_new_beds.objects.all().filter(roon_no=7),
            'rs8': ll[7],
            'rm8_data': pg1_new_beds.objects.all().filter(roon_no=8),
            'rs9': ll[8],
            'rm9_data': pg1_new_beds.objects.all().filter(roon_no=9),
            'rs10': ll[9],
            'rm10_data': pg1_new_beds.objects.all().filter(roon_no=10),
            'rs11': ll[10],
            'rm11_data': pg1_new_beds.objects.all().filter(roon_no=11),
            'rs12': ll[11],
            'rm12_data': pg1_new_beds.objects.all().filter(roon_no=12),
            'rs13': ll[12],
            'rm13_data': pg1_new_beds.objects.all().filter(roon_no=13),
            'rs14': ll[13],
            'rm14_data': pg1_new_beds.objects.all().filter(roon_no=14),
            'rs15': ll[14],
            'rm15_data': pg1_new_beds.objects.all().filter(roon_no=15),
            'rs16': ll[15],
            'rm16_data': pg1_new_beds.objects.all().filter(roon_no=16),
            'rs17': ll[16],
            'rm17_data': pg1_new_beds.objects.all().filter(roon_no=17),
            'rs18': ll[17],
            'rm18_data': pg1_new_beds.objects.all().filter(roon_no=18),
            'rs19': ll[18],
            'rm19_data': pg1_new_beds.objects.all().filter(roon_no=19),
            'rs20': ll[19],
            'rm20_data': pg1_new_beds.objects.all().filter(roon_no=20),
            'rs21': ll[20],
            'rm21_data': pg1_new_beds.objects.all().filter(roon_no=21),
            'rs22': ll[21],
            'rm22_data': pg1_new_beds.objects.all().filter(roon_no=22),

        }
        return render(request, 'branches/branch6/live_print_report/live_monthly_details/feb/feb_print_live.html', context)
    return render(request, 'index.html')



def march_details_live6(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch6/live_print_report/live_monthly_details/march/march_details_live.html', context)
    return render(request, 'index.html')

def march_print_live6(request):
    if 'username' in request.session:
        ll = []
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        context = {
            'brname': 'BRANCH 6 Room Creation Form',
            'table_height': '60px',

            'rs1': ll[0],
            'rm1_data': pg1_new_beds.objects.all().filter(roon_no=1),
            # 'g1_data':g1_data,
            'rs2': ll[1],
            'rm2_data': pg1_new_beds.objects.all().filter(roon_no=2),
            'rs3': ll[2],
            'rm3_data': pg1_new_beds.objects.all().filter(roon_no=3),
            'rs4': ll[3],
            'rm4_data': pg1_new_beds.objects.all().filter(roon_no=4),
            'rs5': ll[4],
            'rm5_data': pg1_new_beds.objects.all().filter(roon_no=5),
            'rs6': ll[5],
            'rm6_data': pg1_new_beds.objects.all().filter(roon_no=6),
            'rs7': ll[6],
            'rm7_data': pg1_new_beds.objects.all().filter(roon_no=7),
            'rs8': ll[7],
            'rm8_data': pg1_new_beds.objects.all().filter(roon_no=8),
            'rs9': ll[8],
            'rm9_data': pg1_new_beds.objects.all().filter(roon_no=9),
            'rs10': ll[9],
            'rm10_data': pg1_new_beds.objects.all().filter(roon_no=10),
            'rs11': ll[10],
            'rm11_data': pg1_new_beds.objects.all().filter(roon_no=11),
            'rs12': ll[11],
            'rm12_data': pg1_new_beds.objects.all().filter(roon_no=12),
            'rs13': ll[12],
            'rm13_data': pg1_new_beds.objects.all().filter(roon_no=13),
            'rs14': ll[13],
            'rm14_data': pg1_new_beds.objects.all().filter(roon_no=14),
            'rs15': ll[14],
            'rm15_data': pg1_new_beds.objects.all().filter(roon_no=15),
            'rs16': ll[15],
            'rm16_data': pg1_new_beds.objects.all().filter(roon_no=16),
            'rs17': ll[16],
            'rm17_data': pg1_new_beds.objects.all().filter(roon_no=17),
            'rs18': ll[17],
            'rm18_data': pg1_new_beds.objects.all().filter(roon_no=18),
            'rs19': ll[18],
            'rm19_data': pg1_new_beds.objects.all().filter(roon_no=19),
            'rs20': ll[19],
            'rm20_data': pg1_new_beds.objects.all().filter(roon_no=20),
            'rs21': ll[20],
            'rm21_data': pg1_new_beds.objects.all().filter(roon_no=21),
            'rs22': ll[21],
            'rm22_data': pg1_new_beds.objects.all().filter(roon_no=22),

        }
        return render(request, 'branches/branch6/live_print_report/live_monthly_details/march/march_print_live.html', context)
    return render(request, 'index.html')



def april_details_live6(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch6/live_print_report/live_monthly_details/april/april_details_live.html', context)
    return render(request, 'index.html')

def april_print_live6(request):
    if 'username' in request.session:
        ll = []
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        context = {
            'brname': 'BRANCH 6 Room Creation Form',
            'table_height': '60px',

            'rs1': ll[0],
            'rm1_data': pg1_new_beds.objects.all().filter(roon_no=1),
            # 'g1_data':g1_data,
            'rs2': ll[1],
            'rm2_data': pg1_new_beds.objects.all().filter(roon_no=2),
            'rs3': ll[2],
            'rm3_data': pg1_new_beds.objects.all().filter(roon_no=3),
            'rs4': ll[3],
            'rm4_data': pg1_new_beds.objects.all().filter(roon_no=4),
            'rs5': ll[4],
            'rm5_data': pg1_new_beds.objects.all().filter(roon_no=5),
            'rs6': ll[5],
            'rm6_data': pg1_new_beds.objects.all().filter(roon_no=6),
            'rs7': ll[6],
            'rm7_data': pg1_new_beds.objects.all().filter(roon_no=7),
            'rs8': ll[7],
            'rm8_data': pg1_new_beds.objects.all().filter(roon_no=8),
            'rs9': ll[8],
            'rm9_data': pg1_new_beds.objects.all().filter(roon_no=9),
            'rs10': ll[9],
            'rm10_data': pg1_new_beds.objects.all().filter(roon_no=10),
            'rs11': ll[10],
            'rm11_data': pg1_new_beds.objects.all().filter(roon_no=11),
            'rs12': ll[11],
            'rm12_data': pg1_new_beds.objects.all().filter(roon_no=12),
            'rs13': ll[12],
            'rm13_data': pg1_new_beds.objects.all().filter(roon_no=13),
            'rs14': ll[13],
            'rm14_data': pg1_new_beds.objects.all().filter(roon_no=14),
            'rs15': ll[14],
            'rm15_data': pg1_new_beds.objects.all().filter(roon_no=15),
            'rs16': ll[15],
            'rm16_data': pg1_new_beds.objects.all().filter(roon_no=16),
            'rs17': ll[16],
            'rm17_data': pg1_new_beds.objects.all().filter(roon_no=17),
            'rs18': ll[17],
            'rm18_data': pg1_new_beds.objects.all().filter(roon_no=18),
            'rs19': ll[18],
            'rm19_data': pg1_new_beds.objects.all().filter(roon_no=19),
            'rs20': ll[19],
            'rm20_data': pg1_new_beds.objects.all().filter(roon_no=20),
            'rs21': ll[20],
            'rm21_data': pg1_new_beds.objects.all().filter(roon_no=21),
            'rs22': ll[21],
            'rm22_data': pg1_new_beds.objects.all().filter(roon_no=22),

        }
        return render(request, 'branches/branch6/live_print_report/live_monthly_details/april/april_print_live.html', context)
    return render(request, 'index.html')


def may_details_live6(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch6/live_print_report/live_monthly_details/may/may_details_live.html', context)
    return render(request, 'index.html')

def may_print_live6(request):
    if 'username' in request.session:
        ll = []
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        context = {
            'brname': 'BRANCH 6 Room Creation Form',
            'table_height': '60px',

            'rs1': ll[0],
            'rm1_data': pg1_new_beds.objects.all().filter(roon_no=1),
            # 'g1_data':g1_data,
            'rs2': ll[1],
            'rm2_data': pg1_new_beds.objects.all().filter(roon_no=2),
            'rs3': ll[2],
            'rm3_data': pg1_new_beds.objects.all().filter(roon_no=3),
            'rs4': ll[3],
            'rm4_data': pg1_new_beds.objects.all().filter(roon_no=4),
            'rs5': ll[4],
            'rm5_data': pg1_new_beds.objects.all().filter(roon_no=5),
            'rs6': ll[5],
            'rm6_data': pg1_new_beds.objects.all().filter(roon_no=6),
            'rs7': ll[6],
            'rm7_data': pg1_new_beds.objects.all().filter(roon_no=7),
            'rs8': ll[7],
            'rm8_data': pg1_new_beds.objects.all().filter(roon_no=8),
            'rs9': ll[8],
            'rm9_data': pg1_new_beds.objects.all().filter(roon_no=9),
            'rs10': ll[9],
            'rm10_data': pg1_new_beds.objects.all().filter(roon_no=10),
            'rs11': ll[10],
            'rm11_data': pg1_new_beds.objects.all().filter(roon_no=11),
            'rs12': ll[11],
            'rm12_data': pg1_new_beds.objects.all().filter(roon_no=12),
            'rs13': ll[12],
            'rm13_data': pg1_new_beds.objects.all().filter(roon_no=13),
            'rs14': ll[13],
            'rm14_data': pg1_new_beds.objects.all().filter(roon_no=14),
            'rs15': ll[14],
            'rm15_data': pg1_new_beds.objects.all().filter(roon_no=15),
            'rs16': ll[15],
            'rm16_data': pg1_new_beds.objects.all().filter(roon_no=16),
            'rs17': ll[16],
            'rm17_data': pg1_new_beds.objects.all().filter(roon_no=17),
            'rs18': ll[17],
            'rm18_data': pg1_new_beds.objects.all().filter(roon_no=18),
            'rs19': ll[18],
            'rm19_data': pg1_new_beds.objects.all().filter(roon_no=19),
            'rs20': ll[19],
            'rm20_data': pg1_new_beds.objects.all().filter(roon_no=20),
            'rs21': ll[20],
            'rm21_data': pg1_new_beds.objects.all().filter(roon_no=21),
            'rs22': ll[21],
            'rm22_data': pg1_new_beds.objects.all().filter(roon_no=22),

        }
        return render(request, 'branches/branch6/live_print_report/live_monthly_details/may/may_print_live.html', context)
    return render(request, 'index.html')

def june_details_live6(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch6/live_print_report/live_monthly_details/june/june_dtails_live.html', context)
    return render(request, 'index.html')

def june_print_live6(request):
    if 'username' in request.session:
        ll = []
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        context = {
            'brname': 'BRANCH 6 Room Creation Form',
            'table_height': '60px',

            'rs1': ll[0],
            'rm1_data': pg1_new_beds.objects.all().filter(roon_no=1),
            # 'g1_data':g1_data,
            'rs2': ll[1],
            'rm2_data': pg1_new_beds.objects.all().filter(roon_no=2),
            'rs3': ll[2],
            'rm3_data': pg1_new_beds.objects.all().filter(roon_no=3),
            'rs4': ll[3],
            'rm4_data': pg1_new_beds.objects.all().filter(roon_no=4),
            'rs5': ll[4],
            'rm5_data': pg1_new_beds.objects.all().filter(roon_no=5),
            'rs6': ll[5],
            'rm6_data': pg1_new_beds.objects.all().filter(roon_no=6),
            'rs7': ll[6],
            'rm7_data': pg1_new_beds.objects.all().filter(roon_no=7),
            'rs8': ll[7],
            'rm8_data': pg1_new_beds.objects.all().filter(roon_no=8),
            'rs9': ll[8],
            'rm9_data': pg1_new_beds.objects.all().filter(roon_no=9),
            'rs10': ll[9],
            'rm10_data': pg1_new_beds.objects.all().filter(roon_no=10),
            'rs11': ll[10],
            'rm11_data': pg1_new_beds.objects.all().filter(roon_no=11),
            'rs12': ll[11],
            'rm12_data': pg1_new_beds.objects.all().filter(roon_no=12),
            'rs13': ll[12],
            'rm13_data': pg1_new_beds.objects.all().filter(roon_no=13),
            'rs14': ll[13],
            'rm14_data': pg1_new_beds.objects.all().filter(roon_no=14),
            'rs15': ll[14],
            'rm15_data': pg1_new_beds.objects.all().filter(roon_no=15),
            'rs16': ll[15],
            'rm16_data': pg1_new_beds.objects.all().filter(roon_no=16),
            'rs17': ll[16],
            'rm17_data': pg1_new_beds.objects.all().filter(roon_no=17),
            'rs18': ll[17],
            'rm18_data': pg1_new_beds.objects.all().filter(roon_no=18),
            'rs19': ll[18],
            'rm19_data': pg1_new_beds.objects.all().filter(roon_no=19),
            'rs20': ll[19],
            'rm20_data': pg1_new_beds.objects.all().filter(roon_no=20),
            'rs21': ll[20],
            'rm21_data': pg1_new_beds.objects.all().filter(roon_no=21),
            'rs22': ll[21],
            'rm22_data': pg1_new_beds.objects.all().filter(roon_no=22),

        }
        return render(request, 'branches/branch6/live_print_report/live_monthly_details/june/june_print_live.html', context)
    return render(request, 'index.html')

def july_details_live6(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch6/live_print_report/live_monthly_details/july/july_details_live.html', context)
    return render(request, 'index.html')

def july_print_live6(request):
    if 'username' in request.session:
        ll = []
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        context = {
            'brname': 'BRANCH 6 Room Creation Form',
            'table_height': '60px',

            'rs1': ll[0],
            'rm1_data': pg1_new_beds.objects.all().filter(roon_no=1),
            # 'g1_data':g1_data,
            'rs2': ll[1],
            'rm2_data': pg1_new_beds.objects.all().filter(roon_no=2),
            'rs3': ll[2],
            'rm3_data': pg1_new_beds.objects.all().filter(roon_no=3),
            'rs4': ll[3],
            'rm4_data': pg1_new_beds.objects.all().filter(roon_no=4),
            'rs5': ll[4],
            'rm5_data': pg1_new_beds.objects.all().filter(roon_no=5),
            'rs6': ll[5],
            'rm6_data': pg1_new_beds.objects.all().filter(roon_no=6),
            'rs7': ll[6],
            'rm7_data': pg1_new_beds.objects.all().filter(roon_no=7),
            'rs8': ll[7],
            'rm8_data': pg1_new_beds.objects.all().filter(roon_no=8),
            'rs9': ll[8],
            'rm9_data': pg1_new_beds.objects.all().filter(roon_no=9),
            'rs10': ll[9],
            'rm10_data': pg1_new_beds.objects.all().filter(roon_no=10),
            'rs11': ll[10],
            'rm11_data': pg1_new_beds.objects.all().filter(roon_no=11),
            'rs12': ll[11],
            'rm12_data': pg1_new_beds.objects.all().filter(roon_no=12),
            'rs13': ll[12],
            'rm13_data': pg1_new_beds.objects.all().filter(roon_no=13),
            'rs14': ll[13],
            'rm14_data': pg1_new_beds.objects.all().filter(roon_no=14),
            'rs15': ll[14],
            'rm15_data': pg1_new_beds.objects.all().filter(roon_no=15),
            'rs16': ll[15],
            'rm16_data': pg1_new_beds.objects.all().filter(roon_no=16),
            'rs17': ll[16],
            'rm17_data': pg1_new_beds.objects.all().filter(roon_no=17),
            'rs18': ll[17],
            'rm18_data': pg1_new_beds.objects.all().filter(roon_no=18),
            'rs19': ll[18],
            'rm19_data': pg1_new_beds.objects.all().filter(roon_no=19),
            'rs20': ll[19],
            'rm20_data': pg1_new_beds.objects.all().filter(roon_no=20),
            'rs21': ll[20],
            'rm21_data': pg1_new_beds.objects.all().filter(roon_no=21),
            'rs22': ll[21],
            'rm22_data': pg1_new_beds.objects.all().filter(roon_no=22),

        }
        return render(request, 'branches/branch6/live_print_report/live_monthly_details/july/july_print_live.html', context)
    return render(request, 'index.html')


def auguest_details_live6(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch6/live_print_report/live_monthly_details/aug/aug_details_live.html', context)
    return render(request, 'index.html')

def auguest_print_live6(request):
    if 'username' in request.session:
        ll = []
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        context = {
            'brname': 'BRANCH 6 Room Creation Form',
            'table_height': '60px',

            'rs1': ll[0],
            'rm1_data': pg1_new_beds.objects.all().filter(roon_no=1),
            # 'g1_data':g1_data,
            'rs2': ll[1],
            'rm2_data': pg1_new_beds.objects.all().filter(roon_no=2),
            'rs3': ll[2],
            'rm3_data': pg1_new_beds.objects.all().filter(roon_no=3),
            'rs4': ll[3],
            'rm4_data': pg1_new_beds.objects.all().filter(roon_no=4),
            'rs5': ll[4],
            'rm5_data': pg1_new_beds.objects.all().filter(roon_no=5),
            'rs6': ll[5],
            'rm6_data': pg1_new_beds.objects.all().filter(roon_no=6),
            'rs7': ll[6],
            'rm7_data': pg1_new_beds.objects.all().filter(roon_no=7),
            'rs8': ll[7],
            'rm8_data': pg1_new_beds.objects.all().filter(roon_no=8),
            'rs9': ll[8],
            'rm9_data': pg1_new_beds.objects.all().filter(roon_no=9),
            'rs10': ll[9],
            'rm10_data': pg1_new_beds.objects.all().filter(roon_no=10),
            'rs11': ll[10],
            'rm11_data': pg1_new_beds.objects.all().filter(roon_no=11),
            'rs12': ll[11],
            'rm12_data': pg1_new_beds.objects.all().filter(roon_no=12),
            'rs13': ll[12],
            'rm13_data': pg1_new_beds.objects.all().filter(roon_no=13),
            'rs14': ll[13],
            'rm14_data': pg1_new_beds.objects.all().filter(roon_no=14),
            'rs15': ll[14],
            'rm15_data': pg1_new_beds.objects.all().filter(roon_no=15),
            'rs16': ll[15],
            'rm16_data': pg1_new_beds.objects.all().filter(roon_no=16),
            'rs17': ll[16],
            'rm17_data': pg1_new_beds.objects.all().filter(roon_no=17),
            'rs18': ll[17],
            'rm18_data': pg1_new_beds.objects.all().filter(roon_no=18),
            'rs19': ll[18],
            'rm19_data': pg1_new_beds.objects.all().filter(roon_no=19),
            'rs20': ll[19],
            'rm20_data': pg1_new_beds.objects.all().filter(roon_no=20),
            'rs21': ll[20],
            'rm21_data': pg1_new_beds.objects.all().filter(roon_no=21),
            'rs22': ll[21],
            'rm22_data': pg1_new_beds.objects.all().filter(roon_no=22),

        }
        return render(request, 'branches/branch6/live_print_report/live_monthly_details/aug/aug_print_live.html', context)
    return render(request, 'index.html')


def sept_details_live6(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch6/live_print_report/live_monthly_details/sept/sept_details_live.html', context)
    return render(request, 'index.html')

def sept_print_live6(request):
    if 'username' in request.session:
        ll = []
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        context = {
            'brname': 'BRANCH 6 Room Creation Form',
            'table_height': '60px',

            'rs1': ll[0],
            'rm1_data': pg1_new_beds.objects.all().filter(roon_no=1),
            # 'g1_data':g1_data,
            'rs2': ll[1],
            'rm2_data': pg1_new_beds.objects.all().filter(roon_no=2),
            'rs3': ll[2],
            'rm3_data': pg1_new_beds.objects.all().filter(roon_no=3),
            'rs4': ll[3],
            'rm4_data': pg1_new_beds.objects.all().filter(roon_no=4),
            'rs5': ll[4],
            'rm5_data': pg1_new_beds.objects.all().filter(roon_no=5),
            'rs6': ll[5],
            'rm6_data': pg1_new_beds.objects.all().filter(roon_no=6),
            'rs7': ll[6],
            'rm7_data': pg1_new_beds.objects.all().filter(roon_no=7),
            'rs8': ll[7],
            'rm8_data': pg1_new_beds.objects.all().filter(roon_no=8),
            'rs9': ll[8],
            'rm9_data': pg1_new_beds.objects.all().filter(roon_no=9),
            'rs10': ll[9],
            'rm10_data': pg1_new_beds.objects.all().filter(roon_no=10),
            'rs11': ll[10],
            'rm11_data': pg1_new_beds.objects.all().filter(roon_no=11),
            'rs12': ll[11],
            'rm12_data': pg1_new_beds.objects.all().filter(roon_no=12),
            'rs13': ll[12],
            'rm13_data': pg1_new_beds.objects.all().filter(roon_no=13),
            'rs14': ll[13],
            'rm14_data': pg1_new_beds.objects.all().filter(roon_no=14),
            'rs15': ll[14],
            'rm15_data': pg1_new_beds.objects.all().filter(roon_no=15),
            'rs16': ll[15],
            'rm16_data': pg1_new_beds.objects.all().filter(roon_no=16),
            'rs17': ll[16],
            'rm17_data': pg1_new_beds.objects.all().filter(roon_no=17),
            'rs18': ll[17],
            'rm18_data': pg1_new_beds.objects.all().filter(roon_no=18),
            'rs19': ll[18],
            'rm19_data': pg1_new_beds.objects.all().filter(roon_no=19),
            'rs20': ll[19],
            'rm20_data': pg1_new_beds.objects.all().filter(roon_no=20),
            'rs21': ll[20],
            'rm21_data': pg1_new_beds.objects.all().filter(roon_no=21),
            'rs22': ll[21],
            'rm22_data': pg1_new_beds.objects.all().filter(roon_no=22),

        }
        return render(request, 'branches/branch6/live_print_report/live_monthly_details/sept/sept_print_live.html', context)
    return render(request, 'index.html')


def october_details_live6(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch6/live_print_report/live_monthly_details/oct/oct_details_live.html', context)
    return render(request, 'index.html')

def october_print_live6(request):
    if 'username' in request.session:
        ll = []
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        context = {
            'brname': 'BRANCH 6 Room Creation Form',
            'table_height': '60px',

            'rs1': ll[0],
            'rm1_data': pg1_new_beds.objects.all().filter(roon_no=1),
            # 'g1_data':g1_data,
            'rs2': ll[1],
            'rm2_data': pg1_new_beds.objects.all().filter(roon_no=2),
            'rs3': ll[2],
            'rm3_data': pg1_new_beds.objects.all().filter(roon_no=3),
            'rs4': ll[3],
            'rm4_data': pg1_new_beds.objects.all().filter(roon_no=4),
            'rs5': ll[4],
            'rm5_data': pg1_new_beds.objects.all().filter(roon_no=5),
            'rs6': ll[5],
            'rm6_data': pg1_new_beds.objects.all().filter(roon_no=6),
            'rs7': ll[6],
            'rm7_data': pg1_new_beds.objects.all().filter(roon_no=7),
            'rs8': ll[7],
            'rm8_data': pg1_new_beds.objects.all().filter(roon_no=8),
            'rs9': ll[8],
            'rm9_data': pg1_new_beds.objects.all().filter(roon_no=9),
            'rs10': ll[9],
            'rm10_data': pg1_new_beds.objects.all().filter(roon_no=10),
            'rs11': ll[10],
            'rm11_data': pg1_new_beds.objects.all().filter(roon_no=11),
            'rs12': ll[11],
            'rm12_data': pg1_new_beds.objects.all().filter(roon_no=12),
            'rs13': ll[12],
            'rm13_data': pg1_new_beds.objects.all().filter(roon_no=13),
            'rs14': ll[13],
            'rm14_data': pg1_new_beds.objects.all().filter(roon_no=14),
            'rs15': ll[14],
            'rm15_data': pg1_new_beds.objects.all().filter(roon_no=15),
            'rs16': ll[15],
            'rm16_data': pg1_new_beds.objects.all().filter(roon_no=16),
            'rs17': ll[16],
            'rm17_data': pg1_new_beds.objects.all().filter(roon_no=17),
            'rs18': ll[17],
            'rm18_data': pg1_new_beds.objects.all().filter(roon_no=18),
            'rs19': ll[18],
            'rm19_data': pg1_new_beds.objects.all().filter(roon_no=19),
            'rs20': ll[19],
            'rm20_data': pg1_new_beds.objects.all().filter(roon_no=20),
            'rs21': ll[20],
            'rm21_data': pg1_new_beds.objects.all().filter(roon_no=21),
            'rs22': ll[21],
            'rm22_data': pg1_new_beds.objects.all().filter(roon_no=22),

        }
        return render(request, 'branches/branch6/live_print_report/live_monthly_details/oct/oct_print_live.html', context)
    return render(request, 'index.html')


def nov_details_live6(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch6/live_print_report/live_monthly_details/nov/nov_details_live.html', context)
    return render(request, 'index.html')

def nov_print_live6(request):
    if 'username' in request.session:
        ll = []
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        context = {
            'brname': 'BRANCH 6 Room Creation Form',
            'table_height': '60px',

            'rs1': ll[0],
            'rm1_data': pg1_new_beds.objects.all().filter(roon_no=1),
            # 'g1_data':g1_data,
            'rs2': ll[1],
            'rm2_data': pg1_new_beds.objects.all().filter(roon_no=2),
            'rs3': ll[2],
            'rm3_data': pg1_new_beds.objects.all().filter(roon_no=3),
            'rs4': ll[3],
            'rm4_data': pg1_new_beds.objects.all().filter(roon_no=4),
            'rs5': ll[4],
            'rm5_data': pg1_new_beds.objects.all().filter(roon_no=5),
            'rs6': ll[5],
            'rm6_data': pg1_new_beds.objects.all().filter(roon_no=6),
            'rs7': ll[6],
            'rm7_data': pg1_new_beds.objects.all().filter(roon_no=7),
            'rs8': ll[7],
            'rm8_data': pg1_new_beds.objects.all().filter(roon_no=8),
            'rs9': ll[8],
            'rm9_data': pg1_new_beds.objects.all().filter(roon_no=9),
            'rs10': ll[9],
            'rm10_data': pg1_new_beds.objects.all().filter(roon_no=10),
            'rs11': ll[10],
            'rm11_data': pg1_new_beds.objects.all().filter(roon_no=11),
            'rs12': ll[11],
            'rm12_data': pg1_new_beds.objects.all().filter(roon_no=12),
            'rs13': ll[12],
            'rm13_data': pg1_new_beds.objects.all().filter(roon_no=13),
            'rs14': ll[13],
            'rm14_data': pg1_new_beds.objects.all().filter(roon_no=14),
            'rs15': ll[14],
            'rm15_data': pg1_new_beds.objects.all().filter(roon_no=15),
            'rs16': ll[15],
            'rm16_data': pg1_new_beds.objects.all().filter(roon_no=16),
            'rs17': ll[16],
            'rm17_data': pg1_new_beds.objects.all().filter(roon_no=17),
            'rs18': ll[17],
            'rm18_data': pg1_new_beds.objects.all().filter(roon_no=18),
            'rs19': ll[18],
            'rm19_data': pg1_new_beds.objects.all().filter(roon_no=19),
            'rs20': ll[19],
            'rm20_data': pg1_new_beds.objects.all().filter(roon_no=20),
            'rs21': ll[20],
            'rm21_data': pg1_new_beds.objects.all().filter(roon_no=21),
            'rs22': ll[21],
            'rm22_data': pg1_new_beds.objects.all().filter(roon_no=22),

        }
        return render(request, 'branches/branch6/live_print_report/live_monthly_details/nov/nov_print_live.html', context)
    return render(request, 'index.html')


def dec_details_live6(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch6/live_print_report/live_monthly_details/dec/dec_details_live.html', context)
    return render(request, 'index.html')

def dec_print_live6(request):
    if 'username' in request.session:
        ll = []
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        context = {
            'brname': 'BRANCH 6 Room Creation Form',
            'table_height': '60px',

            'rs1': ll[0],
            'rm1_data': pg1_new_beds.objects.all().filter(roon_no=1),
            # 'g1_data':g1_data,
            'rs2': ll[1],
            'rm2_data': pg1_new_beds.objects.all().filter(roon_no=2),
            'rs3': ll[2],
            'rm3_data': pg1_new_beds.objects.all().filter(roon_no=3),
            'rs4': ll[3],
            'rm4_data': pg1_new_beds.objects.all().filter(roon_no=4),
            'rs5': ll[4],
            'rm5_data': pg1_new_beds.objects.all().filter(roon_no=5),
            'rs6': ll[5],
            'rm6_data': pg1_new_beds.objects.all().filter(roon_no=6),
            'rs7': ll[6],
            'rm7_data': pg1_new_beds.objects.all().filter(roon_no=7),
            'rs8': ll[7],
            'rm8_data': pg1_new_beds.objects.all().filter(roon_no=8),
            'rs9': ll[8],
            'rm9_data': pg1_new_beds.objects.all().filter(roon_no=9),
            'rs10': ll[9],
            'rm10_data': pg1_new_beds.objects.all().filter(roon_no=10),
            'rs11': ll[10],
            'rm11_data': pg1_new_beds.objects.all().filter(roon_no=11),
            'rs12': ll[11],
            'rm12_data': pg1_new_beds.objects.all().filter(roon_no=12),
            'rs13': ll[12],
            'rm13_data': pg1_new_beds.objects.all().filter(roon_no=13),
            'rs14': ll[13],
            'rm14_data': pg1_new_beds.objects.all().filter(roon_no=14),
            'rs15': ll[14],
            'rm15_data': pg1_new_beds.objects.all().filter(roon_no=15),
            'rs16': ll[15],
            'rm16_data': pg1_new_beds.objects.all().filter(roon_no=16),
            'rs17': ll[16],
            'rm17_data': pg1_new_beds.objects.all().filter(roon_no=17),
            'rs18': ll[17],
            'rm18_data': pg1_new_beds.objects.all().filter(roon_no=18),
            'rs19': ll[18],
            'rm19_data': pg1_new_beds.objects.all().filter(roon_no=19),
            'rs20': ll[19],
            'rm20_data': pg1_new_beds.objects.all().filter(roon_no=20),
            'rs21': ll[20],
            'rm21_data': pg1_new_beds.objects.all().filter(roon_no=21),
            'rs22': ll[21],
            'rm22_data': pg1_new_beds.objects.all().filter(roon_no=22),

        }
        return render(request, 'branches/branch6/live_print_report/live_monthly_details/dec/dec_print_live.html', context)
    return render(request, 'index.html')



def viewall_vaccant_room6(request):
    context = {
        'vr': pg1_new_beds.objects.all().exclude(flag=2).order_by('roon_no')
    }
    return render(request, 'branches/branch6/reports/vaccant_room/viewall_vaccant_room.html', context)

#########FULL PAID GUEST START HERE ############

def full_paid_guest6(request):
    context = {
        'fpr': pg1_new_guest.objects.all().filter(flag=2,june_due_amt='0',june_rent_flag=200).order_by('roon_no')
    }
    return render(request, 'branches/branch6/reports/paid_rent/full_paid_guest.html', context)

def may_full_paid_guest6(request):
    context = {
        'fpr': pg1_new_guest.objects.all().filter(flag=2,may_due_amt='0',may_rent_flag=200).order_by('roon_no')
    }
    return render(request, 'branches/branch6/reports/paid_rent/paid_monthly_reports/may/may_full_paid_guest.html', context)

def june_full_paid_guest6(request):
    context = {
        'fpr': pg1_new_guest.objects.all().filter(flag=2,june_due_amt='0',june_rent_flag=200).order_by('roon_no')
    }
    return render(request, 'branches/branch6/reports/paid_rent/paid_monthly_reports/jun/june_full_paid_guest.html', context)

def july_full_paid_guest6(request):
    context = {
        'fpr': pg1_new_guest.objects.all().filter(flag=2,july_due_amt='0',july_rent_flag=200).order_by('roon_no')
    }
    return render(request, 'branches/branch6/reports/paid_rent/paid_monthly_reports/jul/july_full_paid_guest.html', context)

def aug_full_paid_guest6(request):
    context = {
        'fpr': pg1_new_guest.objects.all().filter(flag=2,auguest_due_amt='0',auguest_rent_flag=200).order_by('roon_no')
    }
    return render(request, 'branches/branch6/reports/paid_rent/paid_monthly_reports/aug/aug_full_paid_guest.html', context)
#

#########FULL PAID GUEST END HERE ############

#########PARTIALLY PAID GUEST START HERE ############

def partially_paid_guest_choose_months6(request):
    if 'username' in request.session:
        return render(request, 'branches/branch6/reports/paid_rent/partially_paid_guest_choose_months.html')

def may_partially_paid_guest6(request):
    context = {
        'ppr': pg1_new_guest.objects.all().filter(flag=2,may_rent_flag=200).exclude(may_due_amt='0').order_by('roon_no')
    }
    return render(request, 'branches/branch6/reports/paid_rent/paid_monthly_reports/may/may_partially_paid_guest.html', context)
def table_may_partially_paid_guest6(request):
    context = {
        'ppr': pg1_new_guest.objects.all().filter(flag=2,may_rent_flag=200).exclude(may_due_amt='0').order_by('roon_no'),
    }
    return render(request, 'branches/branch6/reports/paid_rent/paid_monthly_reports/may/table_may_partially_paid_guest.html', context)

def june_partially_paid_guest6(request):
    context = {
        'ppr': pg1_new_guest.objects.all().filter(flag=2,june_rent_flag=200).exclude(june_due_amt='0').order_by('roon_no')
    }
    return render(request, 'branches/branch6/reports/paid_rent/paid_monthly_reports/jun/june_partially_paid_guest.html', context)
def table_june_partially_paid_guest6(request):
    context = {
        'ppr': pg1_new_guest.objects.all().filter(flag=2,june_rent_flag=200).exclude(june_due_amt='0').order_by('roon_no'),
    }
    return render(request, 'branches/branch6/reports/paid_rent/paid_monthly_reports/jun/table_june_partially_paid_guest.html', context)

def july_partially_paid_guest6(request):
    context = {
        'ppr': pg1_new_guest.objects.all().filter(flag=2,july_rent_flag=200).exclude(july_due_amt='0').order_by('roon_no')
    }
    return render(request, 'branches/branch6/reports/paid_rent/paid_monthly_reports/jul/july_partially_paid_guest.html', context)
def table_july_partially_paid_guest6(request):
    context = {
        'ppr': pg1_new_guest.objects.all().filter(flag=2,july_rent_flag=200).exclude(july_due_amt='0').order_by('roon_no'),
    }
    return render(request, 'branches/branch6/reports/paid_rent/paid_monthly_reports/jul/table_july_partially_paid_guest.html', context)



#########PARTIALLY PAID GUEST START HERE ############

