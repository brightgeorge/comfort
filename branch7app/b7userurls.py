from django.urls import path, include

#from . import admin_branch7
from . import admin_branch7
from . import branch7
from . import reports7
from . import payment7
from . import admin_dashboard_calculations_br7


urlpatterns = [
    path('branch1_dashboard7/', branch7.branch1_dashboard7, name='branch1_dashboard7'),

#**room creation start here
    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi7/',admin_branch7.branch1_room_create_regi7,name='branch1_room_create_regi7'),
    path('view_all_room7/',admin_branch7.view_all_room7,name='view_all_room7'),
    path('delete_room7/<id>',admin_branch7.delete_room7,name='delete_room7'),

    path('branch1_room_create7/',admin_branch7.branch1_room_create7,name='branch1_room_create7'),

#**room creation end here


#bed creation start here

    path('pg1_bed_create_regi7/', admin_branch7.pg1_bed_create_regi7, name='pg1_bed_create_regi7'),
    path('pg1_view_all_beds7/', admin_branch7.pg1_view_all_beds7, name='pg1_view_all_beds7'),
    path('delete_bed7/<id>', admin_branch7.delete_bed7, name='delete_bed7'),

    path('pg1_bed_create7/', admin_branch7.pg1_bed_create7, name='pg1_bed_create7'),

    path('single_pg1_bed_create_regi7/',admin_branch7.single_pg1_bed_create_regi7,name='single_pg1_bed_create_regi7'),
    path('update_bed_basic_details7/<id>',admin_branch7.update_bed_basic_details7, name='update_bed_basic_details7'),

#bed creation end here

#guest
    path('br1_admit_guest7/<id>',branch7.br1_admit_guest7,name='br1_admit_guest7'),
    path('view_all_new_guest7/',branch7.view_all_new_guest7,name='view_all_new_guest7'),
    path('update_br1_admit_guest7/<id>',branch7.update_br1_admit_guest7,name='update_br1_admit_guest7'),
    path('vacate_br1_guest7/<id>',branch7.vacate_br1_guest7,name='vacate_br1_guest7'),
    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),

#guest end here


#*********reports start here

#unpaid rent start here
    path('unpaid_rent_choose_months7/',branch7.unpaid_rent_choose_months7,name='unpaid_rent_choose_months7'),

    path('jan_unpaid_rent7/', branch7.jan_unpaid_rent7, name='jan_unpaid_rent7'),
    path('table_jan_unpaid_rent7/', branch7.table_jan_unpaid_rent7, name='table_jan_unpaid_rent7'),
    path('feb_unpaid_rent7/', branch7.feb_unpaid_rent7, name='feb_unpaid_rent7'),
    path('table_feb_unpaid_rent7/', branch7.table_feb_unpaid_rent7, name='table_feb_unpaid_rent7'),
    path('mar_unpaid_rent7/', branch7.mar_unpaid_rent7, name='mar_unpaid_rent7'),
    path('table_mar_unpaid_rent7/', branch7.table_mar_unpaid_rent7, name='table_mar_unpaid_rent7'),
    path('april_unpaid_rent7/', branch7.april_unpaid_rent7, name='april_unpaid_rent7'),
    path('table_april_unpaid_rent7/', branch7.table_april_unpaid_rent7, name='table_april_unpaid_rent7'),

    path('may_unpaid_rent7/', branch7.may_unpaid_rent7, name='may_unpaid_rent7'),
    path('table_may_unpaid_rent7/', branch7.table_may_unpaid_rent7, name='table_may_unpaid_rent7'),
    path('june_unpaid_rent7/', branch7.june_unpaid_rent7, name='june_unpaid_rent7'),
    path('table_june_unpaid_rent7/', branch7.table_june_unpaid_rent7, name='table_june_unpaid_rent7'),
    path('july_unpaid_rent7/', branch7.july_unpaid_rent7, name='july_unpaid_rent7'),
    path('table_july_unpaid_rent7',branch7.table_july_unpaid_rent7,name='table_july_unpaid_rent7'),
    path('aug_unpaid_rent7/', branch7.aug_unpaid_rent7, name='aug_unpaid_rent7'),
    path('table_aug_unpaid_rent7/',branch7.table_aug_unpaid_rent7,name='table_aug_unpaid_rent7'),

    path('sept_unpaid_rent7/', branch7.sept_unpaid_rent7, name='sept_unpaid_rent7'),
    path('table_sept_unpaid_rent7/', branch7.table_sept_unpaid_rent7, name='table_sept_unpaid_rent7'),
    path('oct_unpaid_rent7/', branch7.oct_unpaid_rent7, name='oct_unpaid_rent7'),
    path('table_oct_unpaid_rent7/', branch7.table_oct_unpaid_rent7, name='table_oct_unpaid_rent7'),
    path('nov_unpaid_rent7/', branch7.nov_unpaid_rent7, name='nov_unpaid_rent7'),
    path('dec_unpaid_rent7/', branch7.dec_unpaid_rent7, name='dec_unpaid_rent7'),
    path('table_dec_unpaid_rent7/', branch7.table_dec_unpaid_rent7, name='table_dec_unpaid_rent7'),

    path('details_of_unpaid_guests7/<id>',branch7.details_of_unpaid_guests7,name='details_of_unpaid_guests7'),

#unpaid rent end here

#paid rent start here
    path('paid_rent_choose_months7/',branch7.paid_rent_choose_months7,name='paid_rent_choose_months7'),
    path('partially_paid_guest_choose_months7/',reports7.partially_paid_guest_choose_months7,name='partially_paid_guest_choose_months7'),

    path('jan_paid_rent7/', branch7.jan_paid_rent7, name='jan_paid_rent7'),
    path('feb_paid_rent7/', branch7.feb_paid_rent7, name='feb_paid_rent7'),
    path('mar_paid_rent7/', branch7.mar_paid_rent7, name='mar_paid_rent7'),

    path('april_paid_rent7/', branch7.april_paid_rent7, name='april_paid_rent7'),
    path('may_paid_rent7/', branch7.may_paid_rent7, name='may_paid_rent7'),
    path('table_may_paid_rent7/', branch7.table_may_paid_rent7, name='table_may_paid_rent7'),
    path('may_full_paid_guest7/', reports7.may_full_paid_guest7, name='may_full_paid_guest7'),
    path('may_partially_paid_guest7/', reports7.may_partially_paid_guest7, name='may_partially_paid_guest7'),
    path('table_may_partially_paid_guest7/', reports7.table_may_partially_paid_guest7, name='table_may_partially_paid_guest7'),
    path('june_paid_rent7/', branch7.june_paid_rent7, name='june_paid_rent7'),
    path('table_june_paid_rent7/', branch7.table_june_paid_rent7, name='table_june_paid_rent7'),
    path('june_full_paid_guest7/', reports7.june_full_paid_guest7, name='june_full_paid_guest7'),
    path('june_partially_paid_guest7/', reports7.june_partially_paid_guest7, name='june_partially_paid_guest7'),
    path('table_june_partially_paid_guest7/', reports7.table_june_partially_paid_guest7, name='table_june_partially_paid_guest7'),

    path('july_paid_rent7/', branch7.july_paid_rent7, name='july_paid_rent7'),
    path('table_july_paid_rent7/', branch7.table_july_paid_rent7, name='table_july_paid_rent7'),
    path('july_full_paid_guest7/', reports7.july_full_paid_guest7, name='july_full_paid_guest7'),
    path('july_partially_paid_guest7/', reports7.july_partially_paid_guest7, name='july_partially_paid_guest7'),
    path('table_july_partially_paid_guest7/', reports7.table_july_partially_paid_guest7, name='table_july_partially_paid_guest7'),

    path('aug_paid_rent7/', branch7.aug_paid_rent7, name='aug_paid_rent7'),
    path('sept_paid_rent7/', branch7.sept_paid_rent7, name='sept_paid_rent7'),

    path('oct_paid_rent7/', branch7.oct_paid_rent7, name='oct_paid_rent7'),
    path('nov_paid_rent7/', branch7.nov_paid_rent7, name='nov_paid_rent7'),
    path('dec_paid_rent7/', branch7.dec_paid_rent7, name='dec_paid_rent7'),

    path('details_of_paid_guests7/<id>',branch7.details_of_paid_guests7,name='details_of_paid_guests7'),
    path('full_paid_guest7/',reports7.full_paid_guest7,name='full_paid_guest7'),

#paid rent end here

#*********reports end here



##################################
#_ADVANCE7 START HERE
################################


path('choose_months_advance7/',branch7.choose_months_advance7,name='choose_months_advance7'),

path('jan_advance7/', branch7.jan_advance7, name='jan_advance7'),
path('jan_make_payments_advance7/<id>', branch7.jan_make_payments_advance7,name='jan_make_payments_advance7'),
path('feb_advance7/', branch7.feb_advance7, name='feb_advance7'),
path('feb_make_payments_advance7/<id>', branch7.feb_make_payments_advance7,name='feb_make_payments_advance7'),
path('march_advance7/', branch7.march_advance7, name='march_advance7'),
path('march_make_payments_advance7/<id>', branch7.march_make_payments_advance7,name='march_make_payments_advance7'),
path('april_advance7/', branch7.april_advance7, name='april_advance7'),
path('april_make_payments_advance7/<id>', branch7.april_make_payments_advance7, name='april_make_payments_advance7'),

path('may_advance7/',branch7.may_advance7,name='may_advance7'),
path('may_make_payments_advance7/<id>', branch7.may_make_payments_advance7, name='may_make_payments_advance7'),
path('june_advance7/',branch7.june_advance7,name='june_advance7'),
path('june_make_payments_advance7/<id>', branch7.june_make_payments_advance7, name='june_make_payments_advance7'),
path('july_advance7/',branch7.july_advance7,name='july_advance7'),
path('july_make_payments_advance7/<id>', branch7.july_make_payments_advance7, name='july_make_payments_advance7'),
path('auguest_advance7/', branch7.auguest_advance7, name='auguest_advance7'),
path('auguest_make_payments_advance7/<id>', branch7.auguest_make_payments_advance7, name='auguest_make_payments_advance7'),

path('sept_advance7/', branch7.sept_advance7, name='sept_advance7'),
path('sept_make_payments_advance7/<id>', branch7.sept_make_payments_advance7,name='sept_make_payments_advance7'),
path('october_advance7/', branch7.october_advance7, name='october_advance7'),
path('october_make_payments_advance7/<id>', branch7.october_make_payments_advance7, name='october_make_payments_advance7'),
path('nov_advance7/', branch7.nov_advance7, name='nov_advance7'),
path('nov_make_payments_advance7/<id>', branch7.nov_make_payments_advance7,name='nov_make_payments_advance7'),
path('dec_advance7/', branch7.dec_advance7, name='dec_advance7'),
path('dec_make_payments_advance7/<id>', branch7.dec_make_payments_advance7, name='dec_make_payments_advance7'),



##################################
#_ADVANCE7 END HERE
################################


##################################
#PAYMENTS START HERE
################################

    path('choose_months7/',branch7.choose_months7,name='choose_months7'),

    path('jan7/',branch7.jan7,name='jan7'),
    path('jan_manke_payments7/<id>',branch7.jan_manke_payments7,name='jan_manke_payments7'),

    path('feb7/',branch7.feb7,name='feb7'),
    path('feb_manke_payments7/<id>',branch7.feb_manke_payments7,name='feb_manke_payments7'),

    path('march7/',branch7.march7,name='march7'),
    path('march_manke_payments7/<id>',branch7.march_manke_payments7,name='march_manke_payments7'),

    path('april7/',branch7.april7,name='april7'),
    path('april_make_payments7/<id>',branch7.april_make_payments7,name='april_make_payments7'),

    path('may7/',branch7.may7,name='may7'),
    path('may_make_payments7/<id>',branch7.may_make_payments7,name='may_make_payments7'),

    path('june7/',branch7.june7,name='june7'),
    path('june_make_payments7/<id>',branch7.june_make_payments7,name='june_make_payments7'),

    path('july7/',branch7.july7,name='july7'),
    path('july_make_payments7/<id>',branch7.july_make_payments7,name='july_make_payments7'),

    path('aug7/',branch7.aug7,name='aug7'),
    path('aug_make_payments7/<id>',branch7.aug_make_payments7,name='aug_make_payments7'),

    path('sept7/',branch7.sept7,name='sept7'),
    path('sept_make_payments7/<id>',branch7.sept_make_payments7,name='sept_make_payments7'),

    path('oct7/',branch7.oct7,name='oct7'),
    path('oct_make_payments7/<id>',branch7.oct_make_payments7,name='oct_make_payments7'),

    path('nov7/',branch7.nov7,name='nov7'),
    path('nov_make_payments7/<id>',branch7.nov_make_payments7,name='nov_make_payments7'),

    path('dec7/',branch7.dec7,name='dec7'),
    path('dec_make_payments7/<id>',branch7.dec_make_payments7,name='dec_make_payments7'),

##################################
#PAYMENTS END HERE
################################

##################################
#MONTHLY MANAGEMENT PAYMENTS START HERE
################################

    path('choose_user7/', payment7.choose_user7, name='choose_user7'),
    path('payment_user_details7/<id>', payment7.payment_user_details7, name='payment_user_details7'),

    path('monthly_jan_make_payments7/<id>', payment7.monthly_jan_make_payments7, name='monthly_jan_make_payments7'),
    path('monthly_feb_make_payments7/<id>', payment7.monthly_feb_make_payments7, name='monthly_feb_make_payments7'),
    path('monthly_march_make_payments7/<id>', payment7.monthly_march_make_payments7, name='monthly_march_make_payments7'),
    path('monthly_april_make_payments7/<id>', payment7.monthly_april_make_payments7, name='monthly_april_make_payments7'),
    path('monthly_may_make_payments7/<id>', payment7.monthly_may_make_payments7, name='monthly_may_make_payments7'),
    path('monthly_june_make_payments7/<id>', payment7.monthly_june_make_payments7, name='monthly_june_make_payments7'),

    path('monthly_july_make_payments7/<id>', payment7.monthly_july_make_payments7, name='monthly_july_make_payments7'),
    path('monthly_aug_make_payments7/<id>', payment7.monthly_aug_make_payments7, name='monthly_aug_make_payments7'),
    path('monthly_sept_make_payments7/<id>', payment7.monthly_sept_make_payments7, name='monthly_sept_make_payments7'),
    path('monthly_oct_make_payments7/<id>', payment7.monthly_oct_make_payments7, name='monthly_oct_make_payments7'),
    path('monthly_nov_make_payments7/<id>', payment7.monthly_nov_make_payments7, name='monthly_nov_make_payments7'),
    path('monthly_dec_make_payments7/<id>', payment7.monthly_dec_make_payments7, name='monthly_dec_make_payments7'),

##################################
#MONTHLY MANAGEMENT PAYMENTS END HERE
################################

##################################
#PRINT OUTS START HERE
################################

    path('detail_guest_general7/',branch7.detail_guest_general7,name='detail_guest_general7'),

    path('jan_print7/',branch7.jan_print7,name='jan_print7'),
    path('feb_print7/',branch7.feb_print7,name='feb_print7'),
    path('march_print7/',branch7.march_print7,name='march_print7'),
    path('april_print7/',branch7.april_print7,name='april_print7'),

    path('may_print7/',branch7.may_print7,name='may_print7'),
    path('june_print7/',branch7.june_print7,name='june_print7'),
    path('july_print7/', branch7.july_print7, name='july_print7'),
    path('aug_print7/', branch7.aug_print7, name='aug_print7'),

    path('sept_print7/', branch7.sept_print7, name='sept_print7'),
    path('oct_print7/', branch7.oct_print7, name='oct_print7'),
    path('nov_print7/', branch7.nov_print7, name='nov_print7'),
    path('dec_print7/', branch7.dec_print7, name='dec_print7'),

##################################
#PRINT OUTS END HERE
################################


########################################
# CLOSE MONTHS START HERE
###########################

    path('jan_close7/', branch7.jan_close7, name='jan_close7'),
    path('jan_close_decision_page7/', branch7.jan_close_decision_page7, name='jan_close_decision_page7'),
    path('feb_close7/', branch7.feb_close7, name='feb_close7'),
    path('feb_close_decision_page7/', branch7.feb_close_decision_page7, name='feb_close_decision_page7'),
    path('mar_close7/', branch7.mar_close7, name='mar_close7'),
    path('mar_close_decision_page/', branch7.mar_close_decision_page7, name='mar_close_decision_page7'),
    path('apr_close7/', branch7.apr_close7, name='apr_close7'),
    path('apr_close_decision_page7/', branch7.apr_close_decision_page7, name='apr_close_decision_page7'),

    path('may_close7/', branch7.may_close7, name='may_close7'),
    path('may_close_decision_page7/', branch7.may_close_decision_page7, name='may_close_decision_page7'),
    path('jun_close7/', branch7.jun_close7, name='jun_close7'),
    path('jun_close_decision_page7/', branch7.jun_close_decision_page7, name='jun_close_decision_page7'),
    path('jul_close7/', branch7.jul_close7, name='jul_close7'),
    path('jul_close_decision_page7/', branch7.jul_close_decision_page7, name='jul_close_decision_page7'),
    path('aug_close7/', branch7.aug_close7, name='aug_close7'),
    path('aug_close_decision_page7/', branch7.aug_close_decision_page7, name='aug_close_decision_page7'),

    path('sep_close7/', branch7.sep_close7, name='sep_close7'),
    path('sep_close_decision_page7/', branch7.sep_close_decision_page7, name='sep_close_decision_page7'),
    path('oct_close7/', branch7.oct_close7, name='oct_close7'),
    path('oct_close_decision_page7/', branch7.oct_close_decision_page7, name='oct_close_decision_page7'),
    path('nov_close7/', branch7.nov_close7, name='nov_close7'),
    path('nov_close_decision_page7/', branch7.nov_close_decision_page7, name='nov_close_decision_page7'),

    path('detailed_report_choose_months7/',reports7.detailed_report_choose_months7,name='detailed_report_choose_months7'),
    path('may_details_live7/', reports7.may_details_live7, name='may_details_live7'),
    path('may_print_live7/', reports7.may_print_live7, name='may_print_live7'),
    path('june_details_live7/',reports7.june_details_live7,name='june_details_live7'),
    path('june_print_live7/', reports7.june_print_live7, name='june_print_live7'),
    path('july_details_live7/', reports7.july_details_live7, name='july_details_live7'),
    path('july_print_live7/', reports7.july_print_live7, name='july_print_live7'),

    path('viewall_vaccant_room7/', reports7.viewall_vaccant_room7, name='viewall_vaccant_room7'),

    #path('d7/', branch7.dynamic, name='dynamic'),

    #path('manage_bed7/', branch7.manage_bed7, name='manage_bed7'),
    #path('manage_new_guest7/', branch7.manage_new_guest7, name='manage_new_guest7'),
    #path('manage_update_new_guest7/<id>', branch7.manage_update_new_guest7, name='manage_update_new_guest7'),
    #path('manage_update_beds7/<id>', branch7.manage_update_beds7, name='manage_update_beds7'),

########################################
# CLOSE MONTHS END HERE
###########################


########################################
# DUE AMT MANAGEMENT START HERE
###########################

    path('view_all_due_amt7/', branch7.view_all_due_amt7, name='view_all_due_amt7'),
    path('due_amt_mgt_choose_months7/', branch7.due_amt_mgt_choose_months7, name='due_amt_mgt_choose_months7'),

    path('view_may_account_details7/', branch7.view_may_account_details7, name='view_may_account_details7'),
    path('may_account_mgt7/<id>', branch7.may_account_mgt7, name='may_account_mgt7'),

    path('view_june_account_details7/', branch7.view_june_account_details7, name='view_june_account_details7'),
    path('june_account_mgt7/<id>', branch7.june_account_mgt7, name='june_account_mgt7'),
    path('view_july_account_details7/', branch7.view_july_account_details7, name='view_july_account_details7'),
    path('july_account_mgt7/<id>', branch7.july_account_mgt7, name='july_account_mgt7'),

    ########################################
# DUE AMT MANAGEMENT END HERE
###########################



##################################
#VACATE GUEST DETAILS START HERE
################################

    path('viewall_vacate_guest7/',branch7.viewall_vacate_guest7,name='viewall_vacate_guest7'),
    path('details_of_vacate_guest7/<id>',branch7.details_of_vacate_guest7,name='details_of_vacate_guest7'),

#********vacate guest payments start here**********

    path('jan_manke_payments_vacate7/<id>', branch7.jan_manke_payments_vacate7, name='jan_manke_payments_vacate7'),
    path('feb_manke_payments_vacate7/<id>', branch7.feb_manke_payments_vacate7, name='feb_manke_payments_vacate7'),
    path('march_manke_payments_vacate7/<id>', branch7.march_manke_payments_vacate7, name='march_manke_payments_vacate7'),
    path('april_make_payments_vacate7/<id>', branch7.april_make_payments_vacate7, name='april_make_payments_vacate7'),

    path('may_make_payments_vacate7/<id>', branch7.may_make_payments_vacate7, name='may_make_payments_vacate7'),
    path('june_make_payments_vacate7/<id>', branch7.june_make_payments_vacate7, name='june_make_payments_vacate7'),
    path('july_make_payments_vacate7/<id>', branch7.july_make_payments_vacate7, name='july_make_payments_vacate7'),
    path('aug_make_payments_vacate7/<id>', branch7.aug_make_payments_vacate7, name='aug_make_payments_vacate7'),

    path('sept_make_payments_vacate7/<id>', branch7.sept_make_payments_vacate7, name='sept_make_payments_vacate7'),
    path('oct_make_payments_vacate7/<id>', branch7.oct_make_payments_vacate7, name='oct_make_payments_vacate7'),
    path('nov_make_payments_vacate7/<id>', branch7.nov_make_payments_vacate7, name='nov_make_payments_vacate7'),
    path('dec_make_payments_vacate7/<id>', branch7.dec_make_payments_vacate7, name='dec_make_payments_vacate7'),

#********vacate guest payments end here**********

##################################
#VACATE GUEST DETAILS END HERE
################################

########################################
# DASHBOARD REPORTS START HERE
###########################

    path('monthly_details_due7', admin_dashboard_calculations_br7.monthly_details_due7, name='monthly_details_due7'),
    path('monthly_collection_details7/', admin_dashboard_calculations_br7.monthly_collection_details7, name='monthly_collection_details7'),

########################################
# DASHBOARD REPORTS END HERE
###########################





]