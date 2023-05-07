from django.contrib import admin
from django.urls import path
from . import views
from . import admin_branch1

from . import branch1
#from . import branch2
#from . import branch3
from . import reports1

d='test'

urlpatterns = [
    path('', views.index, name='index'),
    path('login_request/', views.login_request, name='login_request'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # ****user start here *****
    path('view_all_users/', views.view_all_users, name='view_all_users'),
    path('create_user/', views.create_user, name='create_user'),
    path('user_regi/', views.user_regi, name='user_regi'),
    path('delete_user/<id>', views.delete_user, name='delete_user'),
    path('user_update/<id>', views.user_update, name='user_update'),
    # ****user end here ******

#branch one start here
    path('branch1_dashboard/',branch1.branch1_dashboard,name='branch1_dashboard'),
#**room creation start here

    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi/',admin_branch1.branch1_room_create_regi,name='branch1_room_create_regi'),
    path('view_all_rooms/',admin_branch1.view_all_rooms,name='view_all_rooms'),
    path('delete_room/<id>',admin_branch1.delete_room,name='delete_room'),

    path('branch1_room_create/',admin_branch1.branch1_room_create,name='branch1_room_create'),

#**room creation end here
#bed creation start here

    path('pg1_bed_create_regi/', admin_branch1.pg1_bed_create_regi, name='pg1_bed_create_regi'),
    path('pg1_view_all_beds/', admin_branch1.pg1_view_all_beds, name='pg1_view_all_beds'),
    path('delete_bed/<id>', admin_branch1.delete_bed, name='delete_bed'),

    path('pg1_bed_create/', admin_branch1.pg1_bed_create, name='pg1_bed_create'),

    path('single_pg1_bed_create_regi/', admin_branch1.single_pg1_bed_create_regi, name='single_pg1_bed_create_regi'),
    path('update_bed_basic_details/<id>', admin_branch1.update_bed_basic_details, name='update_bed_basic_details'),

    #bed creation end here
#guest
    path('br1_admit_guest/<id>',branch1.br1_admit_guest,name='br1_admit_guest'),
    path('view_all_new_guest/',branch1.view_all_new_guest,name='view_all_new_guest'),
    path('update_br1_admit_guest/<id>',branch1.update_br1_admit_guest,name='update_br1_admit_guest'),
    path('vacate_br1_guest/<id>',branch1.vacate_br1_guest,name='vacate_br1_guest'),
    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),
#guest end here

#*********reports start here

#unpaid rent start here
    path('unpaid_rent_choose_months/',branch1.unpaid_rent_choose_months,name='unpaid_rent_choose_months'),

    path('jan_unpaid_rent/', branch1.jan_unpaid_rent, name='jan_unpaid_rent'),
    path('feb_unpaid_rent/', branch1.feb_unpaid_rent, name='feb_unpaid_rent'),
    path('mar_unpaid_rent/', branch1.mar_unpaid_rent, name='mar_unpaid_rent'),
    path('april_unpaid_rent/', branch1.april_unpaid_rent, name='april_unpaid_rent'),

    path('may_unpaid_rent/', branch1.may_unpaid_rent, name='may_unpaid_rent'),
    path('june_unpaid_rent/', branch1.june_unpaid_rent, name='june_unpaid_rent'),
    path('july_unpaid_rent/', branch1.july_unpaid_rent, name='july_unpaid_rent'),
    path('aug_unpaid_rent/', branch1.aug_unpaid_rent, name='aug_unpaid_rent'),

    path('sept_unpaid_rent/', branch1.sept_unpaid_rent, name='sept_unpaid_rent'),
    path('oct_unpaid_rent/', branch1.oct_unpaid_rent, name='oct_unpaid_rent'),
    path('nov_unpaid_rent/', branch1.nov_unpaid_rent, name='nov_unpaid_rent'),
    path('dec_unpaid_rent/', branch1.dec_unpaid_rent, name='dec_unpaid_rent'),

    path('details_of_unpaid_guests/<id>',branch1.details_of_unpaid_guests,name='details_of_unpaid_guests'),

#unpaid rent end here

#paid rent start here
    path('paid_rent_choose_months/',branch1.paid_rent_choose_months,name='paid_rent_choose_months'),

    path('jan_paid_rent/', branch1.jan_paid_rent, name='jan_paid_rent'),
    path('feb_paid_rent/', branch1.feb_paid_rent, name='feb_paid_rent'),
    path('mar_paid_rent/', branch1.mar_paid_rent, name='mar_paid_rent'),
    path('april_paid_rent/', branch1.april_paid_rent, name='april_paid_rent'),

    path('may_paid_rent/', branch1.may_paid_rent, name='may_paid_rent'),
    path('june_paid_rent/', branch1.june_paid_rent, name='june_paid_rent'),
    path('july_paid_rent/', branch1.july_paid_rent, name='july_paid_rent'),
    path('aug_paid_rent/', branch1.aug_paid_rent, name='aug_paid_rent'),

    path('sept_paid_rent/', branch1.sept_paid_rent, name='sept_paid_rent'),
    path('oct_paid_rent/', branch1.oct_paid_rent, name='oct_paid_rent'),
    path('nov_paid_rent/', branch1.nov_paid_rent, name='nov_paid_rent'),
    path('dec_paid_rent/', branch1.dec_paid_rent, name='dec_paid_rent'),

    path('details_of_paid_guests/<id>',branch1.details_of_paid_guests,name='details_of_paid_guests'),
    path('full_paid_guest/', reports1.full_paid_guest, name='full_paid_guest'),

#paid rent end here


#*********reports end here

##################################
#PAYMENTS START HERE
################################

    path('choose_months/',branch1.choose_months,name='choose_months'),

    path('jan/',branch1.jan,name='jan'),
    path('jan_manke_payments/<id>',branch1.jan_manke_payments,name='jan_manke_payments'),

    path('feb/',branch1.feb,name='feb'),
    path('feb_manke_payments/<id>',branch1.feb_manke_payments,name='feb_manke_payments'),

    path('march/',branch1.march,name='march'),
    path('march_manke_payments/<id>',branch1.march_manke_payments,name='march_manke_payments'),

    path('april/',branch1.april,name='april'),
    path('april_make_payments/<id>',branch1.april_make_payments,name='april_make_payments'),

    path('may/',branch1.may,name='may'),
    path('may_make_payments/<id>',branch1.may_make_payments,name='may_make_payments'),

    path('june/',branch1.june,name='june'),
    path('june_make_payments/<id>',branch1.june_make_payments,name='june_make_payments'),

    path('july/',branch1.july,name='july'),
    path('july_make_payments/<id>',branch1.july_make_payments,name='july_make_payments'),

    path('aug/',branch1.aug,name='aug'),
    path('aug_make_payments/<id>',branch1.aug_make_payments,name='aug_make_payments'),

    path('sept/',branch1.sept,name='sept'),
    path('sept_make_payments/<id>',branch1.sept_make_payments,name='sept_make_payments'),

    path('oct/',branch1.oct,name='oct'),
    path('oct_make_payments/<id>',branch1.oct_make_payments,name='oct_make_payments'),

    path('nov/',branch1.nov,name='nov'),
    path('nov_make_payments/<id>',branch1.nov_make_payments,name='nov_make_payments'),

    path('dec/',branch1.dec,name='dec'),
    path('dec_make_payments/<id>',branch1.dec_make_payments,name='dec_make_payments'),

##################################
#PAYMENTS END HERE
################################

##################################
#ADVANCE START HERE
################################

    path('choose_months_advance/',branch1.choose_months_advance,name='choose_months_advance'),

    path('april_advane/', branch1.april_advane, name='april_advane'),
    path('april_make_payments_advance/<id>', branch1.april_make_payments_advance, name='april_make_payments_advance'),

    path('may_advane/',branch1.may_advane,name='may_advane'),
    path('may_make_payments_advance/<id>', branch1.may_make_payments_advance, name='may_make_payments_advance'),
    path('june_advane/',branch1.june_advane,name='june_advane'),
    path('june_make_payments_advance/<id>', branch1.june_make_payments_advance, name='june_make_payments_advance'),
    path('july_advane/',branch1.july_advane,name='july_advane'),
    path('july_make_payments_advance/<id>', branch1.july_make_payments_advance, name='july_make_payments_advance'),
    path('auguest_advance/', branch1.auguest_advance, name='auguest_advance'),
    path('auguest_make_payments_advance/<id>', branch1.auguest_make_payments_advance, name='auguest_make_payments_advance'),

    path('sept_advance/', branch1.sept_advance, name='sept_advance'),
    path('sept_make_payments_advance/<id>', branch1.sept_make_payments_advance,name='sept_make_payments_advance'),
    path('october_advance/', branch1.october_advance, name='october_advance'),
    path('october_make_payments_advance/<id>', branch1.october_make_payments_advance, name='october_make_payments_advance'),
    path('nov_advance/', branch1.nov_advance, name='nov_advance'),
    path('nov_make_payments_advance/<id>', branch1.nov_make_payments_advance,name='nov_make_payments_advance'),
    path('dec_advance/', branch1.dec_advance, name='dec_advance'),
    path('dec_make_payments_advance/<id>', branch1.dec_make_payments_advance, name='dec_make_payments_advance'),

    ##################################
#ADVANCE END HERE
################################

##################################
#PRINT OUTS START HERE
################################

    path('detail_guest_general/',branch1.detail_guest_general,name='detail_guest_general'),

    path('jan_print/',branch1.jan_print,name='jan_print'),
    path('feb_print/',branch1.feb_print,name='feb_print'),
    path('march_print/',branch1.march_print,name='march_print'),
    path('april_print/',branch1.april_print,name='april_print'),

    path('may_print/',branch1.may_print,name='may_print'),
    path('june_print/',branch1.june_print,name='june_print'),
    path('july_print/', branch1.july_print, name='july_print'),
    path('aug_print/', branch1.aug_print, name='aug_print'),

    path('sept_print/', branch1.sept_print, name='sept_print'),
    path('oct_print/', branch1.oct_print, name='oct_print'),
    path('nov_print/', branch1.nov_print, name='nov_print'),
    path('dec_print/', branch1.dec_print, name='dec_print'),

##################################
#PRINT OUTS END HERE
################################

    path('jan_close/',branch1.jan_close,name='jan_close'),
    path('jan_close_decision_page/',branch1.jan_close_decision_page,name='jan_close_decision_page'),
    path('feb_close/',branch1.feb_close,name='feb_close'),
    path('feb_close_decision_page/',branch1.feb_close_decision_page,name='feb_close_decision_page'),
    path('mar_close/', branch1.mar_close, name='mar_close'),
    path('mar_close_decision_page/', branch1.mar_close_decision_page, name='mar_close_decision_page'),
    path('apr_close/', branch1.apr_close, name='apr_close'),
    path('apr_close_decision_page/', branch1.apr_close_decision_page, name='apr_close_decision_page'),

    path('may_close/', branch1.may_close, name='may_close'),
    path('may_close_decision_page/', branch1.may_close_decision_page, name='may_close_decision_page'),
    path('jun_close/', branch1.jun_close, name='jun_close'),
    path('jun_close_decision_page/', branch1.jun_close_decision_page, name='jun_close_decision_page'),
    path('jul_close/', branch1.jul_close, name='jul_close'),
    path('jul_close_decision_page/', branch1.jul_close_decision_page, name='jul_close_decision_page'),
    path('aug_close/', branch1.aug_close, name='aug_close'),
    path('aug_close_decision_page/', branch1.aug_close_decision_page, name='aug_close_decision_page'),

    path('sep_close/', branch1.sep_close, name='sep_close'),
    path('sep_close_decision_page/', branch1.sep_close_decision_page, name='sep_close_decision_page'),
    path('oct_close/', branch1.oct_close, name='oct_close'),
    path('oct_close_decision_page/', branch1.oct_close_decision_page, name='oct_close_decision_page'),
    path('nov_close/', branch1.nov_close, name='nov_close'),
    path('nov_close_decision_page/', branch1.nov_close_decision_page, name='nov_close_decision_page'),

    ##################################
#VACATE GUEST DETAILS START HERE
################################

    path('viewall_vacate_guest/',branch1.viewall_vacate_guest,name='viewall_vacate_guest'),
    path('details_of_vacate_guest/<id>',branch1.details_of_vacate_guest,name='details_of_vacate_guest'),

#********vacate guest payments start here**********

    path('jan_manke_payments_vacate/<id>', branch1.jan_manke_payments_vacate, name='jan_manke_payments_vacate'),
    path('feb_manke_payments_vacate/<id>', branch1.feb_manke_payments_vacate, name='feb_manke_payments_vacate'),
    path('march_manke_payments_vacate/<id>', branch1.march_manke_payments_vacate, name='march_manke_payments_vacate'),
    path('april_make_payments_vacate/<id>', branch1.april_make_payments_vacate, name='april_make_payments_vacate'),

    path('may_make_payments_vacate/<id>', branch1.may_make_payments_vacate, name='may_make_payments_vacate'),
    path('june_make_payments_vacate/<id>', branch1.june_make_payments_vacate, name='june_make_payments_vacate'),
    path('july_make_payments_vacate/<id>', branch1.july_make_payments_vacate, name='july_make_payments_vacate'),
    path('aug_make_payments_vacate/<id>', branch1.aug_make_payments_vacate, name='aug_make_payments_vacate'),

    path('sept_make_payments_vacate/<id>', branch1.sept_make_payments_vacate, name='sept_make_payments_vacate'),
    path('oct_make_payments_vacate/<id>', branch1.oct_make_payments_vacate, name='oct_make_payments_vacate'),
    path('nov_make_payments_vacate/<id>', branch1.nov_make_payments_vacate, name='nov_make_payments_vacate'),
    path('dec_make_payments_vacate/<id>', branch1.dec_make_payments_vacate, name='dec_make_payments_vacate'),

#********vacate guest payments end here**********

##################################
#VACATE GUEST DETAILS END HERE
################################

    path('may_print_live/', reports1.may_print_live, name='may_print_live'),
    path('viewall_vaccant_room/', reports1.viewall_vaccant_room, name='viewall_vaccant_room'),

    #branch one end here

    path('pysql/',branch1.pysql,name='pysql'+d),
    #logout
    path('logout/',views.logout,name='logout'),

]