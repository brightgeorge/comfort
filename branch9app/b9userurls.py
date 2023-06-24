from django.urls import path, include

# from . import admin_branch9
from . import admin_branch9
from . import branch9
from . import reports9

urlpatterns = [
    path('branch1_dashboard9/', branch9.branch1_dashboard9, name='branch1_dashboard9'),

    # **room creation start here
    # path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi9/', admin_branch9.branch1_room_create_regi9, name='branch1_room_create_regi9'),
    path('view_all_room9/', admin_branch9.view_all_room9, name='view_all_room9'),
    path('delete_room9/<id>', admin_branch9.delete_room9, name='delete_room9'),

    path('branch1_room_create9/', admin_branch9.branch1_room_create9, name='branch1_room_create9'),

    # **room creation end here

    # bed creation start here

    path('pg1_bed_create_regi9/', admin_branch9.pg1_bed_create_regi9, name='pg1_bed_create_regi9'),
    path('pg1_view_all_beds9/', admin_branch9.pg1_view_all_beds9, name='pg1_view_all_beds9'),
    path('delete_bed9/<id>', admin_branch9.delete_bed9, name='delete_bed9'),

    path('pg1_bed_create9/', admin_branch9.pg1_bed_create9, name='pg1_bed_create9'),

    path('single_pg1_bed_create_regi9/', admin_branch9.single_pg1_bed_create_regi9, name='single_pg1_bed_create_regi9'),
    path('update_bed_basic_details9/<id>', admin_branch9.update_bed_basic_details9, name='update_bed_basic_details9'),

    # bed creation end here

    # guest
    path('br1_admit_guest9/<id>', branch9.br1_admit_guest9, name='br1_admit_guest9'),
    path('view_all_new_guest9/', branch9.view_all_new_guest9, name='view_all_new_guest9'),
    path('update_br1_admit_guest9/<id>', branch9.update_br1_admit_guest9, name='update_br1_admit_guest9'),
    path('vacate_br1_guest9/<id>', branch9.vacate_br1_guest9, name='vacate_br1_guest9'),
    # path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    # path('admit_guest/',views.admit_guest,name='admit_guest'),

    # guest end here

    # *********reports start here

    # unpaid rent start here
    path('unpaid_rent_choose_months9/', branch9.unpaid_rent_choose_months9, name='unpaid_rent_choose_months9'),

    path('jan_unpaid_rent9/', branch9.jan_unpaid_rent9, name='jan_unpaid_rent9'),
    path('table_jan_unpaid_rent9/', branch9.table_jan_unpaid_rent9, name='table_jan_unpaid_rent9'),
    path('feb_unpaid_rent9/', branch9.feb_unpaid_rent9, name='feb_unpaid_rent9'),
    path('table_feb_unpaid_rent9/', branch9.table_feb_unpaid_rent9, name='table_feb_unpaid_rent9'),
    path('mar_unpaid_rent9/', branch9.mar_unpaid_rent9, name='mar_unpaid_rent9'),
    path('table_mar_unpaid_rent9/', branch9.table_mar_unpaid_rent9, name='table_mar_unpaid_rent9'),
    path('april_unpaid_rent9/', branch9.april_unpaid_rent9, name='april_unpaid_rent9'),
    path('table_april_unpaid_rent9/', branch9.table_april_unpaid_rent9, name='table_april_unpaid_rent9'),

    path('may_unpaid_rent9/', branch9.may_unpaid_rent9, name='may_unpaid_rent9'),
    path('table_may_unpaid_rent9/', branch9.table_may_unpaid_rent9, name='table_may_unpaid_rent9'),
    path('june_unpaid_rent9/', branch9.june_unpaid_rent9, name='june_unpaid_rent9'),
    path('table_june_unpaid_rent9/', branch9.table_june_unpaid_rent9, name='table_june_unpaid_rent9'),
    path('july_unpaid_rent9/', branch9.july_unpaid_rent9, name='july_unpaid_rent9'),
    path('table_july_unpaid_rent9', branch9.table_july_unpaid_rent9, name='table_july_unpaid_rent9'),
    path('aug_unpaid_rent9/', branch9.aug_unpaid_rent9, name='aug_unpaid_rent9'),
    path('table_aug_unpaid_rent9/', branch9.table_aug_unpaid_rent9, name='table_aug_unpaid_rent9'),

    path('sept_unpaid_rent9/', branch9.sept_unpaid_rent9, name='sept_unpaid_rent9'),
    path('table_sept_unpaid_rent9/', branch9.table_sept_unpaid_rent9, name='table_sept_unpaid_rent9'),
    path('oct_unpaid_rent9/', branch9.oct_unpaid_rent9, name='oct_unpaid_rent9'),
    path('table_oct_unpaid_rent9/', branch9.table_oct_unpaid_rent9, name='table_oct_unpaid_rent9'),
    path('nov_unpaid_rent9/', branch9.nov_unpaid_rent9, name='nov_unpaid_rent9'),
    path('dec_unpaid_rent9/', branch9.dec_unpaid_rent9, name='dec_unpaid_rent9'),
    path('table_dec_unpaid_rent9/', branch9.table_dec_unpaid_rent9, name='table_dec_unpaid_rent9'),

    path('details_of_unpaid_guests9/<id>', branch9.details_of_unpaid_guests9, name='details_of_unpaid_guests9'),

    # unpaid rent end here

    # paid rent start here
    path('paid_rent_choose_months9/', branch9.paid_rent_choose_months9, name='paid_rent_choose_months9'),
    path('partially_paid_guest_choose_months9/', reports9.partially_paid_guest_choose_months9,
         name='partially_paid_guest_choose_months9'),

    path('jan_paid_rent9/', branch9.jan_paid_rent9, name='jan_paid_rent9'),
    path('feb_paid_rent9/', branch9.feb_paid_rent9, name='feb_paid_rent9'),
    path('mar_paid_rent9/', branch9.mar_paid_rent9, name='mar_paid_rent9'),

    path('april_paid_rent9/', branch9.april_paid_rent9, name='april_paid_rent9'),
    path('may_paid_rent9/', branch9.may_paid_rent9, name='may_paid_rent9'),
    path('table_may_paid_rent9/', branch9.table_may_paid_rent9, name='table_may_paid_rent9'),
    path('may_full_paid_guest9/', reports9.may_full_paid_guest9, name='may_full_paid_guest9'),
    path('may_partially_paid_guest9/', reports9.may_partially_paid_guest9, name='may_partially_paid_guest9'),
    path('table_may_partially_paid_guest9/', reports9.table_may_partially_paid_guest9,
         name='table_may_partially_paid_guest9'),
    path('june_paid_rent9/', branch9.june_paid_rent9, name='june_paid_rent9'),
    path('table_june_paid_rent9/', branch9.table_june_paid_rent9, name='table_june_paid_rent9'),
    path('june_full_paid_guest9/', reports9.june_full_paid_guest9, name='june_full_paid_guest9'),
    path('june_partially_paid_guest9/', reports9.june_partially_paid_guest9, name='june_partially_paid_guest9'),
    path('table_june_partially_paid_guest9/', reports9.table_june_partially_paid_guest9,
         name='table_june_partially_paid_guest9'),

    path('july_paid_rent9/', branch9.july_paid_rent9, name='july_paid_rent9'),
    path('table_july_paid_rent9/', branch9.table_july_paid_rent9, name='table_july_paid_rent9'),
    path('july_full_paid_guest9/', reports9.july_full_paid_guest9, name='july_full_paid_guest9'),
    path('july_partially_paid_guest9/', reports9.july_partially_paid_guest9, name='july_partially_paid_guest9'),
    path('table_july_partially_paid_guest9/', reports9.table_july_partially_paid_guest9,
         name='table_july_partially_paid_guest9'),

    path('aug_paid_rent9/', branch9.aug_paid_rent9, name='aug_paid_rent9'),
    path('sept_paid_rent9/', branch9.sept_paid_rent9, name='sept_paid_rent9'),

    path('oct_paid_rent9/', branch9.oct_paid_rent9, name='oct_paid_rent9'),
    path('nov_paid_rent9/', branch9.nov_paid_rent9, name='nov_paid_rent9'),
    path('dec_paid_rent9/', branch9.dec_paid_rent9, name='dec_paid_rent9'),

    path('details_of_paid_guests9/<id>', branch9.details_of_paid_guests9, name='details_of_paid_guests9'),
    path('full_paid_guest9/', reports9.full_paid_guest9, name='full_paid_guest9'),

    # paid rent end here

    # *********reports end here

    ##################################
    # _ADVANCE9 START HERE
    ################################

    path('choose_months_advance9/', branch9.choose_months_advance9, name='choose_months_advance9'),

    path('jan_advance9/', branch9.jan_advance9, name='jan_advance9'),
    path('jan_make_payments_advance9/<id>', branch9.jan_make_payments_advance9, name='jan_make_payments_advance9'),
    path('feb_advance9/', branch9.feb_advance9, name='feb_advance9'),
    path('feb_make_payments_advance9/<id>', branch9.feb_make_payments_advance9, name='feb_make_payments_advance9'),
    path('march_advance9/', branch9.march_advance9, name='march_advance9'),
    path('march_make_payments_advance9/<id>', branch9.march_make_payments_advance9,
         name='march_make_payments_advance9'),
    path('april_advance9/', branch9.april_advance9, name='april_advance9'),
    path('april_make_payments_advance9/<id>', branch9.april_make_payments_advance9,
         name='april_make_payments_advance9'),

    path('may_advance9/', branch9.may_advance9, name='may_advance9'),
    path('may_make_payments_advance9/<id>', branch9.may_make_payments_advance9, name='may_make_payments_advance9'),
    path('june_advance9/', branch9.june_advance9, name='june_advance9'),
    path('june_make_payments_advance9/<id>', branch9.june_make_payments_advance9, name='june_make_payments_advance9'),
    path('july_advance9/', branch9.july_advance9, name='july_advance9'),
    path('july_make_payments_advance9/<id>', branch9.july_make_payments_advance9, name='july_make_payments_advance9'),
    path('auguest_advance9/', branch9.auguest_advance9, name='auguest_advance9'),
    path('auguest_make_payments_advance9/<id>', branch9.auguest_make_payments_advance9,
         name='auguest_make_payments_advance9'),

    path('sept_advance9/', branch9.sept_advance9, name='sept_advance9'),
    path('sept_make_payments_advance9/<id>', branch9.sept_make_payments_advance9, name='sept_make_payments_advance9'),
    path('october_advance9/', branch9.october_advance9, name='october_advance9'),
    path('october_make_payments_advance9/<id>', branch9.october_make_payments_advance9,
         name='october_make_payments_advance9'),
    path('nov_advance9/', branch9.nov_advance9, name='nov_advance9'),
    path('nov_make_payments_advance9/<id>', branch9.nov_make_payments_advance9, name='nov_make_payments_advance9'),
    path('dec_advance9/', branch9.dec_advance9, name='dec_advance9'),
    path('dec_make_payments_advance9/<id>', branch9.dec_make_payments_advance9, name='dec_make_payments_advance9'),

    ##################################
    # _ADVANCE9 END HERE
    ################################

    ##################################
    # PAYMENTS START HERE
    ################################

    path('choose_months9/', branch9.choose_months9, name='choose_months9'),

    path('jan9/', branch9.jan9, name='jan9'),
    path('jan_manke_payments9/<id>', branch9.jan_manke_payments9, name='jan_manke_payments9'),

    path('feb9/', branch9.feb9, name='feb9'),
    path('feb_manke_payments9/<id>', branch9.feb_manke_payments9, name='feb_manke_payments9'),

    path('march9/', branch9.march9, name='march9'),
    path('march_manke_payments9/<id>', branch9.march_manke_payments9, name='march_manke_payments9'),

    path('april9/', branch9.april9, name='april9'),
    path('april_make_payments9/<id>', branch9.april_make_payments9, name='april_make_payments9'),

    path('may9/', branch9.may9, name='may9'),
    path('may_make_payments9/<id>', branch9.may_make_payments9, name='may_make_payments9'),

    path('june9/', branch9.june9, name='june9'),
    path('june_make_payments9/<id>', branch9.june_make_payments9, name='june_make_payments9'),

    path('july9/', branch9.july9, name='july9'),
    path('july_make_payments9/<id>', branch9.july_make_payments9, name='july_make_payments9'),

    path('aug9/', branch9.aug9, name='aug9'),
    path('aug_make_payments9/<id>', branch9.aug_make_payments9, name='aug_make_payments9'),

    path('sept9/', branch9.sept9, name='sept9'),
    path('sept_make_payments9/<id>', branch9.sept_make_payments9, name='sept_make_payments9'),

    path('oct9/', branch9.oct9, name='oct9'),
    path('oct_make_payments9/<id>', branch9.oct_make_payments9, name='oct_make_payments9'),

    path('nov9/', branch9.nov9, name='nov9'),
    path('nov_make_payments9/<id>', branch9.nov_make_payments9, name='nov_make_payments9'),

    path('dec9/', branch9.dec9, name='dec9'),
    path('dec_make_payments9/<id>', branch9.dec_make_payments9, name='dec_make_payments9'),

    ##################################
    # PAYMENTS END HERE
    ################################

    ##################################
    # PRINT OUTS START HERE
    ################################

    path('detail_guest_general9/', branch9.detail_guest_general9, name='detail_guest_general9'),

    path('jan_print9/', branch9.jan_print9, name='jan_print9'),
    path('feb_print9/', branch9.feb_print9, name='feb_print9'),
    path('march_print9/', branch9.march_print9, name='march_print9'),
    path('april_print9/', branch9.april_print9, name='april_print9'),

    path('may_print9/', branch9.may_print9, name='may_print9'),
    path('june_print9/', branch9.june_print9, name='june_print9'),
    path('july_print9/', branch9.july_print9, name='july_print9'),
    path('aug_print9/', branch9.aug_print9, name='aug_print9'),

    path('sept_print9/', branch9.sept_print9, name='sept_print9'),
    path('oct_print9/', branch9.oct_print9, name='oct_print9'),
    path('nov_print9/', branch9.nov_print9, name='nov_print9'),
    path('dec_print9/', branch9.dec_print9, name='dec_print9'),

    ##################################
    # PRINT OUTS END HERE
    ################################

    ########################################
    # CLOSE MONTHS START HERE
    ###########################

    path('jan_close9/', branch9.jan_close9, name='jan_close9'),
    path('jan_close_decision_page9/', branch9.jan_close_decision_page9, name='jan_close_decision_page9'),
    path('feb_close9/', branch9.feb_close9, name='feb_close9'),
    path('feb_close_decision_page9/', branch9.feb_close_decision_page9, name='feb_close_decision_page9'),
    path('mar_close9/', branch9.mar_close9, name='mar_close9'),
    path('mar_close_decision_page/', branch9.mar_close_decision_page9, name='mar_close_decision_page9'),
    path('apr_close9/', branch9.apr_close9, name='apr_close9'),
    path('apr_close_decision_page9/', branch9.apr_close_decision_page9, name='apr_close_decision_page9'),

    path('may_close9/', branch9.may_close9, name='may_close9'),
    path('may_close_decision_page9/', branch9.may_close_decision_page9, name='may_close_decision_page9'),
    path('jun_close9/', branch9.jun_close9, name='jun_close9'),
    path('jun_close_decision_page9/', branch9.jun_close_decision_page9, name='jun_close_decision_page9'),
    path('jul_close9/', branch9.jul_close9, name='jul_close9'),
    path('jul_close_decision_page9/', branch9.jul_close_decision_page9, name='jul_close_decision_page9'),
    path('aug_close9/', branch9.aug_close9, name='aug_close9'),
    path('aug_close_decision_page9/', branch9.aug_close_decision_page9, name='aug_close_decision_page9'),

    path('sep_close9/', branch9.sep_close9, name='sep_close9'),
    path('sep_close_decision_page9/', branch9.sep_close_decision_page9, name='sep_close_decision_page9'),
    path('oct_close9/', branch9.oct_close9, name='oct_close9'),
    path('oct_close_decision_page9/', branch9.oct_close_decision_page9, name='oct_close_decision_page9'),
    path('nov_close9/', branch9.nov_close9, name='nov_close9'),
    path('nov_close_decision_page9/', branch9.nov_close_decision_page9, name='nov_close_decision_page9'),

    path('detailed_report_choose_months9/', reports9.detailed_report_choose_months9,
         name='detailed_report_choose_months9'),
    path('may_print_live9/', reports9.may_print_live9, name='may_print_live9'),
    path('june_dtails_live9/', reports9.june_dtails_live9, name='june_dtails_live9'),
    path('june_print_live9/', reports9.june_print_live9, name='june_print_live9'),
    path('viewall_vaccant_room9/', reports9.viewall_vaccant_room9, name='viewall_vaccant_room9'),

    # path('d9/', branch9.dynamic, name='dynamic'),

    # path('manage_bed9/', branch9.manage_bed9, name='manage_bed9'),
    # path('manage_new_guest9/', branch9.manage_new_guest9, name='manage_new_guest9'),
    # path('manage_update_new_guest9/<id>', branch9.manage_update_new_guest9, name='manage_update_new_guest9'),
    # path('manage_update_beds9/<id>', branch9.manage_update_beds9, name='manage_update_beds9'),

    ########################################
    # CLOSE MONTHS END HERE
    ###########################

    ########################################
    # DUE AMT MANAGEMENT START HERE
    ###########################

    path('view_all_due_amt9/', branch9.view_all_due_amt9, name='view_all_due_amt9'),
    path('due_amt_mgt_choose_months9/', branch9.due_amt_mgt_choose_months9, name='due_amt_mgt_choose_months9'),

    path('view_may_account_details9/', branch9.view_may_account_details9, name='view_may_account_details9'),
    path('may_account_mgt9/<id>', branch9.may_account_mgt9, name='may_account_mgt9'),

    path('view_june_account_details9/', branch9.view_june_account_details9, name='view_june_account_details9'),
    path('june_account_mgt9/<id>', branch9.june_account_mgt9, name='june_account_mgt9'),
    path('view_july_account_details9/', branch9.view_july_account_details9, name='view_july_account_details9'),
    path('july_account_mgt9/<id>', branch9.july_account_mgt9, name='july_account_mgt9'),

    ########################################
    # DUE AMT MANAGEMENT END HERE
    ###########################

    ##################################
    # VACATE GUEST DETAILS START HERE
    ################################

    path('viewall_vacate_guest9/', branch9.viewall_vacate_guest9, name='viewall_vacate_guest9'),
    path('details_of_vacate_guest9/<id>', branch9.details_of_vacate_guest9, name='details_of_vacate_guest9'),

    # ********vacate guest payments start here**********

    path('jan_manke_payments_vacate9/<id>', branch9.jan_manke_payments_vacate9, name='jan_manke_payments_vacate9'),
    path('feb_manke_payments_vacate9/<id>', branch9.feb_manke_payments_vacate9, name='feb_manke_payments_vacate9'),
    path('march_manke_payments_vacate9/<id>', branch9.march_manke_payments_vacate9,
         name='march_manke_payments_vacate9'),
    path('april_make_payments_vacate9/<id>', branch9.april_make_payments_vacate9, name='april_make_payments_vacate9'),

    path('may_make_payments_vacate9/<id>', branch9.may_make_payments_vacate9, name='may_make_payments_vacate9'),
    path('june_make_payments_vacate9/<id>', branch9.june_make_payments_vacate9, name='june_make_payments_vacate9'),
    path('july_make_payments_vacate9/<id>', branch9.july_make_payments_vacate9, name='july_make_payments_vacate9'),
    path('aug_make_payments_vacate9/<id>', branch9.aug_make_payments_vacate9, name='aug_make_payments_vacate9'),

    path('sept_make_payments_vacate9/<id>', branch9.sept_make_payments_vacate9, name='sept_make_payments_vacate9'),
    path('oct_make_payments_vacate9/<id>', branch9.oct_make_payments_vacate9, name='oct_make_payments_vacate9'),
    path('nov_make_payments_vacate9/<id>', branch9.nov_make_payments_vacate9, name='nov_make_payments_vacate9'),
    path('dec_make_payments_vacate9/<id>', branch9.dec_make_payments_vacate9, name='dec_make_payments_vacate9'),

    # ********vacate guest payments end here**********

    ##################################
    # VACATE GUEST DETAILS END HERE
    ################################

]

