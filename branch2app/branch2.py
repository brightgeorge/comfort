import datetime as datetime
from django.shortcuts import render
from django.contrib import messages

#from myapp.models import *
from branch2app.models import *
import datetime
from . import admin_dashboard_calculations_br2
import branch2app

database_name='cpg'
database_password = '#123.com#'
database_user = 'root'
database_host = 'localhost'

import pymysql as py
import pymysql.cursors

#new guest start here

def branch1_dashboard2(request):
    if 'username' in request.session:
        us = request.session['username']
        a = admin_dashboard_calculations_br2.grand_total_collection()
        from datetime import datetime
        cmm = datetime.now().month
        cm = cmm - 1
        gtc = a[cm]

        context = {
            'name': us,
            'total_count_active_guests': admin_dashboard_calculations_br2.total_count_active_guests(),
            'total_count_vaccant_rooms': admin_dashboard_calculations_br2.total_count_vaccant_rooms(),
            'grand_total_collection': gtc,
            'total_collection_advance': admin_dashboard_calculations_br2.total_collection_advance(),
            'total_discount': admin_dashboard_calculations_br2.total_discount(),

            'total_colatable_amount': admin_dashboard_calculations_br2.total_colatable_amount(),
            'total_collected_amount': admin_dashboard_calculations_br2.total_collected_amount(),
            'total_due': admin_dashboard_calculations_br2.total_due(),
            'l': admin_dashboard_calculations_br2.grand_total(),
            # 'total_collection_discount_june' : admin_dashboard_calculations_br2.total_collection_discount_june(),
            'y': admin_dashboard_calculations_br2.bar_chart(),
        }

    return render(request,'branches/branch2/branch1index.html',context)
    return render(request,'index.html')

def admit_guest2(request):
    return render(request,'branches/branch2/new_guest/admit_guest.html')

def br1_admit_guest2(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            selfmob = request.POST.get('selfmobno')
            chk_mob = pg1_new_guest.objects.all().filter(self_mob=selfmob).exists()
            if chk_mob == True:
                l = []
                data = pg1_new_beds.objects.all()
                for i in data:
                    l.append(i.share_type)
                print('l', l)
                context = {
                    'brname': 'BRANCH 2 Room Creation Form',
                    'br': pg1_new_beds.objects.all().filter(roon_no=1).order_by('roon_no'),
                    'rn1': l[0]

                }
                messages.info(request, 'guest already exists')
                #return render(request, 'branches/branch1/new_guest/view_all_new_guest.html', context)
                return view_all_new_guest2(request)
            else:
                name = request.POST.get('name')
                advance = request.POST.get('advance')
                monthlyrent = request.POST.get('monthlyrent')
                selfmob = request.POST.get('selfmobno')
                age = request.POST.get('age')
                address = request.POST.get('paddress')
                pname = request.POST.get('pname')
                pmob = request.POST.get('pmob')

                ic = pg1_new_beds.objects.get(id=id)
                ic.name = name
                ic.advance = advance
                ic.monthly_rent = monthlyrent
                ic.self_mob = selfmob
                ic.age = age
                ic.permanent_address = address
                ic.parent_name = pname
                ic.parent_mob = pmob

                import datetime
                ic.guest_join_date = datetime.date.today()
                d = datetime.datetime.now()
                ic.guest_join_month = d.strftime("%m")

                gcsaves = pg1_new_guest.objects.all()
                a = len(gcsaves)
                ic.guest_code = int(a)+1

                ic.jan_due_amt = 0
                ic.feb_due_amt = 0
                ic.march_due_amt = 0
                ic.april_due_amt = 0
                ic.may_due_amt = 0
                ic.june_due_amt = 0
                ic.july_due_amt = 0
                ic.auguest_due_amt = 0
                ic.sept_due_amt = 0
                ic.october_due_amt = 0
                ic.nov_due_amt = 0
                ic.dec_due_amt = 0

                ic.flag = 2
                ic.save()
##################################################
                gd=[]
                gud=pg1_new_beds.objects.all().filter(id=id)
                for i in gud:
                    gd.append(i.roon_no)
                    gd.append(i.room_name)
                    gd.append(i.bed_no)
                    gd.append(i.bed_code)
                    gd.append(i.share_type)
                print(gd)
                ic = pg1_new_guest()

                ic.roon_no = gd[0]
                ic.room_name = gd[1]
                ic.bed_no = gd[2]

                ic.created_by = request.session['username']
                ic.bed_code = gd[3]
                ic.share_type = gd[4]

                ic.name = name
                ic.advance = advance
                ic.monthly_rent = monthlyrent
                ic.self_mob = selfmob
                ic.age = age
                ic.permanent_address = address
                ic.parent_name = pname
                ic.parent_mob = pmob

                import datetime
                ic.guest_join_date = datetime.date.today()
                d = datetime.datetime.now()
                ic.guest_join_month = d.strftime("%m")

                gcsaves = pg1_new_guest.objects.all()
                a = len(gcsaves)
                ic.guest_code = int(a)+1

                import datetime

                print(datetime.datetime.now())
                x = datetime.datetime.now()
                print(x.strftime("%x"))
                r = x.strftime("%x")
                # r='11/2/23'
                print('my', r)
                print(type(r))
                l = []
                for i in r:
                    l.append(i)
                print(l)

                ll = []
                for i in l:
                    ll.append(l[0])
                    ll.append(l[1])
                    break
                print(ll)

                s = ''
                s = ''.join(ll)
                print('mystr', s)
                ml = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

                tot = 0
                for i in ml:
                    tot = tot + 1
                    if i == s:
                        tot = tot - 1
                        break
                print('mytit', tot)

                n = 12 - tot
                print(n)

                nn = []

                for i in range(n):
                    nn.append(100)

                    # nns=''
                    # nns=''.join(nn)
                nns = nn

                tot = 0
                for i in ml:
                    tot = tot + 1
                    if i == s:
                        tot = tot - 1
                        ml[tot:] = nns

                print(ml)
                il = []
                for i in ml:
                    il.append(int(i))
                print(il)

                ic.jan_rent = 0
                ic.jan_advance = 0
                ic.jan_due_amt = 0
                ic.jan_dis_amt = 0
                ic.jan_rent_flag = il[0]

                ic.feb_rent = 0
                ic.feb_advance = 0
                ic.feb_due_amt = 0
                ic.feb_dis_amt = 0
                ic.feb_rent_flag = il[1]

                ic.march_rent = 0
                ic.march_advance = 0
                ic.march_due_amt = 0
                ic.march_dis_amt = 0
                ic.march_rent_flag = il[2]

                ic.april_rent = 0
                ic.april_advance = 0
                ic.april_due_amt = 0
                ic.april_dis_amt = 0
                ic.april_rent_flag = il[3]

                ic.may_rent = 0
                ic.may_advance = 0
                ic.may_due_amt = 0
                ic.may_dis_amt = 0
                ic.may_rent_flag = il[4]

                ic.june_rent = 0
                ic.june_advance = 0
                ic.june_due_amt = 0
                ic.june_dis_amt = 0
                ic.june_rent_flag = il[5]

                ic.july_rent = 0
                ic.july_advance = 0
                ic.july_due_amt = 0
                ic.july_dis_amt = 0
                ic.july_rent_flag = il[6]

                ic.auguest_rent = 0
                ic.auguest_advance = 0
                ic.auguest_due_amt = 0
                ic.auguest_dis_amt = 0
                ic.auguest_rent_flag = il[7]

                ic.sept_rent = 0
                ic.sept_advance = 0
                ic.sept_due_amt = 0
                ic.sept_dis_amt = 0
                ic.sept_rent_flag = il[8]

                ic.october_rent = 0
                ic.october_advance = 0
                ic.october_due_amt = 0
                ic.october_dis_amt = 0
                ic.october_rent_flag = il[9]

                ic.nov_rent = 0
                ic.nov_advance = 0
                ic.nov_due_amt = 0
                ic.nov_dis_amt = 0
                ic.nov_rent_flag = il[10]

                ic.dec_rent = 0
                ic.dec_advance = 0
                ic.dec_due_amt = 0
                ic.dec_dis_amt = 0
                ic.dec_rent_flag = il[11]

                ic.flag = 2

                ic.save()

                l = []
                data = pg1_new_beds.objects.all()
                for i in data:
                    l.append(i.share_type)
                print('l', l)
                context = {
                    'brname': 'BRANCH 2 Room Creation Form',
                    'br': pg1_new_beds.objects.all().filter(roon_no=1).order_by('roon_no'),
                    'rn1': l[0]
                }
                messages.info(request, 'BRANCH2 guest created sucessfully')
                #return render(request, 'branches/branch1/new_guest/view_all_new_guest.html', context)
                return view_all_new_guest2(request)

        context = {
            'sd' : pg1_new_beds.objects.get(id=id)
        }
        return render(request,'branches/branch2/new_guest/new_guest_creation_page.html',context)
    return render(request,'index.html')


def view_all_new_guest2(request):
    
    if 'username' in request.session:
        l=[]
        data=pg1_new_beds.objects.all()
        for i in data:
            l.append(i.share_type)

        ll=[]
        rsdata=room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        g1_data=pg1_new_beds.objects.all().filter(roon_no=1),
        print('room share type of branch22',ll)
        print('room share type of branchl0', ll[0])
        print('room share type of branchl7', ll[7])


        context = {
            'brname': 'BRANCH 2 Room Creation Form',
            'br': pg1_new_beds.objects.all().filter(roon_no=101).order_by('roon_no'),
            'rn1':l[0],
            'table_height' : '40px',

            'r101':ll[0],
            '101_data':pg1_new_beds.objects.all().filter(roon_no=101),
            #'g1_data':g1_data,
            'r102': ll[1],
            '102_data': pg1_new_beds.objects.all().filter(roon_no=102),
            'r103': ll[2],
            '103_data': pg1_new_beds.objects.all().filter(roon_no=103),
            # 'g1_data':g1_data,
            'r104': ll[3],
            '104_data': pg1_new_beds.objects.all().filter(roon_no=104),
            'r106': ll[4],
            '106_data': pg1_new_beds.objects.all().filter(roon_no=106),
            # 'g1_data':g1_data,
            'r107': ll[5],
            '107_data': pg1_new_beds.objects.all().filter(roon_no=107),
            'r108': ll[6],
            '108_data': pg1_new_beds.objects.all().filter(roon_no=108),
            # 'g1_data':g1_data,
            'r109': ll[7],
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
        return render(request,'branches/branch2/new_guest/view_all_new_guest.html',context)
    return render(request,'index.html')


def update_br1_admit_guest2(request, id):
    if request.method == 'POST':
        selfmob = request.POST.get('selfmobno')
        #chk_mob = pg1_new_guest.objects.all().filter(self_mob=selfmob).exists()
        chk_mob = 10
        if chk_mob == 11:
            l = []
            data = pg1_new_beds.objects.all()
            for i in data:
                l.append(i.share_type)
            print('l', l)
            context = {
                'brname': 'BRANCH 2 Room Creation Form',
                'br': pg1_new_beds.objects.all().filter(roon_no=1).order_by('roon_no'),
                'rn1': l[0]

            }
            messages.info(request, 'BRANCH2 guest already exists')
            # return render(request, 'branches/branch1/new_guest/view_all_new_guest.html', context)
            return view_all_new_guest2(request)
        else:
            name = request.POST.get('name')
            advance = request.POST.get('advance')
            monthlyrent = request.POST.get('monthlyrent')
            selfmob = request.POST.get('selfmobno')
            age = request.POST.get('age')
            address = request.POST.get('paddress')
            pname = request.POST.get('pname')
            pmob = request.POST.get('pmob')

            ic = pg1_new_beds.objects.get(id=id)
            ic.name = name
            ic.advance = advance
            ic.monthly_rent = monthlyrent
            ic.self_mob = selfmob
            ic.age = age
            ic.permanent_address = address
            ic.parent_name = pname
            ic.parent_mob = pmob

            ic.flag = 2
            ic.save()
            ##################################################
            gd = []
            gud = pg1_new_beds.objects.all().filter(id=id)
            for i in gud:
                gd.append(i.guest_code)

            gc = pg1_new_guest.objects.get(guest_code=gd[0])
            gc.created_by = request.session['username']

            gc.name = name
            gc.advance = advance
            gc.monthly_rent = monthlyrent
            gc.self_mob = selfmob
            gc.age = age
            gc.permanent_address = address
            gc.parent_name = pname
            gc.parent_mob = pmob

            gc.flag = 2
            gc.save()

            messages.info(request, 'BRANCH2 guest updated sucessfully')
            return view_all_new_guest2(request)

    context = {
        'sd': pg1_new_beds.objects.get(id=id)
    }
    return render(request, 'branches/branch2/new_guest/update_br1_admit_guest.html', context)


def vacate_br1_guest2(request, id):
    if request.method == 'POST':
        selfmob = request.POST.get('selfmobno')
        #chk_mob = pg1_new_guest.objects.all().filter(self_mob=selfmob).exists()
        chk_mob = 10
        if chk_mob == 11:
            l = []
            data = pg1_new_beds.objects.all()
            for i in data:
                l.append(i.share_type)
            print('l', l)
            context = {
                'brname': 'BRANCH 2 Room Creation Form',
                #'br': pg1_new_beds.objects.all().filter(roon_no=1).order_by('roon_no'),
                'rn1': l[0]

            }
            messages.info(request, 'guest already exists')
            # return render(request, 'branches/branch1/new_guest/view_all_new_guest.html', context)
            return view_all_new_guest2(request)
        else:

            gd = []
            gud = pg1_new_beds.objects.all().filter(id=id)
            for i in gud:
                gd.append(i.guest_code)

            gc = pg1_new_guest.objects.get(guest_code=gd[0])
            gc.created_by = request.session['username']
            # gc.roon_no = gd[1]
            import datetime
            gc.guest_vacated_date = datetime.date.today()
            d = datetime.datetime.now()
            gc.guest_vacate_month = d.strftime("%m")
            gc.flag = 3
            gc.save()

            ic = pg1_new_beds.objects.get(id=id)
            ic.name = ''
            ic.advance = ''
            ic.monthly_rent = ''
            ic.self_mob = ''
            ic.age = 0
            ic.permanent_address = ''
            ic.parent_name = ''
            ic.parent_mob = 0

            ic.guest_code = 0
            ic.remark = ''
            ic.guest_join_date = ''
            ic.guest_join_month = ''
            ic.guest_vacated_date = ''
            ic.guest_vacate_month = ''

            ic.jan_rent = 0
            ic.jan_advance = ''
            ic.jan_due_amt = ''
            ic.jan_dis_amt = ''
            ic.jan_rent_rec_date = ''
            ic.jan_rent_flag = 0

            ic.feb_rent = 0
            ic.feb_advance = ''
            ic.feb_due_amt = ''
            ic.feb_dis_amt = ''
            ic.feb_rent_rec_date = ''
            ic.feb_rent_flag = 0

            ic.march_rent = 0
            ic.march_advance = ''
            ic.march_due_amt = ''
            ic.march_dis_amt = ''
            ic.march_rent_rec_date = ''
            ic.march_rent_flag = 0

            ic.april_rent = 0
            ic.april_advance = ''
            ic.april_due_amt = ''
            ic.april_dis_amt = ''
            ic.april_rent_rec_date = ''
            ic.april_rent_flag = 0

            ic.may_rent = 0
            ic.may_advance = ''
            ic.may_due_amt = ''
            ic.may_dis_amt = ''
            ic.may_rent_rec_date = ''
            ic.may_rent_flag = 0

            ic.june_rent = 0
            ic.june_advance = ''
            ic.june_due_amt = ''
            ic.june_dis_amt = ''
            ic.june_rent_rec_date = ''
            ic.june_rent_flag = 0

            ic.july_rent = 0
            ic.july_advance = ''
            ic.july_due_amt = ''
            ic.july_dis_amt = ''
            ic.july_rent_rec_date = ''
            ic.july_rent_flag = 0

            ic.auguest_rent = 0
            ic.auguest_advance = ''
            ic.auguest_due_amt = ''
            ic.auguest_dis_amt = ''
            ic.auguest_rent_rec_date = ''
            ic.auguest_rent_flag = 0

            ic.sept_rent = 0
            ic.sept_advance = ''
            ic.sept_due_amt = ''
            ic.sept_dis_amt = ''
            ic.sept_rent_rec_date = ''
            ic.sept_rent_flag = 0

            ic.october_rent = 0
            ic.october_advance = ''
            ic.october_due_amt = ''
            ic.october_dis_amt = ''
            ic.october_rent_rec_date = ''
            ic.october_rent_flag = 0

            ic.nov_rent = 0
            ic.nov_advance = ''
            ic.nov_due_amt = ''
            ic.nov_dis_amt = ''
            ic.nov_rent_rec_date = ''
            ic.nov_rent_flag = 0

            ic.dec_rent = 0
            ic.dec_advance = ''
            ic.dec_due_amt = ''
            ic.dec_dis_amt = ''
            ic.dec_rent_rec_date = ''
            ic.dec_rent_flag = 0

            ic.flag = 3
            ic.save()
            ##################################################


            messages.info(request, 'BRANCH2 guest Vacated sucessfully')
            return view_all_new_guest2(request)

    context = {
        'sd': pg1_new_beds.objects.get(id=id)
    }
    return render(request, 'branches/branch2/new_guest/vacate_br1_guest.html', context)


#new guest end here
################################

##################################
#REPORTS START HERE
################################

#**basic guest details start here

def guest_basic_details(request):
    context = {
        'up': pg1_new_guest.objects.all().filter(april_rent_flag=100, flag=1).order_by('roon_no'),
        'name': request.session['username'],
        'month_name': 'APRIL',
        'rs':8
    }
    return render(request,'branches/branch1/reports/print/guest_basic_details.html',context)

#**basic guest details end here

def unpaid_rent(request):
    import datetime
    print(datetime.datetime.now())
    x = datetime.datetime.now()
    print(x.strftime("%x"))
    r = x.strftime("%x")
    # r='11/2/23'
    print('my', r)
    print(type(r))
    l = []
    for i in r:
        l.append(i)
    print(l)

    ll = []
    for i in l:
        ll.append(l[0])
        ll.append(l[1])
        break
    print(ll)

    s = ''
    s = ''.join(ll)
    print('mystr', s)
    jan = 'jan_rent_flag'
    feb = 'feb_rent_flag'
    mar = 'march_rent_flag'
    dic = {
        '01': jan,
        '02': feb,
        '03': mar
    }

    print(dic[s])
    p=dic[s]

    aa='pg1_new_guest.objects.all().filter('
    bb='=100,flag=1),'
    c=aa+p+bb
    print(c)
    z=pg1_new_guest.objects.all().filter(march_rent_flag=100,flag=1),
    context = {
        'up': z,
        'name' : request.session['username']
    }
    return render(request, 'branches/branch1/reports/unpaid_rent/unpaid_rent.html', context)

def paid_rent(request):
    context = {
        'up': pg1_new_guest.objects.all().filter(march_rent_flag=200,flag=1),
        'name' : request.session['username']
    }
    return render(request, 'branches/branch1/reports/paid_rent/paid_rent.html', context)


# ************unpaid rent start here********

def unpaid_rent_choose_months2(request):
    if 'username' in request.session:
        return render(request, 'branches/branch2/reports/unpaid_rent/unpaid_rent_choose_months.html')


def jan_unpaid_rent2(request):
    if 'username' in request.session:
        context = {
            'up': pg1_new_guest.objects.all().filter(jan_rent_flag=100, flag=2).order_by('roon_no'),
            'name': request.session['username'],
            'month_name': 'JANUARY'
        }
        return render(request, 'branches/branch2/reports/unpaid_rent/unpaid_monthly_reports/jan/jan_unpaid_rent.html', context)
def table_jan_unpaid_rent2(request):
    if 'username' in request.session:
        context = {
            'up': pg1_new_guest.objects.all().filter(jan_rent_flag=100, flag=2).order_by('roon_no'),
            'name': request.session['username'],
            'month_name': 'JANUARY'
        }
        return render(request, 'branches/branch2/reports/unpaid_rent/unpaid_monthly_reports/jan/table_jan_unpaid_rent.html', context)


def feb_unpaid_rent2(request):
    if 'username' in request.session:
        context = {
            'up': pg1_new_guest.objects.all().filter(feb_rent_flag=100, flag=2).order_by('roon_no'),
            'name': request.session['username'],
            'month_name': 'FEB'
        }
        return render(request, 'branches/branch2/reports/unpaid_rent/unpaid_monthly_reports/feb/feb_unpaid_rent.html', context)
def table_feb_unpaid_rent2(request):
    if 'username' in request.session:
        context = {
            'up': pg1_new_guest.objects.all().filter(feb_rent_flag=100, flag=2).order_by('roon_no'),
            'name': request.session['username'],
            'month_name': 'FEB'
        }
        return render(request, 'branches/branch2/reports/unpaid_rent/unpaid_monthly_reports/feb/table_feb_unpaid_rent.html', context)


def mar_unpaid_rent2(request):
    if 'username' in request.session:
        context = {
            'up': pg1_new_guest.objects.all().filter(march_rent_flag=100, flag=2).order_by('roon_no'),
            'name': request.session['username'],
            'month_name': 'MARCH'
        }
        return render(request, 'branches/branch2/reports/unpaid_rent/unpaid_monthly_reports/mar/mar_unpaid_rent.html', context)
def table_mar_unpaid_rent2(request):
    if 'username' in request.session:
        context = {
            'up': pg1_new_guest.objects.all().filter(march_rent_flag=100, flag=2).order_by('roon_no'),
            'name': request.session['username'],
            'month_name': 'MARCH'
        }
        return render(request, 'branches/branch2/reports/unpaid_rent/unpaid_monthly_reports/mar/table_mar_unpaid_rent.html', context)


def april_unpaid_rent2(request):
    if 'username' in request.session:
        context = {
            'up': pg1_new_guest.objects.all().filter(april_rent_flag=100, flag=2).order_by('roon_no'),
            'name': request.session['username'],
            'month_name': 'APRIL'
        }
        return render(request, 'branches/branch2/reports/unpaid_rent/unpaid_monthly_reports/apr/april_unpaid_rent.html', context)
def table_april_unpaid_rent2(request):
    if 'username' in request.session:
        context = {
            'up': pg1_new_guest.objects.all().filter(april_rent_flag=100, flag=2).order_by('roon_no'),
            'name': request.session['username'],
            'month_name': 'APRIL'
        }
        return render(request, 'branches/branch2/reports/unpaid_rent/unpaid_monthly_reports/apr/table_april_unpaid_rent.html', context)


def may_unpaid_rent2(request):
    if 'username' in request.session:
        context = {
            'up': pg1_new_guest.objects.all().filter(may_rent_flag=100, flag=2).order_by('roon_no'),
            'name': request.session['username'],
            'month_name': 'MAY',
        }
        return render(request, 'branches/branch2/reports/unpaid_rent/unpaid_monthly_reports/may/may_unpaid_rent.html', context)
def table_may_unpaid_rent2(request):
    if 'username' in request.session:
        context = {
            'up': pg1_new_guest.objects.all().filter(may_rent_flag=100, flag=2).order_by('roon_no'),
            'name': request.session['username'],
            'month_name': 'MAY',
        }
        return render(request, 'branches/branch2/reports/unpaid_rent/unpaid_monthly_reports/may/table_may_unpaid_rent.html', context)

def june_unpaid_rent2(request):
    if 'username' in request.session:
        context = {
            'up': pg1_new_guest.objects.all().filter(june_rent_flag=100, flag=2).order_by('roon_no'),
            'name': request.session['username'],
            'month_name': 'JUNE'
        }
        return render(request, 'branches/branch2/reports/unpaid_rent/unpaid_monthly_reports/jun/jun_unpaid_rent.html', context)
def table_june_unpaid_rent2(request):
    if 'username' in request.session:
        context = {
            'up': pg1_new_guest.objects.all().filter(june_rent_flag=100, flag=2).order_by('roon_no'),
            'name': request.session['username'],
            'month_name': 'JUNE'
        }
        return render(request, 'branches/branch2/reports/unpaid_rent/unpaid_monthly_reports/jun/table_june_unpaid_rent.html', context)

def july_unpaid_rent2(request):
    if 'username' in request.session:
        context = {
            'up': pg1_new_guest.objects.all().filter(july_rent_flag=100, flag=2).order_by('roon_no'),
            'name': request.session['username'],
            'month_name': 'JULY'
        }
        return render(request, 'branches/branch2/reports/unpaid_rent/unpaid_monthly_reports/jul/july_unpaid_rent.html', context)
def table_july_unpaid_rent2(request):
    if 'username' in request.session:
        context = {
            'up': pg1_new_guest.objects.all().filter(july_rent_flag=100, flag=2).order_by('roon_no'),
            'name': request.session['username'],
            'month_name': 'JULY'
        }
        return render(request, 'branches/branch2/reports/unpaid_rent/unpaid_monthly_reports/jul/table_july_unpaid_rent.html', context)


def aug_unpaid_rent2(request):
    if 'username' in request.session:
        context = {
            'up': pg1_new_guest.objects.all().filter(auguest_rent_flag=100, flag=2).order_by('roon_no'),
            'name': request.session['username'],
            'month_name': 'AUGUST'
        }
        return render(request, 'branches/branch2/reports/unpaid_rent/unpaid_monthly_reports/aug/aug_unpaid_rent.html', context)
def table_aug_unpaid_rent2(request):
    if 'username' in request.session:
        context = {
            'up': pg1_new_guest.objects.all().filter(auguest_rent_flag=100, flag=2).order_by('roon_no'),
            'name': request.session['username'],
            'month_name': 'AUGUST'
        }
        return render(request, 'branches/branch2/reports/unpaid_rent/unpaid_monthly_reports/aug/table_aug_unpaid_rent.html', context)


def sept_unpaid_rent2(request):
    if 'username' in request.session:
        context = {
            'up': pg1_new_guest.objects.all().filter(sept_rent_flag=100, flag=2).order_by('roon_no'),
            'name': request.session['username'],
            'month_name': 'SEPT'
        }
        return render(request, 'branches/branch2/reports/unpaid_rent/unpaid_monthly_reports/sep/sept_unpaid_rent.html', context)
def table_sept_unpaid_rent2(request):
    if 'username' in request.session:
        context = {
            'up': pg1_new_guest.objects.all().filter(sept_rent_flag=100, flag=2).order_by('roon_no'),
            'name': request.session['username'],
            'month_name': 'SEPT'
        }
        return render(request, 'branches/branch2/reports/unpaid_rent/unpaid_monthly_reports/sept/table_sept_unpaid_rent.html', context)


def oct_unpaid_rent2(request):
    if 'username' in request.session:
        context = {
            'up': pg1_new_guest.objects.all().filter(october_rent_flag=100, flag=2).order_by('roon_no'),
            'name': request.session['username'],
            'month_name': 'OCTOBER'
        }
        return render(request, 'branches/branch2/reports/unpaid_rent/unpaid_monthly_reports/oct/oct_unpaid_rent2.html', context)
def table_oct_unpaid_rent2(request):
    if 'username' in request.session:
        context = {
            'up': pg1_new_guest.objects.all().filter(october_rent_flag=100, flag=2).order_by('roon_no'),
            'name': request.session['username'],
            'month_name': 'OCTOBER'
        }
        return render(request, 'branches/branch2/reports/unpaid_rent/unpaid_monthly_reports/oct/table_oct_unpaid_rent.html', context)


def nov_unpaid_rent2(request):
    if 'username' in request.session:
        context = {
            'up': pg1_new_guest.objects.all().filter(nov_rent_flag=100, flag=2).order_by('roon_no'),
            'name': request.session['username'],
            'month_name': 'NOVEMBER'
        }
        return render(request, 'branches/branch2/reports/unpaid_rent/unpaid_monthly_reports/nov/nov_unpaid_rent.html', context)
def table_nov_unpaid_rent2(request):
    if 'username' in request.session:
        context = {
            'up': pg1_new_guest.objects.all().filter(nov_rent_flag=100, flag=2).order_by('roon_no'),
            'name': request.session['username'],
            'month_name': 'NOVEMBER'
        }
        return render(request, 'branches/branch2/reports/unpaid_rent/unpaid_monthly_reports/nov/table_nov_unpaid_rent.html', context)


def dec_unpaid_rent2(request):
    if 'username' in request.session:
        context = {
            'up': pg1_new_guest.objects.all().filter(dec_rent_flag=100, flag=2).order_by('roon_no').order_by('roon_no'),
            'name': request.session['username'],
            'month_name': 'DECEMBER'
        }
        return render(request, 'branches/branch2/reports/unpaid_rent/unpaid_monthly_reports/dec/dec_unpaid_rent.html', context)
def table_dec_unpaid_rent2(request):
    if 'username' in request.session:
        context = {
            'up': pg1_new_guest.objects.all().filter(dec_rent_flag=100, flag=2).order_by('roon_no').order_by('roon_no'),
            'name': request.session['username'],
            'month_name': 'DECEMBER'
        }
        return render(request, 'branches/branch2/reports/unpaid_rent/unpaid_monthly_reports/dec/table_dec_unpaid_rent.html', context)


# details_of_unpaid_guests start here

def details_of_unpaid_guests2(request, id):
    rno = pg1_new_guest.objects.all().filter(id=id)
    l = []
    for i in rno:
        l.append(str(i.roon_no))
    s = ''.join(l)
    context = {
        'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2, may_rent_flag__gt=99),
        'user_details': pg1_new_guest.objects.all().filter(id=id),
    }
    return render(request, 'branches/branch2/reports/unpaid_rent/details_of_unpaid_guests.html', context)


# details_of_unpaid_guests end here

# *********unpaid rent end here ************




# ************paid rent start here********


def paid_rent_choose_months2(request):
    if 'username' in request.session:
        return render(request, 'branches/branch2/reports/paid_rent/paid_rent_choose_months.html')


def jan_paid_rent2(request):
    if 'username' in request.session:
        l = []
        unp = pg1_new_guest.objects.all().filter(jan_rent_flag=200, flag=1)
        for i in unp:
            l.append(str(i.jan_rent))
            break
        s = ''.join(l)
        context = {
            'up': pg1_new_guest.objects.all().filter(jan_rent_flag=200, flag=1),
            'name': request.session['username'],
            'amt': s,
            'month_name': 'JAN'
        }
        return render(request, 'branches/branch2/reports/paid_rent/paid_monthly_reports/jan/jan_paid_rent.html', context)
def table_jan_paid_rent2(request):
    if 'username' in request.session:
        l = []
        unp = pg1_new_guest.objects.all().filter(jan_rent_flag=200, flag=1)
        for i in unp:
            l.append(str(i.jan_rent))
            break
        s = ''.join(l)
        context = {
            'up': pg1_new_guest.objects.all().filter(jan_rent_flag=200, flag=1),
            'name': request.session['username'],
            'amt': s,
            'month_name': 'JAN'
        }
        return render(request, 'branches/branch2/reports/paid_rent/paid_monthly_reports/jan/table_jan_paid_rent.html', context)


def feb_paid_rent2(request):
    if 'username' in request.session:
        l = []
        unp = pg1_new_guest.objects.all().filter(feb_rent_flag=200, flag=1)
        for i in unp:
            l.append(str(i.feb_rent))
            break
        s = ''.join(l)
        context = {
            'up': pg1_new_guest.objects.all().filter(feb_rent_flag=200, flag=1),
            'name': request.session['username'], 'amt': s,
            'month_name': 'FEB'
        }
        return render(request, 'branches/branch2/reports/paid_rent/paid_monthly_reports/feb/feb_paid_rent.html', context)
def table_feb_paid_rent2(request):
    if 'username' in request.session:
        l = []
        unp = pg1_new_guest.objects.all().filter(feb_rent_flag=200, flag=1)
        for i in unp:
            l.append(str(i.feb_rent))
            break
        s = ''.join(l)
        context = {
            'up': pg1_new_guest.objects.all().filter(feb_rent_flag=200, flag=1),
            'name': request.session['username'], 'amt': s,
            'month_name': 'FEB'
        }
        return render(request, 'branches/branch2/reports/paid_rent/paid_monthly_reports/feb/table_feb_paid_rent.html', context)


def mar_paid_rent2(request):
    if 'username' in request.session:
        l = []
        unp = pg1_new_guest.objects.all().filter(march_rent_flag=200, flag=1)
        for i in unp:
            l.append(str(i.march_rent))
            break
        s = ''.join(l)
        context = {
            'up': pg1_new_guest.objects.all().filter(march_rent_flag=200, flag=1),
            'name': request.session['username'],
            'amt': s,
            'month_name': 'MARCH'
        }
        return render(request, 'branches/branch2/reports/paid_rent/paid_monthly_reports/mar/mar_paid_rent.html', context)
def table_mar_paid_rent2(request):
    if 'username' in request.session:
        l = []
        unp = pg1_new_guest.objects.all().filter(march_rent_flag=200, flag=1)
        for i in unp:
            l.append(str(i.march_rent))
            break
        s = ''.join(l)
        context = {
            'up': pg1_new_guest.objects.all().filter(march_rent_flag=200, flag=1),
            'name': request.session['username'],
            'amt': s,
            'month_name': 'MARCH'
        }
        return render(request, 'branches/branch2/reports/paid_rent/paid_monthly_reports/mar/table_mar_paid_rent.html', context)


def april_paid_rent2(request):
    if 'username' in request.session:
        l = []
        unp = pg1_new_guest.objects.all().filter(april_rent_flag=200, flag=2)
        for i in unp:
            l.append(str(i.april_rent))

        print(l)
        s = ''.join(l)
        print(s)
        context = {
            'up': pg1_new_guest.objects.all().filter(april_rent_flag=200, flag=2),
            'name': request.session['username'],
            'pamt': s,
            'month_name': 'APRIL'
        }
        return render(request, 'branches/branch2/reports/paid_rent/paid_monthly_reports/apr/april_paid_rent.html', context)
def table_april_paid_rent2(request):
    if 'username' in request.session:
        l = []
        unp = pg1_new_guest.objects.all().filter(april_rent_flag=200, flag=2)
        for i in unp:
            l.append(str(i.april_rent))

        print(l)
        s = ''.join(l)
        print(s)
        context = {
            'up': pg1_new_guest.objects.all().filter(april_rent_flag=200, flag=2),
            'name': request.session['username'],
            'pamt': s,
            'month_name': 'APRIL'
        }
        return render(request, 'branches/branch2/reports/paid_rent/paid_monthly_reports/apr/table_april_paid_rent.html', context)


def may_paid_rent2(request):
    if 'username' in request.session:
        l = []
        unp = pg1_new_guest.objects.all().filter(may_rent_flag=200, flag=2)
        for i in unp:
            l.append(str(i.may_rent))
            break
        s = ''.join(l)
        context = {
            'up': pg1_new_guest.objects.all().filter(may_rent_flag=200, flag=2),
            'name': request.session['username'],
            'amt': s,
            'month_name': 'MAY'
        }
        return render(request, 'branches/branch2/reports/paid_rent/paid_monthly_reports/may/may_paid_rent.html', context)
def table_may_paid_rent2(request):
    if 'username' in request.session:
        l = []
        unp = pg1_new_guest.objects.all().filter(may_rent_flag=200, flag=2)
        for i in unp:
            l.append(str(i.may_rent))
            break
        s = ''.join(l)
        context = {
            'up': pg1_new_guest.objects.all().filter(may_rent_flag=200, flag=2),
            'name': request.session['username'],
            'amt': s,
            'month_name': 'MAY'
        }
        return render(request, 'branches/branch2/reports/paid_rent/paid_monthly_reports/may/table_may_paid_rent.html', context)

def june_paid_rent2(request):
    if 'username' in request.session:
        l = []
        unp = pg1_new_guest.objects.all().filter(june_rent_flag=200, flag=2)
        for i in unp:
            l.append(str(i.june_rent))
            break
        s = ''.join(l)
        context = {
            'up': pg1_new_guest.objects.all().filter(june_rent_flag=200, flag=2),
            'name': request.session['username'],
            'amt': s,
            'month_name': 'JUNE'
        }
        return render(request, 'branches/branch2/reports/paid_rent/paid_monthly_reports/jun/june_paid_rent.html', context)
def table_june_paid_rent2(request):
    if 'username' in request.session:
        l = []
        unp = pg1_new_guest.objects.all().filter(june_rent_flag=200, flag=2)
        for i in unp:
            l.append(str(i.june_rent))
            break
        s = ''.join(l)
        context = {
            'up': pg1_new_guest.objects.all().filter(june_rent_flag=200, flag=2),
            'name': request.session['username'],
            'amt': s,
            'month_name': 'JUNE'
        }
        return render(request, 'branches/branch2/reports/paid_rent/paid_monthly_reports/jun/table_june_paid_rent.html', context)


def july_paid_rent2(request):
    if 'username' in request.session:
        l = []
        unp = pg1_new_guest.objects.all().filter(july_rent_flag=200, flag=2)
        for i in unp:
            l.append(str(i.july_rent))
            break
        s = ''.join(l)
        context = {
            'up': pg1_new_guest.objects.all().filter(july_rent_flag=200, flag=2),
            'name': request.session['username'],
            'amt': s,
            'month_name': 'JULY'
        }
        return render(request, 'branches/branch2/reports/paid_rent/paid_monthly_reports/jul/july_paid_rent.html', context)
def table_july_paid_rent2(request):
    if 'username' in request.session:
        l = []
        unp = pg1_new_guest.objects.all().filter(july_rent_flag=200, flag=2)
        for i in unp:
            l.append(str(i.july_rent))
            break
        s = ''.join(l)
        context = {
            'up': pg1_new_guest.objects.all().filter(july_rent_flag=200, flag=2),
            'name': request.session['username'],
            'amt': s,
            'month_name': 'JULY'
        }
        return render(request, 'branches/branch2/reports/paid_rent/paid_monthly_reports/jul/table_july_paid_rent.html', context)


def aug_paid_rent2(request):
    if 'username' in request.session:
        l = []
        unp = pg1_new_guest.objects.all().filter(auguest_rent_flag=200, flag=2)
        for i in unp:
            l.append(str(i.auguest_rent))
            break
        s = ''.join(l)
        context = {
            'up': pg1_new_guest.objects.all().filter(auguest_rent_flag=200, flag=2),
            'name': request.session['username'],
            'amt': s,
            'month_name': 'AUGUST'
        }
        return render(request, 'branches/branch2/reports/paid_rent/paid_monthly_reports/aug/aug_paid_rent.html', context)
def table_aug_paid_rent2(request):
    if 'username' in request.session:
        l = []
        unp = pg1_new_guest.objects.all().filter(auguest_rent_flag=200, flag=2)
        for i in unp:
            l.append(str(i.auguest_rent))
            break
        s = ''.join(l)
        context = {
            'up': pg1_new_guest.objects.all().filter(auguest_rent_flag=200, flag=2),
            'name': request.session['username'],
            'amt': s,
            'month_name': 'AUGUST'
        }
        return render(request, 'branches/branch2/reports/paid_rent/paid_monthly_reports/aug/table_aug_paid_rent.html', context)


def sept_paid_rent2(request):
    if 'username' in request.session:
        l = []
        unp = pg1_new_guest.objects.all().filter(sept_rent_flag=200, flag=2)
        for i in unp:
            l.append(str(i.sept_rent))
            break
        s = ''.join(l)
        context = {
            'up': pg1_new_guest.objects.all().filter(sept_rent_flag=200, flag=2),
            'name': request.session['username'],
            'amt': s,
            'month_name': 'SEPT'
        }
        return render(request, 'branches/branch2/reports/paid_rent/paid_monthly_reports/sept/sept_paid_rent.html', context)
def table_sept_paid_rent2(request):
    if 'username' in request.session:
        l = []
        unp = pg1_new_guest.objects.all().filter(sept_rent_flag=200, flag=2)
        for i in unp:
            l.append(str(i.sept_rent))
            break
        s = ''.join(l)
        context = {
            'up': pg1_new_guest.objects.all().filter(sept_rent_flag=200, flag=2),
            'name': request.session['username'],
            'amt': s,
            'month_name': 'SEPT'
        }
        return render(request, 'branches/branch2/reports/paid_rent/paid_monthly_reports/sept/table_sept_paid_rent.html', context)


def oct_paid_rent2(request):
    if 'username' in request.session:
        l = []
        unp = pg1_new_guest.objects.all().filter(october_rent_flag=200, flag=2)
        for i in unp:
            l.append(str(i.october_rent))
            break
        s = ''.join(l)
        context = {
            'up': pg1_new_guest.objects.all().filter(october_rent_flag=200, flag=2),
            'name': request.session['username'],
            'amt': s,
            'month_name': 'OCTOBER'
        }
        return render(request, 'branches/branch2/reports/paid_rent/paid_monthly_reports/oct/oct_paid_rent.html', context)
def table_oct_paid_rent2(request):
    if 'username' in request.session:
        l = []
        unp = pg1_new_guest.objects.all().filter(october_rent_flag=200, flag=2)
        for i in unp:
            l.append(str(i.october_rent))
            break
        s = ''.join(l)
        context = {
            'up': pg1_new_guest.objects.all().filter(october_rent_flag=200, flag=2),
            'name': request.session['username'],
            'amt': s,
            'month_name': 'OCTOBER'
        }
        return render(request, 'branches/branch2/reports/paid_rent/paid_monthly_reports/oct/table_oct_paid_rent.html', context)


def nov_paid_rent2(request):
    if 'username' in request.session:
        l = []
        unp = pg1_new_guest.objects.all().filter(nov_rent_flag=200, flag=2)
        for i in unp:
            l.append(str(i.nov_rent))
            break
        s = ''.join(l)
        context = {
            'up': pg1_new_guest.objects.all().filter(nov_rent_flag=200, flag=2),
            'name': request.session['username'],
            'amt': s,
            'month_name': 'NOVEMBER'
        }
        return render(request, 'branches/branch2/reports/paid_rent/paid_monthly_reports/nov/nov_paid_rent.html', context)
def table_nov_paid_rent2(request):
    if 'username' in request.session:
        l = []
        unp = pg1_new_guest.objects.all().filter(nov_rent_flag=200, flag=2)
        for i in unp:
            l.append(str(i.nov_rent))
            break
        s = ''.join(l)
        context = {
            'up': pg1_new_guest.objects.all().filter(nov_rent_flag=200, flag=2),
            'name': request.session['username'],
            'amt': s,
            'month_name': 'NOVEMBER'
        }
        return render(request, 'branches/branch2/reports/paid_rent/paid_monthly_reports/nov/table_nov_paid_rent.html', context)


def dec_paid_rent2(request):
    if 'username' in request.session:
        l = []
        unp = pg1_new_guest.objects.all().filter(dec_rent_flag=200, flag=2)
        for i in unp:
            l.append(str(i.dec_rent))
            break
        s = ''.join(l)
        context = {
            'up': pg1_new_guest.objects.all().filter(dec_rent_flag=200, flag=2),
            'name': request.session['username'],
            'amt': s,
            'month_name': 'DECEMBER'
        }
        return render(request, 'branches/branch2/reports/paid_rent/paid_monthly_reports/dec/dec_paid_rent.html', context)
def table_dec_paid_rent2(request):
    if 'username' in request.session:
        l = []
        unp = pg1_new_guest.objects.all().filter(dec_rent_flag=200, flag=2)
        for i in unp:
            l.append(str(i.dec_rent))
            break
        s = ''.join(l)
        context = {
            'up': pg1_new_guest.objects.all().filter(dec_rent_flag=200, flag=2),
            'name': request.session['username'],
            'amt': s,
            'month_name': 'DECEMBER'
        }
        return render(request, 'branches/branch2/reports/paid_rent/paid_monthly_reports/dec/table_dec_paid_rent.html', context)



# *********paid rent end here ************



#details_of_paid_guests start here

def details_of_paid_guests2(request,id):
    rno = pg1_new_guest.objects.all().filter(id=id)
    l = []
    for i in rno:
        l.append(str(i.roon_no))
    s = ''.join(l)
    context = {
        'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2, may_rent_flag__gt=99),
        'user_details': pg1_new_guest.objects.all().filter(id=id),
    }
    return render(request,'branches/branch2/reports/paid_rent/details_of_paid_guests.html',context)

#details_of_paid_guests end here


##################################
#REPORTS END HERE
################################

##################################
#PAYMENTS END HERE
################################

def choose_months2(request):
    if 'username' in request.session:
        return render(request,'branches/branch2/payments/choose_months.html')

#jan make payments start here
def jan2(request):
    if 'username' in request.session:
        rn = request.POST.get('rno')
        context={
            'pd':pg1_new_guest.objects.all().filter(roon_no=rn,flag=2,jan_rent_flag__gt=99),
            'roomno':rn,
            'room_name' : room_pg1.objects.all(),
            'room': room_pg1.objects.all(),

        }
        return render(request, 'branches/branch2/payments/details_of_months/jan/jan.html',context)

def jan_manke_payments2(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')

            jp = pg1_new_guest.objects.get(id=id)
            jp.jan_rent = amt
            jp.remark = remark
            jp.jan_due_amt = remark
            #jp.jan_rent_rec_date = datetime.date.today()
            jp.jan_rent_rec_date = date
            jp.jan_rent_flag = 200
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            jp = pg1_new_beds.objects.get(guest_code=l[0])
            jp.jan_rent = amt
            jp.remark = remark
            jp.jan_due_amt = remark
            #jp.jan_rent_rec_date = datetime.date.today()
            jp.jan_rent_rec_date = date
            jp.jan_rent_flag = 200
            jp.save()


            rno= pg1_new_guest.objects.all().filter(id=id)
            l=[]
            for i in rno:
                l.append(str(i.roon_no))
            s=''.join(l)
            context = {
                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2,jan_rent_flag__gt=99),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all(),
            }
            return render(request, 'branches/branch2/payments/details_of_months/jan/jan.html',context)
        rn = request.POST.get('rno')

        context = {
            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2,jan_rent_flag__gt=99),
            'roomno': rn,
            'sd' : pg1_new_guest.objects.get(id=id)
        }
        return render(request, 'branches/branch2/payments/details_of_months/jan/jan_manke_payments.html', context)

#jan make payments start here

#feb make payments start here
def feb2(request):
    if 'username' in request.session:
        rn = request.POST.get('rno')
        context={
            'pd':pg1_new_guest.objects.all().filter(roon_no=rn,flag=2,feb_rent_flag__gt=99),
            'roomno':rn,
            'room': room_pg1.objects.all(),
        }
        return render(request, 'branches/branch2/payments/details_of_months/feb/feb.html',context)

def feb_manke_payments2(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')

            jp = pg1_new_guest.objects.get(id=id)
            jp.feb_rent = amt
            jp.remark = remark
            jp.feb_due_amt = remark
            #jp.feb_rent_rec_date = datetime.date.today()
            jp.feb_rent_rec_date = date
            jp.feb_rent_flag = 200
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            jp = pg1_new_beds.objects.get(guest_code=l[0])
            jp.feb_rent = amt
            jp.remark = remark
            jp.feb_due_amt = remark
            #jp.feb_rent_rec_date = datetime.date.today()
            jp.feb_rent_rec_date = date
            jp.feb_rent_flag = 200
            jp.save()

            rno= pg1_new_guest.objects.all().filter(id=id)
            l=[]
            for i in rno:
                l.append(str(i.roon_no))
            s=''.join(l)
            context = {
                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2,feb_rent_flag__gt=99),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all(),
            }
            return render(request, 'branches/branch2/payments/details_of_months/feb/feb.html',context)
        rn = request.POST.get('rno')

        context = {
            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd' : pg1_new_guest.objects.get(id=id)
        }
        return render(request, 'branches/branch2/payments/details_of_months/feb/feb_manke_payments.html', context)

#feb make payments start here

#march make payments start here
def march2(request):
    if 'username' in request.session:
        rn = request.POST.get('rno')
        context={
            'pd':pg1_new_guest.objects.all().filter(roon_no=rn,flag=2,march_rent_flag__gt=99),
            'roomno':rn,
            'room': room_pg1.objects.all(),
        }
        return render(request, 'branches/branch2/payments/details_of_months/march/march.html',context)

def march_manke_payments2(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')

            jp = pg1_new_guest.objects.get(id=id)
            jp.march_rent = amt
            jp.remark = remark
            jp.march_due_amt = remark
            #jp.march_rent_rec_date = datetime.date.today()
            jp.march_rent_rec_date = date
            jp.march_rent_flag = 200
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            jp = pg1_new_beds.objects.get(guest_code=l[0])
            jp.march_rent = amt
            jp.remark = remark
            jp.march_due_amt = remark
            #jp.march_rent_rec_date = datetime.date.today()
            jp.march_rent_rec_date = date
            jp.march_rent_flag = 200
            jp.save()

            rno= pg1_new_guest.objects.all().filter(id=id)
            l=[]
            for i in rno:
                l.append(str(i.roon_no))
            s=''.join(l)
            context = {
                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2,march_rent_flag__gt=99),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all(),
            }
            return render(request, 'branches/branch2/payments/details_of_months/march/march.html',context)
        rn = request.POST.get('rno')

        context = {
            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd' : pg1_new_guest.objects.get(id=id)
        }
        return render(request, 'branches/branch2/payments/details_of_months/march/march_manke_payments.html', context)

#march make payments start here


#april make payments start here
def april2(request):
    if 'username' in request.session:
        rn = request.POST.get('rno')
        context={
            'pd':pg1_new_guest.objects.all().filter(roon_no=rn,flag=2,april_rent_flag__gt=99),
            'roomno':rn,
            'room' : room_pg1.objects.all(),
            #'room_name': room_pg1.objects.all(),
        }
        return render(request, 'branches/branch2/payments/details_of_months/april/april.html',context)

def april_make_payments2(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')

            jp = pg1_new_guest.objects.get(id=id)
            jp.april_rent = amt
            jp.remark = remark
            jp.april_due_amt = remark
            #jp.april_rent_rec_date = datetime.date.today()
            jp.april_rent_rec_date = date
            jp.april_rent_flag = 200
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            jp = pg1_new_beds.objects.get(guest_code=l[0])
            jp.april_rent = amt
            jp.remark = remark
            jp.april_due_amt = remark
            #jp.april_rent_rec_date = datetime.date.today()
            jp.april_rent_rec_date = date
            jp.april_rent_flag = 200
            jp.save()

            rno= pg1_new_guest.objects.all().filter(id=id)
            l=[]
            for i in rno:
                l.append(str(i.roon_no))
            s=''.join(l)
            context = {
                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2,april_rent_flag__gt=99),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all(),
            }
            return render(request, 'branches/branch2/payments/details_of_months/april/april.html',context)
        rn = request.POST.get('rno')

        context = {
            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd' : pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all(),
            'user_details': pg1_new_guest.objects.all().filter(id=id)
        }
        return render(request, 'branches/branch2/payments/details_of_months/april/april_make_payments.html', context)

#april make payments start here


#may make payments start here
def may2(request):
    if 'username' in request.session:
        rn = request.POST.get('rno')
        context={
            'pd':pg1_new_guest.objects.all().filter(roon_no=rn,flag=2,may_rent_flag__gt=99),
            'roomno':rn,
            'room': room_pg1.objects.all(),

        }
        return render(request, 'branches/branch2/payments/details_of_months/may/may.html',context)

def may_make_payments2(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt = request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')
            due_amt = request.POST.get('dueamt')
            dis_amt = request.POST.get('disamt')

            jp = pg1_new_guest.objects.get(id=id)
            jp.may_rent = amt
            jp.remark = remark
            jp.may_due_amt = due_amt
            jp.june_due_amt = due_amt
            jp.may_dis_amt = dis_amt
            # jp.may_rent_rec_date = datetime.date.today()
            jp.may_rent_rec_date = date
            jp.may_rent_flag = 200
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            # jp = pg1_new_beds.objects.get(guest_code=l[0])
            import branch2app
            jp = branch2app.models.pg1_new_beds.objects.get(guest_code=l[0])
            jp.may_rent = amt
            jp.remark = remark
            jp.may_due_amt = due_amt
            jp.june_due_amt = due_amt
            jp.may_dis_amt = dis_amt
            # jp.may_rent_rec_date = datetime.date.today()
            jp.may_rent_rec_date = date
            jp.may_rent_flag = 200
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.roon_no))
            s = ''.join(l)
            context = {
                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2, may_rent_flag__gt=99),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all(),
            }
            return render(request, 'branches/branch2/payments/details_of_months/may/may.html', context)
        rn = request.POST.get('rno')

        rno = pg1_new_guest.objects.all().filter(id=id)
        l = []
        for i in rno:
            l.append(str(i.guest_code))
        gc = ''.join(l)
        print('lll', l)

        import branch2app
        total_discout_amt = []
        pg1_new_beds = branch2app.models.pg1_new_guest.objects.all().filter(flag=2, guest_code=l[0])
        for i in pg1_new_beds:
            total_discout_amt.append(int(i.may_dis_amt))

        context = {
            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd': pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all(),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
            'discount_amt': total_discout_amt[0],
        }
        return render(request, 'branches/branch2/payments/details_of_months/may/may_make_payments.html', context)

#may make payments start here

#june make payments start here
def june2(request):
    if 'username' in request.session:
        rn = request.POST.get('rno')
        context={
            'pd':pg1_new_guest.objects.all().filter(roon_no=rn,flag=2,june_rent_flag__gt=99),
            'roomno':rn,
            'room': room_pg1.objects.all(),
        }
        return render(request, 'branches/branch2/payments/details_of_months/june/june.html',context)

def june_make_payments2(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt = request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')
            due_amt = request.POST.get('dueamt')
            dis_amt = request.POST.get('disamt')

            jp = pg1_new_guest.objects.get(id=id)
            jp.june_rent = amt
            jp.remark = remark
            jp.june_due_amt = due_amt
            jp.july_due_amt = due_amt
            jp.june_dis_amt = dis_amt
            # jp.june_rent_rec_date = datetime.date.today()
            jp.june_rent_rec_date = date
            jp.june_rent_flag = 200
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            import branch2app
            jp = branch2app.models.pg1_new_beds.objects.get(guest_code=l[0])
            jp.june_rent = amt
            jp.remark = remark
            jp.june_due_amt = due_amt
            jp.july_due_amt = due_amt
            jp.june_dis_amt = dis_amt
            # jp.june_rent_rec_date = datetime.date.today()
            jp.june_rent_rec_date = date
            jp.june_rent_flag = 200
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.roon_no))
            s = ''.join(l)

            context = {
                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2, june_rent_flag__gt=99),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all(),

            }
            return render(request, 'branches/branch2/payments/details_of_months/june/june.html', context)
        rn = request.POST.get('rno')

        rno = pg1_new_guest.objects.all().filter(id=id)
        l = []
        for i in rno:
            l.append(str(i.guest_code))
        gc = ''.join(l)
        print('lll', l)

        import branch2app
        total_discout_amt = []
        pg1_new_beds = branch2app.models.pg1_new_guest.objects.all().filter(flag=2, guest_code=l[0])
        for i in pg1_new_beds:
            total_discout_amt.append(int(i.june_dis_amt))

        context = {
            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd': pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all(),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
            'discount_amt': total_discout_amt[0],
        }
        return render(request, 'branches/branch2/payments/details_of_months/june/june_make_payments.html', context)

#june make payments start here

#july make payments start here
def july2(request):
    if 'username' in request.session:
        rn = request.POST.get('rno')
        context={
            'pd':pg1_new_guest.objects.all().filter(roon_no=rn,flag=2,july_rent_flag__gt=99),
            'roomno':rn,
            'room': room_pg1.objects.all(),
        }
        return render(request, 'branches/branch2/payments/details_of_months/july/july.html',context)

def july_make_payments2(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt = request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')
            due_amt = request.POST.get('dueamt')
            dis_amt = request.POST.get('disamt')

            jp = pg1_new_guest.objects.get(id=id)
            jp.july_rent = amt
            jp.remark = remark
            jp.july_due_amt = due_amt
            jp.auguest_due_amt = due_amt
            jp.july_dis_amt = dis_amt
            # jp.july_rent_rec_date = datetime.date.today()
            jp.july_rent_rec_date = date
            jp.july_rent_flag = 200
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            # jp = pg1_new_beds.objects.get(guest_code=l[0])
            import branch2app
            jp = branch2app.models.pg1_new_beds.objects.get(guest_code=l[0])
            jp.july_rent = dis_amt
            jp.remark = remark
            jp.july_due_amt = due_amt
            jp.auguest_due_amt = due_amt
            jp.july_dis_amt = dis_amt
            # jp.july_rent_rec_date = datetime.date.today()
            jp.july_rent_rec_date = date
            jp.july_rent_flag = 200
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.roon_no))
            s = ''.join(l)

            context = {
                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2, july_rent_flag__gt=99),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all(),
            }
            return render(request, 'branches/branch2/payments/details_of_months/july/july.html', context)
        rn = request.POST.get('rno')

        rno = pg1_new_guest.objects.all().filter(id=id)
        l = []
        for i in rno:
            l.append(str(i.guest_code))
        gc = ''.join(l)
        print('lll', l)

        import branch2app
        total_discout_amt = []
        pg1_new_beds = branch2app.models.pg1_new_guest.objects.all().filter(flag=2, guest_code=l[0])
        for i in pg1_new_beds:
            total_discout_amt.append(int(i.july_dis_amt))

        context = {
            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd': pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all(),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
            'discount_amt': total_discout_amt[0],
        }
        return render(request,'branches/branch2/payments/details_of_months/july/july_make_payments.html', context)

#july make payments start here

#agu make payments start here
def aug2(request):
    if 'username' in request.session:
        rn = request.POST.get('rno')
        context={
            'pd':pg1_new_guest.objects.all().filter(roon_no=rn,flag=2,auguest_rent_flag__gt=99),
            'roomno':rn,
            'room': room_pg1.objects.all(),
        }
        return render(request, 'branches/branch2/payments/details_of_months/aug/aug.html',context)

def aug_make_payments2(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')

            jp = pg1_new_guest.objects.get(id=id)
            jp.auguest_rent = amt
            jp.remark = remark
            jp.auguest_due_amt = remark
            #jp.auguest_rent_rec_date = datetime.date.today()
            jp.auguest_rent_rec_date = date
            jp.auguest_rent_flag = 200
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            jp = pg1_new_beds.objects.get(guest_code=l[0])
            jp.auguest_rent = amt
            jp.remark = remark
            jp.auguest_due_amt = remark
            #jp.auguest_rent_rec_date = datetime.date.today()
            jp.auguest_rent_rec_date = date
            jp.auguest_rent_flag = 200
            jp.save()

            rno= pg1_new_guest.objects.all().filter(id=id)
            l=[]
            for i in rno:
                l.append(str(i.roon_no))
            s=''.join(l)
            context = {
                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2,auguest_rent_flag__gt=99),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all(),
            }
            return render(request, 'branches/branch2/payments/details_of_months/aug/aug.html',context)
        rn = request.POST.get('rno')

        context = {
            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd' : pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all(),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
        }
        return render(request,'branches/branch2/payments/details_of_months/aug/aug_make_payments.html', context)

#aug make payments start here

#sept make payments start here
def sept2(request):
    if 'username' in request.session:
        rn = request.POST.get('rno')
        context={
            'pd':pg1_new_guest.objects.all().filter(roon_no=rn,flag=2,sept_rent_flag__gt=99),
            'roomno':rn,
            'room': room_pg1.objects.all(),
        }
        return render(request, 'branches/branch2/payments/details_of_months/sept/sept.html',context)

def sept_make_payments2(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')

            jp = pg1_new_guest.objects.get(id=id)
            jp.sept_rent = amt
            jp.remark = remark
            jp.sept_due_amt = remark
            #jp.sept_rent_rec_date = datetime.date.today()
            jp.sept_rent_rec_date = date
            jp.sept_rent_flag = 200
            jp.save()


            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            jp = pg1_new_beds.objects.get(guest_code=l[0])
            jp.sept_rent = amt
            jp.remark = remark
            jp.sept_due_amt = remark
            #jp.sept_rent_rec_date = datetime.date.today()
            jp.sept_rent_rec_date = date
            jp.sept_rent_flag = 200
            jp.save()

            rno= pg1_new_guest.objects.all().filter(id=id)
            l=[]
            for i in rno:
                l.append(str(i.roon_no))
            s=''.join(l)
            context = {
                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2,sept_rent_flag__gt=99),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all(),
            }
            return render(request, 'branches/branch2/payments/details_of_months/sept/sept.html',context)
        rn = request.POST.get('rno')

        context = {
            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=1),
            'roomno': rn,
            'sd' : pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all(),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
        }
        return render(request,'branches/branch2/payments/details_of_months/sept/sept_make_payments.html', context)

#sept make payments start here

#oct make payments start here
def oct2(request):
    if 'username' in request.session:
        rn = request.POST.get('rno')
        context={
            'pd':pg1_new_guest.objects.all().filter(roon_no=rn,flag=2,october_rent_flag__gt=99),
            'roomno':rn,
            'room': room_pg1.objects.all(),
        }
        return render(request, 'branches/branch2/payments/details_of_months/oct/oct.html',context)

def oct_make_payments2(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')

            jp = pg1_new_guest.objects.get(id=id)
            jp.october_rent = amt
            jp.remark = remark
            jp.october_due_amt = remark
            #jp.october_rent_rec_date = datetime.date.today()
            jp.october_rent_rec_date = date
            jp.october_rent_flag = 200
            jp.save()


            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            jp = pg1_new_beds.objects.get(guest_code=l[0])
            jp.october_rent = amt
            jp.remark = remark
            jp.october_due_amt = remark
            #jp.october_rent_rec_date = datetime.date.today()
            jp.october_rent_rec_date = date
            jp.october_rent_flag = 200
            jp.save()

            rno= pg1_new_guest.objects.all().filter(id=id)
            l=[]
            for i in rno:
                l.append(str(i.roon_no))
            s=''.join(l)
            context = {
                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2,october_rent_flag__gt=99),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all(),
            }
            return render(request, 'branches/branch2/payments/details_of_months/oct/oct.html',context)
        rn = request.POST.get('rno')

        context = {
            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd' : pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all(),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
        }
        return render(request,'branches/branch2/payments/details_of_months/oct/oct_make_payments.html', context)

#oct make payments start here

#nov make payments start here
def nov2(request):
    if 'username' in request.session:
        rn = request.POST.get('rno')
        context={
            'pd':pg1_new_guest.objects.all().filter(roon_no=rn,flag=2,nov_rent_flag__gt=99),
            'roomno':rn,
            'room': room_pg1.objects.all(),
        }
        return render(request, 'branches/branch2/payments/details_of_months/nov/nov.html',context)

def nov_make_payments2(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')

            jp = pg1_new_guest.objects.get(id=id)
            jp.nov_rent = amt
            jp.remark = remark
            jp.nov_due_amt = remark
            #jp.nov_rent_rec_date = datetime.date.today()
            jp.nov_rent_rec_date = date
            jp.nov_rent_flag = 200
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            jp = pg1_new_beds.objects.get(guest_code=l[0])
            jp.nov_rent = amt
            jp.remark = remark
            jp.nov_due_amt = remark
            #jp.nov_rent_rec_date = datetime.date.today()
            jp.nov_rent_rec_date = date
            jp.nov_rent_flag = 200
            jp.save()

            rno= pg1_new_guest.objects.all().filter(id=id)
            l=[]
            for i in rno:
                l.append(str(i.roon_no))
            s=''.join(l)
            context = {
                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2,nov_rent_flag__gt=99),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all(),
            }
            return render(request, 'branches/branch2/payments/details_of_months/nov/nov.html',context)
        rn = request.POST.get('rno')

        context = {
            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd' : pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all(),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
        }
        return render(request,'branches/branch2/payments/details_of_months/nov/nov_make_payments.html', context)

#nov make payments start here

#dec make payments start here
def dec2(request):
    if 'username' in request.session:
        rn = request.POST.get('rno')
        context={
            'pd':pg1_new_guest.objects.all().filter(roon_no=rn,flag=2,dec_rent_flag__gt=99),
            'roomno':rn,
            'room': room_pg1.objects.all(),
        }
        return render(request, 'branches/branch2/payments/details_of_months/dec/dec.html',context)

def dec_make_payments2(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')

            jp = pg1_new_guest.objects.get(id=id)
            jp.dec_rent = amt
            jp.remark = remark
            jp.dec_due_amt = remark
            #jp.dec_rent_rec_date = datetime.date.today()
            jp.dec_rent_rec_date = date
            jp.dec_rent_flag = 200
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            jp = pg1_new_beds.objects.get(guest_code=l[0])
            jp.dec_rent = amt
            jp.remark = remark
            jp.dec_due_amt = remark
            #jp.dec_rent_rec_date = datetime.date.today()
            jp.dec_rent_rec_date = date
            jp.dec_rent_flag = 200
            jp.save()

            rno= pg1_new_guest.objects.all().filter(id=id)
            l=[]
            for i in rno:
                l.append(str(i.roon_no))
            s=''.join(l)
            context = {
                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2,dec_rent_flag__gt=99),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all(),
            }
            return render(request, 'branches/branch2/payments/details_of_months/dec/dec.html',context)
        rn = request.POST.get('rno')

        context = {
            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd' : pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all(),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
        }
        return render(request,'branches/branch2/payments/details_of_months/dec/dec_make_payments.html', context)

#dec make payments start here

##################################
#PAYMENTS END HERE
################################


##################################
# ADVANCE START HERE
################################

def choose_months_advance2(request):
    if 'username' in request.session:
        return render(request, 'branches/branch2/advance/choose_months_advance.html')


def jan_advance2(request):
    if 'username' in request.session:
        rn = request.POST.get('rno')
        context = {
            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2, jan_rent_flag__gt=99),
            'roomno': rn,
            'room': room_pg1.objects.all(),

        }
        return render(request, 'branches/branch2/advance/details_of_months/jan/jan_advance.html', context)
    return render(request, 'index.html')


def jan_make_payments_advance2(request, id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt = request.POST.get('janamt')
            remark = request.POST.get('janremark')
            dis = request.POST.get('discount')

            jp = pg1_new_guest.objects.get(id=id)
            jp.jan_advance = amt
            jp.remark = remark
            jp.jan_due_amt = amt
            jp.jan_dis_amt = dis
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            jp = pg1_new_beds.objects.get(guest_code=l[0])
            jp.jan_advance = amt
            jp.remark = remark
            jp.jan_due_amt = amt
            jp.jan_dis_amt = dis
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.roon_no))
            s = ''.join(l)
            context = {
                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2, jan_rent_flag__gt=99),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all(),
            }
            return render(request, 'branches/branch2/advance/details_of_months/jan/jan_advance.html', context)
        rn = request.POST.get('rno')

        context = {
            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd': pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all(),
            'user_details': pg1_new_guest.objects.all().filter(id=id)
        }
        return render(request, 'branches/branch2/advance/details_of_months/feb/feb_make_payments_advance.html', context)
    return render(request, 'index.html')


def feb_advance2(request):
    if 'username' in request.session:
        rn = request.POST.get('rno')
        context = {
            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2, feb_rent_flag__gt=99),
            'roomno': rn,
            'room': room_pg1.objects.all(),
        }
        return render(request, 'branches/branch2/advance/details_of_months/feb/feb_advance.html', context)
    return render(request, 'index.html')


def feb_make_payments_advance2(request, id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt = request.POST.get('janamt')
            remark = request.POST.get('janremark')
            dis = request.POST.get('discount')

            jp = pg1_new_guest.objects.get(id=id)
            jp.feb_advance = amt
            jp.remark = remark
            jp.feb_due_amt = amt
            jp.feb_dis_amt = dis
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            jp = pg1_new_beds.objects.get(guest_code=l[0])
            jp.feb_advance = amt
            jp.remark = remark
            jp.feb_due_amt = amt
            jp.feb_dis_amt = dis
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.roon_no))
            s = ''.join(l)
            context = {
                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2, feb_rent_flag__gt=99),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all(),
            }
            return render(request, 'branches/branch2/advance/details_of_months/feb/feb_advance.html', context)
        rn = request.POST.get('rno')

        context = {
            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd': pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all(),
            'user_details': pg1_new_guest.objects.all().filter(id=id)
        }
        return render(request, 'branches/branch2/advance/details_of_months/feb/feb_make_payments_advance.html', context)
    return render(request, 'index.html')


def march_advance2(request):
    if 'username' in request.session:
        rn = request.POST.get('rno')
        context = {
            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2, march_rent_flag__gt=99),
            'roomno': rn,
            'room': room_pg1.objects.all(),
        }
        return render(request, 'branches/branch2/advance/details_of_months/march/march_advance.html', context)
    return render(request, 'index.html')


def march_make_payments_advance2(request, id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt = request.POST.get('janamt')
            remark = request.POST.get('janremark')
            dis = request.POST.get('discount')

            jp = pg1_new_guest.objects.get(id=id)
            jp.march_advance = amt
            jp.remark = remark
            jp.march_due_amt = amt
            jp.march_dis_amt = dis
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            jp = pg1_new_beds.objects.get(guest_code=l[0])
            jp.march_advance = amt
            jp.remark = remark
            jp.march_due_amt = amt
            jp.march_dis_amt = dis
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.roon_no))
            s = ''.join(l)
            context = {
                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2, march_rent_flag__gt=99),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all(),
            }
            return render(request, 'branches/branch2/advance/details_of_months/march/march_advance.html', context)
        rn = request.POST.get('rno')

        context = {
            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd': pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all(),
            'user_details': pg1_new_guest.objects.all().filter(id=id)
        }
        return render(request, 'branches/branch2/advance/details_of_months/march/march_make_payments_advance.html',
                      context)
    return render(request, 'index.html')


def april_advance2(request):
    if 'username' in request.session:
        rn = request.POST.get('rno')
        context = {
            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2, april_rent_flag__gt=99),
            'roomno': rn,
            'room': room_pg1.objects.all(),

        }
        return render(request, 'branches/branch2/advance/details_of_months/april/april_advance.html', context)
    return render(request, 'index.html')


def april_make_payments_advance2(request, id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt = request.POST.get('janamt')
            remark = request.POST.get('janremark')
            dis = request.POST.get('discount')

            jp = pg1_new_guest.objects.get(id=id)
            jp.april_advance = amt
            jp.remark = remark
            jp.april_due_amt = amt
            jp.april_dis_amt = dis
            # jp.may_rent_rec_date = datetime.date.today()

            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            jp = pg1_new_beds.objects.get(guest_code=l[0])
            jp.april_advance = amt
            jp.remark = remark
            jp.april_due_amt = amt
            jp.april_dis_amt = dis
            # jp.may_rent_rec_date = datetime.date.today()

            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.roon_no))
            s = ''.join(l)
            context = {
                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2, april_rent_flag__gt=99),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all(),
            }
            return render(request, 'branches/branch2/advance/details_of_months/april/april_advance.html', context)
        rn = request.POST.get('rno')

        context = {
            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd': pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all(),
            'user_details': pg1_new_guest.objects.all().filter(id=id)
        }
        return render(request, 'branches/branch2/advance/details_of_months/april/april_make_payments_advance.html',
                      context)
    return render(request, 'index.html')


def may_advance2(request):
    if 'username' in request.session:
        rn = request.POST.get('rno')
        context = {
            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2, may_rent_flag__gt=99),
            'roomno': rn,
            'room': room_pg1.objects.all(),

        }
        return render(request, 'branches/branch2/advance/details_of_months/may/may_advance.html', context)
    return render(request, 'index.html')


def may_make_payments_advance2(request, id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt = request.POST.get('janamt')
            remark = request.POST.get('janremark')
            dis = request.POST.get('discount')

            jp = pg1_new_guest.objects.get(id=id)
            jp.may_advance = amt
            jp.remark = remark
            jp.may_due_amt = amt
            jp.may_dis_amt = dis
            # jp.may_rent_rec_date = datetime.date.today()

            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            jp = pg1_new_beds.objects.get(guest_code=l[0])
            jp.may_advance = amt
            jp.remark = remark
            jp.may_due_amt = amt
            jp.may_dis_amt = dis
            # jp.may_rent_rec_date = datetime.date.today()

            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.roon_no))
            s = ''.join(l)
            context = {
                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2, may_rent_flag__gt=99),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all(),
            }
            return render(request, 'branches/branch2/advance/details_of_months/may/may_advance.html', context)
        rn = request.POST.get('rno')

        context = {
            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd': pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all(),
            'user_details': pg1_new_guest.objects.all().filter(id=id)
        }
        return render(request, 'branches/branch2/advance/details_of_months/may/may_make_payments_advance.html', context)
    return render(request, 'index.html')


def june_advance2(request):
    if 'username' in request.session:
        rn = request.POST.get('rno')
        context = {
            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2, june_rent_flag__gt=99),
            'roomno': rn,
            'room': room_pg1.objects.all(),

        }
        return render(request, 'branches/branch2/advance/details_of_months/june/june_advance.html', context)
    return render(request, 'index.html')


def june_make_payments_advance2(request, id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt = request.POST.get('janamt')
            remark = request.POST.get('janremark')
            dis = request.POST.get('discount')

            jp = pg1_new_guest.objects.get(id=id)
            jp.june_advance = amt
            jp.remark = remark
            jp.june_due_amt = amt
            jp.june_dis_amt = dis
            # jp.may_rent_rec_date = datetime.date.today()

            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            jp = pg1_new_beds.objects.get(guest_code=l[0])
            jp.june_advance = amt
            jp.remark = remark
            jp.june_due_amt = amt
            jp.june_dis_amt = dis
            # jp.may_rent_rec_date = datetime.date.today()

            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.roon_no))
            s = ''.join(l)
            context = {
                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2, june_rent_flag__gt=99),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all(),
            }
            return render(request, 'branches/branch2/advance/details_of_months/june/june_advance.html', context)
        rn = request.POST.get('rno')

        context = {
            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd': pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all(),
            'user_details': pg1_new_guest.objects.all().filter(id=id)
        }
        return render(request, 'branches/branch2/advance/details_of_months/june/june_make_payments_advance.html',
                      context)
    return render(request, 'index.html')


def july_advance2(request):
    if 'username' in request.session:
        rn = request.POST.get('rno')
        context = {
            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2, july_rent_flag__gt=99),
            'roomno': rn,
            'room': room_pg1.objects.all(),

        }
        return render(request, 'branches/branch2/advance/details_of_months/july/july_advance.html', context)
    return render(request, 'index.html')


def july_make_payments_advance2(request, id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt = request.POST.get('janamt')
            remark = request.POST.get('janremark')
            dis = request.POST.get('discount')

            jp = pg1_new_guest.objects.get(id=id)
            jp.july_advance = amt
            jp.july_dis_amt = dis
            jp.remark = remark
            jp.july_due_amt = amt
            # jp.may_rent_rec_date = datetime.date.today()

            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            jp = pg1_new_beds.objects.get(guest_code=l[0])
            jp.july_advance = amt
            jp.remark = remark
            jp.july_dis_amt = dis
            jp.july_due_amt = amt
            # jp.may_rent_rec_date = datetime.date.today()

            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.roon_no))
            s = ''.join(l)
            context = {
                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2, july_rent_flag__gt=99),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all(),
            }
            return render(request, 'branches/branch2/advance/details_of_months/july/july_advance.html', context)
        rn = request.POST.get('rno')

        context = {
            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd': pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all(),
            'user_details': pg1_new_guest.objects.all().filter(id=id)
        }
        return render(request, 'branches/branch2/advance/details_of_months/july/july_make_payments_advance.html',
                      context)
    return render(request, 'index.html')


def auguest_advance2(request):
    if 'username' in request.session:
        rn = request.POST.get('rno')
        context = {
            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2, auguest_rent_flag__gt=99),
            'roomno': rn,
            'room': room_pg1.objects.all(),

        }
        return render(request, 'branches/branch2/advance/details_of_months/aug/aug_advance.html', context)
    return render(request, 'index.html')


def auguest_make_payments_advance2(request, id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt = request.POST.get('janamt')
            remark = request.POST.get('janremark')
            dis = request.POST.get('discount')

            jp = pg1_new_guest.objects.get(id=id)
            jp.auguest_advance = amt
            jp.remark = remark
            jp.auguest_due_amt = amt
            jp.auguest_dis_amt = dis
            # jp.may_rent_rec_date = datetime.date.today()

            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            jp = pg1_new_beds.objects.get(guest_code=l[0])
            jp.auguest_advance = amt
            jp.remark = remark
            jp.auguest_due_amt = amt
            jp.auguest_dis_amt = dis
            # jp.may_rent_rec_date = datetime.date.today()

            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.roon_no))
            s = ''.join(l)
            context = {
                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2, auguest_rent_flag__gt=99),
                'room': room_pg1.objects.all(),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
            }
            return render(request, 'branches/branch2/advance/details_of_months/aug/aug_advance.html', context)
        rn = request.POST.get('rno')

        context = {
            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd': pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all(),
            'user_details': pg1_new_guest.objects.all().filter(id=id)
        }
        return render(request, 'branches/branch2/advance/details_of_months/aug/aug_make_payments_advance.html', context)
    return render(request, 'index.html')


def sept_advance2(request):
    if 'username' in request.session:
        rn = request.POST.get('rno')
        context = {
            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2, sept_rent_flag__gt=99),
            'roomno': rn,
            'room': room_pg1.objects.all(),

        }
        return render(request, 'branches/branch2/advance/details_of_months/sept/sept_advance.html', context)
    return render(request, 'index.html')


def sept_make_payments_advance2(request, id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt = request.POST.get('janamt')
            remark = request.POST.get('janremark')
            dis = request.POST.get('discount')

            jp = pg1_new_guest.objects.get(id=id)
            jp.sept_advance = amt
            jp.remark = remark
            jp.sept_due_amt = amt
            jp.sept_dis_amt = dis
            # jp.may_rent_rec_date = datetime.date.today()

            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            jp = pg1_new_beds.objects.get(guest_code=l[0])
            jp.sept_advance = amt
            jp.remark = remark
            jp.sept_due_amt = amt
            jp.sept_dis_amt = dis
            # jp.may_rent_rec_date = datetime.date.today()

            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.roon_no))
            s = ''.join(l)
            context = {
                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2, sept_rent_flag__gt=99),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all(),
            }
            return render(request, 'branches/branch2/advance/details_of_months/sept/sept_advance.html', context)
        rn = request.POST.get('rno')

        context = {
            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd': pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all(),
            'user_details': pg1_new_guest.objects.all().filter(id=id)
        }
        return render(request, 'branches/branch2/advance/details_of_months/sept/sept_make_payments_advance.html',
                      context)
    return render(request, 'index.html')


def october_advance2(request):
    if 'username' in request.session:
        rn = request.POST.get('rno')
        context = {
            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2, october_rent_flag__gt=99),
            'roomno': rn,
            'room': room_pg1.objects.all(),

        }
        return render(request, 'branches/branch2/advance/details_of_months/oct/oct_advance.html', context)
    return render(request, 'index.html')


def october_make_payments_advance2(request, id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt = request.POST.get('janamt')
            remark = request.POST.get('janremark')
            dis = request.POST.get('discount')

            jp = pg1_new_guest.objects.get(id=id)
            jp.october_advance = amt
            jp.remark = remark
            jp.october_due_amt = amt
            jp.october_dis_amt = dis
            # jp.may_rent_rec_date = datetime.date.today()

            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            jp = pg1_new_beds.objects.get(guest_code=l[0])
            jp.october_advance = amt
            jp.remark = remark
            jp.october_due_amt = amt
            jp.october_dis_amt = dis
            # jp.may_rent_rec_date = datetime.date.today()

            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.roon_no))
            s = ''.join(l)
            context = {
                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2, october_rent_flag__gt=99),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all(),
            }
            return render(request, 'branches/branch2/advance/details_of_months/oct/oct_advance.html', context)
        rn = request.POST.get('rno')

        context = {
            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd': pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all(),
            'user_details': pg1_new_guest.objects.all().filter(id=id)
        }
        return render(request, 'branches/branch2/advance/details_of_months/oct/oct_make_payments_advance.html', context)
    return render(request, 'index.html')


def nov_advance2(request):
    if 'username' in request.session:
        rn = request.POST.get('rno')
        context = {
            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2, nov_rent_flag__gt=99),
            'roomno': rn,
            'room': room_pg1.objects.all(),

        }
        return render(request, 'branches/branch2/advance/details_of_months/nov/nov_advance.html', context)
    return render(request, 'index.html')


def nov_make_payments_advance2(request, id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt = request.POST.get('janamt')
            remark = request.POST.get('janremark')
            dis = request.POST.get('discount')

            jp = pg1_new_guest.objects.get(id=id)
            jp.nov_advance = amt
            jp.remark = remark
            jp.nov_due_amt = amt
            jp.nov_dis_amt = dis
            # jp.may_rent_rec_date = datetime.date.today()

            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            jp = pg1_new_beds.objects.get(guest_code=l[0])
            jp.nov_advance = amt
            jp.remark = remark
            jp.nov_due_amt = amt
            jp.nov_dis_amt = dis
            # jp.may_rent_rec_date = datetime.date.today()

            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.roon_no))
            s = ''.join(l)
            context = {
                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2, nov_rent_flag__gt=99),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all(),
            }
            return render(request, 'branches/branch2/advance/details_of_months/nov/nov_advance.html', context)
        rn = request.POST.get('rno')

        context = {
            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd': pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all(),
            'user_details': pg1_new_guest.objects.all().filter(id=id)
        }
        return render(request, 'branches/branch2/advance/details_of_months/nov/nov_make_payments_advance.html', context)
    return render(request, 'index.html')


def dec_advance2(request):
    if 'username' in request.session:
        rn = request.POST.get('rno')
        context = {
            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2, dec_rent_flag__gt=99),
            'roomno': rn,
            'room': room_pg1.objects.all(),

        }
        return render(request, 'branches/branch2/advance/details_of_months/dec/dec_advance.html', context)
    return render(request, 'index.html')


def dec_make_payments_advance2(request, id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt = request.POST.get('janamt')
            remark = request.POST.get('janremark')
            dis = request.POST.get('discount')

            jp = pg1_new_guest.objects.get(id=id)
            jp.dec_advance = amt
            jp.remark = remark
            jp.dec_due_amt = amt
            jp.dec_dis_amt = dis
            # jp.may_rent_rec_date = datetime.date.today()

            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            jp = pg1_new_beds.objects.get(guest_code=l[0])
            jp.dec_advance = amt
            jp.remark = remark
            jp.dec_due_amt = amt
            jp.dec_dis_amt = dis
            # jp.may_rent_rec_date = datetime.date.today()

            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.roon_no))
            s = ''.join(l)
            context = {
                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2, dec_rent_flag__gt=99),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all(),
            }
            return render(request, 'branches/branch2/advance/details_of_months/dec/dec_advance.html', context)
        rn = request.POST.get('rno')

        context = {
            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd': pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all(),
            'user_details': pg1_new_guest.objects.all().filter(id=id)
        }
        return render(request, 'branches/branch2/advance/details_of_months/dec/dec_make_payments_advance.html', context)
    return render(request, 'index.html')


##################################
# ADVANCE END HERE
################################


##################################
#PRINT OUTS START HERE
################################
def detail_guest_general2(request):
    if 'username' in request.session:
        l = []
        data = pg1_new_beds.objects.all()
        for i in data:
            l.append(i.share_type)

        ll = []
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

        return render(request,'branches/branch2/print_outs/detail_guest_general.html',context)
    return render(request, 'index.html')

def jan_print2(request):
    if 'username' in request.session:
        l = []
        data = pg1_new_beds.objects.all()
        for i in data:
            l.append(i.share_type)

        ll = []
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
        return render(request,'branches/branch2/print_outs/jan_print.html',context)
    return render(request, 'index.html')


def jan_close2(request):
    if 'username' in request.session:
        chk = branch_closing.objects.all().filter(jan='', branch_name='branch2').exists()
        print(chk)
        if chk == True:
            conn = py.connect(host=database_host, user=database_user, password=database_password,database=database_name)
            query = 'create table branch2app_branch1_closing_jan select * from branch2app_pg1_new_beds'
            # create cursor object to execute the query
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(query)

            bc = branch_closing.objects.get(branch_name='branch2')
            bc.jan = 1
            bc.save()
            return feb_print2(request)

    return render(request,'index.html')

def jan_close_decision_page2(request):
    if 'username' in request.session:
        chk = branch_closing.objects.all().filter(jan='', branch_name='branch2').exists()
        print(chk)
        if chk == True:
            return render(request, 'branches/branch2/close_months/jan_months_close_page.html')
        if chk == False:
            return feb_print2(request)
    return render(request,'index.html')


def feb_print2(request):
    if 'username' in request.session:
        l = []
        data = pg1_new_beds.objects.all()
        for i in data:
            l.append(i.share_type)

        ll = []
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
        return render(request,'branches/branch2/print_outs/feb_print.html',context)
    return render(request, 'index.html')

def feb_close2(request):
    if 'username' in request.session:
        chk = branch_closing.objects.all().filter(feb='', branch_name='branch2').exists()
        print(chk)
        if chk == True:
            conn = py.connect(host=database_host, user=database_user, password=database_password,database=database_name)
            query = 'create table branch2app_branch1_closing_feb select * from branch2app_pg1_new_beds'
            # create cursor object to execute the query
            cur = conn.cursor()
            cur.execute(query)

            bc = branch_closing.objects.get(branch_name='branch2')
            bc.feb = 1
            bc.save()
            return march_print2(request)

    return render(request,'index.html')

def feb_close_decision_page2(request):
    if 'username' in request.session:
        chk = branch_closing.objects.all().filter(feb='', branch_name='branch2').exists()
        print(chk)
        if chk == True:
            return render(request, 'branches/branch2/close_months/feb_months_close_page.html')
        if chk == False:
            return march_print2(request)
    return render(request,'index.html')

def march_print2(request):
    if 'username' in request.session:
        l = []
        data = pg1_new_beds.objects.all()
        for i in data:
            l.append(i.share_type)

        ll = []
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
        return render(request,'branches/branch2/print_outs/march_print.html',context)
    return render(request, 'index.html')



def mar_close2(request):
    if 'username' in request.session:
        chk = branch_closing.objects.all().filter(mar='', branch_name='branch2').exists()
        print('MARCH CLOS',chk)
        if chk == True:
            conn = py.connect(host=database_host, user=database_user, password=database_password,database=database_name)
            query = 'create table branch2app_branch1_closing_mar select * from branch2app_pg1_new_beds'
            # create cursor object to execute the query
            cur = conn.cursor()
            cur.execute(query)

            bc = branch_closing.objects.get(branch_name='branch2')
            bc.mar = 1
            bc.save()
            return april_print2(request)
    return render(request,'index.html')

def mar_close_decision_page2(request):
    if 'username' in request.session:
        chk = branch_closing.objects.all().filter(mar='', branch_name='branch2').exists()
        print(chk)
        if chk == True:
            return render(request, 'branches/branch2/close_months/mar_months_close_page.html')
        if chk == False:
            return april_print2(request)
    return render(request,'index.html')

def april_print2(request):
    if 'username' in request.session:
        l = []
        data = pg1_new_beds.objects.all()
        for i in data:
            l.append(i.share_type)

        ll = []
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

        return render(request,'branches/branch2/print_outs/april_print.html',context)
    return render(request,'index.html')


def apr_close2(request):
    if 'username' in request.session:
        chk = branch_closing.objects.all().filter(apr='', branch_name='branch2').exists()
        print(chk)
        if chk == True:
            conn = py.connect(host=database_host, user=database_user, password=database_password,database=database_name)
            query = 'create table branch2app_branch1_closing_apr select * from branch2app_pg1_new_beds'
            # create cursor object to execute the query
            cur = conn.cursor()
            cur.execute(query)

            bc = branch_closing.objects.get(branch_name='branch2')
            bc.apr = 1
            bc.save()
            return may_print2(request)
    return render(request,'index.html')

def apr_close_decision_page2(request):
    if 'username' in request.session:
        chk = branch_closing.objects.all().filter(apr='', branch_name='branch2').exists()
        print(chk)
        if chk == True:
            return render(request, 'branches/branch2/close_months/apr_months_close_page.html')
        if chk == False:
            return may_print2(request)
    return render(request,'index.html')



def may_print2(request):
    if 'username' in request.session:
        l = []
        data = pg1_new_beds.objects.all()
        for i in data:
            l.append(i.share_type)

        ll = []
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
        return render(request,'branches/branch2/print_outs/may_print.html',context)
    return render(request, 'index.html')



def may_close2(request):
    if 'username' in request.session:
        chk = branch_closing.objects.all().filter(may='', branch_name='branch2').exists()
        print(chk)
        if chk == True:
            conn = py.connect(host=database_host, user=database_user, password=database_password,database=database_name)
            query = 'create table branch2app_branch1_closing_may select * from branch2app_pg1_new_beds'
            # create cursor object to execute the query
            cur = conn.cursor()
            cur.execute(query)

            bc = branch_closing.objects.get(branch_name='branch2')
            bc.may = 1
            bc.save()
            return june_print2(request)
    return render(request,'index.html')

def may_close_decision_page2(request):
    if 'username' in request.session:
        chk = branch_closing.objects.all().filter(may='', branch_name='branch2').exists()
        print(chk)
        if chk == True:
            return render(request, 'branches/branch2/close_months/may_months_close_page.html')
        if chk == False:
            return june_print2(request)
    return render(request,'index.html')



def june_print2(request):
    if 'username' in request.session:
        l = []
        data = pg1_new_beds.objects.all()
        for i in data:
            l.append(i.share_type)

        ll = []
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
        return render(request,'branches/branch2/print_outs/june_print.html',context)
    return render(request, 'index.html')

def jun_close2(request):
    if 'username' in request.session:
        chk = branch_closing.objects.all().filter(jun='', branch_name='branch2').exists()
        print(chk)
        if chk == True:
            conn = py.connect(host=database_host, user=database_user, password=database_password,database=database_name)
            query = 'create table branch2app_branch1_closing_jun select * from branch2app_pg1_new_beds'
            # create cursor object to execute the query
            cur = conn.cursor()
            cur.execute(query)

            bc = branch_closing.objects.get(branch_name='branch2')
            bc.jun = 1
            bc.save()
            return july_print2(request)
    return render(request,'index.html')

def jun_close_decision_page2(request):
    if 'username' in request.session:
        chk = branch_closing.objects.all().filter(jun='', branch_name='branch2').exists()
        print(chk)
        if chk == True:
            return render(request, 'branches/branch2/close_months/jun_months_close_page.html')
        if chk == False:
            return july_print2(request)
    return render(request,'index.html')


def july_print2(request):
    if 'username' in request.session:
        l = []
        data = pg1_new_beds.objects.all()
        for i in data:
            l.append(i.share_type)

        ll = []
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
        return render(request,'branches/branch2/print_outs/july_print.html',context)
    return render(request, 'index.html')


def jul_close2(request):
    if 'username' in request.session:
        chk = branch_closing.objects.all().filter(jul='', branch_name='branch2').exists()
        print(chk)
        if chk == True:
            conn = py.connect(host=database_host, user=database_user, password=database_password,database=database_name)
            query = 'create table branch2app_branch1_closing_jul select * from branch2app_pg1_new_beds'
            # create cursor object to execute the query
            cur = conn.cursor()
            cur.execute(query)

            bc = branch_closing.objects.get(branch_name='branch2')
            bc.jul = 1
            bc.save()
            return aug_print2(request)
    return render(request,'index.html')

def jul_close_decision_page2(request):
    if 'username' in request.session:
        chk = branch_closing.objects.all().filter(jul='', branch_name='branch2').exists()
        print(chk)
        if chk == True:
            return render(request, 'branches/branch2/close_months/jul_months_close_page.html')
        if chk == False:
            return aug_print2(request)
    return render(request,'index.html')


def aug_print2(request):
    if 'username' in request.session:
        l = []
        data = pg1_new_beds.objects.all()
        for i in data:
            l.append(i.share_type)

        ll = []
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
        return render(request,'branches/branch2/print_outs/aug_print.html',context)
    return render(request, 'index.html')


def aug_close2(request):
    if 'username' in request.session:
        chk = branch_closing.objects.all().filter(aug='', branch_name='branch2').exists()
        print(chk)
        if chk == True:
            conn = py.connect(host=database_host, user=database_user, password=database_password,database=database_name)
            query = 'create table branch2app_branch1_closing_aug select * from branch2app_pg1_new_beds'
            # create cursor object to execute the query
            cur = conn.cursor()
            cur.execute(query)

            bc = branch_closing.objects.get(branch_name='branch2')
            bc.aug = 1
            bc.save()
            return sept_print2(request)
    return render(request,'index.html')

def aug_close_decision_page2(request):
    if 'username' in request.session:
        chk = branch_closing.objects.all().filter(aug='', branch_name='branch2').exists()
        print(chk)
        if chk == True:
            return render(request, 'branches/branch2/close_months/aug_months_close_page.html')
        if chk == False:
            return sept_print2(request)
    return render(request,'index.html')


def sept_print2(request):
    if 'username' in request.session:
        l = []
        data = pg1_new_beds.objects.all()
        for i in data:
            l.append(i.share_type)

        ll = []
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
            '408_data': pg1_new_beds.objects.all().filter(roon_no=308),
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
        return render(request,'branches/branch2/print_outs/sept_print.html',context)
    return render(request, 'index.html')

def sep_close2(request):
    if 'username' in request.session:
        chk = branch_closing.objects.all().filter(sep='', branch_name='branch2').exists()
        print('MYSEP CHDK ',chk)
        if chk == True:
            conn = py.connect(host=database_host, user=database_user, password=database_password,database=database_name)
            query = 'create table branch2app_branch1_closing_sep select * from branch2app_pg1_new_beds'
            # create cursor object to execute the query
            cur = conn.cursor()
            cur.execute(query)

            bc = branch_closing.objects.get(branch_name='branch2')
            bc.sep = 1
            bc.save()
            return oct_print2(request)
    return render(request,'index.html')

def sep_close_decision_page2(request):
    if 'username' in request.session:
        chk = branch_closing.objects.all().filter(sep='', branch_name='branch2').exists()
        print(chk)
        if chk == True:
            return render(request, 'branches/branch2/close_months/sep_months_close_page.html')
        if chk == False:
            return oct_print2(request)
    return render(request,'index.html')


def oct_print2(request):
    if 'username' in request.session:
        l = []
        data = pg1_new_beds.objects.all()
        for i in data:
            l.append(i.share_type)

        ll = []
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
        return render(request,'branches/branch2/print_outs/oct_print.html',context)
    return render(request, 'index.html')



def oct_close2(request):
    if 'username' in request.session:
        chk = branch_closing.objects.all().filter(oct='', branch_name='branch2').exists()
        print(chk)
        if chk == True:
            conn = py.connect(host=database_host, user=database_user, password=database_password,database=database_name)
            query = 'create table branch2app_branch1_closing_oct select * from branch2app_pg1_new_beds'
            # create cursor object to execute the query
            cur = conn.cursor()
            cur.execute(query)

            bc = branch_closing.objects.get(branch_name='branch2')
            bc.oct = 1
            bc.save()
            return nov_print2(request)
    return render(request,'index.html')

def oct_close_decision_page2(request):
    if 'username' in request.session:
        chk = branch_closing.objects.all().filter(oct='', branch_name='branch2').exists()
        print(chk)
        if chk == True:
            return render(request, 'branches/branch2/close_months/oct_months_close_page.html')
        if chk == False:
            return nov_print2(request)
    return render(request,'index.html')


def nov_print2(request):
    if 'username' in request.session:
        l = []
        data = pg1_new_beds.objects.all()
        for i in data:
            l.append(i.share_type)

        ll = []
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
        return render(request,'branches/branch2/print_outs/nov_print.html',context)
    return render(request, 'index.html')


def nov_close2(request):
    if 'username' in request.session:
        chk = branch_closing.objects.all().filter(nov='', branch_name='branch2').exists()
        print(chk)
        if chk == True:
            conn = py.connect(host=database_host, user=database_user, password=database_password,database=database_name)
            query = 'create table branch2app_branch1_closing_nov select * from branch2app_pg1_new_beds'
            # create cursor object to execute the query
            cur = conn.cursor()
            cur.execute(query)

            bc = branch_closing.objects.get(branch_name='branch2')
            bc.nov = 1
            bc.save()
            return dec_print2(request)
    return render(request,'index.html')

def nov_close_decision_page2(request):
    if 'username' in request.session:
        chk = branch_closing.objects.all().filter(nov='', branch_name='branch2').exists()
        print(chk)
        if chk == True:
            return render(request, 'branches/branch2/close_months/nov_months_close_page.html')
        if chk == False:
            return dec_print2(request)
    return render(request,'index.html')


def dec_print2(request):
    if 'username' in request.session:
        l = []
        data = pg1_new_beds.objects.all()
        for i in data:
            l.append(i.share_type)

        ll = []
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
        return render(request,'branches/branch2/print_outs/dec_print.html',context)
    return render(request, 'index.html')

##################################
#PRINT OUTS END HERE
################################

##################################
#VACATE GUEST DETAILS START HERE
################################

def viewall_vacate_guest2(request):
    context = {
        'vg' : pg1_new_guest.objects.all().filter(flag=3,remark__gt='0').exclude(remark = '').order_by('-id')
    }
    return render(request,'branches/branch2/vacate_guest/viewall_vacate_guest.html',context)

def details_of_vacate_guest2(request,id):
    context = {
        'user_details': pg1_new_guest.objects.all().filter(id=id),
    }
    return render(request,'branches/branch2/vacate_guest/details_of_vacate_guest.html',context)


# ***********vacate guest payments start here*******

def jan_manke_payments_vacate2(request, id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt = request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')
            due_amt = request.POST.get('dueamt')
            dis_amt = request.POST.get('disamt')

            jp = pg1_new_guest.objects.get(id=id)
            jp.jan_rent = amt
            jp.remark = remark
            jp.jan_due_amt = due_amt
            jp.jan_dis_amt = dis_amt
            jp.jan_rent_rec_date = date
            jp.jan_rent_flag = 200
            jp.save()

            context = {
                'user_details': pg1_new_guest.objects.all().filter(id=id)
            }
            return render(request, 'branches/branch2/vacate_guest/details_of_vacate_guest.html', context)

        rno = pg1_new_guest.objects.all().filter(id=id)
        l = []
        for i in rno:
            l.append(str(i.guest_code))
        gc = ''.join(l)
        print('lll', l)

        import branch2app
        total_discout_amt = []
        pg1_new_beds = branch2app.models.pg1_new_guest.objects.all().filter(flag=3, guest_code=l[0])
        for i in pg1_new_beds:
            total_discout_amt.append(int(i.jan_dis_amt))

        context = {
            'sd': pg1_new_guest.objects.get(id=id),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
            'discount_amt': total_discout_amt[0],
        }
        return render(request, 'branches/branch2/payments/details_of_months/jan/jan_manke_payments_vacate.html',context)


def feb_manke_payments_vacate2(request, id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt = request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')
            due_amt = request.POST.get('dueamt')
            dis_amt = request.POST.get('disamt')

            jp = pg1_new_guest.objects.get(id=id)
            jp.feb_rent = amt
            jp.remark = remark
            jp.feb_due_amt = due_amt
            jp.feb_dis_amt = dis_amt
            jp.feb_rent_rec_date = date
            jp.feb_rent_flag = 200
            jp.save()
            context = {
                'user_details': pg1_new_guest.objects.all().filter(id=id),
            }
            return render(request, 'branches/branch2/vacate_guest/details_of_vacate_guest.html', context)

        rno = pg1_new_guest.objects.all().filter(id=id)
        l = []
        for i in rno:
            l.append(str(i.guest_code))
        gc = ''.join(l)
        print('lll', l)

        import branch2app
        total_discout_amt = []
        pg1_new_beds = branch2app.models.pg1_new_guest.objects.all().filter(flag=3, guest_code=l[0])
        for i in pg1_new_beds:
            total_discout_amt.append(int(i.feb_dis_amt))

        context = {
            'sd': pg1_new_guest.objects.get(id=id),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
            'discount_amt': total_discout_amt[0],
        }
        return render(request, 'branches/branch2/payments/details_of_months/feb/feb_manke_payments_vacate.html',context)


def march_manke_payments_vacate2(request, id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt = request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')
            due_amt = request.POST.get('dueamt')
            dis_amt = request.POST.get('disamt')

            jp = pg1_new_guest.objects.get(id=id)
            jp.march_rent = amt
            jp.remark = remark
            jp.march_due_amt = due_amt
            jp.march_dis_amt = dis_amt
            jp.march_rent_rec_date = date
            jp.march_rent_flag = 200
            jp.save()
            context = {
                'user_details': pg1_new_guest.objects.all().filter(id=id),
            }
            return render(request, 'branches/branch2/vacate_guest/details_of_vacate_guest.html', context)

        rno = pg1_new_guest.objects.all().filter(id=id)
        l = []
        for i in rno:
            l.append(str(i.guest_code))
        gc = ''.join(l)
        print('lll', l)

        import branch2app
        total_discout_amt = []
        pg1_new_beds = branch2app.models.pg1_new_guest.objects.all().filter(flag=3, guest_code=l[0])
        for i in pg1_new_beds:
            total_discout_amt.append(int(i.march_dis_amt))

        context = {
            'sd': pg1_new_guest.objects.get(id=id),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
            'discount_amt': total_discout_amt[0],
        }
        return render(request, 'branches/branch2/payments/details_of_months/march/march_manke_payments_vacate.html',context)


def april_make_payments_vacate2(request, id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt = request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')
            due_amt = request.POST.get('dueamt')
            dis_amt = request.POST.get('disamt')

            jp = pg1_new_guest.objects.get(id=id)
            jp.april_rent = amt
            jp.remark = remark
            jp.april_due_amt = due_amt
            jp.april_dis_amt = dis_amt
            jp.april_rent_rec_date = date
            jp.april_rent_flag = 200
            jp.save()

            context = {
                'user_details': pg1_new_guest.objects.all().filter(id=id),
            }
            return render(request, 'branches/branch2/vacate_guest/details_of_vacate_guest.html', context)

        rno = pg1_new_guest.objects.all().filter(id=id)
        l = []
        for i in rno:
            l.append(str(i.guest_code))
        gc = ''.join(l)
        print('lll', l)

        import branch2app
        total_discout_amt = []
        pg1_new_beds = branch2app.models.pg1_new_guest.objects.all().filter(flag=3, guest_code=l[0])
        for i in pg1_new_beds:
            total_discout_amt.append(int(i.april_dis_amt))

        context = {
            'sd': pg1_new_guest.objects.get(id=id),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
            'discount_amt': total_discout_amt[0],
        }
        return render(request,'branches/branch2/vacate_guest/vacate_payments/details_of_months/april/april_make_payments_vacate.html',context)


def may_make_payments_vacate2(request, id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt = request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')
            due_amt = request.POST.get('dueamt')
            dis_amt = request.POST.get('disamt')

            jp = pg1_new_guest.objects.get(id=id)
            jp.may_rent = amt
            jp.remark = remark
            jp.may_due_amt = due_amt
            jp.may_dis_amt = dis_amt
            jp.may_rent_rec_date = date
            jp.may_rent_flag = 200
            jp.save()
            context = {
                'user_details': pg1_new_guest.objects.all().filter(id=id),
            }
            return render(request, 'branches/branch2/vacate_guest/details_of_vacate_guest.html', context)

        rno = pg1_new_guest.objects.all().filter(id=id)
        l = []
        for i in rno:
            l.append(str(i.guest_code))
        gc = ''.join(l)
        print('lll', l)

        import branch2app
        total_discout_amt = []
        pg1_new_beds = branch2app.models.pg1_new_guest.objects.all().filter(flag=3, guest_code=l[0])
        for i in pg1_new_beds:
            total_discout_amt.append(int(i.may_dis_amt))

        context = {
            'sd': pg1_new_guest.objects.get(id=id),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
            'discount_amt': total_discout_amt[0],
        }
        return render(request,'branches/branch2/vacate_guest/vacate_payments/details_of_months/may/may_make_payments_vacate.html',context)


def june_make_payments_vacate2(request, id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt = request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')
            due_amt = request.POST.get('dueamt')
            dis_amt = request.POST.get('disamt')

            jp = pg1_new_guest.objects.get(id=id)
            jp.june_rent = amt
            jp.remark = remark
            jp.june_due_amt = due_amt
            jp.june_dis_amt = dis_amt
            jp.june_rent_rec_date = date
            jp.june_rent_flag = 200
            jp.save()
            context = {
                'user_details': pg1_new_guest.objects.all().filter(id=id)
            }
            return render(request, 'branches/branch2/vacate_guest/details_of_vacate_guest.html', context)

        rno = pg1_new_guest.objects.all().filter(id=id)
        l = []
        for i in rno:
            l.append(str(i.guest_code))
        gc = ''.join(l)
        print('lll', l)

        import branch2app
        total_discout_amt = []
        pg1_new_beds = branch2app.models.pg1_new_guest.objects.all().filter(flag=3, guest_code=l[0])
        for i in pg1_new_beds:
            total_discout_amt.append(int(i.june_dis_amt))

        context = {
            'sd': pg1_new_guest.objects.get(id=id),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
            'discount_amt': total_discout_amt[0],
        }
        return render(request,'branches/branch2/vacate_guest/vacate_payments/details_of_months/june/june_make_payments_vacate.html',context)


def july_make_payments_vacate2(request, id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt = request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')
            due_amt = request.POST.get('dueamt')
            dis_amt = request.POST.get('disamt')

            jp = pg1_new_guest.objects.get(id=id)
            jp.july_rent = amt
            jp.remark = remark
            jp.july_due_amt = due_amt
            jp.july_dis_amt = dis_amt
            jp.july_rent_rec_date = date
            jp.july_rent_flag = 200
            jp.save()
            context = {
                'user_details': pg1_new_guest.objects.all().filter(id=id),
            }
            return render(request, 'branches/branch2/vacate_guest/details_of_vacate_guest.html', context)
        rno = pg1_new_guest.objects.all().filter(id=id)
        l = []
        for i in rno:
            l.append(str(i.guest_code))
        gc = ''.join(l)
        print('lll', l)

        import branch2app
        total_discout_amt = []
        pg1_new_beds = branch2app.models.pg1_new_guest.objects.all().filter(flag=3, guest_code=l[0])
        for i in pg1_new_beds:
            total_discout_amt.append(int(i.july_dis_amt))
        context = {
            'user_details': pg1_new_guest.objects.all().filter(id=id),
            'sd': pg1_new_guest.objects.get(id=id),
            'discount_amt': total_discout_amt[0],
        }
        return render(request,'branches/branch2/vacate_guest/vacate_payments/details_of_months/july/july_make_payments_vacate.html',context)


def aug_make_payments_vacate2(request, id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt = request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')
            due_amt = request.POST.get('dueamt')
            dis_amt = request.POST.get('disamt')

            jp = pg1_new_guest.objects.get(id=id)
            jp.auguest_rent = amt
            jp.remark = remark
            jp.auguest_due_amt = due_amt
            jp.auguest_dis_amt = dis_amt
            jp.auguest_rent_rec_date = date
            jp.auguest_rent_flag = 200
            jp.save()

            context = {
                'user_details': pg1_new_guest.objects.all().filter(id=id),
            }
            return render(request, 'branches/branch2/vacate_guest/details_of_vacate_guest.html', context)

        rno = pg1_new_guest.objects.all().filter(id=id)
        l = []
        for i in rno:
            l.append(str(i.guest_code))
            gc = ''.join(l)
        print('lll', l)

        import branch2app
        total_discout_amt = []
        pg1_new_beds = branch2app.models.pg1_new_guest.objects.all().filter(flag=3, guest_code=l[0])
        for i in pg1_new_beds:
            total_discout_amt.append(int(i.auguest_dis_amt))

        context = {
            'sd': pg1_new_guest.objects.get(id=id),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
            'discount_amt': total_discout_amt[0],
        }
        return render(request,'branches/branch2/vacate_guest/vacate_payments/details_of_months/aug/aug_make_payments_vacate.html',context)


def sept_make_payments_vacate2(request, id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt = request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')
            due_amt = request.POST.get('dueamt')
            dis_amt = request.POST.get('disamt')

            jp = pg1_new_guest.objects.get(id=id)
            jp.sept_rent = amt
            jp.remark = remark
            jp.sept_due_amt = due_amt
            jp.sept_dis_amt = dis_amt
            jp.sept_rent_rec_date = date
            jp.sept_rent_flag = 200
            jp.save()

            context = {
                'user_details': pg1_new_guest.objects.all().filter(id=id),
            }
            return render(request, 'branches/branch2/vacate_guest/details_of_vacate_guest.html', context)

        rno = pg1_new_guest.objects.all().filter(id=id)
        l = []
        for i in rno:
            l.append(str(i.guest_code))
        gc = ''.join(l)
        print('lll', l)

        import branch2app
        total_discout_amt = []
        pg1_new_beds = branch2app.models.pg1_new_guest.objects.all().filter(flag=3, guest_code=l[0])
        for i in pg1_new_beds:
            total_discout_amt.append(int(i.sept_dis_amt))

        context = {
            'sd': pg1_new_guest.objects.get(id=id),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
            'discount_amt': total_discout_amt[0],
        }
        return render(request,'branches/branch2/vacate_guest/vacate_payments/details_of_months/sept/sept_make_payments_vacate.html',context)


def oct_make_payments_vacate2(request, id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt = request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')
            due_amt = request.POST.get('dueamt')
            dis_amt = request.POST.get('disamt')

            jp = pg1_new_guest.objects.get(id=id)
            jp.october_rent = amt
            jp.remark = remark
            jp.october_due_amt = due_amt
            jp.october_dis_amt = dis_amt
            jp.october_rent_rec_date = date
            jp.october_rent_flag = 200
            jp.save()
            context = {
                'user_details': pg1_new_guest.objects.all().filter(id=id),
            }
            return render(request, 'branches/branch2/vacate_guest/details_of_vacate_guest.html', context)

        rno = pg1_new_guest.objects.all().filter(id=id)
        l = []
        for i in rno:
            l.append(str(i.guest_code))
        gc = ''.join(l)
        print('lll', l)

        import branch2app
        total_discout_amt = []
        pg1_new_beds = branch2app.models.pg1_new_guest.objects.all().filter(flag=3, guest_code=l[0])
        for i in pg1_new_beds:
            total_discout_amt.append(int(i.october_dis_amt))

        context = {
            'sd': pg1_new_guest.objects.get(id=id),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
            'discount_amt': total_discout_amt[0],
        }
        return render(request,'branches/branch2/vacate_guest/vacate_payments/details_of_months/oct/oct_make_payments_vacate.html',context)


def nov_make_payments_vacate2(request, id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt = request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')
            due_amt = request.POST.get('dueamt')
            dis_amt = request.POST.get('disamt')

            jp = pg1_new_guest.objects.get(id=id)
            jp.nov_rent = amt
            jp.remark = remark
            jp.nov_due_amt = due_amt
            jp.nov_dis_amt = dis_amt
            jp.nov_rent_rec_date = date
            jp.nov_rent_flag = 200
            jp.save()
            context = {
                'user_details': pg1_new_guest.objects.all().filter(id=id),
            }
            return render(request, 'branches/branch2/vacate_guest/details_of_vacate_guest.html', context)

        rno = pg1_new_guest.objects.all().filter(id=id)
        l = []
        for i in rno:
            l.append(str(i.guest_code))
        gc = ''.join(l)
        print('lll', l)

        import branch2app
        total_discout_amt = []
        pg1_new_beds = branch2app.models.pg1_new_guest.objects.all().filter(flag=3, guest_code=l[0])
        for i in pg1_new_beds:
            total_discout_amt.append(int(i.nov_dis_amt))

        context = {
            'sd': pg1_new_guest.objects.get(id=id),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
            'discount_amt': total_discout_amt[0],
        }
        return render(request,'branches/branch2/vacate_guest/vacate_payments/details_of_months/nov/nov_make_payments_vacate.html',context)


def dec_make_payments_vacate2(request, id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt = request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')
            due_amt = request.POST.get('dueamt')
            dis_amt = request.POST.get('disamt')

            jp = pg1_new_guest.objects.get(id=id)
            jp.dec_rent = amt
            jp.remark = remark
            jp.dec_due_amt = due_amt
            jp.dec_dis_amt = dis_amt
            jp.dec_rent_rec_date = date
            jp.dec_rent_flag = 200
            jp.save()
            context = {
                'user_details': pg1_new_guest.objects.all().filter(id=id),
            }
            return render(request, 'branches/branch2/vacate_guest/details_of_vacate_guest.html', context)

        rno = pg1_new_guest.objects.all().filter(id=id)
        l = []
        for i in rno:
            l.append(str(i.guest_code))
        gc = ''.join(l)
        print('lll', l)

        import branch2app
        total_discout_amt = []
        pg1_new_beds = branch2app.models.pg1_new_guest.objects.all().filter(flag=3, guest_code=l[0])
        for i in pg1_new_beds:
            total_discout_amt.append(int(i.dec_dis_amt))

        context = {
            'sd': pg1_new_guest.objects.get(id=id),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
            'discount_amt': total_discout_amt[0],
        }
        return render(request,'branches/branch2/vacate_guest/vacate_payments/details_of_months/dec/dec_make_payments_vacate.html',context)



# ************vacate guest payments end here*******



##################################
#VACATE GUEST DETAILS END HERE
################################


########################################
#DUE AMT MANAGEMENT START HERE
###########################

def view_all_due_amt2(request):
    context={
        'due_amt' : pg1_new_beds.objects.all().filter(flag=2).order_by('roon_no'),
    }
    return render(request, 'branches/branch2/due_amt_mgt/view_all_due_amt.html',context)

def due_amt_mgt_choose_months2(request):
    return render(request, 'branches/branch2/due_amt_mgt/due_amt_mgt_choose_months.html')


def view_may_account_details2(request):
    context = {
        'due_amt': pg1_new_guest.objects.all().filter(flag=2,may_rent_flag__gt=99).order_by('roon_no'),
    }
    return render(request, 'branches/branch2/due_amt_mgt/monthly_detailes_due_amt/may/view_may_account_details.html',context)
def may_account_mgt2(request, id):
    if 'username' in request.session:
        if request.method == 'POST':
            paid_amt = request.POST.get('pamt')
            advance = request.POST.get('adv')
            discount = request.POST.get('dis')
            due_amt = request.POST.get('due')
            remark = request.POST.get('rem')

            import branch2app
            rno = branch2app.models.pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))

            import branch2app
            ic = branch2app.models.pg1_new_guest.objects.get(guest_code=l[0])
            ic.may_rent = paid_amt
            ic.may_advance = advance
            ic.may_dis_amt = discount
            ic.may_due_amt = due_amt
            ic.remark = remark
            ic.save()

            ic = pg1_new_beds.objects.get(guest_code=l[0])
            ic.may_rent = paid_amt
            ic.may_advance = advance
            ic.may_dis_amt = discount
            ic.may_due_amt = due_amt
            ic.remark = remark
            ic.save()
            return view_may_account_details2(request)

        context = {
            'sd': pg1_new_guest.objects.get(id=id),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
        }
        return render(request, 'branches/branch2/due_amt_mgt/monthly_detailes_due_amt/may/may_account_mgt.html',context)


def view_june_account_details2(request):
    context = {
        'due_amt': pg1_new_guest.objects.all().filter(flag=2,june_rent_flag__gt=99).order_by('roon_no'),
    }
    return render(request,'branches/branch2/due_amt_mgt/monthly_detailes_due_amt/june/view_june_account_details.html',context)
def june_account_mgt2(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            paid_amt = request.POST.get('pamt')
            advance = request.POST.get('adv')
            discount = request.POST.get('dis')
            due_amt = request.POST.get('due')
            remark = request.POST.get('rem')

            import branch2app
            rno = branch2app.models.pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))

            import branch2app
            ic = branch2app.models.pg1_new_guest.objects.get(guest_code=l[0])
            ic.june_rent = paid_amt
            ic.june_advance = advance
            ic.june_dis_amt = discount
            ic.june_due_amt = due_amt
            ic.remark = remark
            ic.save()

            import branch2app
            ic = branch2app.models.pg1_new_beds.objects.get(guest_code=l[0])
            ic.june_rent = paid_amt
            ic.june_advance = advance
            ic.june_dis_amt = discount
            ic.june_due_amt = due_amt
            ic.remark = remark
            ic.save()
            return view_june_account_details2(request)

        context = {
            'sd' : pg1_new_guest.objects.get(id=id),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
        }
        return render(request,'branches/branch2/due_amt_mgt/monthly_detailes_due_amt/june/june_account_mgt.html',context)


def view_july_account_details2(request):
    context = {
        'due_amt': pg1_new_guest.objects.all().filter(flag=2,july_rent_flag__gt=99).order_by('roon_no'),
    }
    return render(request,'branches/branch2/due_amt_mgt/monthly_detailes_due_amt/july/view_july_account_details.html',context)
def july_account_mgt2(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            paid_amt = request.POST.get('pamt')
            advance = request.POST.get('adv')
            discount = request.POST.get('dis')
            due_amt = request.POST.get('due')
            remark = request.POST.get('rem')

            import branch2app
            rno = branch2app.models.pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))

            import branch2app
            ic = branch2app.models.pg1_new_guest.objects.get(guest_code=l[0])
            ic.july_rent = paid_amt
            ic.july_advance = advance
            ic.july_dis_amt = discount
            ic.july_due_amt = due_amt
            ic.remark = remark
            ic.save()

            ic = pg1_new_beds.objects.get(guest_code=l[0])
            ic.july_rent = paid_amt
            ic.july_advance = advance
            ic.july_dis_amt = discount
            ic.july_due_amt = due_amt
            ic.remark = remark
            ic.save()
            return view_july_account_details2(request)

        context = {
            'sd' : pg1_new_guest.objects.get(id=id),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
        }
        return render(request,'branches/branch2/due_amt_mgt/monthly_detailes_due_amt/july/july_account_mgt.html',context)




########################################
#DUE AMT MANAGEMENT END HERE
###########################




def pysql (request):
    chk = branch_closing.objects.all().filter(jan='',branch_name='branch1').exists()
    print(chk)
    if chk == True:

        conn = py.connect(host=database_host, user=database_user, password=database_password, database=database_name)
        query = 'create table myapp_branch1_closing_jan select * from myapp_pg1_new_beds'
        # create cursor object to execute the query
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute(query)

        bc=branch_closing.objects.get(branch_name='branch1')
        bc.jan = 1
        bc.save()

        return render (request,'branches/branch1/test.html')
    return branch1_dashboard (request)

