import datetime as datetime
from django.shortcuts import render
from django.contrib import messages

from myapp.models import *

import datetime

database_name = 'cpg'
database_password = '#123.com#'
database_user = 'root'
database_host = 'localhost'

import pymysql as py
import pymysql.cursors

def detailed_report_choose_months(request):
    if 'username' in request.session:
        return render(request, 'branches/branch1/live_print_report/detailed_report_choose_months.html')
    return render(request, 'index.html')

def may_details_live(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch1/live_print_report/live_monthly_details/may/may_details_live.html', context)
    return render(request, 'index.html')

def may_print_live(request):
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
            'br': pg1_new_beds.objects.all().filter(roon_no=1).order_by('roon_no'),
            'rn1': l[0],
            'table_height': '40px',

            'g1': ll[0],
            'g1_data': pg1_new_beds.objects.all().filter(roon_no=1),
            # 'g1_data':g1_data,
            'g2': ll[1],
            'g2_data': pg1_new_beds.objects.all().filter(roon_no=2),
            'g3': ll[2],
            'g3_data': pg1_new_beds.objects.all().filter(roon_no=3),
            'g5': ll[3],
            'g5_data': pg1_new_beds.objects.all().filter(roon_no=4),
            'g6': ll[4],
            'g6_data': pg1_new_beds.objects.all().filter(roon_no=5),
            'g7': ll[5],
            'g7_data': pg1_new_beds.objects.all().filter(roon_no=6),
            'g8': ll[6],
            'g8_data': pg1_new_beds.objects.all().filter(roon_no=7),
            'g9': ll[7],
            'g9_data': pg1_new_beds.objects.all().filter(roon_no=8),
            'rs101': ll[8],
            '101_data': pg1_new_beds.objects.all().filter(roon_no=9),
            'rs102': ll[9],
            '102_data': pg1_new_beds.objects.all().filter(roon_no=10),
            'rs103': ll[10],
            '103_data': pg1_new_beds.objects.all().filter(roon_no=11),
            'rs104': ll[11],
            '104_data': pg1_new_beds.objects.all().filter(roon_no=12),
            'rs105': ll[12],
            '105_data': pg1_new_beds.objects.all().filter(roon_no=13),
            'rs106': ll[13],
            '106_data': pg1_new_beds.objects.all().filter(roon_no=14),
            'rs107': ll[14],
            '107_data': pg1_new_beds.objects.all().filter(roon_no=15),
            'rs108': ll[15],
            '108_data': pg1_new_beds.objects.all().filter(roon_no=16),
            'rs109': ll[16],
            '109_data': pg1_new_beds.objects.all().filter(roon_no=17),
            'rs110': ll[17],
            '110_data': pg1_new_beds.objects.all().filter(roon_no=18),
            'rs111': ll[18],
            '111_data': pg1_new_beds.objects.all().filter(roon_no=19),
            'rs112': ll[19],
            '112_data': pg1_new_beds.objects.all().filter(roon_no=20),
            'rs113': ll[20],
            '113_data': pg1_new_beds.objects.all().filter(roon_no=21),
            'rs114': ll[21],
            '114_data': pg1_new_beds.objects.all().filter(roon_no=22),
            'rs115': ll[22],
            '115_data': pg1_new_beds.objects.all().filter(roon_no=23),
            'rs116': ll[23],
            '116_data': pg1_new_beds.objects.all().filter(roon_no=24),
            'rs117': ll[24],
            '117_data': pg1_new_beds.objects.all().filter(roon_no=25),
            'rs118': ll[25],
            '118_data': pg1_new_beds.objects.all().filter(roon_no=26),

            'rs201': ll[26],
            '201_data': pg1_new_beds.objects.all().filter(roon_no=27),
            'rs202': ll[27],
            '202_data': pg1_new_beds.objects.all().filter(roon_no=28),
            'rs203': ll[28],
            '203_data': pg1_new_beds.objects.all().filter(roon_no=29),
            'rs204': ll[29],
            '204_data': pg1_new_beds.objects.all().filter(roon_no=30),
            'rs205': ll[30],
            '205_data': pg1_new_beds.objects.all().filter(roon_no=31),
            'rs206': ll[31],
            '206_data': pg1_new_beds.objects.all().filter(roon_no=32),

            'rs207': ll[32],
            '207_data': pg1_new_beds.objects.all().filter(roon_no=33),
            'rs208': ll[33],
            '208_data': pg1_new_beds.objects.all().filter(roon_no=34),
            'rs209': ll[34],
            '209_data': pg1_new_beds.objects.all().filter(roon_no=35),
            'rs210': ll[35],
            '210_data': pg1_new_beds.objects.all().filter(roon_no=36),
            'rs211': ll[36],
            '211_data': pg1_new_beds.objects.all().filter(roon_no=37),
            'rs212': ll[37],
            '212_data': pg1_new_beds.objects.all().filter(roon_no=38),
            'rs213': ll[38],
            '213_data': pg1_new_beds.objects.all().filter(roon_no=39),

            'rs214': ll[39],
            '214_data': pg1_new_beds.objects.all().filter(roon_no=40),
            'rs215': ll[40],
            '215_data': pg1_new_beds.objects.all().filter(roon_no=41),
            'rs216': ll[41],
            '216_data': pg1_new_beds.objects.all().filter(roon_no=42),
            'rs217': ll[42],
            '217_data': pg1_new_beds.objects.all().filter(roon_no=43),
            'rs218': ll[43],
            '218_data': pg1_new_beds.objects.all().filter(roon_no=44),

            ##############################################

            'rs301': ll[44],
            '301_data': pg1_new_beds.objects.all().filter(roon_no=45),
            'rs302': ll[45],
            '302_data': pg1_new_beds.objects.all().filter(roon_no=46),
            'rs303': ll[46],
            '303_data': pg1_new_beds.objects.all().filter(roon_no=47),
            'rs304': ll[47],
            '304_data': pg1_new_beds.objects.all().filter(roon_no=48),
            'rs305': ll[48],
            '305_data': pg1_new_beds.objects.all().filter(roon_no=49),
            'rs306': ll[49],
            '306_data': pg1_new_beds.objects.all().filter(roon_no=50),

            'rs307': ll[50],
            '307_data': pg1_new_beds.objects.all().filter(roon_no=51),
            'rs308': ll[51],
            '308_data': pg1_new_beds.objects.all().filter(roon_no=52),
            'rs309': ll[52],
            '309_data': pg1_new_beds.objects.all().filter(roon_no=53),
            'rs310': ll[53],
            '310_data': pg1_new_beds.objects.all().filter(roon_no=54),
            'rs311': ll[54],
            '311_data': pg1_new_beds.objects.all().filter(roon_no=55),
            'rs312': ll[55],
            '312_data': pg1_new_beds.objects.all().filter(roon_no=56),
            'rs313': ll[56],
            '313_data': pg1_new_beds.objects.all().filter(roon_no=57),

            'rs314': ll[57],
            '314_data': pg1_new_beds.objects.all().filter(roon_no=58),
            'rs315': ll[58],
            '315_data': pg1_new_beds.objects.all().filter(roon_no=59),
            'rs316': ll[59],
            '316_data': pg1_new_beds.objects.all().filter(roon_no=60),
            'rs317': ll[60],
            '317_data': pg1_new_beds.objects.all().filter(roon_no=61),
            'rs318': ll[61],
            '318_data': pg1_new_beds.objects.all().filter(roon_no=62),

            ########################

            'rs401': ll[62],
            '401_data': pg1_new_beds.objects.all().filter(roon_no=63),
            'rs402': ll[63],
            '402_data': pg1_new_beds.objects.all().filter(roon_no=64),
            'rs403': ll[64],
            '403_data': pg1_new_beds.objects.all().filter(roon_no=65),
            'rs404': ll[65],
            '404_data': pg1_new_beds.objects.all().filter(roon_no=66),
            'rs405': ll[66],
            '405_data': pg1_new_beds.objects.all().filter(roon_no=67),
            'rs406': ll[67],
            '406_data': pg1_new_beds.objects.all().filter(roon_no=68),

            'rs407': ll[68],
            '407_data': pg1_new_beds.objects.all().filter(roon_no=69),
            'rs408': ll[69],
            '408_data': pg1_new_beds.objects.all().filter(roon_no=70),
            'rs409': ll[70],
            '409_data': pg1_new_beds.objects.all().filter(roon_no=71),
            'rs410': ll[71],
            '410_data': pg1_new_beds.objects.all().filter(roon_no=72),
            'rs411': ll[72],
            '411_data': pg1_new_beds.objects.all().filter(roon_no=73),
            'rs412': ll[73],
            '412_data': pg1_new_beds.objects.all().filter(roon_no=74),

            'rs501': ll[74],
            '501_data': pg1_new_beds.objects.all().filter(roon_no=75),

            ###########################
            'myl': ll,

        }
        return render(request, 'branches/branch1/live_print_report/live_monthly_details/may/may_print_live.html', context)
    return render(request, 'index.html')

def june_details_live(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch1/live_print_report/live_monthly_details/june/june_dtails_live.html', context)
    return render(request, 'index.html')

def june_print_live(request):
    if 'username' in request.session:
        ll = []
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        context = {
            'brname': 'BRANCH 2 Room Creation Form',
            'br': pg1_new_beds.objects.all().filter(roon_no=1).order_by('roon_no'),

            'table_height': '40px',

            'g1': ll[0],
            'g1_data': pg1_new_beds.objects.all().filter(roon_no=1),
            # 'g1_data':g1_data,
            'g2': ll[1],
            'g2_data': pg1_new_beds.objects.all().filter(roon_no=2),
            'g3': ll[2],
            'g3_data': pg1_new_beds.objects.all().filter(roon_no=3),
            'g5': ll[3],
            'g5_data': pg1_new_beds.objects.all().filter(roon_no=4),
            'g6': ll[4],
            'g6_data': pg1_new_beds.objects.all().filter(roon_no=5),
            'g7': ll[5],
            'g7_data': pg1_new_beds.objects.all().filter(roon_no=6),
            'g8': ll[6],
            'g8_data': pg1_new_beds.objects.all().filter(roon_no=7),
            'g9': ll[7],
            'g9_data': pg1_new_beds.objects.all().filter(roon_no=8),
            'rs101': ll[8],
            '101_data': pg1_new_beds.objects.all().filter(roon_no=9),
            'rs102': ll[9],
            '102_data': pg1_new_beds.objects.all().filter(roon_no=10),
            'rs103': ll[10],
            '103_data': pg1_new_beds.objects.all().filter(roon_no=11),
            'rs104': ll[11],
            '104_data': pg1_new_beds.objects.all().filter(roon_no=12),
            'rs105': ll[12],
            '105_data': pg1_new_beds.objects.all().filter(roon_no=13),
            'rs106': ll[13],
            '106_data': pg1_new_beds.objects.all().filter(roon_no=14),
            'rs107': ll[14],
            '107_data': pg1_new_beds.objects.all().filter(roon_no=15),
            'rs108': ll[15],
            '108_data': pg1_new_beds.objects.all().filter(roon_no=16),
            'rs109': ll[16],
            '109_data': pg1_new_beds.objects.all().filter(roon_no=17),
            'rs110': ll[17],
            '110_data': pg1_new_beds.objects.all().filter(roon_no=18),
            'rs111': ll[18],
            '111_data': pg1_new_beds.objects.all().filter(roon_no=19),
            'rs112': ll[19],
            '112_data': pg1_new_beds.objects.all().filter(roon_no=20),
            'rs113': ll[20],
            '113_data': pg1_new_beds.objects.all().filter(roon_no=21),
            'rs114': ll[21],
            '114_data': pg1_new_beds.objects.all().filter(roon_no=22),
            'rs115': ll[22],
            '115_data': pg1_new_beds.objects.all().filter(roon_no=23),
            'rs116': ll[23],
            '116_data': pg1_new_beds.objects.all().filter(roon_no=24),
            'rs117': ll[24],
            '117_data': pg1_new_beds.objects.all().filter(roon_no=25),
            'rs118': ll[25],
            '118_data': pg1_new_beds.objects.all().filter(roon_no=26),

            'rs201': ll[26],
            '201_data': pg1_new_beds.objects.all().filter(roon_no=27),
            'rs202': ll[27],
            '202_data': pg1_new_beds.objects.all().filter(roon_no=28),
            'rs203': ll[28],
            '203_data': pg1_new_beds.objects.all().filter(roon_no=29),
            'rs204': ll[29],
            '204_data': pg1_new_beds.objects.all().filter(roon_no=30),
            'rs205': ll[30],
            '205_data': pg1_new_beds.objects.all().filter(roon_no=31),
            'rs206': ll[31],
            '206_data': pg1_new_beds.objects.all().filter(roon_no=32),

            'rs207': ll[32],
            '207_data': pg1_new_beds.objects.all().filter(roon_no=33),
            'rs208': ll[33],
            '208_data': pg1_new_beds.objects.all().filter(roon_no=34),
            'rs209': ll[34],
            '209_data': pg1_new_beds.objects.all().filter(roon_no=35),
            'rs210': ll[35],
            '210_data': pg1_new_beds.objects.all().filter(roon_no=36),
            'rs211': ll[36],
            '211_data': pg1_new_beds.objects.all().filter(roon_no=37),
            'rs212': ll[37],
            '212_data': pg1_new_beds.objects.all().filter(roon_no=38),
            'rs213': ll[38],
            '213_data': pg1_new_beds.objects.all().filter(roon_no=39),

            'rs214': ll[39],
            '214_data': pg1_new_beds.objects.all().filter(roon_no=40),
            'rs215': ll[40],
            '215_data': pg1_new_beds.objects.all().filter(roon_no=41),
            'rs216': ll[41],
            '216_data': pg1_new_beds.objects.all().filter(roon_no=42),
            'rs217': ll[42],
            '217_data': pg1_new_beds.objects.all().filter(roon_no=43),
            'rs218': ll[43],
            '218_data': pg1_new_beds.objects.all().filter(roon_no=44),

            ##############################################

            'rs301': ll[44],
            '301_data': pg1_new_beds.objects.all().filter(roon_no=45),
            'rs302': ll[45],
            '302_data': pg1_new_beds.objects.all().filter(roon_no=46),
            'rs303': ll[46],
            '303_data': pg1_new_beds.objects.all().filter(roon_no=47),
            'rs304': ll[47],
            '304_data': pg1_new_beds.objects.all().filter(roon_no=48),
            'rs305': ll[48],
            '305_data': pg1_new_beds.objects.all().filter(roon_no=49),
            'rs306': ll[49],
            '306_data': pg1_new_beds.objects.all().filter(roon_no=50),

            'rs307': ll[50],
            '307_data': pg1_new_beds.objects.all().filter(roon_no=51),
            'rs308': ll[51],
            '308_data': pg1_new_beds.objects.all().filter(roon_no=52),
            'rs309': ll[52],
            '309_data': pg1_new_beds.objects.all().filter(roon_no=53),
            'rs310': ll[53],
            '310_data': pg1_new_beds.objects.all().filter(roon_no=54),
            'rs311': ll[54],
            '311_data': pg1_new_beds.objects.all().filter(roon_no=55),
            'rs312': ll[55],
            '312_data': pg1_new_beds.objects.all().filter(roon_no=56),
            'rs313': ll[56],
            '313_data': pg1_new_beds.objects.all().filter(roon_no=57),

            'rs314': ll[57],
            '314_data': pg1_new_beds.objects.all().filter(roon_no=58),
            'rs315': ll[58],
            '315_data': pg1_new_beds.objects.all().filter(roon_no=59),
            'rs316': ll[59],
            '316_data': pg1_new_beds.objects.all().filter(roon_no=60),
            'rs317': ll[60],
            '317_data': pg1_new_beds.objects.all().filter(roon_no=61),
            'rs318': ll[61],
            '318_data': pg1_new_beds.objects.all().filter(roon_no=62),

            ########################

            'rs401': ll[62],
            '401_data': pg1_new_beds.objects.all().filter(roon_no=63),
            'rs402': ll[63],
            '402_data': pg1_new_beds.objects.all().filter(roon_no=64),
            'rs403': ll[64],
            '403_data': pg1_new_beds.objects.all().filter(roon_no=65),
            'rs404': ll[65],
            '404_data': pg1_new_beds.objects.all().filter(roon_no=66),
            'rs405': ll[66],
            '405_data': pg1_new_beds.objects.all().filter(roon_no=67),
            'rs406': ll[67],
            '406_data': pg1_new_beds.objects.all().filter(roon_no=68),

            'rs407': ll[68],
            '407_data': pg1_new_beds.objects.all().filter(roon_no=69),
            'rs408': ll[69],
            '408_data': pg1_new_beds.objects.all().filter(roon_no=70),
            'rs409': ll[70],
            '409_data': pg1_new_beds.objects.all().filter(roon_no=71),
            'rs410': ll[71],
            '410_data': pg1_new_beds.objects.all().filter(roon_no=72),
            'rs411': ll[72],
            '411_data': pg1_new_beds.objects.all().filter(roon_no=73),
            'rs412': ll[73],
            '412_data': pg1_new_beds.objects.all().filter(roon_no=74),

            'rs501': ll[74],
            '501_data': pg1_new_beds.objects.all().filter(roon_no=75),

            ###########################
            'myl': ll,

        }
        return render(request, 'branches/branch1/live_print_report/live_monthly_details/june/june_print_live.html', context)
    return render(request, 'index.html')


def july_details_live(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch1/live_print_report/live_monthly_details/july/july_details_live.html', context)
    return render(request, 'index.html')

def july_print_live(request):
    if 'username' in request.session:
        ll = []
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        context = {
            'brname': 'BRANCH 2 Room Creation Form',
            'br': pg1_new_beds.objects.all().filter(roon_no=1).order_by('roon_no'),

            'table_height': '40px',

            'g1': ll[0],
            'g1_data': pg1_new_beds.objects.all().filter(roon_no=1),
            # 'g1_data':g1_data,
            'g2': ll[1],
            'g2_data': pg1_new_beds.objects.all().filter(roon_no=2),
            'g3': ll[2],
            'g3_data': pg1_new_beds.objects.all().filter(roon_no=3),
            'g5': ll[3],
            'g5_data': pg1_new_beds.objects.all().filter(roon_no=4),
            'g6': ll[4],
            'g6_data': pg1_new_beds.objects.all().filter(roon_no=5),
            'g7': ll[5],
            'g7_data': pg1_new_beds.objects.all().filter(roon_no=6),
            'g8': ll[6],
            'g8_data': pg1_new_beds.objects.all().filter(roon_no=7),
            'g9': ll[7],
            'g9_data': pg1_new_beds.objects.all().filter(roon_no=8),
            'rs101': ll[8],
            '101_data': pg1_new_beds.objects.all().filter(roon_no=9),
            'rs102': ll[9],
            '102_data': pg1_new_beds.objects.all().filter(roon_no=10),
            'rs103': ll[10],
            '103_data': pg1_new_beds.objects.all().filter(roon_no=11),
            'rs104': ll[11],
            '104_data': pg1_new_beds.objects.all().filter(roon_no=12),
            'rs105': ll[12],
            '105_data': pg1_new_beds.objects.all().filter(roon_no=13),
            'rs106': ll[13],
            '106_data': pg1_new_beds.objects.all().filter(roon_no=14),
            'rs107': ll[14],
            '107_data': pg1_new_beds.objects.all().filter(roon_no=15),
            'rs108': ll[15],
            '108_data': pg1_new_beds.objects.all().filter(roon_no=16),
            'rs109': ll[16],
            '109_data': pg1_new_beds.objects.all().filter(roon_no=17),
            'rs110': ll[17],
            '110_data': pg1_new_beds.objects.all().filter(roon_no=18),
            'rs111': ll[18],
            '111_data': pg1_new_beds.objects.all().filter(roon_no=19),
            'rs112': ll[19],
            '112_data': pg1_new_beds.objects.all().filter(roon_no=20),
            'rs113': ll[20],
            '113_data': pg1_new_beds.objects.all().filter(roon_no=21),
            'rs114': ll[21],
            '114_data': pg1_new_beds.objects.all().filter(roon_no=22),
            'rs115': ll[22],
            '115_data': pg1_new_beds.objects.all().filter(roon_no=23),
            'rs116': ll[23],
            '116_data': pg1_new_beds.objects.all().filter(roon_no=24),
            'rs117': ll[24],
            '117_data': pg1_new_beds.objects.all().filter(roon_no=25),
            'rs118': ll[25],
            '118_data': pg1_new_beds.objects.all().filter(roon_no=26),

            'rs201': ll[26],
            '201_data': pg1_new_beds.objects.all().filter(roon_no=27),
            'rs202': ll[27],
            '202_data': pg1_new_beds.objects.all().filter(roon_no=28),
            'rs203': ll[28],
            '203_data': pg1_new_beds.objects.all().filter(roon_no=29),
            'rs204': ll[29],
            '204_data': pg1_new_beds.objects.all().filter(roon_no=30),
            'rs205': ll[30],
            '205_data': pg1_new_beds.objects.all().filter(roon_no=31),
            'rs206': ll[31],
            '206_data': pg1_new_beds.objects.all().filter(roon_no=32),

            'rs207': ll[32],
            '207_data': pg1_new_beds.objects.all().filter(roon_no=33),
            'rs208': ll[33],
            '208_data': pg1_new_beds.objects.all().filter(roon_no=34),
            'rs209': ll[34],
            '209_data': pg1_new_beds.objects.all().filter(roon_no=35),
            'rs210': ll[35],
            '210_data': pg1_new_beds.objects.all().filter(roon_no=36),
            'rs211': ll[36],
            '211_data': pg1_new_beds.objects.all().filter(roon_no=37),
            'rs212': ll[37],
            '212_data': pg1_new_beds.objects.all().filter(roon_no=38),
            'rs213': ll[38],
            '213_data': pg1_new_beds.objects.all().filter(roon_no=39),

            'rs214': ll[39],
            '214_data': pg1_new_beds.objects.all().filter(roon_no=40),
            'rs215': ll[40],
            '215_data': pg1_new_beds.objects.all().filter(roon_no=41),
            'rs216': ll[41],
            '216_data': pg1_new_beds.objects.all().filter(roon_no=42),
            'rs217': ll[42],
            '217_data': pg1_new_beds.objects.all().filter(roon_no=43),
            'rs218': ll[43],
            '218_data': pg1_new_beds.objects.all().filter(roon_no=44),

            ##############################################

            'rs301': ll[44],
            '301_data': pg1_new_beds.objects.all().filter(roon_no=45),
            'rs302': ll[45],
            '302_data': pg1_new_beds.objects.all().filter(roon_no=46),
            'rs303': ll[46],
            '303_data': pg1_new_beds.objects.all().filter(roon_no=47),
            'rs304': ll[47],
            '304_data': pg1_new_beds.objects.all().filter(roon_no=48),
            'rs305': ll[48],
            '305_data': pg1_new_beds.objects.all().filter(roon_no=49),
            'rs306': ll[49],
            '306_data': pg1_new_beds.objects.all().filter(roon_no=50),

            'rs307': ll[50],
            '307_data': pg1_new_beds.objects.all().filter(roon_no=51),
            'rs308': ll[51],
            '308_data': pg1_new_beds.objects.all().filter(roon_no=52),
            'rs309': ll[52],
            '309_data': pg1_new_beds.objects.all().filter(roon_no=53),
            'rs310': ll[53],
            '310_data': pg1_new_beds.objects.all().filter(roon_no=54),
            'rs311': ll[54],
            '311_data': pg1_new_beds.objects.all().filter(roon_no=55),
            'rs312': ll[55],
            '312_data': pg1_new_beds.objects.all().filter(roon_no=56),
            'rs313': ll[56],
            '313_data': pg1_new_beds.objects.all().filter(roon_no=57),

            'rs314': ll[57],
            '314_data': pg1_new_beds.objects.all().filter(roon_no=58),
            'rs315': ll[58],
            '315_data': pg1_new_beds.objects.all().filter(roon_no=59),
            'rs316': ll[59],
            '316_data': pg1_new_beds.objects.all().filter(roon_no=60),
            'rs317': ll[60],
            '317_data': pg1_new_beds.objects.all().filter(roon_no=61),
            'rs318': ll[61],
            '318_data': pg1_new_beds.objects.all().filter(roon_no=62),

            ########################

            'rs401': ll[62],
            '401_data': pg1_new_beds.objects.all().filter(roon_no=63),
            'rs402': ll[63],
            '402_data': pg1_new_beds.objects.all().filter(roon_no=64),
            'rs403': ll[64],
            '403_data': pg1_new_beds.objects.all().filter(roon_no=65),
            'rs404': ll[65],
            '404_data': pg1_new_beds.objects.all().filter(roon_no=66),
            'rs405': ll[66],
            '405_data': pg1_new_beds.objects.all().filter(roon_no=67),
            'rs406': ll[67],
            '406_data': pg1_new_beds.objects.all().filter(roon_no=68),

            'rs407': ll[68],
            '407_data': pg1_new_beds.objects.all().filter(roon_no=69),
            'rs408': ll[69],
            '408_data': pg1_new_beds.objects.all().filter(roon_no=70),
            'rs409': ll[70],
            '409_data': pg1_new_beds.objects.all().filter(roon_no=71),
            'rs410': ll[71],
            '410_data': pg1_new_beds.objects.all().filter(roon_no=72),
            'rs411': ll[72],
            '411_data': pg1_new_beds.objects.all().filter(roon_no=73),
            'rs412': ll[73],
            '412_data': pg1_new_beds.objects.all().filter(roon_no=74),

            'rs501': ll[74],
            '501_data': pg1_new_beds.objects.all().filter(roon_no=75),

            ###########################
            'myl': ll,

        }
        return render(request, 'branches/branch1/live_print_report/live_monthly_details/july/july_print_live.html', context)
    return render(request, 'index.html')



def viewall_vaccant_room(request):
    context = {
        'vr': pg1_new_beds.objects.all().exclude(flag=2).order_by('roon_no')
    }
    return render(request, 'branches/branch1/reports/vaccant_room/viewall_vaccant_room.html', context)

#########FULL PAID GUEST START HERE ############

def full_paid_guest(request):
    context = {
        'fpr': pg1_new_guest.objects.all().filter(flag=2,june_due_amt='0',june_rent_flag=200).order_by('roon_no')
    }
    return render(request, 'branches/branch1/reports/paid_rent/full_paid_guest.html', context)

def may_full_paid_guest(request):
    context = {
        'fpr': pg1_new_guest.objects.all().filter(flag=2,may_due_amt='0',may_rent_flag=200).order_by('roon_no')
    }
    return render(request, 'branches/branch1/reports/paid_rent/paid_monthly_reports/may/may_full_paid_guest.html', context)

def june_full_paid_guest(request):
    context = {
        'fpr': pg1_new_guest.objects.all().filter(flag=2,june_due_amt='0',june_rent_flag=200).order_by('roon_no')
    }
    return render(request, 'branches/branch1/reports/paid_rent/paid_monthly_reports/jun/june_full_paid_guest.html', context)

def july_full_paid_guest(request):
    context = {
        'fpr': pg1_new_guest.objects.all().filter(flag=2,july_due_amt='0',july_rent_flag=200).order_by('roon_no')
    }
    return render(request, 'branches/branch1/reports/paid_rent/paid_monthly_reports/jul/july_full_paid_guest.html', context)

def aug_full_paid_guest(request):
    context = {
        'fpr': pg1_new_guest.objects.all().filter(flag=2,auguest_due_amt='0',auguest_rent_flag=200).order_by('roon_no')
    }
    return render(request, 'branches/branch1/reports/paid_rent/paid_monthly_reports/aug/aug_full_paid_guest.html', context)
#

#########FULL PAID GUEST END HERE ############

#########PARTIALLY PAID GUEST START HERE ############

def partially_paid_guest_choose_months(request):
    if 'username' in request.session:
        return render(request, 'branches/branch1/reports/paid_rent/partially_paid_guest_choose_months.html')

def may_partially_paid_guest(request):
    context = {
        'ppr': pg1_new_guest.objects.all().filter(flag=2,may_rent_flag=200).exclude(may_due_amt='0').order_by('roon_no')
    }
    return render(request, 'branches/branch1/reports/paid_rent/paid_monthly_reports/may/may_partially_paid_guest.html', context)
def table_may_partially_paid_guest(request):
    context = {
        'ppr': pg1_new_guest.objects.all().filter(flag=2,may_rent_flag=200).exclude(may_due_amt='0').order_by('roon_no'),
    }
    return render(request, 'branches/branch1/reports/paid_rent/paid_monthly_reports/may/table_may_partially_paid_guest.html', context)

def june_partially_paid_guest(request):
    context = {
        'ppr': pg1_new_guest.objects.all().filter(flag=2,june_rent_flag=200).exclude(june_due_amt='0').order_by('roon_no')
    }
    return render(request, 'branches/branch1/reports/paid_rent/paid_monthly_reports/jun/june_partially_paid_guest.html', context)
def table_june_partially_paid_guest(request):
    context = {
        'ppr': pg1_new_guest.objects.all().filter(flag=2,june_rent_flag=200).exclude(june_due_amt='0').order_by('roon_no'),
    }
    return render(request, 'branches/branch1/reports/paid_rent/paid_monthly_reports/jun/table_june_partially_paid_guest.html', context)

def july_partially_paid_guest(request):
    context = {
        'ppr': pg1_new_guest.objects.all().filter(flag=2,july_rent_flag=200).exclude(july_due_amt='0').order_by('roon_no')
    }
    return render(request, 'branches/branch1/reports/paid_rent/paid_monthly_reports/jul/july_partially_paid_guest.html', context)
def table_july_partially_paid_guest(request):
    context = {
        'ppr': pg1_new_guest.objects.all().filter(flag=2,july_rent_flag=200).exclude(july_due_amt='0').order_by('roon_no'),
    }
    return render(request, 'branches/branch1/reports/paid_rent/paid_monthly_reports/jul/table_july_partially_paid_guest.html', context)



#########PARTIALLY PAID GUEST START HERE ############
