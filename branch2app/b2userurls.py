from django.contrib import admin
from django.urls import path, include

from django.urls import path
from . import views
from . import admin_branch2

#from . import branch1
from . import branch2
from . import reports2


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
    path('branch1_dashboard2/', branch2.branch1_dashboard2, name='branch1_dashboard2'),

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

    path('single_pg1_bed_create_regi2/', admin_branch2.single_pg1_bed_create_regi2, name='single_pg1_bed_create_regi2'),
    path('update_bed_basic_details2/<id>', admin_branch2.update_bed_basic_details2, name='update_bed_basic_details2'),

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
    path('march_advance2/', branch2.march_advance2, name='march_advance'+name),
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
    path('table_jan_unpaid_rent2/', branch2.table_jan_unpaid_rent2, name='table_jan_unpaid_rent2'),
    path('feb_unpaid_rent2/', branch2.feb_unpaid_rent2, name='feb_unpaid_rent2'),
    path('table_feb_unpaid_rent2/', branch2.table_feb_unpaid_rent2, name='table_feb_unpaid_rent2'),
    path('mar_unpaid_rent2/', branch2.mar_unpaid_rent2, name='mar_unpaid_rent2'),
    path('table_mar_unpaid_rent2/', branch2.table_mar_unpaid_rent2, name='table_mar_unpaid_rent2'),
    path('april_unpaid_rent2/', branch2.april_unpaid_rent2, name='april_unpaid_rent2'),
    path('table_april_unpaid_rent2/', branch2.table_april_unpaid_rent2, name='table_april_unpaid_rent2'),

    path('may_unpaid_rent2/', branch2.may_unpaid_rent2, name='may_unpaid_rent2'),
    path('table_may_unpaid_rent2/', branch2.table_may_unpaid_rent2, name='table_may_unpaid_rent2'),
    path('june_unpaid_rent2/', branch2.june_unpaid_rent2, name='june_unpaid_rent2'),
    path('table_june_unpaid_rent2/', branch2.table_june_unpaid_rent2, name='table_june_unpaid_rent2'),
    path('july_unpaid_rent2/', branch2.july_unpaid_rent2, name='july_unpaid_rent2'),
    path('table_july_unpaid_rent2',branch2.table_july_unpaid_rent2,name='table_july_unpaid_rent2'),
    path('aug_unpaid_rent2/', branch2.aug_unpaid_rent2, name='aug_unpaid_rent2'),
    path('table_aug_unpaid_rent2/',branch2.table_aug_unpaid_rent2,name='table_aug_unpaid_rent2'),

    path('sept_unpaid_rent2/', branch2.sept_unpaid_rent2, name='sept_unpaid_rent2'),
    path('table_sept_unpaid_rent2/', branch2.table_sept_unpaid_rent2, name='table_sept_unpaid_rent2'),
    path('oct_unpaid_rent2/', branch2.oct_unpaid_rent2, name='oct_unpaid_rent2'),
    path('table_oct_unpaid_rent2/', branch2.table_oct_unpaid_rent2, name='table_oct_unpaid_rent2'),
    path('nov_unpaid_rent2/', branch2.nov_unpaid_rent2, name='nov_unpaid_rent2'),
    path('dec_unpaid_rent2/', branch2.dec_unpaid_rent2, name='dec_unpaid_rent2'),
    path('table_dec_unpaid_rent2/', branch2.table_dec_unpaid_rent2, name='table_dec_unpaid_rent2'),

    path('details_of_unpaid_guests2/<id>',branch2.details_of_unpaid_guests2,name='details_of_unpaid_guests2'),

#unpaid rent end here



#paid rent start here
    path('paid_rent_choose_months2/',branch2.paid_rent_choose_months2,name='paid_rent_choose_months2'),
    path('partially_paid_guest_choose_months2/',reports2.partially_paid_guest_choose_months2,name='partially_paid_guest_choose_months2'),

    path('jan_paid_rent2/', branch2.jan_paid_rent2, name='jan_paid_rent2'),
    path('feb_paid_rent2/', branch2.feb_paid_rent2, name='feb_paid_rent2'),
    path('mar_paid_rent2/', branch2.mar_paid_rent2, name='mar_paid_rent2'),

    path('april_paid_rent2/', branch2.april_paid_rent2, name='april_paid_rent2'),
    path('may_paid_rent2/', branch2.may_paid_rent2, name='may_paid_rent2'),
    path('table_may_paid_rent2/', branch2.table_may_paid_rent2, name='table_may_paid_rent2'),
    path('may_full_paid_guest2/', reports2.may_full_paid_guest2, name='may_full_paid_guest2'),
    path('may_partially_paid_guest2/', reports2.may_partially_paid_guest2, name='may_partially_paid_guest2'),
    path('table_may_partially_paid_guest2/', reports2.table_may_partially_paid_guest2, name='table_may_partially_paid_guest2'),
    path('june_paid_rent2/', branch2.june_paid_rent2, name='june_paid_rent2'),
    path('table_june_paid_rent2/', branch2.table_june_paid_rent2, name='table_june_paid_rent2'),
    path('june_full_paid_guest2/', reports2.june_full_paid_guest2, name='june_full_paid_guest2'),
    path('june_partially_paid_guest2/', reports2.june_partially_paid_guest2, name='june_partially_paid_guest2'),
    path('table_june_partially_paid_guest2/', reports2.table_june_partially_paid_guest2, name='table_june_partially_paid_guest2'),

    path('july_paid_rent2/', branch2.july_paid_rent2, name='july_paid_rent2'),
    path('table_july_paid_rent2/', branch2.table_july_paid_rent2, name='table_july_paid_rent2'),
    path('july_full_paid_guest2/', reports2.july_full_paid_guest2, name='july_full_paid_guest2'),
    path('july_partially_paid_guest2/', reports2.july_partially_paid_guest2, name='july_partially_paid_guest2'),
    path('table_july_partially_paid_guest2/', reports2.table_july_partially_paid_guest2, name='table_july_partially_paid_guest2'),

    path('aug_paid_rent2/', branch2.aug_paid_rent2, name='aug_paid_rent2'),
    path('sept_paid_rent2/', branch2.sept_paid_rent2, name='sept_paid_rent2'),

    path('oct_paid_rent2/', branch2.oct_paid_rent2, name='oct_paid_rent2'),
    path('nov_paid_rent2/', branch2.nov_paid_rent2, name='nov_paid_rent2'),
    path('dec_paid_rent2/', branch2.dec_paid_rent2, name='dec_paid_rent2'),

    path('details_of_paid_guests2/<id>',branch2.details_of_paid_guests2,name='details_of_paid_guests2'),
    path('full_paid_guest2/',reports2.full_paid_guest2,name='full_paid_guest2'),

#paid rent end here



#*********reports end here


##################################
#VACATE GUEST DETAILS START HERE
################################

    path('viewall_vacate_guest2/',branch2.viewall_vacate_guest2,name='viewall_vacate_guest2'),
    path('details_of_vacate_guest2/<id>',branch2.details_of_vacate_guest2,name='details_of_vacate_guest2'),

#********vacate guest payments start here**********

    path('jan_manke_payments_vacate2/<id>', branch2.jan_manke_payments_vacate2, name='jan_manke_payments_vacate2'),
    path('feb_manke_payments_vacate2/<id>', branch2.feb_manke_payments_vacate2, name='feb_manke_payments_vacate2'),
    path('march_manke_payments_vacate2/<id>', branch2.march_manke_payments_vacate2, name='march_manke_payments_vacate2'),
    path('april_make_payments_vacate2/<id>', branch2.april_make_payments_vacate2, name='april_make_payments_vacate2'),

    path('may_make_payments_vacate2/<id>', branch2.may_make_payments_vacate2, name='may_make_payments_vacate2'),
    path('june_make_payments_vacate2/<id>', branch2.june_make_payments_vacate2, name='june_make_payments_vacate2'),
    path('july_make_payments_vacate2/<id>', branch2.july_make_payments_vacate2, name='july_make_payments_vacate2'),
    path('aug_make_payments_vacate2/<id>', branch2.aug_make_payments_vacate2, name='aug_make_payments_vacate2'),

    path('sept_make_payments_vacate2/<id>', branch2.sept_make_payments_vacate2, name='sept_make_payments_vacate2'),
    path('oct_make_payments_vacate2/<id>', branch2.oct_make_payments_vacate2, name='oct_make_payments_vacate2'),
    path('nov_make_payments_vacate2/<id>', branch2.nov_make_payments_vacate2, name='nov_make_payments_vacate2'),
    path('dec_make_payments_vacate2/<id>', branch2.dec_make_payments_vacate2, name='dec_make_payments_vacate2'),

#********vacate guest payments end here**********

##################################
#VACATE GUEST DETAILS END HERE
################################



##################################
#PRINT OUTS START HERE
################################

    path('detail_guest_general2/',branch2.detail_guest_general2,name='detail_guest_general2'),

    path('jan_print2/',branch2.jan_print2,name='jan_print2'),
    path('feb_print2/',branch2.feb_print2,name='feb_print2'),
    path('march_print2/',branch2.march_print2,name='march_print2'),
    path('april_print2/',branch2.april_print2,name='april_print2'),

    path('may_print2/',branch2.may_print2,name='may_print2'),
    path('june_print2/',branch2.june_print2,name='june_print2'),
    path('july_print2/', branch2.july_print2, name='july_print2'),
    path('aug_print2/', branch2.aug_print2, name='aug_print2'),

    path('sept_print2/', branch2.sept_print2, name='sept_print2'),
    path('oct_print2/', branch2.oct_print2, name='oct_print2'),
    path('nov_print2/', branch2.nov_print2, name='nov_print2'),
    path('dec_print2/', branch2.dec_print2, name='dec_print2'),

##################################
#PRINT OUTS END HERE
################################

    path('jan_close2/', branch2.jan_close2, name='jan_close2'),
    path('jan_close_decision_page2/', branch2.jan_close_decision_page2, name='jan_close_decision_page2'),
    path('feb_close/', branch2.feb_close2, name='feb_close2'),
    path('feb_close_decision_page2/', branch2.feb_close_decision_page2, name='feb_close_decision_page2'),
    path('mar_close2/', branch2.mar_close2, name='mar_close2'),
    path('mar_close_decision_page/', branch2.mar_close_decision_page2, name='mar_close_decision_page2'),
    path('apr_close2/', branch2.apr_close2, name='apr_close2'),
    path('apr_close_decision_page2/', branch2.apr_close_decision_page2, name='apr_close_decision_page2'),

    path('may_close2/', branch2.may_close2, name='may_close2'),
    path('may_close_decision_page2/', branch2.may_close_decision_page2, name='may_close_decision_page2'),
    path('jun_close2/', branch2.jun_close2, name='jun_close2'),
    path('jun_close_decision_page2/', branch2.jun_close_decision_page2, name='jun_close_decision_page2'),
    path('jul_close2/', branch2.jul_close2, name='jul_close2'),
    path('jul_close_decision_page2/', branch2.jul_close_decision_page2, name='jul_close_decision_page2'),
    path('aug_close2/', branch2.aug_close2, name='aug_close2'),
    path('aug_close_decision_page2/', branch2.aug_close_decision_page2, name='aug_close_decision_page2'),

    path('sep_close2/', branch2.sep_close2, name='sep_close2'),
    path('sep_close_decision_page2/', branch2.sep_close_decision_page2, name='sep_close_decision_page2'),
    path('oct_close2/', branch2.oct_close2, name='oct_close2'),
    path('oct_close_decision_page2/', branch2.oct_close_decision_page2, name='oct_close_decision_page2'),
    path('nov_close2/', branch2.nov_close2, name='nov_close2'),
    path('nov_close_decision_page2/', branch2.nov_close_decision_page2, name='nov_close_decision_page2'),

    path('detailed_report_choose_months2/', reports2.detailed_report_choose_months2,name='detailed_report_choose_months2'),
    path('may_print_live2/', reports2.may_print_live2, name='may_print_live2'),
    path('june_dtails_live2/', reports2.june_dtails_live2, name='june_dtails_live2'),
    path('june_print_live2/', reports2.june_print_live2, name='june_print_live2'),
    path('viewall_vaccant_room2/', reports2.viewall_vaccant_room2, name='viewall_vaccant_room2'),



########################################
# DUE AMT MANAGEMENT START HERE
###########################

    path('view_all_due_amt2/', branch2.view_all_due_amt2, name='view_all_due_amt2'),
    path('due_amt_mgt_choose_months2/', branch2.due_amt_mgt_choose_months2, name='due_amt_mgt_choose_months2'),

    path('view_may_account_details2/',branch2.view_may_account_details2,name='view_may_account_details2'),
    path('may_account_mgt2/<id>', branch2.may_account_mgt2, name='may_account_mgt2'),

    path('view_june_account_details2/', branch2.view_june_account_details2, name='view_june_account_details2'),
    path('june_account_mgt2/<id>',branch2.june_account_mgt2,name='june_account_mgt2'),
    path('view_july_account_details2/', branch2.view_july_account_details2, name='view_july_account_details2'),
    path('july_account_mgt2/<id>',branch2.july_account_mgt2,name='july_account_mgt2'),

########################################
# DUE AMT MANAGEMENT END HERE
###########################



]