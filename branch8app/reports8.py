import datetime as datetime
from django.shortcuts import render
from django.contrib import messages

# from myapp.models import *
from branch8app.models import *
import datetime

database_name = 'cpg'
database_password = '#123.com#'
database_user = 'root'
database_host = 'localhost'

import pymysql as py
import pymysql.cursors

def detailed_report_choose_months8(request):
    if 'username' in request.session:
        return render(request, 'branches/branch8/live_print_report/detailed_report_choose_months.html')
    return render(request, 'index.html')

def may_details_live8(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all().order_by('roon_no'),
        }
        return render(request, 'branches/branch8/live_print_report/live_monthly_details/may/may_details_live.html', context)
    return render(request, 'index.html')

def may_print_live8(request):
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
            'brname': 'BRANCH 8 Room Creation Form',
            'table_height': '50px',


            'g2': ll[0],
            'g2_data': pg1_new_beds.objects.all().filter(roon_no=2),
            'g4': ll[1],
            'g4_data': pg1_new_beds.objects.all().filter(roon_no=4),
            'g5': ll[2],
            'g5_data': pg1_new_beds.objects.all().filter(roon_no=5),
            'g6': ll[3],
            'g6_data': pg1_new_beds.objects.all().filter(roon_no=6),
            'g7': ll[4],
            'g7_data': pg1_new_beds.objects.all().filter(roon_no=7),
            'g8': ll[5],
            'g8_data': pg1_new_beds.objects.all().filter(roon_no=8),

            'rs101': ll[6],
            '101_data': pg1_new_beds.objects.all().filter(roon_no=101),
            'rs102': ll[7],
            '102_data': pg1_new_beds.objects.all().filter(roon_no=102),
            'rs103': ll[8],
            '103_data': pg1_new_beds.objects.all().filter(roon_no=103),
            'rs104': ll[9],
            '104_data': pg1_new_beds.objects.all().filter(roon_no=104),
            'rs105': ll[10],
            '105_data': pg1_new_beds.objects.all().filter(roon_no=105),
            'rs106': ll[11],
            '106_data': pg1_new_beds.objects.all().filter(roon_no=106),
            'rs107': ll[12],
            '107_data': pg1_new_beds.objects.all().filter(roon_no=107),
            'rs108': ll[13],
            '108_data': pg1_new_beds.objects.all().filter(roon_no=108),
            'rs109': ll[14],
            '109_data': pg1_new_beds.objects.all().filter(roon_no=109),
            'rs110': ll[15],
            '110_data': pg1_new_beds.objects.all().filter(roon_no=110),
            'rs111': ll[16],
            '111_data': pg1_new_beds.objects.all().filter(roon_no=111),
            'rs112': ll[17],
            '112_data': pg1_new_beds.objects.all().filter(roon_no=112),


            'rs201': ll[18],
            '201_data': pg1_new_beds.objects.all().filter(roon_no=201),
            'rs202': ll[19],
            '202_data': pg1_new_beds.objects.all().filter(roon_no=202),
            'rs203': ll[20],
            '203_data': pg1_new_beds.objects.all().filter(roon_no=203),
            'rs204': ll[21],
            '204_data': pg1_new_beds.objects.all().filter(roon_no=204),
            'rs205': ll[22],
            '205_data': pg1_new_beds.objects.all().filter(roon_no=205),
            'rs206': ll[23],
            '206_data': pg1_new_beds.objects.all().filter(roon_no=206),

            'rs207': ll[24],
            '207_data': pg1_new_beds.objects.all().filter(roon_no=207),
            'rs208': ll[25],
            '208_data': pg1_new_beds.objects.all().filter(roon_no=208),
            'rs209': ll[26],
            '209_data': pg1_new_beds.objects.all().filter(roon_no=209),
            'rs210': ll[27],
            '210_data': pg1_new_beds.objects.all().filter(roon_no=210),
            'rs211': ll[28],
            '211_data': pg1_new_beds.objects.all().filter(roon_no=211),
            'rs212': ll[29],
            '212_data': pg1_new_beds.objects.all().filter(roon_no=212),
            'rs213': ll[30],
            '213_data': pg1_new_beds.objects.all().filter(roon_no=213),
            'rs214': ll[31],
            '214_data': pg1_new_beds.objects.all().filter(roon_no=214),


            ##############################################

            'rs301': ll[32],
            '301_data': pg1_new_beds.objects.all().filter(roon_no=301),
            'rs302': ll[33],
            '302_data': pg1_new_beds.objects.all().filter(roon_no=302),
            'rs303': ll[34],
            '303_data': pg1_new_beds.objects.all().filter(roon_no=303),
            'rs304': ll[35],
            '304_data': pg1_new_beds.objects.all().filter(roon_no=304),
            'rs305': ll[36],
            '305_data': pg1_new_beds.objects.all().filter(roon_no=305),
            'rs306': ll[37],
            '306_data': pg1_new_beds.objects.all().filter(roon_no=306),

            'rs307': ll[38],
            '307_data': pg1_new_beds.objects.all().filter(roon_no=307),
            'rs308': ll[39],
            '308_data': pg1_new_beds.objects.all().filter(roon_no=308),
            'rs309': ll[40],
            '309_data': pg1_new_beds.objects.all().filter(roon_no=309),
            'rs310': ll[41],
            '310_data': pg1_new_beds.objects.all().filter(roon_no=310),
            'rs311': ll[42],
            '311_data': pg1_new_beds.objects.all().filter(roon_no=311),
            'rs312': ll[43],
            '312_data': pg1_new_beds.objects.all().filter(roon_no=312),
            'rs313': ll[44],
            '313_data': pg1_new_beds.objects.all().filter(roon_no=313),
            'rs314': ll[45],
            '314_data': pg1_new_beds.objects.all().filter(roon_no=314),

            ########################

            'rs401': ll[46],
            '401_data': pg1_new_beds.objects.all().filter(roon_no=401),
            'rs402': ll[47],
            '402_data': pg1_new_beds.objects.all().filter(roon_no=402),
            'rs403': ll[48],
            '403_data': pg1_new_beds.objects.all().filter(roon_no=403),
            'rs404': ll[49],
            '404_data': pg1_new_beds.objects.all().filter(roon_no=404),
            'rs405': ll[50],
            '405_data': pg1_new_beds.objects.all().filter(roon_no=405),
            'rs406': ll[51],
            '406_data': pg1_new_beds.objects.all().filter(roon_no=406),

            ######################################

            'rs501': ll[52],
            '501_data': pg1_new_beds.objects.all().filter(roon_no=501),
            'rs502': ll[53],
            '502_data': pg1_new_beds.objects.all().filter(roon_no=502),
            'rs503': ll[54],
            '503_data': pg1_new_beds.objects.all().filter(roon_no=503),

            'rs505': ll[55],
            '505_data': pg1_new_beds.objects.all().filter(roon_no=505),
            'rs506': ll[56],
            '506_data': pg1_new_beds.objects.all().filter(roon_no=506),

            ###########################
            'myl': ll,

        }

        return render(request, 'branches/branch8/live_print_report/live_monthly_details/may/may_print_live.html', context)
    return render(request, 'index.html')

def june_details_live8(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all().order_by('roon_no'),
        }
        return render(request, 'branches/branch8/live_print_report/live_monthly_details/june/june_dtails_live.html', context)
    return render(request, 'index.html')

def june_print_live8(request):
    if 'username' in request.session:
        ll = []
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        context = {
            'brname': 'BRANCH 8 Room Creation Form',
            'table_height': '50px',


            'g2': ll[0],
            'g2_data': pg1_new_beds.objects.all().filter(roon_no=2),
            'g4': ll[1],
            'g4_data': pg1_new_beds.objects.all().filter(roon_no=4),
            'g5': ll[2],
            'g5_data': pg1_new_beds.objects.all().filter(roon_no=5),
            'g6': ll[3],
            'g6_data': pg1_new_beds.objects.all().filter(roon_no=6),
            'g7': ll[4],
            'g7_data': pg1_new_beds.objects.all().filter(roon_no=7),
            'g8': ll[5],
            'g8_data': pg1_new_beds.objects.all().filter(roon_no=8),

            'rs101': ll[6],
            '101_data': pg1_new_beds.objects.all().filter(roon_no=101),
            'rs102': ll[7],
            '102_data': pg1_new_beds.objects.all().filter(roon_no=102),
            'rs103': ll[8],
            '103_data': pg1_new_beds.objects.all().filter(roon_no=103),
            'rs104': ll[9],
            '104_data': pg1_new_beds.objects.all().filter(roon_no=104),
            'rs105': ll[10],
            '105_data': pg1_new_beds.objects.all().filter(roon_no=105),
            'rs106': ll[11],
            '106_data': pg1_new_beds.objects.all().filter(roon_no=106),
            'rs107': ll[12],
            '107_data': pg1_new_beds.objects.all().filter(roon_no=107),
            'rs108': ll[13],
            '108_data': pg1_new_beds.objects.all().filter(roon_no=108),
            'rs109': ll[14],
            '109_data': pg1_new_beds.objects.all().filter(roon_no=109),
            'rs110': ll[15],
            '110_data': pg1_new_beds.objects.all().filter(roon_no=110),
            'rs111': ll[16],
            '111_data': pg1_new_beds.objects.all().filter(roon_no=111),
            'rs112': ll[17],
            '112_data': pg1_new_beds.objects.all().filter(roon_no=112),


            'rs201': ll[18],
            '201_data': pg1_new_beds.objects.all().filter(roon_no=201),
            'rs202': ll[19],
            '202_data': pg1_new_beds.objects.all().filter(roon_no=202),
            'rs203': ll[20],
            '203_data': pg1_new_beds.objects.all().filter(roon_no=203),
            'rs204': ll[21],
            '204_data': pg1_new_beds.objects.all().filter(roon_no=204),
            'rs205': ll[22],
            '205_data': pg1_new_beds.objects.all().filter(roon_no=205),
            'rs206': ll[23],
            '206_data': pg1_new_beds.objects.all().filter(roon_no=206),

            'rs207': ll[24],
            '207_data': pg1_new_beds.objects.all().filter(roon_no=207),
            'rs208': ll[25],
            '208_data': pg1_new_beds.objects.all().filter(roon_no=208),
            'rs209': ll[26],
            '209_data': pg1_new_beds.objects.all().filter(roon_no=209),
            'rs210': ll[27],
            '210_data': pg1_new_beds.objects.all().filter(roon_no=210),
            'rs211': ll[28],
            '211_data': pg1_new_beds.objects.all().filter(roon_no=211),
            'rs212': ll[29],
            '212_data': pg1_new_beds.objects.all().filter(roon_no=212),
            'rs213': ll[30],
            '213_data': pg1_new_beds.objects.all().filter(roon_no=213),
            'rs214': ll[31],
            '214_data': pg1_new_beds.objects.all().filter(roon_no=214),


            ##############################################

            'rs301': ll[32],
            '301_data': pg1_new_beds.objects.all().filter(roon_no=301),
            'rs302': ll[33],
            '302_data': pg1_new_beds.objects.all().filter(roon_no=302),
            'rs303': ll[34],
            '303_data': pg1_new_beds.objects.all().filter(roon_no=303),
            'rs304': ll[35],
            '304_data': pg1_new_beds.objects.all().filter(roon_no=304),
            'rs305': ll[36],
            '305_data': pg1_new_beds.objects.all().filter(roon_no=305),
            'rs306': ll[37],
            '306_data': pg1_new_beds.objects.all().filter(roon_no=306),

            'rs307': ll[38],
            '307_data': pg1_new_beds.objects.all().filter(roon_no=307),
            'rs308': ll[39],
            '308_data': pg1_new_beds.objects.all().filter(roon_no=308),
            'rs309': ll[40],
            '309_data': pg1_new_beds.objects.all().filter(roon_no=309),
            'rs310': ll[41],
            '310_data': pg1_new_beds.objects.all().filter(roon_no=310),
            'rs311': ll[42],
            '311_data': pg1_new_beds.objects.all().filter(roon_no=311),
            'rs312': ll[43],
            '312_data': pg1_new_beds.objects.all().filter(roon_no=312),
            'rs313': ll[44],
            '313_data': pg1_new_beds.objects.all().filter(roon_no=313),
            'rs314': ll[45],
            '314_data': pg1_new_beds.objects.all().filter(roon_no=314),

            ########################

            'rs401': ll[46],
            '401_data': pg1_new_beds.objects.all().filter(roon_no=401),
            'rs402': ll[47],
            '402_data': pg1_new_beds.objects.all().filter(roon_no=402),
            'rs403': ll[48],
            '403_data': pg1_new_beds.objects.all().filter(roon_no=403),
            'rs404': ll[49],
            '404_data': pg1_new_beds.objects.all().filter(roon_no=404),
            'rs405': ll[50],
            '405_data': pg1_new_beds.objects.all().filter(roon_no=405),
            'rs406': ll[51],
            '406_data': pg1_new_beds.objects.all().filter(roon_no=406),

            ######################################

            'rs501': ll[52],
            '501_data': pg1_new_beds.objects.all().filter(roon_no=501),
            'rs502': ll[53],
            '502_data': pg1_new_beds.objects.all().filter(roon_no=502),
            'rs503': ll[54],
            '503_data': pg1_new_beds.objects.all().filter(roon_no=503),

            'rs505': ll[55],
            '505_data': pg1_new_beds.objects.all().filter(roon_no=505),
            'rs506': ll[56],
            '506_data': pg1_new_beds.objects.all().filter(roon_no=506),

            ###########################
            'myl': ll,

        }
        return render(request, 'branches/branch8/live_print_report/live_monthly_details/june/june_print_live.html', context)
    return render(request, 'index.html')

def july_details_live8(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all().order_by('roon_no'),
        }
        return render(request, 'branches/branch8/live_print_report/live_monthly_details/july/july_details_live.html', context)
    return render(request, 'index.html')


def july_print_live8(request):
    if 'username' in request.session:
        ll = []
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        context = {
            'brname': 'BRANCH 8 Room Creation Form',
            'table_height': '50px',


            'g2': ll[0],
            'g2_data': pg1_new_beds.objects.all().filter(roon_no=2),
            'g4': ll[1],
            'g4_data': pg1_new_beds.objects.all().filter(roon_no=4),
            'g5': ll[2],
            'g5_data': pg1_new_beds.objects.all().filter(roon_no=5),
            'g6': ll[3],
            'g6_data': pg1_new_beds.objects.all().filter(roon_no=6),
            'g7': ll[4],
            'g7_data': pg1_new_beds.objects.all().filter(roon_no=7),
            'g8': ll[5],
            'g8_data': pg1_new_beds.objects.all().filter(roon_no=8),

            'rs101': ll[6],
            '101_data': pg1_new_beds.objects.all().filter(roon_no=101),
            'rs102': ll[7],
            '102_data': pg1_new_beds.objects.all().filter(roon_no=102),
            'rs103': ll[8],
            '103_data': pg1_new_beds.objects.all().filter(roon_no=103),
            'rs104': ll[9],
            '104_data': pg1_new_beds.objects.all().filter(roon_no=104),
            'rs105': ll[10],
            '105_data': pg1_new_beds.objects.all().filter(roon_no=105),
            'rs106': ll[11],
            '106_data': pg1_new_beds.objects.all().filter(roon_no=106),
            'rs107': ll[12],
            '107_data': pg1_new_beds.objects.all().filter(roon_no=107),
            'rs108': ll[13],
            '108_data': pg1_new_beds.objects.all().filter(roon_no=108),
            'rs109': ll[14],
            '109_data': pg1_new_beds.objects.all().filter(roon_no=109),
            'rs110': ll[15],
            '110_data': pg1_new_beds.objects.all().filter(roon_no=110),
            'rs111': ll[16],
            '111_data': pg1_new_beds.objects.all().filter(roon_no=111),
            'rs112': ll[17],
            '112_data': pg1_new_beds.objects.all().filter(roon_no=112),


            'rs201': ll[18],
            '201_data': pg1_new_beds.objects.all().filter(roon_no=201),
            'rs202': ll[19],
            '202_data': pg1_new_beds.objects.all().filter(roon_no=202),
            'rs203': ll[20],
            '203_data': pg1_new_beds.objects.all().filter(roon_no=203),
            'rs204': ll[21],
            '204_data': pg1_new_beds.objects.all().filter(roon_no=204),
            'rs205': ll[22],
            '205_data': pg1_new_beds.objects.all().filter(roon_no=205),
            'rs206': ll[23],
            '206_data': pg1_new_beds.objects.all().filter(roon_no=206),

            'rs207': ll[24],
            '207_data': pg1_new_beds.objects.all().filter(roon_no=207),
            'rs208': ll[25],
            '208_data': pg1_new_beds.objects.all().filter(roon_no=208),
            'rs209': ll[26],
            '209_data': pg1_new_beds.objects.all().filter(roon_no=209),
            'rs210': ll[27],
            '210_data': pg1_new_beds.objects.all().filter(roon_no=210),
            'rs211': ll[28],
            '211_data': pg1_new_beds.objects.all().filter(roon_no=211),
            'rs212': ll[29],
            '212_data': pg1_new_beds.objects.all().filter(roon_no=212),
            'rs213': ll[30],
            '213_data': pg1_new_beds.objects.all().filter(roon_no=213),
            'rs214': ll[31],
            '214_data': pg1_new_beds.objects.all().filter(roon_no=214),


            ##############################################

            'rs301': ll[32],
            '301_data': pg1_new_beds.objects.all().filter(roon_no=301),
            'rs302': ll[33],
            '302_data': pg1_new_beds.objects.all().filter(roon_no=302),
            'rs303': ll[34],
            '303_data': pg1_new_beds.objects.all().filter(roon_no=303),
            'rs304': ll[35],
            '304_data': pg1_new_beds.objects.all().filter(roon_no=304),
            'rs305': ll[36],
            '305_data': pg1_new_beds.objects.all().filter(roon_no=305),
            'rs306': ll[37],
            '306_data': pg1_new_beds.objects.all().filter(roon_no=306),

            'rs307': ll[38],
            '307_data': pg1_new_beds.objects.all().filter(roon_no=307),
            'rs308': ll[39],
            '308_data': pg1_new_beds.objects.all().filter(roon_no=308),
            'rs309': ll[40],
            '309_data': pg1_new_beds.objects.all().filter(roon_no=309),
            'rs310': ll[41],
            '310_data': pg1_new_beds.objects.all().filter(roon_no=310),
            'rs311': ll[42],
            '311_data': pg1_new_beds.objects.all().filter(roon_no=311),
            'rs312': ll[43],
            '312_data': pg1_new_beds.objects.all().filter(roon_no=312),
            'rs313': ll[44],
            '313_data': pg1_new_beds.objects.all().filter(roon_no=313),
            'rs314': ll[45],
            '314_data': pg1_new_beds.objects.all().filter(roon_no=314),

            ########################

            'rs401': ll[46],
            '401_data': pg1_new_beds.objects.all().filter(roon_no=401),
            'rs402': ll[47],
            '402_data': pg1_new_beds.objects.all().filter(roon_no=402),
            'rs403': ll[48],
            '403_data': pg1_new_beds.objects.all().filter(roon_no=403),
            'rs404': ll[49],
            '404_data': pg1_new_beds.objects.all().filter(roon_no=404),
            'rs405': ll[50],
            '405_data': pg1_new_beds.objects.all().filter(roon_no=405),
            'rs406': ll[51],
            '406_data': pg1_new_beds.objects.all().filter(roon_no=406),

            ######################################

            'rs501': ll[52],
            '501_data': pg1_new_beds.objects.all().filter(roon_no=501),
            'rs502': ll[53],
            '502_data': pg1_new_beds.objects.all().filter(roon_no=502),
            'rs503': ll[54],
            '503_data': pg1_new_beds.objects.all().filter(roon_no=503),

            'rs505': ll[55],
            '505_data': pg1_new_beds.objects.all().filter(roon_no=505),
            'rs506': ll[56],
            '506_data': pg1_new_beds.objects.all().filter(roon_no=506),

            ###########################
            'myl': ll,

        }
        return render(request, 'branches/branch8/live_print_report/live_monthly_details/july/july_print_live.html', context)
    return render(request, 'index.html')


def viewall_vaccant_room8(request):
    context = {
        'vr': pg1_new_beds.objects.all().exclude(flag=2).order_by('roon_no')
    }
    return render(request, 'branches/branch8/reports/vaccant_room/viewall_vaccant_room.html', context)

#########FULL PAID GUEST START HERE ############

def full_paid_guest8(request):
    context = {
        'fpr': pg1_new_guest.objects.all().filter(flag=2,june_due_amt='0',june_rent_flag=200).order_by('roon_no')
    }
    return render(request, 'branches/branch8/reports/paid_rent/full_paid_guest.html', context)

def may_full_paid_guest8(request):
    context = {
        'fpr': pg1_new_guest.objects.all().filter(flag=2,may_due_amt='0',may_rent_flag=200).order_by('roon_no')
    }
    return render(request, 'branches/branch8/reports/paid_rent/paid_monthly_reports/may/may_full_paid_guest.html', context)

def june_full_paid_guest8(request):
    context = {
        'fpr': pg1_new_guest.objects.all().filter(flag=2,june_due_amt='0',june_rent_flag=200).order_by('roon_no')
    }
    return render(request, 'branches/branch8/reports/paid_rent/paid_monthly_reports/jun/june_full_paid_guest.html', context)

def july_full_paid_guest8(request):
    context = {
        'fpr': pg1_new_guest.objects.all().filter(flag=2,july_due_amt='0',july_rent_flag=200).order_by('roon_no')
    }
    return render(request, 'branches/branch8/reports/paid_rent/paid_monthly_reports/jul/july_full_paid_guest.html', context)

def aug_full_paid_guest8(request):
    context = {
        'fpr': pg1_new_guest.objects.all().filter(flag=2,auguest_due_amt='0',auguest_rent_flag=200).order_by('roon_no')
    }
    return render(request, 'branches/branch8/reports/paid_rent/paid_monthly_reports/aug/aug_full_paid_guest.html', context)
#

#########FULL PAID GUEST END HERE ############

#########PARTIALLY PAID GUEST START HERE ############

def partially_paid_guest_choose_months8(request):
    if 'username' in request.session:
        return render(request, 'branches/branch8/reports/paid_rent/partially_paid_guest_choose_months.html')

def may_partially_paid_guest8(request):
    context = {
        'ppr': pg1_new_guest.objects.all().filter(flag=2,may_rent_flag=200).exclude(may_due_amt='0').order_by('roon_no')
    }
    return render(request, 'branches/branch8/reports/paid_rent/paid_monthly_reports/may/may_partially_paid_guest.html', context)
def table_may_partially_paid_guest8(request):
    context = {
        'ppr': pg1_new_guest.objects.all().filter(flag=2,may_rent_flag=200).exclude(may_due_amt='0').order_by('roon_no'),
    }
    return render(request, 'branches/branch8/reports/paid_rent/paid_monthly_reports/may/table_may_partially_paid_guest.html', context)

def june_partially_paid_guest8(request):
    context = {
        'ppr': pg1_new_guest.objects.all().filter(flag=2,june_rent_flag=200).exclude(june_due_amt='0').order_by('roon_no')
    }
    return render(request, 'branches/branch8/reports/paid_rent/paid_monthly_reports/jun/june_partially_paid_guest.html', context)
def table_june_partially_paid_guest8(request):
    context = {
        'ppr': pg1_new_guest.objects.all().filter(flag=2,june_rent_flag=200).exclude(june_due_amt='0').order_by('roon_no'),
    }
    return render(request, 'branches/branch8/reports/paid_rent/paid_monthly_reports/jun/table_june_partially_paid_guest.html', context)

def july_partially_paid_guest8(request):
    context = {
        'ppr': pg1_new_guest.objects.all().filter(flag=2,july_rent_flag=200).exclude(july_due_amt='0').order_by('roon_no')
    }
    return render(request, 'branches/branch8/reports/paid_rent/paid_monthly_reports/jul/july_partially_paid_guest.html', context)
def table_july_partially_paid_guest8(request):
    context = {
        'ppr': pg1_new_guest.objects.all().filter(flag=2,july_rent_flag=200).exclude(july_due_amt='0').order_by('roon_no'),
    }
    return render(request, 'branches/branch8/reports/paid_rent/paid_monthly_reports/jul/table_july_partially_paid_guest.html', context)



#########PARTIALLY PAID GUEST START HERE ############

