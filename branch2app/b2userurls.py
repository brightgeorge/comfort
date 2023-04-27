from django.contrib import admin
from django.urls import path, include

from django.urls import path
from . import views
from . import admin_branch2

from . import branch1
from . import branch2


d='test'

import myapp.userurls
import branch2app.b2userurls
name='_branch2'
urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('pysql/', branch1.pysql, name='pysql' + d),

    #path('viewall_vacate_guest/',branch1.viewall_vacate_guest,name='viewall_vacate_guest'+name),
    #path('view_all_users/', views.view_all_users, name='view_all_users'),
    #path('view_all_room/', admin_branch2.view_all_room, name='view_all_room'),
    path('branch1_dashboard2/', branch2.branch1_dashboard2, name='branch1_dashboard'+name),

#**room creation start here
    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi2/',admin_branch2.branch1_room_create_regi2,name='branch1_room_create_regi2'),
    path('view_all_room2/',admin_branch2.view_all_room2,name='view_all_room2'),
    path('delete_room2/<id>',admin_branch2.delete_room2,name='delete_room2'),

    path('branch1_room_create2/',admin_branch2.branch1_room_create2,name='branch1_room_create2'),

#**room creation end here

#bed creation start here

    path('pg1_bed_create_regi2/', admin_branch2.pg1_bed_create_regi2, name='pg1_bed_create_regi2'),
    path('pg1_view_all_beds2/', admin_branch2.pg1_view_all_beds2, name='pg1_view_all_beds2'),
    path('delete_bed2/<id>', admin_branch2.delete_bed2, name='delete_bed2'),

    path('pg1_bed_create2/', admin_branch2.pg1_bed_create2, name='pg1_bed_create2'),

#bed creation end here

#guest
    path('br1_admit_guest2/<id>',branch2.br1_admit_guest2,name='br1_admit_guest2'),
    path('view_all_new_guest2/',branch2.view_all_new_guest2,name='view_all_new_guest2'),
    path('update_br1_admit_guest2/<id>',branch2.update_br1_admit_guest2,name='update_br1_admit_guest2'),
    path('vacate_br1_guest2/<id>',branch2.vacate_br1_guest2,name='vacate_br1_guest2'),
    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),
#guest end here



##################################
#PAYMENTS START HERE
################################

    path('choose_months2/',branch2.choose_months2,name='choose_months2'),

    path('jan2/',branch2.jan2,name='jan2'),
    path('jan_manke_payments2/<id>',branch2.jan_manke_payments2,name='jan_manke_payments2'),

    path('feb2/',branch2.feb2,name='feb2'),
    path('feb_manke_payments2/<id>',branch2.feb_manke_payments2,name='feb_manke_payments2'),

    path('march2/',branch2.march2,name='march2'),
    path('march_manke_payments2/<id>',branch2.march_manke_payments2,name='march_manke_payments2'),

    path('april2/',branch2.april2,name='april2'),
    path('april_make_payments2/<id>',branch2.april_make_payments2,name='april_make_payments2'),

    path('may2/',branch2.may2,name='may2'),
    path('may_make_payments2/<id>',branch2.may_make_payments2,name='may_make_payments2'),

    path('june2/',branch2.june2,name='june2'),
    path('june_make_payments2/<id>',branch2.june_make_payments2,name='june_make_payments2'),

    path('july2/',branch2.july2,name='july2'),
    path('july_make_payments2/<id>',branch2.july_make_payments2,name='july_make_payments2'),

    path('aug2/',branch2.aug2,name='aug2'),
    path('aug_make_payments2/<id>',branch2.aug_make_payments2,name='aug_make_payments2'),

    path('sept2/',branch2.sept2,name='sept2'),
    path('sept_make_payments2/<id>',branch2.sept_make_payments2,name='sept_make_payments2'),

    path('oct2/',branch2.oct2,name='oct2'),
    path('oct_make_payments2/<id>',branch2.oct_make_payments2,name='oct_make_payments2'),

    path('nov2/',branch2.nov2,name='nov2'),
    path('nov_make_payments2/<id>',branch2.nov_make_payments2,name='nov_make_payments2'),

    path('dec2/',branch2.dec2,name='dec2'),
    path('dec_make_payments2/<id>',branch2.dec_make_payments2,name='dec_make_payments2'),

##################################
#PAYMENTS END HERE
################################


##################################
#ADVANCE START HERE
################################

    path('choose_months_advance2/',branch2.choose_months_advance2,name='choose_months_advance'+name),

    path('jan_advance2/', branch2.jan_advance2, name='jan_advance'+name),
    path('jan_make_payments_advance2/<id>', branch2.jan_make_payments_advance2,name='jan_make_payments_advance'+name),
    path('feb_advance2/', branch2.feb_advance2, name='feb_advance'+name),
    path('feb_make_payments_advance2/<id>', branch2.feb_make_payments_advance2,name='feb_make_payments_advance' + name),
    path('march_advane2/', branch2.march_advance2, name='march_advance'+name),
    path('march_make_payments_advance2/<id>', branch2.march_make_payments_advance2,name='march_make_payments_advance'+name),
    path('april_advance2/', branch2.april_advane2, name='april_advane'+name),
    path('april_make_payments_advance2/<id>', branch2.april_make_payments_advance2, name='april_make_payments_advance'+name),

    path('may_advane2/',branch2.may_advane2,name='may_advane'+name),
    path('may_make_payments_advance2/<id>', branch2.may_make_payments_advance2, name='may_make_payments_advance'+name),
    path('june_advane2/',branch2.june_advane2,name='june_advane'+name),
    path('june_make_payments_advance2/<id>', branch2.june_make_payments_advance2, name='june_make_payments_advance'+name),
    path('july_advane2/',branch2.july_advance2,name='july_advane'+name),
    path('july_make_payments_advance2/<id>', branch2.july_make_payments_advance2, name='july_make_payments_advance'+name),
    path('auguest_advance2/', branch2.auguest_advance2, name='auguest_advance'+name),
    path('auguest_make_payments_advance2/<id>', branch2.auguest_make_payments_advance2, name='auguest_make_payments_advance'+name),

    path('sept_advance2/', branch2.sept_advance2, name='sept_advance'+name),
    path('sept_make_payments_advance2/<id>', branch2.sept_make_payments_advance2,name='sept_make_payments_advance'+name),
    path('october_advance2/', branch2.october_advance2, name='october_advance'+name),
    path('october_make_payments_advance2/<id>', branch2.october_make_payments_advance2, name='october_make_payments_advance'+name),
    path('nov_advance2/', branch2.nov_advance2, name='nov_advance'+name),
    path('nov_make_payments_advance2/<id>', branch2.nov_make_payments_advance2,name='nov_make_payments_advance'+name),
    path('dec_advance2/', branch2.dec_advance2, name='dec_advance'+name),
    path('dec_make_payments_advance2/<id>', branch2.dec_make_payments_advance2, name='dec_make_payments_advance'+name),

    ##################################
#ADVANCE END HERE
################################


#*********reports start here

#unpaid rent start here
    path('unpaid_rent_choose_months2/',branch2.unpaid_rent_choose_months2,name='unpaid_rent_choose_months2'),

    path('jan_unpaid_rent2/', branch2.jan_unpaid_rent2, name='jan_unpaid_rent2'),
    path('feb_unpaid_rent2/', branch2.feb_unpaid_rent2, name='feb_unpaid_rent2'),
    path('mar_unpaid_rent2/', branch2.mar_unpaid_rent2, name='mar_unpaid_rent2'),
    path('april_unpaid_rent2/', branch2.april_unpaid_rent2, name='april_unpaid_rent2'),

    path('may_unpaid_rent2/', branch2.may_unpaid_rent2, name='may_unpaid_rent2'),
    path('june_unpaid_rent2/', branch2.june_unpaid_rent2, name='june_unpaid_rent2'),
    path('july_unpaid_rent2/', branch2.july_unpaid_rent2, name='july_unpaid_rent2'),
    path('aug_unpaid_rent2/', branch2.aug_unpaid_rent2, name='aug_unpaid_rent2'),

    path('sept_unpaid_rent2/', branch2.sept_unpaid_rent2, name='sept_unpaid_rent2'),
    path('oct_unpaid_rent2/', branch2.oct_unpaid_rent2, name='oct_unpaid_rent2'),
    path('nov_unpaid_rent2/', branch2.nov_unpaid_rent2, name='nov_unpaid_rent2'),
    path('dec_unpaid_rent2/', branch2.dec_unpaid_rent2, name='dec_unpaid_rent2'),

    path('details_of_unpaid_guests2/<id>',branch2.details_of_unpaid_guests2,name='details_of_unpaid_guests2'),

#unpaid rent end here

#paid rent start here
    path('paid_rent_choose_months2/',branch2.paid_rent_choose_months2,name='paid_rent_choose_months2'),

    path('jan_paid_rent2/', branch2.jan_paid_rent2, name='jan_paid_rent2'),
    path('feb_paid_rent2/', branch2.feb_paid_rent2, name='feb_paid_rent2'),
    path('mar_paid_rent2/', branch2.mar_paid_rent2, name='mar_paid_rent2'),
    path('april_paid_rent2/', branch2.april_paid_rent2, name='april_paid_rent2'),

    path('may_paid_rent2/', branch2.may_paid_rent2, name='may_paid_rent2'),
    path('june_paid_rent2/', branch2.june_paid_rent2, name='june_paid_rent2'),
    path('july_paid_rent2/', branch2.july_paid_rent2, name='july_paid_rent2'),
    path('aug_paid_rent2/', branch2.aug_paid_rent2, name='aug_paid_rent2'),

    path('sept_paid_rent2/', branch2.sept_paid_rent2, name='sept_paid_rent2'),
    path('oct_paid_rent2/', branch2.oct_paid_rent2, name='oct_paid_rent2'),
    path('nov_paid_rent2/', branch2.nov_paid_rent2, name='nov_paid_rent2'),
    path('dec_paid_rent2/', branch2.dec_paid_rent2, name='dec_paid_rent2'),

    path('details_of_paid_guests2/<id>',branch2.details_of_paid_guests2,name='details_of_paid_guests2'),

#paid rent end here


#*********reports end here


]