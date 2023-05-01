from django.contrib import admin
from django.urls import path, include

from . import admin_branch4
from . import branch4

urlpatterns = [

    path('branch1_dashboard4/', branch4.branch1_dashboard4, name='branch1_dashboard4'),

#**room creation start here
    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi4/',admin_branch4.branch1_room_create_regi4,name='branch1_room_create_regi4'),
    path('view_all_room4/',admin_branch4.view_all_room4,name='view_all_room4'),
    path('delete_room4/<id>',admin_branch4.delete_room4,name='delete_room4'),

    path('branch1_room_create4/',admin_branch4.branch1_room_create4,name='branch1_room_create4'),

#**room creation end here


#bed creation start here

    path('pg1_bed_create_regi4/', admin_branch4.pg1_bed_create_regi4, name='pg1_bed_create_regi4'),
    path('pg1_view_all_beds4/', admin_branch4.pg1_view_all_beds4, name='pg1_view_all_beds4'),
    path('delete_bed4/<id>', admin_branch4.delete_bed4, name='delete_bed4'),

    path('pg1_bed_create4/', admin_branch4.pg1_bed_create4, name='pg1_bed_create4'),

#bed creation end here

#guest
    path('br1_admit_guest4/<id>',branch4.br1_admit_guest4,name='br1_admit_guest4'),
    path('view_all_new_guest4/',branch4.view_all_new_guest4,name='view_all_new_guest4'),
    path('update_br1_admit_guest4/<id>',branch4.update_br1_admit_guest4,name='update_br1_admit_guest4'),
    path('vacate_br1_guest4/<id>',branch4.vacate_br1_guest4,name='vacate_br1_guest4'),
    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),
#guest end here




##################################
#PAYMENTS START HERE
################################

    path('choose_months4/',branch4.choose_months4,name='choose_months4'),

    path('jan4/',branch4.jan4,name='jan4'),
    path('jan_manke_payments4/<id>',branch4.jan_manke_payments4,name='jan_manke_payments4'),

    path('feb4/',branch4.feb4,name='feb4'),
    path('feb_manke_payments4/<id>',branch4.feb_manke_payments4,name='feb_manke_payments4'),

    path('march4/',branch4.march4,name='march4'),
    path('march_manke_payments4/<id>',branch4.march_manke_payments4,name='march_manke_payments4'),

    path('april4/',branch4.april4,name='april4'),
    path('april_make_payments4/<id>',branch4.april_make_payments4,name='april_make_payments4'),

    path('may4/',branch4.may4,name='may4'),
    path('may_make_payments4/<id>',branch4.may_make_payments4,name='may_make_payments4'),

    path('june4/',branch4.june4,name='june4'),
    path('june_make_payments4/<id>',branch4.june_make_payments4,name='june_make_payments4'),

    path('july4/',branch4.july4,name='july4'),
    path('july_make_payments4/<id>',branch4.july_make_payments4,name='july_make_payments4'),

    path('aug4/',branch4.aug4,name='aug4'),
    path('aug_make_payments4/<id>',branch4.aug_make_payments4,name='aug_make_payments4'),

    path('sept4/',branch4.sept4,name='sept4'),
    path('sept_make_payments4/<id>',branch4.sept_make_payments4,name='sept_make_payments4'),

    path('oct4/',branch4.oct4,name='oct4'),
    path('oct_make_payments4/<id>',branch4.oct_make_payments4,name='oct_make_payments4'),

    path('nov4/',branch4.nov4,name='nov4'),
    path('nov_make_payments4/<id>',branch4.nov_make_payments4,name='nov_make_payments4'),

    path('dec4/',branch4.dec4,name='dec4'),
    path('dec_make_payments4/<id>',branch4.dec_make_payments4,name='dec_make_payments4'),

##################################
#PAYMENTS END HERE
################################




#*********reports start here

#unpaid rent start here
    path('unpaid_rent_choose_months4/',branch4.unpaid_rent_choose_months4,name='unpaid_rent_choose_months4'),

    path('jan_unpaid_rent4/', branch4.jan_unpaid_rent4, name='jan_unpaid_rent4'),
    path('feb_unpaid_rent4/', branch4.feb_unpaid_rent4, name='feb_unpaid_rent4'),
    path('mar_unpaid_rent4/', branch4.mar_unpaid_rent4, name='mar_unpaid_rent4'),
    path('april_unpaid_rent4/', branch4.april_unpaid_rent4, name='april_unpaid_rent4'),

    path('may_unpaid_rent4/', branch4.may_unpaid_rent4, name='may_unpaid_rent4'),
    path('june_unpaid_rent4/', branch4.june_unpaid_rent4, name='june_unpaid_rent4'),
    path('july_unpaid_rent4/', branch4.july_unpaid_rent4, name='july_unpaid_rent4'),
    path('aug_unpaid_rent4/', branch4.aug_unpaid_rent4, name='aug_unpaid_rent4'),

    path('sept_unpaid_rent4/', branch4.sept_unpaid_rent4, name='sept_unpaid_rent4'),
    path('oct_unpaid_rent4/', branch4.oct_unpaid_rent4, name='oct_unpaid_rent4'),
    path('nov_unpaid_rent4/', branch4.nov_unpaid_rent4, name='nov_unpaid_rent4'),
    path('dec_unpaid_rent4/', branch4.dec_unpaid_rent4, name='dec_unpaid_rent4'),

    path('details_of_unpaid_guests4/<id>',branch4.details_of_unpaid_guests4,name='details_of_unpaid_guests4'),

#unpaid rent end here

#paid rent start here
    path('paid_rent_choose_months4/',branch4.paid_rent_choose_months4,name='paid_rent_choose_months4'),

    path('jan_paid_rent4/', branch4.jan_paid_rent4, name='jan_paid_rent4'),
    path('feb_paid_rent4/', branch4.feb_paid_rent4, name='feb_paid_rent4'),
    path('mar_paid_rent4/', branch4.mar_paid_rent4, name='mar_paid_rent4'),
    path('april_paid_rent4/', branch4.april_paid_rent4, name='april_paid_rent4'),

    path('may_paid_rent4/', branch4.may_paid_rent4, name='may_paid_rent4'),
    path('june_paid_rent4/', branch4.june_paid_rent4, name='june_paid_rent4'),
    path('july_paid_rent4/', branch4.july_paid_rent4, name='july_paid_rent4'),
    path('aug_paid_rent4/', branch4.aug_paid_rent4, name='aug_paid_rent4'),

    path('sept_paid_rent4/', branch4.sept_paid_rent4, name='sept_paid_rent4'),
    path('oct_paid_rent4/', branch4.oct_paid_rent4, name='oct_paid_rent4'),
    path('nov_paid_rent4/', branch4.nov_paid_rent4, name='nov_paid_rent4'),
    path('dec_paid_rent4/', branch4.dec_paid_rent4, name='dec_paid_rent4'),

    path('details_of_paid_guests4/<id>',branch4.details_of_paid_guests4,name='details_of_paid_guests4'),

#paid rent end here

#*********reports end here





]