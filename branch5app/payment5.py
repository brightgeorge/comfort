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

def choose_user5(request):
    if 'username' in request.session:
        rn = request.POST.get('rno')
        context={
            'pd':pg1_new_guest.objects.all().filter(roon_no=rn,flag=2),
            'roomno':rn,
            'room': room_pg1.objects.all(),
        }
        return render(request, 'branches/branch5/payments/choose_user.html',context)
def payment_user_details5(request, id):
    context = {
        'pd': pg1_new_guest.objects.all().filter(id=id,flag=2),
    }
    return render(request, 'branches/branch5/payments/payment_user_details.html', context)

def payment_user_details55(request):
    if 'username' in request.session:
        rn = request.POST.get('rno')
        context={
            'pd':pg1_new_guest.objects.all().filter(roon_no=rn,flag=2),
            'roomno':rn,
            'room': room_pg1.objects.all(),
        }
        return render(request, 'branches/branch5/payments/payment_user_details.html',context)


def payment_user_detailssss5(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
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
            #jp.july_rent_rec_date = datetime.date.today()
            jp.july_rent_rec_date = date
            jp.july_rent_flag = 200
            jp.save()


            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            #jp = pg1_new_beds.objects.get(guest_code=l[0])
            import branch5app
            jp = branch5app.models.pg1_new_beds.objects.get(guest_code=l[0])
            jp.july_rent = dis_amt
            jp.remark = remark
            jp.july_due_amt = due_amt
            jp.auguest_due_amt = due_amt
            jp.july_dis_amt = dis_amt
            #jp.july_rent_rec_date = datetime.date.today()
            jp.july_rent_rec_date = date
            jp.july_rent_flag = 200
            jp.save()


            rno= pg1_new_guest.objects.all().filter(id=id)
            l=[]
            for i in rno:
                l.append(str(i.roon_no))
            s=''.join(l)

            context = {
                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2,july_rent_flag__gt=99),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all(),
            }
            return render(request, 'branches/branch5/payments/details_of_months/july/july.html',context)
        rn = request.POST.get('rno')

        rno = pg1_new_guest.objects.all().filter(id=id)
        l = []
        for i in rno:
            l.append(str(i.guest_code))
        gc = ''.join(l)
        print('lll', l)

        import branch5app
        total_discout_amt = []
        pg1_new_beds = branch5app.models.pg1_new_guest.objects.all().filter(flag=2, guest_code=l[0])
        for i in pg1_new_beds:
            total_discout_amt.append(int(i.july_dis_amt))

        context = {
            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd' : pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all(),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
            'discount_amt': total_discout_amt[0],
        }
        return render(request,'branches/branch5/payments/details_of_months/july/july_make_payments.html', context)


