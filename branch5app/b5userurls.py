#b5userurls
from django.contrib import admin
from django.urls import path, include

from . import admin_branch5
from . import branch5
from . import reports5

urlpatterns = [
    path('branch1_dashboard5/', branch5.branch1_dashboard5, name='branch1_dashboard5'),

#**room creation start here
    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi5/',admin_branch5.branch1_room_create_regi5,name='branch1_room_create_regi5'),
    path('view_all_room5/',admin_branch5.view_all_room5,name='view_all_room5'),
    path('delete_room5/<id>',admin_branch5.delete_room5,name='delete_room5'),

    path('branch1_room_create5/',admin_branch5.branch1_room_create5,name='branch1_room_create5'),

#**room creation end here

#bed creation start here

    path('pg1_bed_create_regi5/', admin_branch5.pg1_bed_create_regi5, name='pg1_bed_create_regi5'),
    path('pg1_view_all_beds5/', admin_branch5.pg1_view_all_beds5, name='pg1_view_all_beds5'),
    path('delete_bed5/<id>', admin_branch5.delete_bed5, name='delete_bed5'),

    path('pg1_bed_create5/', admin_branch5.pg1_bed_create5, name='pg1_bed_create5'),

    path('single_pg1_bed_create_regi5/',admin_branch5.single_pg1_bed_create_regi5,name='single_pg1_bed_create_regi5'),
    path('update_bed_basic_details5/<id>',admin_branch5.update_bed_basic_details5, name='update_bed_basic_details5'),

#bed creation end here


#guest
    path('br1_admit_guest5/<id>',branch5.br1_admit_guest5,name='br1_admit_guest5'),
    path('view_all_new_guest5/',branch5.view_all_new_guest5,name='view_all_new_guest5'),
    path('update_br1_admit_guest5/<id>',branch5.update_br1_admit_guest5,name='update_br1_admit_guest5'),
    path('vacate_br1_guest5/<id>',branch5.vacate_br1_guest5,name='vacate_br1_guest5'),
    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),

#guest end here


##################################
#_ADVANCE5 START HERE
################################


path('choose_months_advance5/',branch5.choose_months_advance5,name='choose_months_advance5'),

path('jan_advance5/', branch5.jan_advance5, name='jan_advance5'),
path('jan_make_payments_advance5/<id>', branch5.jan_make_payments_advance5,name='jan_make_payments_advance5'),
path('feb_advance5/', branch5.feb_advance5, name='feb_advance5'),
path('feb_make_payments_advance5/<id>', branch5.feb_make_payments_advance5,name='feb_make_payments_advance5'),
path('march_advance5/', branch5.march_advance5, name='march_advance5'),
path('march_make_payments_advance5/<id>', branch5.march_make_payments_advance5,name='march_make_payments_advance5'),
path('april_advance5/', branch5.april_advance5, name='april_advance5'),
path('april_make_payments_advance5/<id>', branch5.april_make_payments_advance5, name='april_make_payments_advance5'),

path('may_advance5/',branch5.may_advance5,name='may_advance5'),
path('may_make_payments_advance5/<id>', branch5.may_make_payments_advance5, name='may_make_payments_advance5'),
path('june_advance5/',branch5.june_advance5,name='june_advance5'),
path('june_make_payments_advance5/<id>', branch5.june_make_payments_advance5, name='june_make_payments_advance5'),
path('july_advance5/',branch5.july_advance5,name='july_advance5'),
path('july_make_payments_advance5/<id>', branch5.july_make_payments_advance5, name='july_make_payments_advance5'),
path('auguest_advance5/', branch5.auguest_advance5, name='auguest_advance5'),
path('auguest_make_payments_advance5/<id>', branch5.auguest_make_payments_advance5, name='auguest_make_payments_advance5'),

path('sept_advance5/', branch5.sept_advance5, name='sept_advance5'),
path('sept_make_payments_advance5/<id>', branch5.sept_make_payments_advance5,name='sept_make_payments_advance5'),
path('october_advance5/', branch5.october_advance5, name='october_advance5'),
path('october_make_payments_advance5/<id>', branch5.october_make_payments_advance5, name='october_make_payments_advance5'),
path('nov_advance5/', branch5.nov_advance5, name='nov_advance5'),
path('nov_make_payments_advance5/<id>', branch5.nov_make_payments_advance5,name='nov_make_payments_advance5'),
path('dec_advance5/', branch5.dec_advance5, name='dec_advance5'),
path('dec_make_payments_advance5/<id>', branch5.dec_make_payments_advance5, name='dec_make_payments_advance5'),



##################################
#_ADVANCE5 END HERE
################################



##################################
#PAYMENTS START HERE
################################

    path('choose_months5/',branch5.choose_months5,name='choose_months5'),

    path('jan5/',branch5.jan5,name='jan5'),
    path('jan_manke_payments5/<id>',branch5.jan_manke_payments5,name='jan_manke_payments5'),

    path('feb5/',branch5.feb5,name='feb5'),
    path('feb_manke_payments5/<id>',branch5.feb_manke_payments5,name='feb_manke_payments5'),

    path('march5/',branch5.march5,name='march5'),
    path('march_manke_payments5/<id>',branch5.march_manke_payments5,name='march_manke_payments5'),

    path('april5/',branch5.april5,name='april5'),
    path('april_make_payments5/<id>',branch5.april_make_payments5,name='april_make_payments5'),

    path('may5/',branch5.may5,name='may5'),
    path('may_make_payments5/<id>',branch5.may_make_payments5,name='may_make_payments5'),

    path('june5/',branch5.june5,name='june5'),
    path('june_make_payments5/<id>',branch5.june_make_payments5,name='june_make_payments5'),

    path('july5/',branch5.july5,name='july5'),
    path('july_make_payments5/<id>',branch5.july_make_payments5,name='july_make_payments5'),

    path('aug5/',branch5.aug5,name='aug5'),
    path('aug_make_payments5/<id>',branch5.aug_make_payments5,name='aug_make_payments5'),

    path('sept5/',branch5.sept5,name='sept5'),
    path('sept_make_payments5/<id>',branch5.sept_make_payments5,name='sept_make_payments5'),

    path('oct5/',branch5.oct5,name='oct5'),
    path('oct_make_payments5/<id>',branch5.oct_make_payments5,name='oct_make_payments5'),

    path('nov5/',branch5.nov5,name='nov5'),
    path('nov_make_payments5/<id>',branch5.nov_make_payments5,name='nov_make_payments5'),

    path('dec5/',branch5.dec5,name='dec5'),
    path('dec_make_payments5/<id>',branch5.dec_make_payments5,name='dec_make_payments5'),

##################################
#PAYMENTS END HERE
################################



#*********reports start here

#unpaid rent start here
    path('unpaid_rent_choose_months5/',branch5.unpaid_rent_choose_months5,name='unpaid_rent_choose_months5'),

    path('jan_unpaid_rent5/', branch5.jan_unpaid_rent5, name='jan_unpaid_rent5'),
    path('table_jan_unpaid_rent5/', branch5.table_jan_unpaid_rent5, name='table_jan_unpaid_rent5'),
    path('feb_unpaid_rent5/', branch5.feb_unpaid_rent5, name='feb_unpaid_rent5'),
    path('table_feb_unpaid_rent5/', branch5.table_feb_unpaid_rent5, name='table_feb_unpaid_rent5'),
    path('mar_unpaid_rent5/', branch5.mar_unpaid_rent5, name='mar_unpaid_rent5'),
    path('table_mar_unpaid_rent5/', branch5.table_mar_unpaid_rent5, name='table_mar_unpaid_rent5'),
    path('april_unpaid_rent5/', branch5.april_unpaid_rent5, name='april_unpaid_rent5'),
    path('table_april_unpaid_rent5/', branch5.table_april_unpaid_rent5, name='table_april_unpaid_rent5'),

    path('may_unpaid_rent5/', branch5.may_unpaid_rent5, name='may_unpaid_rent5'),
    path('table_may_unpaid_rent5/', branch5.table_may_unpaid_rent5, name='table_may_unpaid_rent5'),
    path('june_unpaid_rent5/', branch5.june_unpaid_rent5, name='june_unpaid_rent5'),
    path('table_june_unpaid_rent5/', branch5.table_june_unpaid_rent5, name='table_june_unpaid_rent5'),
    path('july_unpaid_rent5/', branch5.july_unpaid_rent5, name='july_unpaid_rent5'),
    path('table_july_unpaid_rent5',branch5.table_july_unpaid_rent5,name='table_july_unpaid_rent5'),
    path('aug_unpaid_rent5/', branch5.aug_unpaid_rent5, name='aug_unpaid_rent5'),
    path('table_aug_unpaid_rent5/',branch5.table_aug_unpaid_rent5,name='table_aug_unpaid_rent5'),

    path('sept_unpaid_rent5/', branch5.sept_unpaid_rent5, name='sept_unpaid_rent5'),
    path('table_sept_unpaid_rent5/', branch5.table_sept_unpaid_rent5, name='table_sept_unpaid_rent5'),
    path('oct_unpaid_rent5/', branch5.oct_unpaid_rent5, name='oct_unpaid_rent5'),
    path('table_oct_unpaid_rent5/', branch5.table_oct_unpaid_rent5, name='table_oct_unpaid_rent5'),
    path('nov_unpaid_rent5/', branch5.nov_unpaid_rent5, name='nov_unpaid_rent5'),
    path('dec_unpaid_rent5/', branch5.dec_unpaid_rent5, name='dec_unpaid_rent5'),
    path('table_dec_unpaid_rent5/', branch5.table_dec_unpaid_rent5, name='table_dec_unpaid_rent5'),

    path('details_of_unpaid_guests5/<id>',branch5.details_of_unpaid_guests5,name='details_of_unpaid_guests5'),

#unpaid rent end here

#paid rent start here
    path('paid_rent_choose_months5/',branch5.paid_rent_choose_months5,name='paid_rent_choose_months5'),
    path('partially_paid_guest_choose_months5/',reports5.partially_paid_guest_choose_months5,name='partially_paid_guest_choose_months5'),

    path('jan_paid_rent5/', branch5.jan_paid_rent5, name='jan_paid_rent5'),
    path('feb_paid_rent5/', branch5.feb_paid_rent5, name='feb_paid_rent5'),
    path('mar_paid_rent5/', branch5.mar_paid_rent5, name='mar_paid_rent5'),

    path('april_paid_rent5/', branch5.april_paid_rent5, name='april_paid_rent5'),
    path('may_paid_rent5/', branch5.may_paid_rent5, name='may_paid_rent5'),
    path('table_may_paid_rent5/', branch5.table_may_paid_rent5, name='table_may_paid_rent5'),
    path('may_full_paid_guest5/', reports5.may_full_paid_guest5, name='may_full_paid_guest5'),
    path('may_partially_paid_guest5/', reports5.may_partially_paid_guest5, name='may_partially_paid_guest5'),
    path('table_may_partially_paid_guest5/', reports5.table_may_partially_paid_guest5, name='table_may_partially_paid_guest5'),
    path('june_paid_rent5/', branch5.june_paid_rent5, name='june_paid_rent5'),
    path('table_june_paid_rent5/', branch5.table_june_paid_rent5, name='table_june_paid_rent5'),
    path('june_full_paid_guest5/', reports5.june_full_paid_guest5, name='june_full_paid_guest5'),
    path('june_partially_paid_guest5/', reports5.june_partially_paid_guest5, name='june_partially_paid_guest5'),
    path('table_june_partially_paid_guest5/', reports5.table_june_partially_paid_guest5, name='table_june_partially_paid_guest5'),

    path('july_paid_rent5/', branch5.july_paid_rent5, name='july_paid_rent5'),
    path('table_july_paid_rent5/', branch5.table_july_paid_rent5, name='table_july_paid_rent5'),
    path('july_full_paid_guest5/', reports5.july_full_paid_guest5, name='july_full_paid_guest5'),
    path('july_partially_paid_guest5/', reports5.july_partially_paid_guest5, name='july_partially_paid_guest5'),
    path('table_july_partially_paid_guest5/', reports5.table_july_partially_paid_guest5, name='table_july_partially_paid_guest5'),

    path('aug_paid_rent5/', branch5.aug_paid_rent5, name='aug_paid_rent5'),
    path('sept_paid_rent5/', branch5.sept_paid_rent5, name='sept_paid_rent5'),

    path('oct_paid_rent5/', branch5.oct_paid_rent5, name='oct_paid_rent5'),
    path('nov_paid_rent5/', branch5.nov_paid_rent5, name='nov_paid_rent5'),
    path('dec_paid_rent5/', branch5.dec_paid_rent5, name='dec_paid_rent5'),

    path('details_of_paid_guests5/<id>',branch5.details_of_paid_guests5,name='details_of_paid_guests5'),
    path('full_paid_guest5/',reports5.full_paid_guest5,name='full_paid_guest5'),

#paid rent end here

#*********reports end here


##################################
#VACATE GUEST DETAILS START HERE
################################

    path('viewall_vacate_guest5/',branch5.viewall_vacate_guest5,name='viewall_vacate_guest5'),
    path('details_of_vacate_guest5/<id>',branch5.details_of_vacate_guest5,name='details_of_vacate_guest5'),

#********vacate guest payments start here**********

    path('jan_manke_payments_vacate5/<id>', branch5.jan_manke_payments_vacate5, name='jan_manke_payments_vacate5'),
    path('feb_manke_payments_vacate5/<id>', branch5.feb_manke_payments_vacate5, name='feb_manke_payments_vacate5'),
    path('march_manke_payments_vacate5/<id>', branch5.march_manke_payments_vacate5, name='march_manke_payments_vacate5'),
    path('april_make_payments_vacate5/<id>', branch5.april_make_payments_vacate5, name='april_make_payments_vacate5'),

    path('may_make_payments_vacate5/<id>', branch5.may_make_payments_vacate5, name='may_make_payments_vacate5'),
    path('june_make_payments_vacate5/<id>', branch5.june_make_payments_vacate5, name='june_make_payments_vacate5'),
    path('july_make_payments_vacate5/<id>', branch5.july_make_payments_vacate5, name='july_make_payments_vacate5'),
    path('aug_make_payments_vacate5/<id>', branch5.aug_make_payments_vacate5, name='aug_make_payments_vacate5'),

    path('sept_make_payments_vacate5/<id>', branch5.sept_make_payments_vacate5, name='sept_make_payments_vacate5'),
    path('oct_make_payments_vacate5/<id>', branch5.oct_make_payments_vacate5, name='oct_make_payments_vacate5'),
    path('nov_make_payments_vacate5/<id>', branch5.nov_make_payments_vacate5, name='nov_make_payments_vacate5'),
    path('dec_make_payments_vacate5/<id>', branch5.dec_make_payments_vacate5, name='dec_make_payments_vacate5'),

#********vacate guest payments end here**********

##################################
#VACATE GUEST DETAILS END HERE
################################


##################################
#PRINT OUTS START HERE
################################

    path('detail_guest_general5/',branch5.detail_guest_general5,name='detail_guest_general5'),

    path('jan_print5/',branch5.jan_print5,name='jan_print5'),
    path('feb_print5/',branch5.feb_print5,name='feb_print5'),
    path('march_print5/',branch5.march_print5,name='march_print5'),
    path('april_print5/',branch5.april_print5,name='april_print5'),

    path('may_print5/',branch5.may_print5,name='may_print5'),
    path('june_print5/',branch5.june_print5,name='june_print5'),
    path('july_print5/', branch5.july_print5, name='july_print5'),
    path('aug_print5/', branch5.aug_print5, name='aug_print5'),

    path('sept_print5/', branch5.sept_print5, name='sept_print5'),
    path('oct_print5/', branch5.oct_print5, name='oct_print5'),
    path('nov_print5/', branch5.nov_print5, name='nov_print5'),
    path('dec_print5/', branch5.dec_print5, name='dec_print5'),

##################################
#PRINT OUTS END HERE
################################

    path('jan_close5/', branch5.jan_close5, name='jan_close5'),
    path('jan_close_decision_page5/', branch5.jan_close_decision_page5, name='jan_close_decision_page5'),
    path('feb_close/', branch5.feb_close5, name='feb_close5'),
    path('feb_close_decision_page5/', branch5.feb_close_decision_page5, name='feb_close_decision_page5'),
    path('mar_close5/', branch5.mar_close5, name='mar_close5'),
    path('mar_close_decision_page/', branch5.mar_close_decision_page5, name='mar_close_decision_page5'),
    path('apr_close5/', branch5.apr_close5, name='apr_close5'),
    path('apr_close_decision_page5/', branch5.apr_close_decision_page5, name='apr_close_decision_page5'),

    path('may_close5/', branch5.may_close5, name='may_close5'),
    path('may_close_decision_page5/', branch5.may_close_decision_page5, name='may_close_decision_page5'),
    path('jun_close5/', branch5.jun_close5, name='jun_close5'),
    path('jun_close_decision_page5/', branch5.jun_close_decision_page5, name='jun_close_decision_page5'),
    path('jul_close5/', branch5.jul_close5, name='jul_close5'),
    path('jul_close_decision_page5/', branch5.jul_close_decision_page5, name='jul_close_decision_page5'),
    path('aug_close5/', branch5.aug_close5, name='aug_close5'),
    path('aug_close_decision_page5/', branch5.aug_close_decision_page5, name='aug_close_decision_page5'),

    path('sep_close5/', branch5.sep_close5, name='sep_close5'),
    path('sep_close_decision_page5/', branch5.sep_close_decision_page5, name='sep_close_decision_page5'),
    path('oct_close5/', branch5.oct_close5, name='oct_close5'),
    path('oct_close_decision_page5/', branch5.oct_close_decision_page5, name='oct_close_decision_page5'),
    path('nov_close5/', branch5.nov_close5, name='nov_close5'),
    path('nov_close_decision_page5/', branch5.nov_close_decision_page5, name='nov_close_decision_page5'),

    path('detailed_report_choose_months5/',reports5.detailed_report_choose_months5,name='detailed_report_choose_months5'),
    path('may_print_live5/', reports5.may_print_live5, name='may_print_live5'),
    path('june_dtails_live5/',reports5.june_dtails_live5,name='june_dtails_live5'),
    path('june_print_live5/', reports5.june_print_live5, name='june_print_live5'),
    path('viewall_vaccant_room5/', reports5.viewall_vaccant_room5, name='viewall_vaccant_room5'),

    path('d5/', branch5.dynamic, name='dynamic'),

    path('manage_bed5/', branch5.manage_bed5, name='manage_bed5'),
    path('manage_new_guest5/', branch5.manage_new_guest5, name='manage_new_guest5'),
    path('manage_update_new_guest5/<id>', branch5.manage_update_new_guest5, name='manage_update_new_guest5'),
    path('manage_update_beds5/<id>', branch5.manage_update_beds5, name='manage_update_beds5'),

########################################
# DUE AMT MANAGEMENT START HERE
###########################

    path('view_all_due_amt5/', branch5.view_all_due_amt5, name='view_all_due_amt5'),
    path('due_amt_mgt_choose_months5/', branch5.due_amt_mgt_choose_months5, name='due_amt_mgt_choose_months5'),

    path('view_may_account_details5/',branch5.view_may_account_details5,name='view_may_account_details5'),
    path('may_account_mgt5/<id>', branch5.may_account_mgt5, name='may_account_mgt5'),

    path('view_june_account_details5/', branch5.view_june_account_details5, name='view_june_account_details5'),
    path('june_account_mgt5/<id>',branch5.june_account_mgt5,name='june_account_mgt5'),
    path('view_july_account_details5/', branch5.view_july_account_details5, name='view_july_account_details5'),
    path('july_account_mgt5/<id>',branch5.july_account_mgt5,name='july_account_mgt5'),

########################################
# DUE AMT MANAGEMENT END HERE
###########################

]
