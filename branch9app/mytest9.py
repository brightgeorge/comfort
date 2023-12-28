import datetime as datetime
from django.shortcuts import render
from django.contrib import messages

# from myapp.models import *pg1_new_beds
from branch9app.models import *
# from branch9app.models import pg1_new_beds,pg1_new_guest
import datetime
from . import admin_dashboard_calculations_br9
import branch9app

database_name = 'cpg'
database_password = '#123.com#'
# database_password = ''
database_user = 'root'
database_host = 'localhost'

import pymysql as py
import pymysql.cursors




def custom_view_all_new_guest9(request):
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


        us = request.session['username']
        bgs = background_color.objects.all().filter(username=us)
        bg = background_color.objects.all().filter(username=us).exists()
        a = []
        if bg == True:
            a.append(us)
        else:
            a.append('f')

        context = {
            'bg': bgs,
            'us': us,
            'th_us': a[0],
            'name': us,


            'brname': 'BRANCH 9 Room Creation Form',
            # 'br': pg1_new_beds.objects.all().filter(roon_no=101).order_by('roon_no'),
            'rn1': l[0],
            'table_height': '50px',

            'g2': ll[0],
            'g2_data': pg1_new_beds.objects.all().filter(roon_no=2),


            'rs101': ll[1],
            '101_data': pg1_new_beds.objects.all().filter(roon_no=101),
            'rs102': ll[2],
            '102_data': pg1_new_beds.objects.all().filter(roon_no=102),
            'rs103': ll[3],
            '103_data': pg1_new_beds.objects.all().filter(roon_no=103),
            'rs104': ll[4],
            '104_data': pg1_new_beds.objects.all().filter(roon_no=104),
            'rs105': ll[5],
            '105_data': pg1_new_beds.objects.all().filter(roon_no=105),
            'rs106': ll[6],
            '106_data': pg1_new_beds.objects.all().filter(roon_no=106),
            'rs107': ll[7],
            '107_data': pg1_new_beds.objects.all().filter(roon_no=107),

            'rs108': ll[8],
            '108_data': pg1_new_beds.objects.all().filter(roon_no=108),
            'rs109': ll[9],
            '109_data': pg1_new_beds.objects.all().filter(roon_no=109),
            'rs110': ll[10],
            '110_data': pg1_new_beds.objects.all().filter(roon_no=110),
            'rs111': ll[11],
            '111_data': pg1_new_beds.objects.all().filter(roon_no=111),
            'rs112': ll[12],
            '112_data': pg1_new_beds.objects.all().filter(roon_no=112),

            'rs201': ll[13],
            '201_data': pg1_new_beds.objects.all().filter(roon_no=201),
            'rs202': ll[14],
            '202_data': pg1_new_beds.objects.all().filter(roon_no=202),
            'rs203': ll[15],
            '203_data': pg1_new_beds.objects.all().filter(roon_no=203),
            'rs204': ll[16],
            '204_data': pg1_new_beds.objects.all().filter(roon_no=204),
            'rs205': ll[17],
            '205_data': pg1_new_beds.objects.all().filter(roon_no=205),
            'rs206': ll[18],
            '206_data': pg1_new_beds.objects.all().filter(roon_no=206),

            'rs207': ll[19],
            '207_data': pg1_new_beds.objects.all().filter(roon_no=207),
            'rs208': ll[20],
            '208_data': pg1_new_beds.objects.all().filter(roon_no=208),
            'rs209': ll[21],
            '209_data': pg1_new_beds.objects.all().filter(roon_no=209),
            'rs210': ll[22],
            '210_data': pg1_new_beds.objects.all().filter(roon_no=210),
            'rs211': ll[23],
            '211_data': pg1_new_beds.objects.all().filter(roon_no=211),
            'rs212': ll[24],
            '212_data': pg1_new_beds.objects.all().filter(roon_no=212),

            ##############################################

            'rs301': ll[25],
            '301_data': pg1_new_beds.objects.all().filter(roon_no=301),
            'rs302': ll[26],
            '302_data': pg1_new_beds.objects.all().filter(roon_no=302),
            'rs303': ll[27],
            '303_data': pg1_new_beds.objects.all().filter(roon_no=303),
            'rs304': ll[28],
            '304_data': pg1_new_beds.objects.all().filter(roon_no=304),
            'rs305': ll[29],
            '305_data': pg1_new_beds.objects.all().filter(roon_no=305),
            'rs306': ll[30],
            '306_data': pg1_new_beds.objects.all().filter(roon_no=306),

            'rs307': ll[31],
            '307_data': pg1_new_beds.objects.all().filter(roon_no=307),
            'rs308': ll[32],
            '308_data': pg1_new_beds.objects.all().filter(roon_no=308),
            'rs309': ll[33],
            '309_data': pg1_new_beds.objects.all().filter(roon_no=309),
            'rs310': ll[34],
            '310_data': pg1_new_beds.objects.all().filter(roon_no=310),
            'rs311': ll[35],
            '311_data': pg1_new_beds.objects.all().filter(roon_no=311),
            'rs312': ll[36],
            '312_data': pg1_new_beds.objects.all().filter(roon_no=312),

            ########################

            'rs401': ll[37],
            '401_data': pg1_new_beds.objects.all().filter(roon_no=401),
            'rs402': ll[38],
            '402_data': pg1_new_beds.objects.all().filter(roon_no=402),
            'rs403': ll[39],
            '403_data': pg1_new_beds.objects.all().filter(roon_no=403),
            'rs404': ll[40],
            '404_data': pg1_new_beds.objects.all().filter(roon_no=404),
            'rs405': ll[41],
            '405_data': pg1_new_beds.objects.all().filter(roon_no=405),
            'rs406': ll[42],
            '406_data': pg1_new_beds.objects.all().filter(roon_no=406),

            'rs407': ll[43],
            '407_data': pg1_new_beds.objects.all().filter(roon_no=407),
            'rs408': ll[44],
            '408_data': pg1_new_beds.objects.all().filter(roon_no=408),
            'rs409': ll[45],
            '409_data': pg1_new_beds.objects.all().filter(roon_no=409),
            'rs410': ll[46],
            '410_data': pg1_new_beds.objects.all().filter(roon_no=410),
            'rs411': ll[47],
            '411_data': pg1_new_beds.objects.all().filter(roon_no=411),
            'rs412': ll[48],
            '412_data': pg1_new_beds.objects.all().filter(roon_no=412),

            ######################################

            'rs501': ll[49],
            '501_data': pg1_new_beds.objects.all().filter(roon_no=501),
            'rs502': ll[50],
            '502_data': pg1_new_beds.objects.all().filter(roon_no=502),
            'rs503': ll[51],
            '503_data': pg1_new_beds.objects.all().filter(roon_no=503),
            'rs504': ll[52],
            '504_data': pg1_new_beds.objects.all().filter(roon_no=504),
            'rs505': ll[53],
            '505_data': pg1_new_beds.objects.all().filter(roon_no=505),
            'rs506': ll[54],
            '506_data': pg1_new_beds.objects.all().filter(roon_no=506),

            'rs507': ll[55],
            '507_data': pg1_new_beds.objects.all().filter(roon_no=507),
            'rs508': ll[56],
            '508_data': pg1_new_beds.objects.all().filter(roon_no=508),
            'rs509': ll[57],
            '509_data': pg1_new_beds.objects.all().filter(roon_no=509),
            'rs510': ll[58],
            '510_data': pg1_new_beds.objects.all().filter(roon_no=510),
            'rs511': ll[59],
            '511_data': pg1_new_beds.objects.all().filter(roon_no=511),
            'rs512': ll[60],
            '512_data': pg1_new_beds.objects.all().filter(roon_no=512),

            ###########################
            'myl': ll,

        }

        return render(request, 'branches/branch9/mytest/custom_view_all_new_guest.html', context)
    return render(request, 'index.html')

