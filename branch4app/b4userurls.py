from django.contrib import admin
from django.urls import path, include

from . import admin_branch4
from . import branch4
from . import reports4
from . import payment4
from . import admin_dashboard_calculations_br4

urlpatterns = [

    path('branch1_dashboard4/', branch4.branch1_dashboard4, name='branch1_dashboard4'),
    path('monthly_details_due4', admin_dashboard_calculations_br4.monthly_details_due4, name='monthly_details_due4'),

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
#_ADVANCE4 START HERE
################################


path('choose_months_advance4/',branch4.choose_months_advance4,name='choose_months_advance4'),

path('jan_advance4/', branch4.jan_advance4, name='jan_advance4'),
path('jan_make_payments_advance4/<id>', branch4.jan_make_payments_advance4,name='jan_make_payments_advance4'),
path('feb_advance4/', branch4.feb_advance4, name='feb_advance4'),
path('feb_make_payments_advance4/<id>', branch4.feb_make_payments_advance4,name='feb_make_payments_advance4'),
path('march_advance4/', branch4.march_advance4, name='march_advance4'),
path('march_make_payments_advance4/<id>', branch4.march_make_payments_advance4,name='march_make_payments_advance4'),
path('april_advance4/', branch4.april_advance4, name='april_advance4'),
path('april_make_payments_advance4/<id>', branch4.april_make_payments_advance4, name='april_make_payments_advance4'),

path('may_advance4/',branch4.may_advance4,name='may_advance4'),
path('may_make_payments_advance4/<id>', branch4.may_make_payments_advance4, name='may_make_payments_advance4'),
path('june_advance4/',branch4.june_advance4,name='june_advance4'),
path('june_make_payments_advance4/<id>', branch4.june_make_payments_advance4, name='june_make_payments_advance4'),
path('july_advance4/',branch4.july_advance4,name='july_advance4'),
path('july_make_payments_advance4/<id>', branch4.july_make_payments_advance4, name='july_make_payments_advance4'),
path('auguest_advance4/', branch4.auguest_advance4, name='auguest_advance4'),
path('auguest_make_payments_advance4/<id>', branch4.auguest_make_payments_advance4, name='auguest_make_payments_advance4'),

path('sept_advance4/', branch4.sept_advance4, name='sept_advance4'),
path('sept_make_payments_advance4/<id>', branch4.sept_make_payments_advance4,name='sept_make_payments_advance4'),
path('october_advance4/', branch4.october_advance4, name='october_advance4'),
path('october_make_payments_advance4/<id>', branch4.october_make_payments_advance4, name='october_make_payments_advance4'),
path('nov_advance4/', branch4.nov_advance4, name='nov_advance4'),
path('nov_make_payments_advance4/<id>', branch4.nov_make_payments_advance4,name='nov_make_payments_advance4'),
path('dec_advance4/', branch4.dec_advance4, name='dec_advance4'),
path('dec_make_payments_advance4/<id>', branch4.dec_make_payments_advance4, name='dec_make_payments_advance4'),



##################################
#_ADVANCE4 END HERE
################################



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


##################################
#MONTHLY MANAGEMENT PAYMENTS START HERE
################################

    path('choose_user4/', payment4.choose_user4, name='choose_user4'),
    path('payment_user_details4/<id>', payment4.payment_user_details4, name='payment_user_details4'),

    path('monthly_jan_make_payments4/<id>', payment4.monthly_jan_make_payments4, name='monthly_jan_make_payments4'),
    path('monthly_feb_make_payments4/<id>', payment4.monthly_feb_make_payments4, name='monthly_feb_make_payments4'),
    path('monthly_march_make_payments4/<id>', payment4.monthly_march_make_payments4, name='monthly_march_make_payments4'),
    path('monthly_april_make_payments4/<id>', payment4.monthly_april_make_payments4, name='monthly_april_make_payments4'),
    path('monthly_may_make_payments4/<id>', payment4.monthly_may_make_payments4, name='monthly_may_make_payments4'),
    path('monthly_june_make_payments4/<id>', payment4.monthly_june_make_payments4, name='monthly_june_make_payments4'),

    path('monthly_july_make_payments4/<id>', payment4.monthly_july_make_payments4, name='monthly_july_make_payments4'),
    path('monthly_aug_make_payments4/<id>', payment4.monthly_aug_make_payments4, name='monthly_aug_make_payments4'),
    path('monthly_sept_make_payments4/<id>', payment4.monthly_sept_make_payments4, name='monthly_sept_make_payments4'),
    path('monthly_oct_make_payments4/<id>', payment4.monthly_oct_make_payments4, name='monthly_oct_make_payments4'),
    path('monthly_nov_make_payments4/<id>', payment4.monthly_nov_make_payments4, name='monthly_nov_make_payments4'),
    path('monthly_dec_make_payments4/<id>', payment4.monthly_dec_make_payments4, name='monthly_dec_make_payments4'),

##################################
#MONTHLY MANAGEMENT PAYMENTS END HERE
################################




#*********reports start here

#unpaid rent start here
    path('unpaid_rent_choose_months4/',branch4.unpaid_rent_choose_months4,name='unpaid_rent_choose_months4'),

    path('jan_unpaid_rent4/', branch4.jan_unpaid_rent4, name='jan_unpaid_rent4'),
    path('table_jan_unpaid_rent4/', branch4.table_jan_unpaid_rent4, name='table_jan_unpaid_rent4'),
    path('feb_unpaid_rent4/', branch4.feb_unpaid_rent4, name='feb_unpaid_rent4'),
    path('table_feb_unpaid_rent4/', branch4.table_feb_unpaid_rent4, name='table_feb_unpaid_rent4'),
    path('mar_unpaid_rent4/', branch4.mar_unpaid_rent4, name='mar_unpaid_rent4'),
    path('table_mar_unpaid_rent4/', branch4.table_mar_unpaid_rent4, name='table_mar_unpaid_rent4'),
    path('april_unpaid_rent4/', branch4.april_unpaid_rent4, name='april_unpaid_rent4'),
    path('table_april_unpaid_rent4/', branch4.table_april_unpaid_rent4, name='table_april_unpaid_rent4'),

    path('may_unpaid_rent4/', branch4.may_unpaid_rent4, name='may_unpaid_rent4'),
    path('table_may_unpaid_rent4/', branch4.table_may_unpaid_rent4, name='table_may_unpaid_rent4'),
    path('june_unpaid_rent4/', branch4.june_unpaid_rent4, name='june_unpaid_rent4'),
    path('table_june_unpaid_rent4/', branch4.table_june_unpaid_rent4, name='table_june_unpaid_rent4'),
    path('july_unpaid_rent4/', branch4.july_unpaid_rent4, name='july_unpaid_rent4'),
    path('table_july_unpaid_rent4',branch4.table_july_unpaid_rent4,name='table_july_unpaid_rent4'),
    path('aug_unpaid_rent4/', branch4.aug_unpaid_rent4, name='aug_unpaid_rent4'),
    path('table_aug_unpaid_rent4/',branch4.table_aug_unpaid_rent4,name='table_aug_unpaid_rent4'),

    path('sept_unpaid_rent4/', branch4.sept_unpaid_rent4, name='sept_unpaid_rent4'),
    path('table_sept_unpaid_rent4/', branch4.table_sept_unpaid_rent4, name='table_sept_unpaid_rent4'),
    path('oct_unpaid_rent4/', branch4.oct_unpaid_rent4, name='oct_unpaid_rent4'),
    path('table_oct_unpaid_rent4/', branch4.table_oct_unpaid_rent4, name='table_oct_unpaid_rent4'),
    path('nov_unpaid_rent4/', branch4.nov_unpaid_rent4, name='nov_unpaid_rent4'),
    path('table_nov_unpaid_rent4/', branch4.table_nov_unpaid_rent4, name='table_nov_unpaid_rent4'),
    path('dec_unpaid_rent4/', branch4.dec_unpaid_rent4, name='dec_unpaid_rent4'),
    path('table_dec_unpaid_rent4/', branch4.table_dec_unpaid_rent4, name='table_dec_unpaid_rent4'),



    path('details_of_unpaid_guests4/<id>',branch4.details_of_unpaid_guests4,name='details_of_unpaid_guests4'),

#unpaid rent end here

#paid rent start here
    path('paid_rent_choose_months4/',branch4.paid_rent_choose_months4,name='paid_rent_choose_months4'),
    path('partially_paid_guest_choose_months4/', reports4.partially_paid_guest_choose_months4,name='partially_paid_guest_choose_months4'),

    path('jan_paid_rent4/', branch4.jan_paid_rent4, name='jan_paid_rent4'),
    path('feb_paid_rent4/', branch4.feb_paid_rent4, name='feb_paid_rent4'),
    path('mar_paid_rent4/', branch4.mar_paid_rent4, name='mar_paid_rent4'),

    path('april_paid_rent4/', branch4.april_paid_rent4, name='april_paid_rent4'),
    path('may_paid_rent4/', branch4.may_paid_rent4, name='may_paid_rent4'),
    path('table_may_paid_rent4/', branch4.table_may_paid_rent4, name='table_may_paid_rent4'),
    path('may_full_paid_guest4/', reports4.may_full_paid_guest4, name='may_full_paid_guest4'),
    path('may_partially_paid_guest4/', reports4.may_partially_paid_guest4, name='may_partially_paid_guest4'),
    path('table_may_partially_paid_guest4/', reports4.table_may_partially_paid_guest4,name='table_may_partially_paid_guest4'),
    path('june_paid_rent4/', branch4.june_paid_rent4, name='june_paid_rent4'),
    path('table_june_paid_rent4/', branch4.table_june_paid_rent4, name='table_june_paid_rent4'),
    path('june_full_paid_guest4/', reports4.june_full_paid_guest4, name='june_full_paid_guest4'),
    path('june_partially_paid_guest4/', reports4.june_partially_paid_guest4, name='june_partially_paid_guest4'),
    path('table_june_partially_paid_guest4/', reports4.table_june_partially_paid_guest4,name='table_june_partially_paid_guest4'),

    path('july_paid_rent4/', branch4.july_paid_rent4, name='july_paid_rent4'),
    path('table_july_paid_rent4/', branch4.table_july_paid_rent4, name='table_july_paid_rent4'),
    path('july_full_paid_guest4/', reports4.july_full_paid_guest4, name='july_full_paid_guest4'),
    path('july_partially_paid_guest4/', reports4.july_partially_paid_guest4, name='july_partially_paid_guest4'),
    path('table_july_partially_paid_guest4/', reports4.table_july_partially_paid_guest4,name='table_july_partially_paid_guest4'),

    path('aug_paid_rent4/', branch4.aug_paid_rent4, name='aug_paid_rent4'),
    path('sept_paid_rent4/', branch4.sept_paid_rent4, name='sept_paid_rent4'),

    path('oct_paid_rent4/', branch4.oct_paid_rent4, name='oct_paid_rent4'),
    path('nov_paid_rent4/', branch4.nov_paid_rent4, name='nov_paid_rent4'),
    path('dec_paid_rent4/', branch4.dec_paid_rent4, name='dec_paid_rent4'),

    path('details_of_paid_guests4/<id>',branch4.details_of_paid_guests4,name='details_of_paid_guests4'),
    path('full_paid_guest4/', reports4.full_paid_guest4, name='full_paid_guest4'),

#paid rent end here

#*********reports end here

##################################
#VACATE GUEST DETAILS START HERE
################################

    path('viewall_vacate_guest4/',branch4.viewall_vacate_guest4,name='viewall_vacate_guest4'),
    path('details_of_vacate_guest4/<id>',branch4.details_of_vacate_guest4,name='details_of_vacate_guest4'),

#********vacate guest payments start here**********

    path('jan_manke_payments_vacate4/<id>', branch4.jan_manke_payments_vacate4, name='jan_manke_payments_vacate4'),
    path('feb_manke_payments_vacate4/<id>', branch4.feb_manke_payments_vacate4, name='feb_manke_payments_vacate4'),
    path('march_manke_payments_vacate4/<id>', branch4.march_manke_payments_vacate4, name='march_manke_payments_vacate4'),
    path('april_make_payments_vacate4/<id>', branch4.april_make_payments_vacate4, name='april_make_payments_vacate4'),

    path('may_make_payments_vacate4/<id>', branch4.may_make_payments_vacate4, name='may_make_payments_vacate4'),
    path('june_make_payments_vacate4/<id>', branch4.june_make_payments_vacate4, name='june_make_payments_vacate4'),
    path('july_make_payments_vacate4/<id>', branch4.july_make_payments_vacate4, name='july_make_payments_vacate4'),
    path('aug_make_payments_vacate4/<id>', branch4.aug_make_payments_vacate4, name='aug_make_payments_vacate4'),

    path('sept_make_payments_vacate4/<id>', branch4.sept_make_payments_vacate4, name='sept_make_payments_vacate4'),
    path('oct_make_payments_vacate4/<id>', branch4.oct_make_payments_vacate4, name='oct_make_payments_vacate4'),
    path('nov_make_payments_vacate4/<id>', branch4.nov_make_payments_vacate4, name='nov_make_payments_vacate4'),
    path('dec_make_payments_vacate4/<id>', branch4.dec_make_payments_vacate4, name='dec_make_payments_vacate4'),

#********vacate guest payments end here**********

##################################
#VACATE GUEST DETAILS END HERE
################################



##################################
#PRINT OUTS START HERE
################################

    path('detail_guest_general4/',branch4.detail_guest_general4,name='detail_guest_general4'),

    path('jan_print4/',branch4.jan_print4,name='jan_print4'),
    path('feb_print4/',branch4.feb_print4,name='feb_print4'),
    path('march_print4/',branch4.march_print4,name='march_print4'),
    path('april_print4/',branch4.april_print4,name='april_print4'),

    path('may_print4/',branch4.may_print4,name='may_print4'),
    path('june_print4/',branch4.june_print4,name='june_print4'),
    path('july_print4/', branch4.july_print4, name='july_print4'),
    path('aug_print4/', branch4.aug_print4, name='aug_print4'),

    path('sept_print4/', branch4.sept_print4, name='sept_print4'),
    path('oct_print4/', branch4.oct_print4, name='oct_print4'),
    path('nov_print4/', branch4.nov_print4, name='nov_print4'),
    path('dec_print4/', branch4.dec_print4, name='dec_print4'),

##################################
#PRINT OUTS END HERE
################################

    path('jan_close4/', branch4.jan_close4, name='jan_close4'),
    path('jan_close_decision_page4/', branch4.jan_close_decision_page4, name='jan_close_decision_page4'),
    path('feb_close/', branch4.feb_close4, name='feb_close4'),
    path('feb_close_decision_page4/', branch4.feb_close_decision_page4, name='feb_close_decision_page4'),
    path('mar_close4/', branch4.mar_close4, name='mar_close4'),
    path('mar_close_decision_page/', branch4.mar_close_decision_page4, name='mar_close_decision_page4'),
    path('apr_close4/', branch4.apr_close4, name='apr_close4'),
    path('apr_close_decision_page4/', branch4.apr_close_decision_page4, name='apr_close_decision_page4'),

    path('may_close4/', branch4.may_close4, name='may_close4'),
    path('may_close_decision_page4/', branch4.may_close_decision_page4, name='may_close_decision_page4'),
    path('jun_close4/', branch4.jun_close4, name='jun_close4'),
    path('jun_close_decision_page4/', branch4.jun_close_decision_page4, name='jun_close_decision_page4'),
    path('jul_close4/', branch4.jul_close4, name='jul_close4'),
    path('jul_close_decision_page4/', branch4.jul_close_decision_page4, name='jul_close_decision_page4'),
    path('aug_close4/', branch4.aug_close4, name='aug_close4'),
    path('aug_close_decision_page4/', branch4.aug_close_decision_page4, name='aug_close_decision_page4'),

    path('sep_close4/', branch4.sep_close4, name='sep_close4'),
    path('sep_close_decision_page4/', branch4.sep_close_decision_page4, name='sep_close_decision_page4'),
    path('oct_close4/', branch4.oct_close4, name='oct_close4'),
    path('oct_close_decision_page4/', branch4.oct_close_decision_page4, name='oct_close_decision_page4'),
    path('nov_close4/', branch4.nov_close4, name='nov_close4'),
    path('nov_close_decision_page4/', branch4.nov_close_decision_page4, name='nov_close_decision_page4'),


    path('test/',branch4.pysql,name='pysql'),
    path('d4/', branch4.dynamic, name='dynamic'),


########################################
# DETAILED REPORT START HERE
###########################

    path('detailed_report_choose_months4/',reports4.detailed_report_choose_months4,name='detailed_report_choose_months4'),

    path('jan_details_live4/', reports4.jan_details_live4, name='jan_details_live4'),
    path('jan_print_live4/', reports4.jan_print_live4, name='jan_print_live4'),
    path('feb_details_live4/', reports4.feb_details_live4, name='feb_details_live4'),
    path('feb_print_live4/', reports4.feb_print_live4, name='feb_print_live4'),
    path('march_details_live4/', reports4.march_details_live4, name='march_details_live4'),
    path('march_print_live4/', reports4.march_print_live4, name='march_print_live4'),

    path('april_details_live4/', reports4.april_details_live4, name='april_details_live4'),
    path('april_print_live4/', reports4.april_print_live4, name='april_print_live4'),
    path('may_details_live4/', reports4.may_details_live4, name='may_details_live4'),
    path('may_print_live4/', reports4.may_print_live4, name='may_print_live4'),
    path('june_details_live4/',reports4.june_details_live4,name='june_details_live4'),
    path('june_print_live4/', reports4.june_print_live4, name='june_print_live4'),

    path('july_details_live4/', reports4.july_details_live4, name='july_details_live4'),
    path('july_print_live4/', reports4.july_print_live4, name='july_print_live4'),
    path('auguest_details_live4/', reports4.auguest_details_live4, name='auguest_details_live4'),
    path('auguest_print_live4/', reports4.auguest_print_live4, name='auguest_print_live4'),
    path('sept_details_live4/', reports4.sept_details_live4, name='sept_details_live4'),
    path('sept_print_live4/', reports4.sept_print_live4, name='sept_print_live4'),

    path('october_details_live4/', reports4.october_details_live4, name='october_details_live4'),
    path('october_print_live4/', reports4.october_print_live4, name='october_print_live4'),
    path('nov_details_live4/', reports4.nov_details_live4, name='nov_details_live4'),
    path('nov_print_live4/', reports4.nov_print_live4, name='nov_print_live4'),
    path('dec_details_live4/', reports4.dec_details_live4, name='dec_details_live4'),
    path('dec_print_live4/', reports4.dec_print_live4, name='dec_print_live4'),

########################################
#  DETAILED REPORT END HERE
###########################



    path('viewall_vaccant_room4/',reports4.viewall_vaccant_room4,name='viewall_vaccant_room4'),

########################################
# DUE AMT MANAGEMENT START HERE
###########################

    path('view_all_due_amt4/', branch4.view_all_due_amt4, name='view_all_due_amt4'),
    path('due_amt_mgt_choose_months4/', branch4.due_amt_mgt_choose_months4, name='due_amt_mgt_choose_months4'),

    path('view_may_account_details4/',branch4.view_may_account_details4,name='view_may_account_details4'),
    path('may_account_mgt4/<id>', branch4.may_account_mgt4, name='may_account_mgt4'),

    path('view_june_account_details4/', branch4.view_june_account_details4, name='view_june_account_details4'),
    path('june_account_mgt4/<id>',branch4.june_account_mgt4,name='june_account_mgt4'),
    path('view_july_account_details4/', branch4.view_july_account_details4, name='view_july_account_details4'),
    path('july_account_mgt4/<id>',branch4.july_account_mgt4,name='july_account_mgt4'),

########################################
# DUE AMT MANAGEMENT END HERE
###########################

    path('manage_bed4/', branch4.manage_bed4, name='manage_bed4'),
    path('manage_new_guest4/', branch4.manage_new_guest4, name='manage_new_guest4'),
    path('manage_update_new_guest4/<id>', branch4.manage_update_new_guest4, name='manage_update_new_guest4'),
    path('manage_update_beds4/<id>', branch4.manage_update_beds4, name='manage_update_beds4'),


########################################
# DASHBOARD REPORTS START HERE
###########################

    path('monthly_collection_details4/', admin_dashboard_calculations_br4.monthly_collection_details4, name='monthly_collection_details4'),

########################################
# DASHBOARD REPORTS END HERE
###########################


]