#admin_dahsboard_calculations
#admin_dashboard_reports
#total_vaccant_share_choose_branches
from django.shortcuts import render
from django.contrib import messages

from myapp.models import *
import branch2app
import branch3app
import branch4app
import branch5app

def total_guest():
    tg=[]
    total_guest_br1 = pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br1))
    total_guest_br2= branch2app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br2))
    total_guest_br3 = branch3app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br3))
    total_guest_br4 = branch4app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br4))
    total_guest_br5 = branch5app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br5))
    return sum(tg)

def total_vaccant_share1():
    tsv = []
    total_guest_br1 = pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch2app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch3app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch4app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch5app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return sum(tsv)

def total_vaccant_share2():
    tsv = []
    total_guest_br1 = pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch2app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch3app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch4app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch5app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return sum(tsv)

def total_vaccant_share3():
    tsv = []
    total_guest_br1 = pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch2app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch3app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch4app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch5app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return sum(tsv)

def total_vaccant_share4():
    tsv = []
    total_guest_br1 = pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch2app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch3app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch4app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch5app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return sum(tsv)

def total_vaccant_share5():
    tsv = []
    total_guest_br1 = pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch2app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch3app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch4app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch5app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return sum(tsv)

def total_vaccant_share6():
    tsv = []
    total_guest_br1 = pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch2app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch3app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch4app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch5app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return sum(tsv)

def total_vaccant_room():
    tsv = []
    total_vaccant_room_br1 = total_vaccant_share1()
    tsv.append(total_vaccant_room_br1)
    total_vaccant_room_br2 = total_vaccant_share2()
    tsv.append(total_vaccant_room_br2)
    total_vaccant_room_br3 = total_vaccant_share3()
    tsv.append(total_vaccant_room_br3)
    total_vaccant_room_br4 = total_vaccant_share4()
    tsv.append(total_vaccant_room_br4)
    total_vaccant_room_br5 = total_vaccant_share5()
    tsv.append(total_vaccant_room_br5)
    total_vaccant_room_br6 = total_vaccant_share6()
    tsv.append(total_vaccant_room_br6)
    return sum(tsv)


def total_vaccant_share_branch1():
    tsv = []
    total_guest_br1 = pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br5 = pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return tsv

def total_vaccant_share_branch2():
    tsv = []
    total_guest_br1 = branch2app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch2app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch2app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch2app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch2app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br5 = branch2app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return tsv

def total_vaccant_share_branch3():
    tsv = []
    total_guest_br1 = branch3app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch3app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch3app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch3app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch3app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br5 = branch3app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return tsv

def total_vaccant_share_branch4():
    tsv = []
    total_guest_br1 = branch4app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch4app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch4app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch4app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch4app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br5 = branch4app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return tsv

def total_vaccant_share_branch5():
    tsv = []
    total_guest_br1 = branch5app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch5app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch5app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch5app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch5app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br5 = branch5app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return tsv

def total_vaccant_share_choose_branches(request):
    context = {
        'br1' : total_vaccant_share_branch1(),
        'br2': total_vaccant_share_branch2(),
        'br3': total_vaccant_share_branch3(),
        'br4': total_vaccant_share_branch4(),
        'br5': total_vaccant_share_branch5(),

    }
    return render(request,'admindashboard/admin_dashboard_reports/total_vaccant_share_choose_branches.html',context)

def details_branch1(request):
    context = {
        'tc': pg1_new_beds.objects.all().filter(flag=2),
        'vr': pg1_new_beds.objects.all().exclude(flag=2).order_by('roon_no')
    }
    return render(request, 'admindashboard/admin_dashboard_reports/branch_details/details_branch.html', context)

def details_branch2(request):
    context = {
        'tc' : branch2app.models.pg1_new_beds.objects.all().filter(flag=2),
        'vr': branch2app.models.pg1_new_beds.objects.all().exclude(flag=2).order_by('roon_no'),
    }
    return render(request,'admindashboard/admin_dashboard_reports/branch_details/details_branch.html',context)

def details_branch3(request):
    context = {
        'tc': branch3app.models.pg1_new_beds.objects.all().filter(flag=2),
        'vr': branch3app.models.pg1_new_beds.objects.all().exclude(flag=2).order_by('roon_no')
    }
    return render(request,'admindashboard/admin_dashboard_reports/branch_details/details_branch.html',context)

def details_branch4(request):
    context = {
        'tc': branch4app.models.pg1_new_beds.objects.all().filter(flag=2),
        'vr': branch4app.models.pg1_new_beds.objects.all().exclude(flag=2).order_by('roon_no')
    }
    return render(request,'admindashboard/admin_dashboard_reports/branch_details/details_branch.html',context)

def details_branch5(request):
    context = {
        'tc': branch5app.models.pg1_new_beds.objects.all().filter(flag=2),
        'vr': branch5app.models.pg1_new_beds.objects.all().exclude(flag=2).order_by('roon_no')
    }
    return render(request,'admindashboard/admin_dashboard_reports/branch_details/details_branch.html',context)


