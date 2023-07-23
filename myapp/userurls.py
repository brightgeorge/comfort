from django.contrib import admin
from django.urls import path
from . import views
from . import admin_branch1

from . import branch1
#from . import branch2
#from . import branch3
from . import reports1
from . import admin_dahsboard_calculations
from . import payment1
from . import admin_dashboard_calculations_br1

d='test'

urlpatterns = [
    path('', views.index, name='index'),
    path('login_request/', views.login_request, name='login_request'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('select_branch/',views.select_branch,name='select_branch'),

    path('backgrounds', branch1.backgrounds, name='backgrounds'),
    path('background_regis', branch1.background_regis, name='background_regis'),
    path('custom_background_regis', branch1.custom_background_regis, name='custom_background_regis'),

    path('branchwise_total_guest/',admin_dahsboard_calculations.branchwise_total_guest,name='branchwise_total_guest'),
    path('total_vaccant_share_choose_branches/',admin_dahsboard_calculations.total_vaccant_share_choose_branches,name='total_vaccant_share_choose_branches'),
    path('details_branch1/',admin_dahsboard_calculations.details_branch1,name='details_branch1'),
    path('details_branch2/',admin_dahsboard_calculations.details_branch2,name='details_branch2'),
    path('details_branch3/',admin_dahsboard_calculations.details_branch3,name='details_branch3'),
    path('details_branch4/',admin_dahsboard_calculations.details_branch4,name='details_branch4'),
    path('details_branch5/',admin_dahsboard_calculations.details_branch5,name='details_branch5'),

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
path('table_jan_unpaid_rent/', branch1.table_jan_unpaid_rent, name='table_jan_unpaid_rent'),
path('feb_unpaid_rent/', branch1.feb_unpaid_rent, name='feb_unpaid_rent'),
path('table_feb_unpaid_rent/', branch1.table_feb_unpaid_rent, name='table_feb_unpaid_rent'),
path('mar_unpaid_rent/', branch1.mar_unpaid_rent, name='mar_unpaid_rent'),
path('table_mar_unpaid_rent/', branch1.table_mar_unpaid_rent, name='table_mar_unpaid_rent'),
path('april_unpaid_rent/', branch1.april_unpaid_rent, name='april_unpaid_rent'),
path('table_april_unpaid_rent/', branch1.table_april_unpaid_rent, name='table_april_unpaid_rent'),

path('may_unpaid_rent/', branch1.may_unpaid_rent, name='may_unpaid_rent'),
path('table_may_unpaid_rent/', branch1.table_may_unpaid_rent, name='table_may_unpaid_rent'),
path('june_unpaid_rent/', branch1.june_unpaid_rent, name='june_unpaid_rent'),
path('table_june_unpaid_rent/', branch1.table_june_unpaid_rent, name='table_june_unpaid_rent'),
path('july_unpaid_rent/', branch1.july_unpaid_rent, name='july_unpaid_rent'),
path('table_july_unpaid_rent',branch1.table_july_unpaid_rent,name='table_july_unpaid_rent'),
path('aug_unpaid_rent/', branch1.aug_unpaid_rent, name='aug_unpaid_rent'),
path('table_aug_unpaid_rent/',branch1.table_aug_unpaid_rent,name='table_aug_unpaid_rent'),

path('sept_unpaid_rent/', branch1.sept_unpaid_rent, name='sept_unpaid_rent'),
path('table_sept_unpaid_rent/', branch1.table_sept_unpaid_rent, name='table_sept_unpaid_rent'),
path('oct_unpaid_rent/', branch1.oct_unpaid_rent, name='oct_unpaid_rent'),
path('table_oct_unpaid_rent/', branch1.table_oct_unpaid_rent, name='table_oct_unpaid_rent'),
path('nov_unpaid_rent/', branch1.nov_unpaid_rent, name='nov_unpaid_rent'),
path('table_nov_unpaid_rent/', branch1.table_nov_unpaid_rent, name='table_nov_unpaid_rent'),
path('dec_unpaid_rent/', branch1.dec_unpaid_rent, name='dec_unpaid_rent'),
path('table_dec_unpaid_rent/', branch1.table_dec_unpaid_rent, name='table_dec_unpaid_rent'),

path('details_of_unpaid_guests/<id>',branch1.details_of_unpaid_guests,name='details_of_unpaid_guests'),

#unpaid rent end here

#paid rent start here

#paid rent start here

path('paid_rent_choose_months/',branch1.paid_rent_choose_months,name='paid_rent_choose_months'),
path('partially_paid_guest_choose_months/',reports1.partially_paid_guest_choose_months,name='partially_paid_guest_choose_months'),

path('jan_paid_rent/', branch1.jan_paid_rent, name='jan_paid_rent'),
path('table_jan_paid_rent/', branch1.table_jan_paid_rent, name='table_jan_paid_rent'),
path('jan_full_paid_guest/', reports1.jan_full_paid_guest, name='jan_full_paid_guest'),
path('jan_partially_paid_guest/', reports1.jan_partially_paid_guest, name='jan_partially_paid_guest'),
path('table_jan_partially_paid_guest/', reports1.table_jan_partially_paid_guest,name='table_jan_partially_paid_guest'),

path('feb_paid_rent/', branch1.feb_paid_rent, name='feb_paid_rent'),
path('table_feb_paid_rent/', branch1.table_feb_paid_rent, name='table_feb_paid_rent'),
path('feb_full_paid_guest/', reports1.feb_full_paid_guest, name='feb_full_paid_guest'),
path('feb_partially_paid_guest/', reports1.feb_partially_paid_guest, name='feb_partially_paid_guest'),
path('table_feb_partially_paid_guest/', reports1.table_feb_partially_paid_guest,name='table_feb_partially_paid_guest'),

path('mar_paid_rent/', branch1.mar_paid_rent, name='mar_paid_rent'),
path('table_mar_paid_rent/', branch1.table_mar_paid_rent, name='table_mar_paid_rent'),
path('march_full_paid_guest/', reports1.march_full_paid_guest, name='march_full_paid_guest'),
path('march_partially_paid_guest/', reports1.march_partially_paid_guest, name='march_partially_paid_guest'),
path('table_march_partially_paid_guest/', reports1.table_march_partially_paid_guest,name='table_march_partially_paid_guest'),

path('april_paid_rent/', branch1.april_paid_rent, name='april_paid_rent'),
path('table_april_paid_rent/', branch1.table_april_paid_rent, name='table_april_paid_rent'),
path('april_full_paid_guest/', reports1.april_full_paid_guest, name='april_full_paid_guest'),
path('april_partially_paid_guest/', reports1.april_partially_paid_guest, name='april_partially_paid_guest'),
path('table_april_partially_paid_guest/', reports1.table_april_partially_paid_guest,name='table_april_partially_paid_guest'),

path('may_paid_rent/', branch1.may_paid_rent, name='may_paid_rent'),
path('table_may_paid_rent/', branch1.table_may_paid_rent, name='table_may_paid_rent'),
path('may_full_paid_guest/', reports1.may_full_paid_guest, name='may_full_paid_guest'),
path('may_partially_paid_guest/', reports1.may_partially_paid_guest, name='may_partially_paid_guest'),
path('table_may_partially_paid_guest/', reports1.table_may_partially_paid_guest, name='table_may_partially_paid_guest'),

path('june_paid_rent/', branch1.june_paid_rent, name='june_paid_rent'),
path('table_june_paid_rent/', branch1.table_june_paid_rent, name='table_june_paid_rent'),
path('june_full_paid_guest/', reports1.june_full_paid_guest, name='june_full_paid_guest'),
path('june_partially_paid_guest/', reports1.june_partially_paid_guest, name='june_partially_paid_guest'),
path('table_june_partially_paid_guest/', reports1.table_june_partially_paid_guest, name='table_june_partially_paid_guest'),

path('july_paid_rent/', branch1.july_paid_rent, name='july_paid_rent'),
path('table_july_paid_rent/', branch1.table_july_paid_rent, name='table_july_paid_rent'),
path('july_full_paid_guest/', reports1.july_full_paid_guest, name='july_full_paid_guest'),
path('july_partially_paid_guest/', reports1.july_partially_paid_guest, name='july_partially_paid_guest'),
path('table_july_partially_paid_guest/', reports1.table_july_partially_paid_guest, name='table_july_partially_paid_guest'),

path('aug_paid_rent/', branch1.aug_paid_rent, name='aug_paid_rent'),
path('table_aug_paid_rent/', branch1.table_aug_paid_rent, name='table_aug_paid_rent'),
path('auguest_full_paid_guest/', reports1.auguest_full_paid_guest, name='auguest_full_paid_guest'),
path('auguest_partially_paid_guest/', reports1.auguest_partially_paid_guest,name='auguest_partially_paid_guest'),
path('table_auguest_partially_paid_guest/', reports1.table_auguest_partially_paid_guest,name='table_auguest_partially_paid_guest'),

path('sept_paid_rent/', branch1.sept_paid_rent, name='sept_paid_rent'),
path('table_sept_paid_rent/', branch1.table_sept_paid_rent, name='table_sept_paid_rent'),
path('sept_full_paid_guest/', reports1.sept_full_paid_guest, name='sept_full_paid_guest'),
path('sept_partially_paid_guest/', reports1.sept_partially_paid_guest, name='sept_partially_paid_guest'),
path('table_sept_partially_paid_guest/', reports1.table_sept_partially_paid_guest,name='table_sept_partially_paid_guest'),

path('oct_paid_rent/', branch1.oct_paid_rent, name='oct_paid_rent'),
path('table_oct_paid_rent/', branch1.table_oct_paid_rent, name='table_oct_paid_rent'),
path('october_full_paid_guest/', reports1.october_full_paid_guest, name='october_full_paid_guest'),
path('october_partially_paid_guest/', reports1.october_partially_paid_guest,name='october_partially_paid_guest'),
path('table_october_partially_paid_guest/', reports1.table_october_partially_paid_guest,name='table_october_partially_paid_guest'),

path('nov_paid_rent/', branch1.nov_paid_rent, name='nov_paid_rent'),
path('table_nov_paid_rent/', branch1.table_nov_paid_rent, name='table_nov_paid_rent'),
path('nov_full_paid_guest/', reports1.nov_full_paid_guest, name='nov_full_paid_guest'),
path('nov_partially_paid_guest/', reports1.nov_partially_paid_guest, name='nov_partially_paid_guest'),
path('table_nov_partially_paid_guest/', reports1.table_nov_partially_paid_guest,name='table_nov_partially_paid_guest'),

path('dec_paid_rent/', branch1.dec_paid_rent, name='dec_paid_rent'),
path('table_dec_paid_rent/', branch1.table_dec_paid_rent, name='table_dec_paid_rent'),
path('dec_full_paid_guest/', reports1.dec_full_paid_guest, name='dec_full_paid_guest'),
path('dec_partially_paid_guest/', reports1.dec_partially_paid_guest, name='dec_partially_paid_guest'),
path('table_dec_partially_paid_guest/', reports1.table_dec_partially_paid_guest,name='table_dec_partially_paid_guest'),

path('details_of_paid_guests/<id>',branch1.details_of_paid_guests,name='details_of_paid_guests'),
path('full_paid_guest/',reports1.full_paid_guest,name='full_paid_guest'),

#paid rent end here



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
#MONTHLY MANAGEMENT PAYMENTS START HERE
################################

    path('choose_user/', payment1.choose_user, name='choose_user'),
    path('payment_user_details/<id>', payment1.payment_user_details, name='payment_user_details'),

    path('monthly_jan_make_payments/<id>', payment1.monthly_jan_make_payments, name='monthly_jan_make_payments'),
    path('monthly_feb_make_payments/<id>', payment1.monthly_feb_make_payments, name='monthly_feb_make_payments'),
    path('monthly_march_make_payments/<id>', payment1.monthly_march_make_payments, name='monthly_march_make_payments'),
    path('monthly_april_make_payments/<id>', payment1.monthly_april_make_payments, name='monthly_april_make_payments'),
    path('monthly_may_make_payments/<id>', payment1.monthly_may_make_payments, name='monthly_may_make_payments'),
    path('monthly_june_make_payments/<id>', payment1.monthly_june_make_payments, name='monthly_june_make_payments'),

    path('monthly_july_make_payments/<id>', payment1.monthly_july_make_payments, name='monthly_july_make_payments'),
    path('monthly_aug_make_payments/<id>', payment1.monthly_aug_make_payments, name='monthly_aug_make_payments'),
    path('monthly_sept_make_payments/<id>', payment1.monthly_sept_make_payments, name='monthly_sept_make_payments'),
    path('monthly_oct_make_payments/<id>', payment1.monthly_oct_make_payments, name='monthly_oct_make_payments'),
    path('monthly_nov_make_payments/<id>', payment1.monthly_nov_make_payments, name='monthly_nov_make_payments'),
    path('monthly_dec_make_payments/<id>', payment1.monthly_dec_make_payments, name='monthly_dec_make_payments'),


##################################
#MONTHLY MANAGEMENT PAYMENTS END HERE
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
    path('full_vacated_guest_details',branch1.full_vacated_guest_details,name='full_vacated_guest_details'),
    path('full_vacated_guest_table',branch1.full_vacated_guest_table,name='full_vacated_guest_table'),



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


########################################
# DETAILED REPORT START HERE
###########################

    path('detailed_report_choose_months/',reports1.detailed_report_choose_months,name='detailed_report_choose_months'),

    path('jan_details_live/', reports1.jan_details_live, name='jan_details_live'),
    path('jan_print_live/', reports1.jan_print_live, name='jan_print_live'),
    path('feb_details_live/', reports1.feb_details_live, name='feb_details_live'),
    path('feb_print_live/', reports1.feb_print_live, name='feb_print_live'),
    path('march_details_live/', reports1.march_details_live, name='march_details_live'),
    path('march_print_live/', reports1.march_print_live, name='march_print_live'),

    path('april_details_live/', reports1.april_details_live, name='april_details_live'),
    path('april_print_live/', reports1.april_print_live, name='april_print_live'),
    path('may_details_live/', reports1.may_details_live, name='may_details_live'),
    path('may_print_live/', reports1.may_print_live, name='may_print_live'),
    path('june_details_live/',reports1.june_details_live,name='june_details_live'),
    path('june_print_live/', reports1.june_print_live, name='june_print_live'),

    path('july_details_live/', reports1.july_details_live, name='july_details_live'),
    path('july_print_live/', reports1.july_print_live, name='july_print_live'),
    path('auguest_details_live/', reports1.auguest_details_live, name='auguest_details_live'),
    path('auguest_print_live/', reports1.auguest_print_live, name='auguest_print_live'),
    path('sept_details_live/', reports1.sept_details_live, name='sept_details_live'),
    path('sept_print_live/', reports1.sept_print_live, name='sept_print_live'),

    path('october_details_live/', reports1.october_details_live, name='october_details_live'),
    path('october_print_live/', reports1.october_print_live, name='october_print_live'),
    path('nov_details_live/', reports1.nov_details_live, name='nov_details_live'),
    path('nov_print_live/', reports1.nov_print_live, name='nov_print_live'),
    path('dec_details_live/', reports1.dec_details_live, name='dec_details_live'),
    path('dec_print_live/', reports1.dec_print_live, name='dec_print_live'),

########################################
#  DETAILED REPORT END HERE
###########################



    path('viewall_vaccant_room/', reports1.viewall_vaccant_room, name='viewall_vaccant_room'),

########################################
# DUE AMT MANAGEMENT START HERE
###########################

    path('view_all_due_amt/', branch1.view_all_due_amt, name='view_all_due_amt'),
    path('due_amt_mgt_choose_months/', branch1.due_amt_mgt_choose_months, name='due_amt_mgt_choose_months'),

    path('view_may_account_details/',branch1.view_may_account_details,name='view_may_account_details'),
    path('may_account_mgt/<id>', branch1.may_account_mgt, name='may_account_mgt'),

    path('view_june_account_details/', branch1.view_june_account_details, name='view_june_account_details'),
    path('june_account_mgt/<id>',branch1.june_account_mgt,name='june_account_mgt'),
    path('view_july_account_details/', branch1.view_july_account_details, name='view_july_account_details'),
    path('july_account_mgt/<id>',branch1.july_account_mgt,name='july_account_mgt'),

########################################
# DUE AMT MANAGEMENT END HERE
###########################

########################################
# DASHBOARD REPORTS START HERE
###########################

    path('monthly_details_due', admin_dashboard_calculations_br1.monthly_details_due, name='monthly_details_due'),
    path('monthly_collection_details/', admin_dashboard_calculations_br1.monthly_collection_details, name='monthly_collection_details'),

########################################
# DASHBOARD REPORTS END HERE
###########################



    #branch one end here

    path('pysql/',branch1.pysql,name='pysql'+d),
    #logout
    path('logout/',views.logout,name='logout'),

]