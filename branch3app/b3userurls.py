from django.urls import path

from . import admin_branch3
from . import branch3
from . import reports3
from . import payment3
from . import admin_dashboard_calculations_br3


urlpatterns = [

    path('branch1_dashboard3/', branch3.branch1_dashboard3, name='branch1_dashboard3'),

#**room creation start here
    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi3/',admin_branch3.branch1_room_create_regi3,name='branch1_room_create_regi3'),
    path('view_all_room3/',admin_branch3.view_all_room3,name='view_all_room3'),
    path('delete_room3/<id>',admin_branch3.delete_room3,name='delete_room3'),

    path('branch1_room_create3/',admin_branch3.branch1_room_create3,name='branch1_room_create3'),

#**room creation end here

#bed creation start here

    path('pg1_bed_create_regi3/', admin_branch3.pg1_bed_create_regi3, name='pg1_bed_create_regi3'),
    path('pg1_view_all_beds3/', admin_branch3.pg1_view_all_beds3, name='pg1_view_all_beds3'),
    path('delete_bed3/<id>', admin_branch3.delete_bed3, name='delete_bed3'),

    path('pg1_bed_create3/', admin_branch3.pg1_bed_create3, name='pg1_bed_create3'),

    path('single_pg1_bed_create_regi3/', admin_branch3.single_pg1_bed_create_regi3, name='single_pg1_bed_create_regi3'),
    path('update_bed_basic_details3/<id>', admin_branch3.update_bed_basic_details3, name='update_bed_basic_details3'),

    #bed creation end here

#guest
    path('br1_admit_guest3/<id>',branch3.br1_admit_guest3,name='br1_admit_guest3'),
    path('view_all_new_guest3/',branch3.view_all_new_guest3,name='view_all_new_guest3'),
    path('update_br1_admit_guest3/<id>',branch3.update_br1_admit_guest3,name='update_br1_admit_guest3'),
    path('vacate_br1_guest3/<id>',branch3.vacate_br1_guest3,name='vacate_br1_guest3'),
    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),
#guest end here



##################################
#_ADVANCE3 START HERE
################################


path('choose_months_advance3/',branch3.choose_months_advance3,name='choose_months_advance3'),

path('jan_advance3/', branch3.jan_advance3, name='jan_advance3'),
path('jan_make_payments_advance3/<id>', branch3.jan_make_payments_advance3,name='jan_make_payments_advance3'),
path('feb_advance3/', branch3.feb_advance3, name='feb_advance3'),
path('feb_make_payments_advance3/<id>', branch3.feb_make_payments_advance3,name='feb_make_payments_advance3'),
path('march_advance3/', branch3.march_advance3, name='march_advance3'),
path('march_make_payments_advance3/<id>', branch3.march_make_payments_advance3,name='march_make_payments_advance3'),
path('april_advance3/', branch3.april_advance3, name='april_advance3'),
path('april_make_payments_advance3/<id>', branch3.april_make_payments_advance3, name='april_make_payments_advance3'),

path('may_advance3/',branch3.may_advance3,name='may_advance3'),
path('may_make_payments_advance3/<id>', branch3.may_make_payments_advance3, name='may_make_payments_advance3'),
path('june_advance3/',branch3.june_advance3,name='june_advance3'),
path('june_make_payments_advance3/<id>', branch3.june_make_payments_advance3, name='june_make_payments_advance3'),
path('july_advance3/',branch3.july_advance3,name='july_advance3'),
path('july_make_payments_advance3/<id>', branch3.july_make_payments_advance3, name='july_make_payments_advance3'),
path('auguest_advance3/', branch3.auguest_advance3, name='auguest_advance3'),
path('auguest_make_payments_advance3/<id>', branch3.auguest_make_payments_advance3, name='auguest_make_payments_advance3'),

path('sept_advance3/', branch3.sept_advance3, name='sept_advance3'),
path('sept_make_payments_advance3/<id>', branch3.sept_make_payments_advance3,name='sept_make_payments_advance3'),
path('october_advance3/', branch3.october_advance3, name='october_advance3'),
path('october_make_payments_advance3/<id>', branch3.october_make_payments_advance3, name='october_make_payments_advance3'),
path('nov_advance3/', branch3.nov_advance3, name='nov_advance3'),
path('nov_make_payments_advance3/<id>', branch3.nov_make_payments_advance3,name='nov_make_payments_advance3'),
path('dec_advance3/', branch3.dec_advance3, name='dec_advance3'),
path('dec_make_payments_advance3/<id>', branch3.dec_make_payments_advance3, name='dec_make_payments_advance3'),



    ##################################
#_ADVANCE3 END HERE
################################




##################################
#PAYMENTS START HERE
################################

    path('choose_months3/',branch3.choose_months3,name='choose_months3'),

    path('jan3/',branch3.jan3,name='jan3'),
    path('jan_manke_payments3/<id>',branch3.jan_manke_payments3,name='jan_manke_payments3'),

    path('feb3/',branch3.feb3,name='feb3'),
    path('feb_manke_payments3/<id>',branch3.feb_manke_payments3,name='feb_manke_payments3'),

    path('march3/',branch3.march3,name='march3'),
    path('march_manke_payments3/<id>',branch3.march_manke_payments3,name='march_manke_payments3'),

    path('april3/',branch3.april3,name='april3'),
    path('april_make_payments3/<id>',branch3.april_make_payments3,name='april_make_payments3'),

    path('may3/',branch3.may3,name='may3'),
    path('may_make_payments3/<id>',branch3.may_make_payments3,name='may_make_payments3'),

    path('june3/',branch3.june3,name='june3'),
    path('june_make_payments3/<id>',branch3.june_make_payments3,name='june_make_payments3'),

    path('july3/',branch3.july3,name='july3'),
    path('july_make_payments3/<id>',branch3.july_make_payments3,name='july_make_payments3'),

    path('aug3/',branch3.aug3,name='aug3'),
    path('aug_make_payments3/<id>',branch3.aug_make_payments3,name='aug_make_payments3'),

    path('sept3/',branch3.sept3,name='sept3'),
    path('sept_make_payments3/<id>',branch3.sept_make_payments3,name='sept_make_payments3'),

    path('oct3/',branch3.oct3,name='oct3'),
    path('oct_make_payments3/<id>',branch3.oct_make_payments3,name='oct_make_payments3'),

    path('nov3/',branch3.nov3,name='nov3'),
    path('nov_make_payments3/<id>',branch3.nov_make_payments3,name='nov_make_payments3'),

    path('dec3/',branch3.dec3,name='dec3'),
    path('dec_make_payments3/<id>',branch3.dec_make_payments3,name='dec_make_payments3'),

##################################
#PAYMENTS END HERE
################################



##################################
#MONTHLY MANAGEMENT PAYMENTS START HERE
################################

    path('choose_user3/', payment3.choose_user3, name='choose_user3'),
    path('payment_user_details3/<id>', payment3.payment_user_details3, name='payment_user_details3'),

    path('monthly_jan_make_payments3/<id>', payment3.monthly_jan_make_payments3, name='monthly_jan_make_payments3'),
    path('monthly_feb_make_payments3/<id>', payment3.monthly_feb_make_payments3, name='monthly_feb_make_payments3'),
    path('monthly_march_make_payments3/<id>', payment3.monthly_march_make_payments3, name='monthly_march_make_payments3'),
    path('monthly_april_make_payments3/<id>', payment3.monthly_april_make_payments3, name='monthly_april_make_payments3'),
    path('monthly_may_make_payments3/<id>', payment3.monthly_may_make_payments3, name='monthly_may_make_payments3'),
    path('monthly_june_make_payments3/<id>', payment3.monthly_june_make_payments3, name='monthly_june_make_payments3'),

    path('monthly_july_make_payments3/<id>', payment3.monthly_july_make_payments3, name='monthly_july_make_payments3'),
    path('monthly_aug_make_payments3/<id>', payment3.monthly_aug_make_payments3, name='monthly_aug_make_payments3'),
    path('monthly_sept_make_payments3/<id>', payment3.monthly_sept_make_payments3, name='monthly_sept_make_payments3'),
    path('monthly_oct_make_payments3/<id>', payment3.monthly_oct_make_payments3, name='monthly_oct_make_payments3'),
    path('monthly_nov_make_payments3/<id>', payment3.monthly_nov_make_payments3, name='monthly_nov_make_payments3'),
    path('monthly_dec_make_payments3/<id>', payment3.monthly_dec_make_payments3, name='monthly_dec_make_payments3'),

##################################
#MONTHLY MANAGEMENT PAYMENTS END HERE
################################





#*********reports start here



#unpaid rent start here
    path('unpaid_rent_choose_months3/',branch3.unpaid_rent_choose_months3,name='unpaid_rent_choose_months3'),

    path('jan_unpaid_rent3/', branch3.jan_unpaid_rent3, name='jan_unpaid_rent3'),
    path('table_jan_unpaid_rent3/', branch3.table_jan_unpaid_rent3, name='table_jan_unpaid_rent3'),
    path('feb_unpaid_rent3/', branch3.feb_unpaid_rent3, name='feb_unpaid_rent3'),
    path('table_feb_unpaid_rent3/', branch3.table_feb_unpaid_rent3, name='table_feb_unpaid_rent3'),
    path('mar_unpaid_rent3/', branch3.mar_unpaid_rent3, name='mar_unpaid_rent3'),
    path('table_mar_unpaid_rent3/', branch3.table_mar_unpaid_rent3, name='table_mar_unpaid_rent3'),
    path('april_unpaid_rent3/', branch3.april_unpaid_rent3, name='april_unpaid_rent3'),
    path('table_april_unpaid_rent3/', branch3.table_april_unpaid_rent3, name='table_april_unpaid_rent3'),

    path('may_unpaid_rent3/', branch3.may_unpaid_rent3, name='may_unpaid_rent3'),
    path('table_may_unpaid_rent3/', branch3.table_may_unpaid_rent3, name='table_may_unpaid_rent3'),
    path('june_unpaid_rent3/', branch3.june_unpaid_rent3, name='june_unpaid_rent3'),
    path('table_june_unpaid_rent3/', branch3.table_june_unpaid_rent3, name='table_june_unpaid_rent3'),
    path('july_unpaid_rent3/', branch3.july_unpaid_rent3, name='july_unpaid_rent3'),
    path('table_july_unpaid_rent3',branch3.table_july_unpaid_rent3,name='table_july_unpaid_rent3'),
    path('aug_unpaid_rent3/', branch3.aug_unpaid_rent3, name='aug_unpaid_rent3'),
    path('table_aug_unpaid_rent3/',branch3.table_aug_unpaid_rent3,name='table_aug_unpaid_rent3'),

    path('sept_unpaid_rent3/', branch3.sept_unpaid_rent3, name='sept_unpaid_rent3'),
    path('table_sept_unpaid_rent3/', branch3.table_sept_unpaid_rent3, name='table_sept_unpaid_rent3'),
    path('oct_unpaid_rent3/', branch3.oct_unpaid_rent3, name='oct_unpaid_rent3'),
    path('table_oct_unpaid_rent3/', branch3.table_oct_unpaid_rent3, name='table_oct_unpaid_rent3'),
    path('nov_unpaid_rent3/', branch3.nov_unpaid_rent3, name='nov_unpaid_rent3'),
    path('dec_unpaid_rent3/', branch3.dec_unpaid_rent3, name='dec_unpaid_rent3'),
    path('table_dec_unpaid_rent3/', branch3.table_dec_unpaid_rent3, name='table_dec_unpaid_rent3'),

    path('details_of_unpaid_guests3/<id>',branch3.details_of_unpaid_guests3,name='details_of_unpaid_guests3'),

#unpaid rent end here

#paid rent start here
    path('paid_rent_choose_months3/',branch3.paid_rent_choose_months3,name='paid_rent_choose_months3'),
    path('partially_paid_guest_choose_months3/',reports3.partially_paid_guest_choose_months3,name='partially_paid_guest_choose_months3'),

    path('jan_paid_rent3/', branch3.jan_paid_rent3, name='jan_paid_rent3'),
    path('feb_paid_rent3/', branch3.feb_paid_rent3, name='feb_paid_rent3'),
    path('mar_paid_rent3/', branch3.mar_paid_rent3, name='mar_paid_rent3'),

    path('april_paid_rent3/', branch3.april_paid_rent3, name='april_paid_rent3'),
    path('may_paid_rent3/', branch3.may_paid_rent3, name='may_paid_rent3'),
    path('table_may_paid_rent3/', branch3.table_may_paid_rent3, name='table_may_paid_rent3'),
    path('may_full_paid_guest3/', reports3.may_full_paid_guest3, name='may_full_paid_guest3'),
    path('may_partially_paid_guest3/', reports3.may_partially_paid_guest3, name='may_partially_paid_guest3'),
    path('table_may_partially_paid_guest3/', reports3.table_may_partially_paid_guest3, name='table_may_partially_paid_guest3'),
    path('june_paid_rent3/', branch3.june_paid_rent3, name='june_paid_rent3'),
    path('table_june_paid_rent3/', branch3.table_june_paid_rent3, name='table_june_paid_rent3'),
    path('june_full_paid_guest3/', reports3.june_full_paid_guest3, name='june_full_paid_guest3'),
    path('june_partially_paid_guest3/', reports3.june_partially_paid_guest3, name='june_partially_paid_guest3'),
    path('table_june_partially_paid_guest3/', reports3.table_june_partially_paid_guest3, name='table_june_partially_paid_guest3'),

    path('july_paid_rent3/', branch3.july_paid_rent3, name='july_paid_rent3'),
    path('table_july_paid_rent3/', branch3.table_july_paid_rent3, name='table_july_paid_rent3'),
    path('july_full_paid_guest3/', reports3.july_full_paid_guest3, name='july_full_paid_guest3'),
    path('july_partially_paid_guest3/', reports3.july_partially_paid_guest3, name='july_partially_paid_guest3'),
    path('table_july_partially_paid_guest3/', reports3.table_july_partially_paid_guest3, name='table_july_partially_paid_guest3'),

    path('aug_paid_rent3/', branch3.aug_paid_rent3, name='aug_paid_rent3'),
    path('sept_paid_rent3/', branch3.sept_paid_rent3, name='sept_paid_rent3'),

    path('oct_paid_rent3/', branch3.oct_paid_rent3, name='oct_paid_rent3'),
    path('nov_paid_rent3/', branch3.nov_paid_rent3, name='nov_paid_rent3'),
    path('dec_paid_rent3/', branch3.dec_paid_rent3, name='dec_paid_rent3'),

    path('details_of_paid_guests3/<id>',branch3.details_of_paid_guests3,name='details_of_paid_guests3'),
    path('full_paid_guest3/',reports3.full_paid_guest3,name='full_paid_guest3'),

#paid rent end here



#*********reports end here


##################################
#VACATE GUEST DETAILS START HERE
################################

    path('viewall_vacate_guest3/',branch3.viewall_vacate_guest3,name='viewall_vacate_guest3'),
    path('details_of_vacate_guest3/<id>',branch3.details_of_vacate_guest3,name='details_of_vacate_guest3'),

#********vacate guest payments start here**********

    path('jan_manke_payments_vacate3/<id>', branch3.jan_manke_payments_vacate3, name='jan_manke_payments_vacate3'),
    path('feb_manke_payments_vacate3/<id>', branch3.feb_manke_payments_vacate3, name='feb_manke_payments_vacate3'),
    path('march_manke_payments_vacate3/<id>', branch3.march_manke_payments_vacate3, name='march_manke_payments_vacate3'),
    path('april_make_payments_vacate3/<id>', branch3.april_make_payments_vacate3, name='april_make_payments_vacate3'),

    path('may_make_payments_vacate3/<id>', branch3.may_make_payments_vacate3, name='may_make_payments_vacate3'),
    path('june_make_payments_vacate3/<id>', branch3.june_make_payments_vacate3, name='june_make_payments_vacate3'),
    path('july_make_payments_vacate3/<id>', branch3.july_make_payments_vacate3, name='july_make_payments_vacate3'),
    path('aug_make_payments_vacate3/<id>', branch3.aug_make_payments_vacate3, name='aug_make_payments_vacate3'),

    path('sept_make_payments_vacate3/<id>', branch3.sept_make_payments_vacate3, name='sept_make_payments_vacate3'),
    path('oct_make_payments_vacate3/<id>', branch3.oct_make_payments_vacate3, name='oct_make_payments_vacate3'),
    path('nov_make_payments_vacate3/<id>', branch3.nov_make_payments_vacate3, name='nov_make_payments_vacate3'),
    path('dec_make_payments_vacate3/<id>', branch3.dec_make_payments_vacate3, name='dec_make_payments_vacate3'),

#********vacate guest payments end here**********

##################################
#VACATE GUEST DETAILS END HERE
################################



##################################
#PRINT OUTS START HERE
################################

    path('detail_guest_general3/',branch3.detail_guest_general3,name='detail_guest_general3'),

    path('jan_print3/',branch3.jan_print3,name='jan_print3'),
    path('feb_print3/',branch3.feb_print3,name='feb_print3'),
    path('march_print3/',branch3.march_print3,name='march_print3'),
    path('april_print3/',branch3.april_print3,name='april_print3'),

    path('may_print3/',branch3.may_print3,name='may_print3'),
    path('june_print3/',branch3.june_print3,name='june_print3'),
    path('july_print3/', branch3.july_print3, name='july_print3'),
    path('aug_print3/', branch3.aug_print3, name='aug_print3'),

    path('sept_print3/', branch3.sept_print3, name='sept_print3'),
    path('oct_print3/', branch3.oct_print3, name='oct_print3'),
    path('nov_print3/', branch3.nov_print3, name='nov_print3'),
    path('dec_print3/', branch3.dec_print3, name='dec_print3'),

##################################
#PRINT OUTS END HERE
################################

    path('jan_close3/', branch3.jan_close3, name='jan_close3'),
    path('jan_close_decision_page3/', branch3.jan_close_decision_page3, name='jan_close_decision_page3'),
    path('feb_close/', branch3.feb_close3, name='feb_close3'),
    path('feb_close_decision_page3/', branch3.feb_close_decision_page3, name='feb_close_decision_page3'),
    path('mar_close3/', branch3.mar_close3, name='mar_close3'),
    path('mar_close_decision_page/', branch3.mar_close_decision_page3, name='mar_close_decision_page3'),
    path('apr_close3/', branch3.apr_close3, name='apr_close3'),
    path('apr_close_decision_page3/', branch3.apr_close_decision_page3, name='apr_close_decision_page3'),

    path('may_close3/', branch3.may_close3, name='may_close3'),
    path('may_close_decision_page3/', branch3.may_close_decision_page3, name='may_close_decision_page3'),
    path('jun_close3/', branch3.jun_close3, name='jun_close3'),
    path('jun_close_decision_page3/', branch3.jun_close_decision_page3, name='jun_close_decision_page3'),
    path('jul_close3/', branch3.jul_close3, name='jul_close3'),
    path('jul_close_decision_page3/', branch3.jul_close_decision_page3, name='jul_close_decision_page3'),
    path('aug_close3/', branch3.aug_close3, name='aug_close3'),
    path('aug_close_decision_page3/', branch3.aug_close_decision_page3, name='aug_close_decision_page3'),

    path('sep_close3/', branch3.sep_close3, name='sep_close3'),
    path('sep_close_decision_page3/', branch3.sep_close_decision_page3, name='sep_close_decision_page3'),
    path('oct_close3/', branch3.oct_close3, name='oct_close3'),
    path('oct_close_decision_page3/', branch3.oct_close_decision_page3, name='oct_close_decision_page3'),
    path('nov_close3/', branch3.nov_close3, name='nov_close3'),
    path('nov_close_decision_page3/', branch3.nov_close_decision_page3, name='nov_close_decision_page3'),

    path('detailed_report_choose_months3/', reports3.detailed_report_choose_months3,name='detailed_report_choose_months3'),
    path('may_details_live3/',reports3.may_details_live3,name='may_details_live3'),
    path('may_print_live3/', reports3.may_print_live3, name='may_print_live3'),
    path('june_details_live3/', reports3.june_details_live3, name='june_details_live3'),
    path('june_print_live3/', reports3.june_print_live3, name='june_print_live3'),
    path('july_details_live3/', reports3.july_details_live3, name='july_details_live3'),
    path('july_print_live3/', reports3.july_print_live3, name='july_print_live3'),


    path('viewall_vaccant_room3/', reports3.viewall_vaccant_room3, name='viewall_vaccant_room3'),

    ########################################
# DUE AMT MANAGEMENT START HERE
###########################

    path('view_all_due_amt3/', branch3.view_all_due_amt3, name='view_all_due_amt3'),
    path('due_amt_mgt_choose_months3/', branch3.due_amt_mgt_choose_months3, name='due_amt_mgt_choose_months3'),

    path('view_may_account_details3/',branch3.view_may_account_details3,name='view_may_account_details3'),
    path('may_account_mgt3/<id>', branch3.may_account_mgt3, name='may_account_mgt3'),

    path('view_june_account_details3/', branch3.view_june_account_details3, name='view_june_account_details3'),
    path('june_account_mgt3/<id>',branch3.june_account_mgt3,name='june_account_mgt3'),
    path('view_july_account_details3/', branch3.view_july_account_details3, name='view_july_account_details3'),
    path('july_account_mgt3/<id>',branch3.july_account_mgt3,name='july_account_mgt3'),

########################################
# DUE AMT MANAGEMENT END HERE
###########################

########################################
# DASHBOARD REPORTS START HERE
###########################

    path('monthly_details_due3', admin_dashboard_calculations_br3.monthly_details_due3, name='monthly_details_due3'),
    path('monthly_collection_details3/', admin_dashboard_calculations_br3.monthly_collection_details3, name='monthly_collection_details3'),

########################################
# DASHBOARD REPORTS END HERE
###########################





]