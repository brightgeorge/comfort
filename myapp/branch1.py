import datetime as datetime
from django.shortcuts import render
from django.contrib import messages

from myapp.models import *
import datetime

def branch_index(request):
    if 'username' in request.session:
        return render(request, 'branches/branch1/branch_index.html')

def guest_creation(request):
    if 'username' in request.session:
        context = {
            'rn' : pg1_rooom.objects.all()
        }
        return render(request, 'branches/branch1/guests/guest_creation.html',context)

def guest_creation_regi(request):
    print(request)
    room_no = request.POST.get('roomno')
    name = request.POST.get('name')
    room_type = request.POST.get('roomtype')
    monthly_rent = request.POST.get('monthlyrent')
    advance = request.POST.get('advance')
    age = request.POST.get('age')
    dom = request.POST.get('dob')
    edu_qulification = request.POST.get('eduqualification')
    mail_id = request.POST.get('mailid')
    self_mob_no = request.POST.get('selfmobno')
    id_proof_type = request.POST.get('idprooftype')
    id_proof_no = request.POST.get('idproofno')

    prsnts_emp_name = request.POST.get('presentemployee')
    prsnts_contact_no = request.POST.get('pemployeecontactno')
    prsnts_emp_address = request.POST.get('pempaddress')

    father_name =  request.POST.get('fname')
    father_mob_no = request.POST.get('fmobno')
    emg_contact_no = request.POST.get('emgcontactno')
    relationship = request.POST.get('relatioship')

    permanent_address = request.POST.get('paddress')
    #join_date = datetime.datetime.now()
    fl = request.POST.get('eanable_disable')

    chk = 11
    if fl == None:
        chk = 0
    else:
        chk = 1

    gc = pg1_regform()

    gc.room_no = room_no
    gc.name = name
    gc.room_type = room_type
    gc.monthly_rent = monthly_rent
    gc.advance = advance
    gc.age = age
    gc.dob = dom
    gc.edu_qualification = edu_qulification
    gc.mail_id = mail_id
    gc.self_mob_no = self_mob_no
    gc.id_proof_type = id_proof_type
    gc.id_proof_no = id_proof_no

    gc.prsnt_employee = prsnts_emp_name
    gc.prsnt_emp_contact_no = prsnts_contact_no
    gc.prsnt_emp_address = prsnts_emp_address

    gc.fname = father_name
    gc.fmob_no = father_mob_no
    gc.emg_contact_no = emg_contact_no
    gc.relationship = relationship

    gc.permanent_address = permanent_address
    import datetime
    gc.join_date = datetime.datetime.now()

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
    # print(datetime.date.today())

    gc.jan_rent = 0
    gc.jan_rent_flag = il[0]
    gc.feb_rent = 0
    gc.feb_rent_flag = il[1]
    gc.march_rent = 0
    gc.march_rent_flag = il[2]
    gc.april_rent = 0
    gc.april_rent_flag = il[3]

    gc.may_rent = 0
    gc.may_rent_flag = il[4]
    gc.june_rent = 0
    gc.june_rent_flag = il[5]
    gc.july_rent = 0
    gc.july_rent_flag = il[6]
    gc.aug_rent = 0
    gc.aug_rent_flag = il[7]

    gc.sept_rent = 0
    gc.sept_rent_flag = il[8]
    gc.oct_rent = 0
    gc.oct_rent_flag = il[9]
    gc.nov_rent = 0
    gc.nov_rent_flag = il[10]
    gc.dec_rent = 0
    gc.dec_rent_flag = il[11]

    gc.year = 0
    gc.month = 0
    gc.branch_name = 0
    gc.flag = chk
    gc.save()
    context = {
        'pg1_guests': pg1_regform.objects.all().filter(flag=1),
    }

    return render(request, 'branches/branch1/guests/view_all_guests.html',context)

def view_all_guests(request):
    if 'username' in request.session:
        context = {
            'pg1_guests' : pg1_regform.objects.all().filter(flag=1),
        }
        return render(request,'branches/branch1/guests/view_all_guests.html',context)
    return render(request, 'index.html')

def update_guest_creation(request,id):
    if request.method == 'POST':
        print(request)
        room_no = request.POST.get('roomno')
        name = request.POST.get('name')
        room_type = request.POST.get('roomtype')
        monthly_rent = request.POST.get('monthlyrent')
        advance = request.POST.get('advance')
        age = request.POST.get('age')
        dom = request.POST.get('dob')
        edu_qulification = request.POST.get('eduqualification')
        mail_id = request.POST.get('mailid')
        self_mob_no = request.POST.get('selfmobno')
        id_proof_type = request.POST.get('idprooftype')
        id_proof_no = request.POST.get('idproofno')

        prsnts_emp_name = request.POST.get('presentemployee')
        prsnts_contact_no = request.POST.get('pemployeecontactno')
        prsnts_emp_address = request.POST.get('pempaddress')

        father_name =  request.POST.get('fname')
        father_mob_no = request.POST.get('fmobno')
        emg_contact_no = request.POST.get('emgcontactno')
        relationship = request.POST.get('relatioship')

        permanent_address = request.POST.get('paddress')
        #join_date = datetime.datetime.now()
        fl = request.POST.get('eanable_disable')

        chk = 11
        if fl == None:
            chk = 0
        else:
            chk = 1

        gc = pg1_regform.objects.get(id=id)

        gc.room_no = room_no
        gc.name = name
        gc.room_type = room_type
        gc.monthly_rent = monthly_rent
        gc.advance = advance
        gc.age = age
        gc.dob = dom
        gc.edu_qualification = edu_qulification
        gc.mail_id = mail_id
        gc.self_mob_no = self_mob_no
        gc.id_proof_type = id_proof_type
        gc.id_proof_no = id_proof_no

        gc.prsnt_employee = prsnts_emp_name
        gc.prsnt_emp_contact_no = prsnts_contact_no
        gc.prsnt_emp_address = prsnts_emp_address

        gc.fname = father_name
        gc.fmob_no = father_mob_no
        gc.emg_contact_no = emg_contact_no
        gc.relationship = relationship

        gc.permanent_address = permanent_address
        import datetime
        gc.join_date = datetime.datetime.now()



        gc.year = 0
        gc.month = 0
        gc.branch_name = 0
        gc.flag = chk
        gc.save()

        context = {
            'pg1_guests': pg1_regform.objects.all().filter(flag=1),
        }

        return render(request, 'branches/branch1/guests/view_all_guests.html', context)

    context = {
        'pg1_guests': pg1_regform.objects.all().filter(flag=1),
        'sd':pg1_regform.objects.get(id=id),
        'rn': pg1_rooom.objects.all()
    }

    return render(request, 'branches/branch1/guests/update_guest_creation.html',context)

def delete_guest_creation(request):
    de=pg1_regform.objects.get(id=id)
    de.delet()
    return render(request,'')

##################################
#REPORTS START HERE
################################

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

    aa='pg1_regform.objects.all().filter('
    bb='=100,flag=1),'
    c=aa+p+bb
    print(c)
    z=pg1_regform.objects.all().filter(march_rent_flag=100,flag=1),
    context = {
        'up': z,
        'name' : request.session['username']
    }
    return render(request, 'branches/branch1/reports/unpaid_rent.html', context)

def paid_rent(request):
    context = {
        'up': pg1_regform.objects.all().filter(march_rent_flag=200,flag=1),
        'name' : request.session['username']
    }
    return render(request, 'branches/branch1/reports/paid_rent.html', context)

#************unpaid rent start here********

def unpaid_rent_choose_months(request):
    if 'username' in request.session:
        return render(request, 'branches/branch1/reports/unpaid_rent_choose_months.html')

def jan_unpaid_rent(request):
    if 'username' in request.session:
        context = {
            'up': pg1_regform.objects.all().filter(jan_rent_flag=100, flag=1).order_by('room_no'),
            'name': request.session['username'],
            'month_name': 'JANUARY'
        }
        return render(request, 'branches/branch1/reports/unpaid_rent.html', context)
def feb_unpaid_rent(request):
    if 'username' in request.session:
        context = {
            'up': pg1_regform.objects.all().filter(feb_rent_flag=100, flag=1).order_by('room_no'),
            'name': request.session['username'],
            'month_name': 'FEB'
        }
        return render(request, 'branches/branch1/reports/unpaid_rent.html', context)
def mar_unpaid_rent(request):
    if 'username' in request.session:
        context = {
            'up': pg1_regform.objects.all().filter(march_rent_flag=100, flag=1).order_by('room_no'),
            'name': request.session['username'],
            'month_name': 'MARCH'
        }
        return render(request, 'branches/branch1/reports/unpaid_rent.html', context)
def april_unpaid_rent(request):
    if 'username' in request.session:
        context = {
            'up': pg1_regform.objects.all().filter(april_rent_flag=100, flag=1).order_by('room_no'),
            'name': request.session['username'],
            'month_name':'APRIL'
        }
        return render(request, 'branches/branch1/reports/unpaid_rent.html', context)

def may_unpaid_rent(request):
    if 'username' in request.session:
        context = {
            'up': pg1_regform.objects.all().filter(may_rent_flag=100, flag=1).order_by('room_no'),
            'name': request.session['username'],
            'month_name': 'MAY'
        }
        return render(request, 'branches/branch1/reports/unpaid_rent.html', context)
def june_unpaid_rent(request):
    if 'username' in request.session:
        context = {
            'up': pg1_regform.objects.all().filter(june_rent_flag=100, flag=1).order_by('room_no'),
            'name': request.session['username'],
            'month_name': 'JUNE'
        }
        return render(request, 'branches/branch1/reports/unpaid_rent.html', context)
def july_unpaid_rent(request):
    if 'username' in request.session:
        context = {
            'up': pg1_regform.objects.all().filter(july_rent_flag=100, flag=1).order_by('room_no'),
            'name': request.session['username'],
            'month_name': 'JULY'
        }
        return render(request, 'branches/branch1/reports/unpaid_rent.html', context)
def aug_unpaid_rent(request):
    if 'username' in request.session:
        context = {
            'up': pg1_regform.objects.all().filter(aug_rent_flag=100, flag=1).order_by('room_no'),
            'name': request.session['username'],
            'month_name': 'AUGUST'
        }
        return render(request, 'branches/branch1/reports/unpaid_rent.html', context)

def sept_unpaid_rent(request):
    if 'username' in request.session:
        context = {
            'up': pg1_regform.objects.all().filter(sept_rent_flag=100, flag=1).order_by('room_no'),
            'name': request.session['username'],
            'month_name': 'SEPT'
        }
        return render(request, 'branches/branch1/reports/unpaid_rent.html', context)
def oct_unpaid_rent(request):
    if 'username' in request.session:
        context = {
            'up': pg1_regform.objects.all().filter(oct_rent_flag=100, flag=1).order_by('room_no'),
            'name': request.session['username'],
            'month_name': 'OCTOBER'
        }
        return render(request, 'branches/branch1/reports/unpaid_rent.html', context)
def nov_unpaid_rent(request):
    if 'username' in request.session:
        context = {
            'up': pg1_regform.objects.all().filter(nov_rent_flag=100, flag=1).order_by('room_no'),
            'name': request.session['username'],
            'month_name': 'NOVEMBER'
        }
        return render(request, 'branches/branch1/reports/unpaid_rent.html', context)

def dec_unpaid_rent(request):
    if 'username' in request.session:
        context = {
            'up': pg1_regform.objects.all().filter(dec_rent_flag=100, flag=1).order_by('room_no').order_by('room_no'),
            'name': request.session['username'],
            'month_name': 'DECEMBER'
        }
        return render(request, 'branches/branch1/reports/unpaid_rent.html', context)


#*********unpaid rent end here ************

#************paid rent start here********

def paid_rent_choose_months(request):
    if 'username' in request.session:
        return render(request, 'branches/branch1/reports/paid_rent_choose_months.html')

def jan_paid_rent(request):
    if 'username' in request.session:
        l=[]
        unp=pg1_regform.objects.all().filter(jan_rent_flag=200, flag=1)
        for i in unp:
            l.append(str(i.jan_rent))
            break
        s=''.join(l)
        context = {
            'up': pg1_regform.objects.all().filter(jan_rent_flag=200, flag=1),
            'name': request.session['username'],
            'amt': s,
            'month_name': 'JAN'
        }
        return render(request, 'branches/branch1/reports/paid_rent.html', context)
def feb_paid_rent(request):
    if 'username' in request.session:
        l = []
        unp = pg1_regform.objects.all().filter(feb_rent_flag=200, flag=1)
        for i in unp:
            l.append(str(i.feb_rent))
            break
        s = ''.join(l)
        context = {
            'up': pg1_regform.objects.all().filter(feb_rent_flag=200, flag=1),
            'name': request.session['username'],'amt': s,
            'month_name': 'FEB'
        }
        return render(request, 'branches/branch1/reports/paid_rent.html', context)
def mar_paid_rent(request):
    if 'username' in request.session:
        l = []
        unp = pg1_regform.objects.all().filter(march_rent_flag=200, flag=1)
        for i in unp:
            l.append(str(i.march_rent))
            break
        s = ''.join(l)
        context = {
            'up': pg1_regform.objects.all().filter(march_rent_flag=200, flag=1),
            'name': request.session['username'],
            'amt': s,
            'month_name': 'MARCH'
        }
        return render(request, 'branches/branch1/reports/paid_rent.html', context)
def april_paid_rent(request):
    if 'username' in request.session:
        l = []
        unp = pg1_regform.objects.all().filter(april_rent_flag=200, flag=1)
        for i in unp:
            l.append(str(i.april_rent))
            break
        s = ''.join(l)
        context = {
            'up': pg1_regform.objects.all().filter(april_rent_flag=200, flag=1),
            'name': request.session['username'],
            'amt': s,
            'month_name': 'APRIL'
        }
        return render(request, 'branches/branch1/reports/paid_rent.html', context)

def may_paid_rent(request):
    if 'username' in request.session:
        l = []
        unp = pg1_regform.objects.all().filter(may_rent_flag=200, flag=1)
        for i in unp:
            l.append(str(i.may_rent))
            break
        s = ''.join(l)
        context = {
            'up': pg1_regform.objects.all().filter(may_rent_flag=200, flag=1),
            'name': request.session['username'],
            'amt': s,
            'month_name': 'MAY'
        }
        return render(request, 'branches/branch1/reports/paid_rent.html', context)
def june_paid_rent(request):
    if 'username' in request.session:
        l = []
        unp = pg1_regform.objects.all().filter(june_rent_flag=200, flag=1)
        for i in unp:
            l.append(str(i.june_rent))
            break
        s = ''.join(l)
        context = {
            'up': pg1_regform.objects.all().filter(june_rent_flag=200, flag=1),
            'name': request.session['username'],
            'amt': s,
            'month_name': 'JUNE'
        }
        return render(request, 'branches/branch1/reports/paid_rent.html', context)
def july_paid_rent(request):
    if 'username' in request.session:
        l = []
        unp = pg1_regform.objects.all().filter(july_rent_flag=200, flag=1)
        for i in unp:
            l.append(str(i.july_rent))
            break
        s = ''.join(l)
        context = {
            'up': pg1_regform.objects.all().filter(july_rent_flag=200, flag=1),
            'name': request.session['username'],
            'amt': s,
            'month_name': 'JULY'
        }
        return render(request, 'branches/branch1/reports/paid_rent.html', context)
def aug_paid_rent(request):
    if 'username' in request.session:
        l = []
        unp = pg1_regform.objects.all().filter(aug_rent_flag=200, flag=1)
        for i in unp:
            l.append(str(i.aug_rent))
            break
        s = ''.join(l)
        context = {
            'up': pg1_regform.objects.all().filter(aug_rent_flag=200, flag=1),
            'name': request.session['username'],
            'amt': s,
            'month_name': 'AUGUST'
        }
        return render(request, 'branches/branch1/reports/paid_rent.html', context)

def sept_paid_rent(request):
    if 'username' in request.session:
        l = []
        unp = pg1_regform.objects.all().filter(sept_rent_flag=200, flag=1)
        for i in unp:
            l.append(str(i.sept_rent))
            break
        s = ''.join(l)
        context = {
            'up': pg1_regform.objects.all().filter(sept_rent_flag=200, flag=1),
            'name': request.session['username'],
            'amt': s,
            'month_name': 'SEPT'
        }
        return render(request, 'branches/branch1/reports/paid_rent.html', context)
def oct_paid_rent(request):
    if 'username' in request.session:
        l = []
        unp = pg1_regform.objects.all().filter(oct_rent_flag=200, flag=1)
        for i in unp:
            l.append(str(i.oct_rent))
            break
        s = ''.join(l)
        context = {
            'up': pg1_regform.objects.all().filter(oct_rent_flag=200, flag=1),
            'name': request.session['username'],
            'amt': s,
            'month_name': 'OCTOBER'
        }
        return render(request, 'branches/branch1/reports/paid_rent.html', context)
def nov_paid_rent(request):
    if 'username' in request.session:
        l = []
        unp = pg1_regform.objects.all().filter(nov_rent_flag=200, flag=1)
        for i in unp:
            l.append(str(i.nov_rent))
            break
        s = ''.join(l)
        context = {
            'up': pg1_regform.objects.all().filter(nov_rent_flag=200, flag=1),
            'name': request.session['username'],
            'amt': s,
            'month_name': 'NOVEMBER'
        }
        return render(request, 'branches/branch1/reports/paid_rent.html', context)

def dec_paid_rent(request):
    if 'username' in request.session:
        l = []
        unp = pg1_regform.objects.all().filter(dec_rent_flag=200, flag=1)
        for i in unp:
            l.append(str(i.dec_rent))
            break
        s = ''.join(l)
        context = {
            'up': pg1_regform.objects.all().filter(dec_rent_flag=200, flag=1),
            'name': request.session['username'],
            'amt': s,
            'month_name': 'DECEMBER'
        }
        return render(request, 'branches/branch1/reports/paid_rent.html', context)


#*********paid rent end here ************


##################################
#REPORTS END HERE
################################

##################################
#PAYMENTS END HERE
################################

def choose_months(request):
    if 'username' in request.session:
        return  render(request,'branches/branch1/payments/choose_months.html')

#jan make payments start here
def jan(request):
    if 'username' in request.session:
        rn = request.POST.get('rno')
        context={
            'pd':pg1_regform.objects.all().filter(room_no=rn,flag=1,jan_rent_flag__gt=99),
            'roomno':rn,

        }
        return render(request, 'branches/branch1/payments/details_of_months/jan/jan.html',context)

def jan_manke_payments(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            jp = pg1_regform.objects.get(id=id)
            jp.jan_rent = amt
            jp.jan_rent_flag = 200
            jp.save()

            rno= pg1_regform.objects.all().filter(id=id)
            l=[]
            for i in rno:
                l.append(i.room_no)
            s=''.join(l)
            context = {
                'pd': pg1_regform.objects.all().filter(room_no=s, flag=1,jan_rent_flag__gt=99),
            }
            return render(request, 'branches/branch1/payments/details_of_months/jan/jan.html',context)
        rn = request.POST.get('rno')

        context = {
            'pd': pg1_regform.objects.all().filter(room_no=rn, flag=1,jan_rent_flag__gt=99),
            'roomno': rn,
            'sd' : pg1_regform.objects.get(id=id)
        }
        return render(request, 'branches/branch1/payments/details_of_months/jan/jan_manke_payments.html', context)

#jan make payments start here

#feb make payments start here
def feb(request):
    if 'username' in request.session:
        rn = request.POST.get('rno')
        context={
            'pd':pg1_regform.objects.all().filter(room_no=rn,flag=1,feb_rent_flag__gt=99),
            'roomno':rn,
        }
        return render(request, 'branches/branch1/payments/details_of_months/feb/feb.html',context)

def feb_manke_payments(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            jp = pg1_regform.objects.get(id=id)
            jp.feb_rent = amt
            jp.feb_rent_flag = 200
            jp.save()

            rno= pg1_regform.objects.all().filter(id=id)
            l=[]
            for i in rno:
                l.append(i.room_no)
            s=''.join(l)
            context = {
                'pd': pg1_regform.objects.all().filter(room_no=s, flag=1,feb_rent_flag__gt=99),
            }
            return render(request, 'branches/branch1/payments/details_of_months/feb/feb.html',context)
        rn = request.POST.get('rno')

        context = {
            'pd': pg1_regform.objects.all().filter(room_no=rn, flag=1),
            'roomno': rn,
            'sd' : pg1_regform.objects.get(id=id)
        }
        return render(request, 'branches/branch1/payments/details_of_months/feb/feb_manke_payments.html', context)

#feb make payments start here

#march make payments start here
def march(request):
    if 'username' in request.session:
        rn = request.POST.get('rno')
        context={
            'pd':pg1_regform.objects.all().filter(room_no=rn,flag=1,march_rent_flag__gt=99),
            'roomno':rn,
        }
        return render(request, 'branches/branch1/payments/details_of_months/march/march.html',context)

def march_manke_payments(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            jp = pg1_regform.objects.get(id=id)
            jp.march_rent = amt
            jp.march_rent_flag = 200
            jp.save()

            rno= pg1_regform.objects.all().filter(id=id)
            l=[]
            for i in rno:
                l.append(i.room_no)
            s=''.join(l)
            context = {
                'pd': pg1_regform.objects.all().filter(room_no=s, flag=1,march_rent_flag__gt=99),
            }
            return render(request, 'branches/branch1/payments/details_of_months/march/march.html',context)
        rn = request.POST.get('rno')

        context = {
            'pd': pg1_regform.objects.all().filter(room_no=rn, flag=1),
            'roomno': rn,
            'sd' : pg1_regform.objects.get(id=id)
        }
        return render(request, 'branches/branch1/payments/details_of_months/march/march_manke_payments.html', context)

#march make payments start here


#april make payments start here
def april(request):
    if 'username' in request.session:
        rn = request.POST.get('rno')
        context={
            'pd':pg1_regform.objects.all().filter(room_no=rn,flag=1,april_rent_flag__gt=99),
            'roomno':rn,
        }
        return render(request, 'branches/branch1/payments/details_of_months/april/april.html',context)

def april_make_payments(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            jp = pg1_regform.objects.get(id=id)
            jp.april_rent = amt
            jp.april_rent_flag = 200
            jp.save()

            rno= pg1_regform.objects.all().filter(id=id)
            l=[]
            for i in rno:
                l.append(i.room_no)
            s=''.join(l)
            context = {
                'pd': pg1_regform.objects.all().filter(room_no=s, flag=1,april_rent_flag__gt=99),
            }
            return render(request, 'branches/branch1/payments/details_of_months/april/april.html',context)
        rn = request.POST.get('rno')

        context = {
            'pd': pg1_regform.objects.all().filter(room_no=rn, flag=1),
            'roomno': rn,
            'sd' : pg1_regform.objects.get(id=id)
        }
        return render(request, 'branches/branch1/payments/details_of_months/april/april_make_payments.html', context)

#april make payments start here

#may make payments start here
def may(request):
    if 'username' in request.session:
        rn = request.POST.get('rno')
        context={
            'pd':pg1_regform.objects.all().filter(room_no=rn,flag=1,may_rent_flag__gt=99),
            'roomno':rn,
        }
        return render(request, 'branches/branch1/payments/details_of_months/may/may.html',context)

def may_make_payments(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            jp = pg1_regform.objects.get(id=id)
            jp.may_rent = amt
            jp.may_rent_flag = 200
            jp.save()

            rno= pg1_regform.objects.all().filter(id=id)
            l=[]
            for i in rno:
                l.append(i.room_no)
            s=''.join(l)
            context = {
                'pd': pg1_regform.objects.all().filter(room_no=s, flag=1,may_rent_flag__gt=99),
            }
            return render(request, 'branches/branch1/payments/details_of_months/may/may.html',context)
        rn = request.POST.get('rno')

        context = {
            'pd': pg1_regform.objects.all().filter(room_no=rn, flag=1),
            'roomno': rn,
            'sd' : pg1_regform.objects.get(id=id)
        }
        return render(request, 'branches/branch1/payments/details_of_months/may/may_make_payments.html', context)

#may make payments start here

#june make payments start here
def june(request):
    if 'username' in request.session:
        rn = request.POST.get('rno')
        context={
            'pd':pg1_regform.objects.all().filter(room_no=rn,flag=1,june_rent_flag__gt=99),
            'roomno':rn,
        }
        return render(request, 'branches/branch1/payments/details_of_months/june/june.html',context)

def june_make_payments(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            jp = pg1_regform.objects.get(id=id)
            jp.june_rent = amt
            jp.june_rent_flag = 200
            jp.save()

            rno= pg1_regform.objects.all().filter(id=id)
            l=[]
            for i in rno:
                l.append(i.room_no)
            s=''.join(l)
            context = {
                'pd': pg1_regform.objects.all().filter(room_no=s, flag=1,june_rent_flag__gt=99),
            }
            return render(request, 'branches/branch1/payments/details_of_months/june/june.html',context)
        rn = request.POST.get('rno')

        context = {
            'pd': pg1_regform.objects.all().filter(room_no=rn, flag=1),
            'roomno': rn,
            'sd' : pg1_regform.objects.get(id=id)
        }
        return render(request, 'branches/branch1/payments/details_of_months/june/june_make_payments.html', context)

#june make payments start here

#july make payments start here
def july(request):
    if 'username' in request.session:
        rn = request.POST.get('rno')
        context={
            'pd':pg1_regform.objects.all().filter(room_no=rn,flag=1,july_rent_flag__gt=99),
            'roomno':rn,
        }
        return render(request, 'branches/branch1/payments/details_of_months/july/july.html',context)

def july_make_payments(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            jp = pg1_regform.objects.get(id=id)
            jp.july_rent = amt
            jp.july_rent_flag = 200
            jp.save()

            rno= pg1_regform.objects.all().filter(id=id)
            l=[]
            for i in rno:
                l.append(i.room_no)
            s=''.join(l)
            context = {
                'pd': pg1_regform.objects.all().filter(room_no=s, flag=1,july_rent_flag__gt=99),
            }
            return render(request, 'branches/branch1/payments/details_of_months/july/july.html',context)
        rn = request.POST.get('rno')

        context = {
            'pd': pg1_regform.objects.all().filter(room_no=rn, flag=1),
            'roomno': rn,
            'sd' : pg1_regform.objects.get(id=id)
        }
        return render(request,'branches/branch1/payments/details_of_months/july/july_make_payments.html', context)

#july make payments start here

#agu make payments start here
def aug(request):
    if 'username' in request.session:
        rn = request.POST.get('rno')
        context={
            'pd':pg1_regform.objects.all().filter(room_no=rn,flag=1,aug_rent_flag__gt=99),
            'roomno':rn,
        }
        return render(request, 'branches/branch1/payments/details_of_months/aug/aug.html',context)

def aug_make_payments(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            jp = pg1_regform.objects.get(id=id)
            jp.aug_rent = amt
            jp.aug_rent_flag = 200
            jp.save()

            rno= pg1_regform.objects.all().filter(id=id)
            l=[]
            for i in rno:
                l.append(i.room_no)
            s=''.join(l)
            context = {
                'pd': pg1_regform.objects.all().filter(room_no=s, flag=1,aug_rent_flag__gt=99),
            }
            return render(request, 'branches/branch1/payments/details_of_months/aug/aug.html',context)
        rn = request.POST.get('rno')

        context = {
            'pd': pg1_regform.objects.all().filter(room_no=rn, flag=1),
            'roomno': rn,
            'sd' : pg1_regform.objects.get(id=id)
        }
        return render(request,'branches/branch1/payments/details_of_months/aug/aug_make_payments.html', context)

#aug make payments start here

#sept make payments start here
def sept(request):
    if 'username' in request.session:
        rn = request.POST.get('rno')
        context={
            'pd':pg1_regform.objects.all().filter(room_no=rn,flag=1,sept_rent_flag__gt=99),
            'roomno':rn,
        }
        return render(request, 'branches/branch1/payments/details_of_months/sept/sept.html',context)

def sept_make_payments(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            jp = pg1_regform.objects.get(id=id)
            jp.sept_rent = amt
            jp.sept_rent_flag = 200
            jp.save()

            rno= pg1_regform.objects.all().filter(id=id)
            l=[]
            for i in rno:
                l.append(i.room_no)
            s=''.join(l)
            context = {
                'pd': pg1_regform.objects.all().filter(room_no=s, flag=1,sept_rent_flag__gt=99),
            }
            return render(request, 'branches/branch1/payments/details_of_months/sept/sept.html',context)
        rn = request.POST.get('rno')

        context = {
            'pd': pg1_regform.objects.all().filter(room_no=rn, flag=1),
            'roomno': rn,
            'sd' : pg1_regform.objects.get(id=id)
        }
        return render(request,'branches/branch1/payments/details_of_months/sept/sept_make_payments.html', context)

#sept make payments start here

#oct make payments start here
def oct(request):
    if 'username' in request.session:
        rn = request.POST.get('rno')
        context={
            'pd':pg1_regform.objects.all().filter(room_no=rn,flag=1,oct_rent_flag__gt=99),
            'roomno':rn,
        }
        return render(request, 'branches/branch1/payments/details_of_months/oct/oct.html',context)

def oct_make_payments(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            jp = pg1_regform.objects.get(id=id)
            jp.oct_rent = amt
            jp.oct_rent_flag = 200
            jp.save()

            rno= pg1_regform.objects.all().filter(id=id)
            l=[]
            for i in rno:
                l.append(i.room_no)
            s=''.join(l)
            context = {
                'pd': pg1_regform.objects.all().filter(room_no=s, flag=1,oct_rent_flag__gt=99),
            }
            return render(request, 'branches/branch1/payments/details_of_months/oct/oct.html',context)
        rn = request.POST.get('rno')

        context = {
            'pd': pg1_regform.objects.all().filter(room_no=rn, flag=1),
            'roomno': rn,
            'sd' : pg1_regform.objects.get(id=id)
        }
        return render(request,'branches/branch1/payments/details_of_months/oct/oct_make_payments.html', context)

#oct make payments start here

#nov make payments start here
def nov(request):
    if 'username' in request.session:
        rn = request.POST.get('rno')
        context={
            'pd':pg1_regform.objects.all().filter(room_no=rn,flag=1,nov_rent_flag__gt=99),
            'roomno':rn,
        }
        return render(request, 'branches/branch1/payments/details_of_months/nov/nov.html',context)

def nov_make_payments(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            jp = pg1_regform.objects.get(id=id)
            jp.nov_rent = amt
            jp.nov_rent_flag = 200
            jp.save()

            rno= pg1_regform.objects.all().filter(id=id)
            l=[]
            for i in rno:
                l.append(i.room_no)
            s=''.join(l)
            context = {
                'pd': pg1_regform.objects.all().filter(room_no=s, flag=1,nov_rent_flag__gt=99),
            }
            return render(request, 'branches/branch1/payments/details_of_months/nov/nov.html',context)
        rn = request.POST.get('rno')

        context = {
            'pd': pg1_regform.objects.all().filter(room_no=rn, flag=1),
            'roomno': rn,
            'sd' : pg1_regform.objects.get(id=id)
        }
        return render(request,'branches/branch1/payments/details_of_months/nov/nov_make_payments.html', context)

#nov make payments start here

#dec make payments start here
def dec(request):
    if 'username' in request.session:
        rn = request.POST.get('rno')
        context={
            'pd':pg1_regform.objects.all().filter(room_no=rn,flag=1,dec_rent_flag__gt=99),
            'roomno':rn,
        }
        return render(request, 'branches/branch1/payments/details_of_months/dec/dec.html',context)

def dec_make_payments(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            jp = pg1_regform.objects.get(id=id)
            jp.dec_rent = amt
            jp.dec_rent_flag = 200
            jp.save()

            rno= pg1_regform.objects.all().filter(id=id)
            l=[]
            for i in rno:
                l.append(i.room_no)
            s=''.join(l)
            context = {
                'pd': pg1_regform.objects.all().filter(room_no=s, flag=1,dec_rent_flag__gt=99),
            }
            return render(request, 'branches/branch1/payments/details_of_months/dec/dec.html',context)
        rn = request.POST.get('rno')

        context = {
            'pd': pg1_regform.objects.all().filter(room_no=rn, flag=1),
            'roomno': rn,
            'sd' : pg1_regform.objects.get(id=id)
        }
        return render(request,'branches/branch1/payments/details_of_months/dec/dec_make_payments.html', context)

#dec make payments start here

##################################
#PAYMENTS END HERE
################################