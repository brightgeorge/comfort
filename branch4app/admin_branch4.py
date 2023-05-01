import datetime as datetime
from django.shortcuts import render
from django.contrib import messages

from branch4app.models import *
import datetime

#***branch1 rooms start here

def branch1_room_create4(request):
    if 'username' in request.session:
        context={
            'brname':'BRANCH 4 Room Creation Form',
            'brname': 'BRANCH 4'
        }
        return render(request,'branches/branch4/rooms/create_room.html',context)
    return render(request, 'index.html')

def branch1_room_create_regi4(request):
    if 'username' in request.session:
        if request.method == 'POST':
            chk_room_no = request.POST.get('roonno')
            chk_room = room_pg1.objects.all().filter(roon_no=chk_room_no).exists()
            if chk_room == True:
                context = {
                    'brname': 'BRANCH 4 Room Creation Form',
                    'br': room_pg1.objects.all().order_by('roon_no'),
                    'brname': 'BRANCH 4'
                }
                messages.info(request, 'BRANCH4 roon no already exists')
                return render(request, 'branches/branch3/rooms/view_all_rooms.html', context)
            else:
                room_no = request.POST.get('roonno')
                room_name = request.POST.get('roomname')
                share_type = request.POST.get('sharetype')
                ic=room_pg1()
                ic.roon_no = room_no
                ic.room_name = room_name
                ic.share_type = share_type
                ic.created_by = request.session['username']
                ic.save()

                context = {
                    'brname': 'BRANCH 4 Room Creation Form',
                    'br' : room_pg1.objects.all().order_by('roon_no'),
                    'brname': 'BRANCH 4'
                }
                messages.info(request, 'BRANCH4 room created sucessfully')
                return render(request,'branches/branch4/rooms/view_all_rooms.html',context)
    return render(request, 'index.html')

def view_all_room4(request):
    if 'username' in request.session:
        context = {
            'brname': 'BRANCH 4 Room Creation Form',
            'br': room_pg1.objects.all().order_by('roon_no').values(),
        }
        return render(request,'branches/branch4/rooms/view_all_rooms.html',context)
    return render(request,'index.html')

def delete_room4(request,id):
    if 'username' in request.session:
        dr = room_pg1.objects.get(id=id)
        dr.delete()
        context = {
            'brname': 'BRANCH 4 Room Creation Form',
            'br': room_pg1.objects.all().order_by('roon_no')
        }
        return render(request, 'branches/branch4/rooms/view_all_rooms.html', context)
    return render(request, 'index.html')

#***branch1 rooms end here
#bed creation start here


def pg1_bed_create4(request):
    if 'username' in request.session:
        context={
            'brname':'BRANCH THREE Room Creation Form',
            'brname': 'BRANCH THREE ',
            'roomno' : room_pg1.objects.all()
        }
        return render(request,'branches/branch4/beds/create_beds.html',context)
    return render(request, 'index.html')

def pg1_bed_create_regi4(request):
    if 'username' in request.session:
        if request.method == 'POST':

            chk_bed_no = request.POST.get('bedno')
            print('chk_bed_no', chk_bed_no)
            chk_room_no = request.POST.get('roomno')
            print('chk_room_no', chk_room_no)

            bd_code = chk_bed_no + chk_room_no
            int_bd_code = int(bd_code)
            chk_bd_code = pg1_new_beds.objects.all().filter(bed_code=int_bd_code).exists()

            if chk_bd_code == True:
                context = {
                    'brname': 'BRANCH THREE Room Creation Form',
                    'br': pg1_new_beds.objects.all().order_by('roon_no'),
                    'brname': 'BRANCH 4'
                }
                messages.info(request, 'BRANCH4 bed no already exists')
                return render(request, 'branches/branch4/beds/view_all_beds.html', context)
            else:
                room_no = request.POST.get('roomno')
                room_name = request.POST.get('roomname')
                bed_no = request.POST.get('bedno')
                room_type = request.POST.get('roomtype')

                c = 0
                for i in range(int(room_type)):
                    ic = pg1_new_beds()
                    ic.roon_no = room_no
                    ic.room_name = room_name
                    c = c + 1
                    ic.bed_no = c

                    ic.created_by = request.session['username']
                    ic.bed_code = int_bd_code
                    ic.share_type = room_type

                    ic.guest_code = 0

                    ic.jan_rent = 0
                    ic.jan_advance = 0
                    ic.jan_due_amt = 0
                    ic.jan_rent_flag = 33

                    ic.feb_rent = 0
                    ic.feb_advance = 0
                    ic.feb_due_amt = 0
                    ic.feb_rent_flag = 33

                    ic.march_rent = 0
                    ic.march_advance = 0
                    ic.march_due_amt = 0
                    ic.march_rent_flag = 33

                    ic.april_rent = 0
                    ic.april_advance = 0
                    ic.april_due_amt = 0
                    ic.april_rent_flag = 33

                    ic.may_rent = 0
                    ic.may_advance = 0
                    ic.may_due_amt = 0
                    ic.may_rent_flag = 33

                    ic.june_rent = 0
                    ic.june_advance = 0
                    ic.june_due_amt = 0
                    ic.june_rent_flag = 33

                    ic.july_rent = 0
                    ic.july_advance = 0
                    ic.july_due_amt = 0
                    ic.july_rent_flag = 33

                    ic.auguest_rent = 0
                    ic.auguest_advance = 0
                    ic.auguest_due_amt = 0
                    ic.auguest_rent_flag = 33

                    ic.sept_rent = 0
                    ic.sept_advance = 0
                    ic.sept_due_amt = 0
                    ic.sept_rent_flag = 33

                    ic.october_rent = 0
                    ic.october_advance = 0
                    ic.october_due_amt = 0
                    ic.october_rent_flag = 33

                    ic.nov_rent = 0
                    ic.nov_advance = 0
                    ic.nov_due_amt = 0
                    ic.nov_rent_flag = 33

                    ic.dec_rent = 0
                    ic.dec_advance = 0
                    ic.dec_due_amt = 0
                    ic.dec_rent_flag = 33

                    ic.flag = 1

                    ic.save()

                context = {
                    'brname': 'BRANCH THREE Room Creation Form',
                    'br': pg1_new_beds.objects.all().order_by('roon_no'),
                    'brname': 'BRANCH THREE'
                }
                messages.info(request, 'BRANCH4 room created sucessfully')
                return render(request, 'branches/branch4/beds/view_all_beds.html', context)
    return render(request, 'index.html')


def pg1_view_all_beds4(request):
    if 'username' in request.session:
        context = {
            'brname': 'BRANCH THREE Room',
            'br': pg1_new_beds.objects.all().order_by('roon_no')
        }
        return render(request,'branches/branch4/beds/view_all_beds.html',context)
    return render(request,'index.html')

def delete_bed4(request,id):
    if 'username' in request.session:
        dr = pg1_new_beds.objects.get(id=id)
        dr.delete()
        context = {
            'brname': 'BRANCH THREE Room',
            'br': pg1_new_beds.objects.all().order_by('roon_no')
        }
        return render(request, 'branches/branch4/beds/view_all_beds.html', context)
    return render(request, 'index.html')

#bed creation end here
