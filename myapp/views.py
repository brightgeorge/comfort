from django.shortcuts import render
from django.contrib import messages

from myapp.models import *
import datetime

# Create your views here.

def index(request):
    context={

    }
    return render(request,'index.html',context)

def login_request(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if login.objects.filter(username=username,password=password).exists():
            loginobj=login.objects.get(username=username,password=password)
            request.session['userid']=loginobj.id
            role=loginobj.role

            if role=='Admin':
                tusers=login.objects.all()
                tu=len(tusers)

                tstu = login.objects.all().filter(role='Student')
                ts = len(tstu)
                ll=0

                yl=[]

                yl.append(ll)

                ul=[]
                teul=login.objects.all().filter(user_flage=1)
                ltuel=len(teul)

                tdul = login.objects.all().filter(user_flage=0)
                ltudl = len(tdul)

                ul.append(ltuel)
                ul.append(ltudl)


                request.session['username'] = username
                us = request.session['username']

                context={
                   'user':loginobj,
                    'tus':tu,
                    'tos': ts,

                    'y':yl,
                    'yy':ul,
                    'active_user':ltuel,
                    'total_disableusers':ltudl,
                }
                return render(request,'admindashboard/index.html',context)
            if role=='Student':
                print(datetime.datetime.now())
                x=datetime.datetime.now()
                print(x.strftime("%x"))
                print(datetime.date.today())
                request.session['username'] = username
                us = request.session['username']

                tp = task.objects.all().filter(task_type='plus', task_status=1,task_assigned_to=us)
                tpl = len(tp)
                tm = task.objects.all().filter(task_type='minus', task_status=1,task_assigned_to=us)
                tml = len(tm)
                tt = task.objects.all().filter(task_type='times', task_status=1,task_assigned_to=us)
                ttl = len(tt)
                tdb = task.objects.all().filter(task_type='divided_by', task_status=1,task_assigned_to=us)
                tdbl = len(tdb)
                ll = 0

                yl = []
                yl.append(tpl)
                yl.append(tml)
                yl.append(ttl)
                yl.append(tdbl)
                yl.append(ll)
                context={
                    'user': loginobj,
                    'y':yl
                }

                return render(request, 'studentsdashboard/students_dashboard.html', context)
            if role=='Branch1':
                request.session['username'] = username
                us = request.session['username']
                context = {
                    'user': loginobj,
                    'name' : us
                }
                return render(request,'branches/branch1/branch_index.html', context)
            if role=='Branch2':
                request.session['username'] = username
                us = request.session['username']
                context = {
                    'user': loginobj,
                    'name' : us
                }
                return render(request,'branches/branch2/branch_index.html', context)
            if role=='Branch3':
                request.session['username'] = username
                us = request.session['username']
                context = {
                    'user': loginobj,
                    'name' : us
                }
                return render(request,'branches/branch3/branch_index.html', context)
            if role=='staff':
                return render(request, 'kalyan.html', context={'user': loginobj})
            else:
                return render(request,'index.html',context={'user':loginobj})
        else:
            return render(request,'index.html',context={'msg':'User Name or Password Incorrect'})
    else:
        return render(request,'index.html')

def admin_dashboard(request):
    tusers = login.objects.all()
    tu = len(tusers)

    tstu = login.objects.all().filter(role='Student')
    ts = len(tstu)

    ul = []
    teul = login.objects.all().filter(user_flage=1)
    ltuel = len(teul)

    tdul = login.objects.all().filter(user_flage=0)
    ltudl = len(tdul)

    ul.append(ltuel)
    ul.append(ltudl)

    context = {
        'tus': tu,
        'tos': ts,
        'yy': ul,
        'active_user': ltuel,
        'total_disableusers': ltudl,
    }
    return render (request,'admindashboard/index.html',context)

#************USER SECTION STARTED HERE ***************

def view_all_users(request):
    if 'username' in request.session:
        vu=login.objects.filter(user_flage=1)
        context={
            'users':vu
        }
        return render(request,'admindashboard/users/view_all_users.html',context)
    return render(request,'index.html')

def create_user(request):
    if 'username' in request.session:
        return render(request,'admindashboard/users/user_creation.html')
    return render(request, 'index.html')

def user_regi(request):
    itname = request.POST.get('username')
    chkitemname = login.objects.filter(username=itname).exists()
    print('this is m y test uname',chkitemname)
    empcod= request.POST.get('code')
    chkemcod= login.objects.filter(emp_id=empcod).exists()
    print('this is m y test user code', chkemcod)
    if chkitemname == True or chkemcod == True:
        if chkitemname == True and chkemcod == True:
            messages.info(request, 'User name and Employee Code both are already exists!. please try another one')
        if chkitemname == False and chkemcod == True:
            messages.info(request, 'Employee Code already exists!. please try another one')
        if chkitemname == True and chkemcod == False:
            messages.info(request, 'User name already exists!. please try another one')
        return render(request, 'admindashboard/users/user_creation.html', )
    else:
        if request.method == 'POST':
            ucode=request.POST.get('code')
            empname = request.POST.get('name')
            uname = request.POST.get('username')
            upass = request.POST.get('password')
            urole = request.POST.get('role')
            empbranch = request.POST.get('branch')

            udes = request.POST.get('description')
            fl = request.POST.get('eanable_disable')
            chk = 11
            if fl == None:
                chk = 0
            else:
                chk = 1
            uc=login()
            uc.emp_id = ucode
            uc.emp_name = empname
            uc.username = uname
            uc.password = upass
            uc.role = urole
            uc.emp_branch=empbranch

            uc.emp_description=udes
            uc.user_flage = chk
            uc.save()

    messages.info(request,'user created sucessfully')
    context = {
        'users': login.objects.filter(user_flage=1),
    }
    return render(request,'admindashboard/users/view_all_users.html',context)

def delete_user(request,id):
    if 'username' in request.session:
        de=login.objects.get(id=id)
        de.delete()
        messages.info(request, 'user deleted sucessfully')
        vu = login.objects.all()
        context = {
            'users': login.objects.filter(user_flage=1),
            'users': vu
        }
        return render(request, 'admindashboard/users/view_all_users.html', context)
    return render(request, 'index.html')

def user_update(request,id):
    if request.method == 'POST':
        ucode = request.POST.get('code')
        empname = request.POST.get('name')
        uname = request.POST.get('username')
        upass = request.POST.get('password')
        urole = request.POST.get('role')

        udes = request.POST.get('description')
        fl = request.POST.get('eanable_disable')
        chk = 11
        if fl == None:
            chk = 0
        else:
            chk = 1
        uc = login.objects.get(id=id)
        uc.emp_code = ucode
        uc.emp_name = empname
        uc.username = uname
        uc.password = upass
        uc.role = urole

        uc.emp_description = udes
        uc.user_flage = chk
        uc.save()
        messages.info(request, 'user updated sucessfully')
        return view_all_users(request)

    context = {
        'users': login.objects.filter(user_flage=1),
        'sd': login.objects.get(id=id),
    }
    return render(request,'admindashboard/users/update_user.html',context)

#************USER SECTION END HERE ***************

def registration_form_create(request):
    return render(request,'admindashboard/registrations/reregistration_form_create.html')

def registration_form_regi(request):
    print(request)
    room_no = request.POST.get()
    name = request.POST.get()
    room_type = request.POST.get()
    monthly_rent = request.POST.get()
    advance = request.POST.get()
    age = request.POST.get()
    dom = request.POST.get()
    edu_qulification = request.POST.get()
    mail_id = request.POST.get()
    self_mob_no = request.POST.get()
    id_proof_type = request.POST.get()
    id_proof_no = request.POST.get()

    prsnts_emp_name = request.POST.get()
    prsnts_contact_no = emg_contact_no = request.POST.get()
    prsnts_emp_address = emg_contact_no = request.POST.get()

    father_name = emg_contact_no = request.POST.get()
    father_mob_no = request.POST.get()
    emg_contact_no = request.POST.get()
    relationship = request.POST.get()

    permanent_address = request.POST.get()
    join_date = datetime.datetime.now()

    return render(request, 'admindashboard/registrations/reregistration_form_create.html')

def update_registration_form(request):
    return render(request, 'admindashboard/registrations/update_registration_form.html')

#****************************************************************************************************
#ROOMS ONE START HERE
#***********************************

def select_branch(request):
    if 'username' in request.session:
        return render(request,'admindashboard/rooms/select_branch.html')
    return render(request, 'index.html')

#***branch1 rooms start here

def branch1_room_create(request):
    if 'username' in request.session:
        context={
            'brname':'BRANCH 1 Room Creation Form',
            'brname': 'BRANCH 1'
        }
        return render(request,'admindashboard/rooms/create_room.html',context)
    return render(request, 'index.html')
def branch1_room_create_regi(request):
    if 'username' in request.session:
        if request.method == 'POST':
            chk_room_no = request.POST.get('roonno')
            chk_room = pg1_rooom.objects.all().filter(roon_no=chk_room_no).exists()
            if chk_room == True:
                context = {
                    'brname': 'BRANCH 1 Room Creation Form',
                    'br': pg1_rooom.objects.all().order_by('roon_no'),
                    'brname': 'BRANCH 1'
                }
                messages.info(request, 'roon no already exists')
                return render(request, 'admindashboard/rooms/view_all_rooms.html', context)
            else:
                room_no = request.POST.get('roonno')
                ic=pg1_rooom()
                ic.roon_no = room_no
                ic.created_by = request.session['username']
                ic.save()

                context = {
                    'brname': 'BRANCH 1 Room Creation Form',
                    'br' : pg1_rooom.objects.all().order_by('roon_no'),
                    'brname': 'BRANCH 1'
                }
                messages.info(request, 'room created sucessfully')
                return render(request,'admindashboard/rooms/view_all_rooms.html',context)
    return render(request, 'index.html')

def view_all_rooms(request):
    if 'username' in request.session:
        context = {
            'brname': 'BRANCH 1 Room Creation Form',
            'br': pg1_rooom.objects.all().order_by('roon_no')
        }
        return render(request,'admindashboard/rooms/view_all_rooms.html',context)
    return render(request,'index.html')

def delete_room(request,id):
    if 'username' in request.session:
        dr = pg1_rooom.objects.get(id=id)
        dr.delete()
        context = {
            'brname': 'BRANCH 1 Room Creation Form',
            'br': pg1_rooom.objects.all().order_by('roon_no')
        }
        return render(request, 'admindashboard/rooms/view_all_rooms.html', context)
    return render(request, 'index.html')

#***branch1 rooms end here

#***branch2 rooms start here

def branch2_room_create(request):
    if 'username' in request.session:
        context={
            'brname':'BRANCH 2 Room Creation Form',
            'brname': 'BRANCH 2'
        }
        return render(request,'admindashboard/rooms/create_room.html',context)
    return render(request, 'index.html')
def branch2_room_create_regi(request):
    if 'username' in request.session:
        if request.method == 'POST':
            chk_room_no = request.POST.get('roonno')
            chk_room = pg2_rooom.objects.all().filter(roon_no=chk_room_no).exists()
            if chk_room == True:
                context = {
                    'brname': 'BRANCH 2 Room Creation Form',
                    'br': pg2_rooom.objects.all().order_by('roon_no'),
                    'brname': 'BRANCH 2'
                }
                messages.info(request, 'roon no already exists')
                return render(request, 'admindashboard/rooms/view_all_rooms.html', context)
            else:
                room_no = request.POST.get('roonno')
                ic=pg2_rooom()
                ic.roon_no = room_no
                ic.created_by = request.session['username']
                ic.save()

                context = {
                    'brname': 'BRANCH 2 Room Creation Form',
                    'br' : pg1_rooom.objects.all().order_by('roon_no'),
                    'brname': 'BRANCH 2'
                }
                messages.info(request, 'room created sucessfully')
                return render(request,'admindashboard/rooms/view_all_rooms.html',context)
    return render(request, 'index.html')

def view_all_rooms(request):
    if 'username' in request.session:
        context = {
            'brname': 'BRANCH 2 Room Creation Form',
            'br': pg2_rooom.objects.all().order_by('roon_no')
        }
        return render(request,'admindashboard/rooms/view_all_rooms.html',context)
    return render(request,'index.html')

def delete_room(request,id):
    if 'username' in request.session:
        dr = pg2_rooom.objects.get(id=id)
        dr.delete()
        context = {
            'brname': 'BRANCH 2 Room Creation Form',
            'br': pg2_rooom.objects.all().order_by('roon_no')
        }
        return render(request, 'admindashboard/rooms/view_all_rooms.html', context)
    return render(request, 'index.html')

#***branch2 rooms end here


#****************************************************************************************************
#ROOMS ONE END HERE
#***********************************
#****************************************************************************************************
#head office Reports start HERE
#***********************************

#**unpaid rent start here

def select_month_all_branch_unpaid_rent(request):
    if 'username' in request.session:
        return render(request,'admindashboard/reports/unpaid_rent/select_month_all_branch_unpaid_rent.html')
    return render(request, 'index.html')

def all_branch_unpaid_rent(request):
    return render(request,'admindashboard/reports/unpaid_rent/all_branch_unpaid_rent.html')

def all_jan_unpaid_rent(request):
    if 'username' in request.session:
        context = {
            'up': pg1_regform.objects.all().filter(jan_rent_flag=100, flag=1).order_by('room_no'),
            'name': request.session['username'],
            'month_name': 'JANUARY'
        }
        return render(request,'admindashboard/reports/unpaid_rent/all_branch_unpaid_rent.html',context)

def all_feb_unpaid_rent(request):
    if 'username' in request.session:
        context = {
            'up': pg1_regform.objects.all().filter(feb_rent_flag=100, flag=1).order_by('room_no'),
            'name': request.session['username'],
            'month_name': 'FEB'
        }
        return render(request,'admindashboard/reports/unpaid_rent/all_branch_unpaid_rent.html',context)
def all_mar_unpaid_rent(request):
    if 'username' in request.session:
        context = {
            'up': pg1_regform.objects.all().filter(march_rent_flag=100, flag=1).order_by('room_no'),
            'name': request.session['username'],
            'month_name': 'MARCH'
        }
        return render(request,'admindashboard/reports/unpaid_rent/all_branch_unpaid_rent.html',context)
def all_april_unpaid_rent(request):
    if 'username' in request.session:
        context = {
            'up': pg1_regform.objects.all().filter(april_rent_flag=100, flag=1).order_by('room_no'),
            'name': request.session['username'],
            'month_name':'APRIL'
        }
        return render(request,'admindashboard/reports/unpaid_rent/all_branch_unpaid_rent.html',context)

def all_may_unpaid_rent(request):
    if 'username' in request.session:
        context = {
            'up': pg1_regform.objects.all().filter(may_rent_flag=100, flag=1).order_by('room_no'),
            'name': request.session['username'],
            'month_name': 'MAY'
        }
        return render(request,'admindashboard/reports/unpaid_rent/all_branch_unpaid_rent.html',context)
def all_june_unpaid_rent(request):
    if 'username' in request.session:
        context = {
            'up': pg1_regform.objects.all().filter(june_rent_flag=100, flag=1).order_by('room_no'),
            'name': request.session['username'],
            'month_name': 'JUNE'
        }
        return render(request,'admindashboard/reports/unpaid_rent/all_branch_unpaid_rent.html',context)
def all_july_unpaid_rent(request):
    if 'username' in request.session:
        context = {
            'up': pg1_regform.objects.all().filter(july_rent_flag=100, flag=1).order_by('room_no'),
            'name': request.session['username'],
            'month_name': 'JULY'
        }
        return render(request,'admindashboard/reports/unpaid_rent/all_branch_unpaid_rent.html',context)
def all_aug_unpaid_rent(request):
    if 'username' in request.session:
        context = {
            'up': pg1_regform.objects.all().filter(aug_rent_flag=100, flag=1).order_by('room_no'),
            'name': request.session['username'],
            'month_name': 'AUGUST'
        }
        return render(request,'admindashboard/reports/unpaid_rent/all_branch_unpaid_rent.html',context)

def all_sept_unpaid_rent(request):
    if 'username' in request.session:
        context = {
            'up': pg1_regform.objects.all().filter(sept_rent_flag=100, flag=1).order_by('room_no'),
            'name': request.session['username'],
            'month_name': 'SEPT'
        }
        return render(request,'admindashboard/reports/unpaid_rent/all_branch_unpaid_rent.html',context)
def all_oct_unpaid_rent(request):
    if 'username' in request.session:
        context = {
            'up': pg1_regform.objects.all().filter(oct_rent_flag=100, flag=1).order_by('room_no'),
            'name': request.session['username'],
            'month_name': 'OCTOBER'
        }
        return render(request,'admindashboard/reports/unpaid_rent/all_branch_unpaid_rent.html',context)
def all_nov_unpaid_rent(request):
    if 'username' in request.session:
        context = {
            'up': pg1_regform.objects.all().filter(nov_rent_flag=100, flag=1).order_by('room_no'),
            'name': request.session['username'],
            'month_name': 'NOVEMBER'
        }
        return render(request,'admindashboard/reports/unpaid_rent/all_branch_unpaid_rent.html',context)

def all_dec_unpaid_rent(request):
    if 'username' in request.session:
        context = {
            'up': pg1_regform.objects.all().filter(dec_rent_flag=100, flag=1).order_by('room_no').order_by('room_no'),
            'name': request.session['username'],
            'month_name': 'DECEMBER'
        }
        return render(request,'admindashboard/reports/unpaid_rent/all_branch_unpaid_rent.html',context)

#**unpaid rent end here
#************paid rent start here********

def select_month_all_branch_paid_rent(request):
    if 'username' in request.session:
        #return render(request, 'branches/branch1/reports/paid_rent_choose_months.html')
        return render(request, 'admindashboard/reports/paid_rent/select_month_all_branch_paid_rent.html')

def all_jan_paid_rent(request):
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
        return render(request, 'admindashboard/reports/paid_rent/all_branch_paid_rent.html',context)
def all_feb_paid_rent(request):
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
        return render(request, 'admindashboard/reports/paid_rent/all_branch_paid_rent.html',context)
def all_mar_paid_rent(request):
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
        return render(request, 'admindashboard/reports/paid_rent/all_branch_paid_rent.html',context)
def all_april_paid_rent(request):
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
        return render(request, 'admindashboard/reports/paid_rent/all_branch_paid_rent.html',context)

def all_may_paid_rent(request):
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
        return render(request, 'admindashboard/reports/paid_rent/all_branch_paid_rent.html',context)
def all_june_paid_rent(request):
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
        return render(request, 'admindashboard/reports/paid_rent/all_branch_paid_rent.html',context)
def all_july_paid_rent(request):
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
        return render(request, 'admindashboard/reports/paid_rent/all_branch_paid_rent.html',context)
def all_aug_paid_rent(request):
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
        return render(request, 'admindashboard/reports/paid_rent/all_branch_paid_rent.html',context)

def all_sept_paid_rent(request):
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
        return render(request, 'admindashboard/reports/paid_rent/all_branch_paid_rent.html',context)
def all_oct_paid_rent(request):
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
        return render(request, 'admindashboard/reports/paid_rent/all_branch_paid_rent.html',context)
def all_nov_paid_rent(request):
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
        return render(request, 'admindashboard/reports/paid_rent/all_branch_paid_rent.html',context)

def all_dec_paid_rent(request):
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
        return render(request, 'admindashboard/reports/paid_rent/all_branch_paid_rent.html',context)


#*********paid rent end here ************

#****************************************************************************************************
#head office Reports ONE END HERE
#***********************************
def logout(request):
    if 'username' in request.session:
        request.session.flush()
    return render(request,'index.html')
