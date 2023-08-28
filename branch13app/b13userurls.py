from django.urls import path, include

# from . import admin_branch9
#from . import admin_branch9
from . import branch13
#from . import reports9
#from . import payment9
#from . import admin_dashboard_calculations_br9
from . import accounts13

urlpatterns = [

    path('branch1_dashboard13/', branch13.branch1_dashboard13, name='branch1_dashboard13'),



#####********************************************************************************************************
#ACCOUNTS START HERE
####***************************************************


#########################################################
###******CREATER MASTER START HERE
###################################################################################


##******************CATERGORY CREATER START HERE

    path('view_all_category13/', accounts13.view_all_category13, name='view_all_category13'),
    path('create_new_category13/', accounts13.create_new_category13, name='create_new_category13'),
    path('regi_new_category13/', accounts13.regi_new_category13, name='regi_new_category13'),
    path('update_category13/<id>',accounts13.update_category13,name='update_category13'),

    path('delete_category13/<id>', accounts13.delete_category13, name='delete_category13'),
    path('view_all_category_delete13/', accounts13.view_all_category_delete13, name='view_all_category_delete13'),

    ##*****************CATERY CREATER END HERE


##******************ITEM CREATER START HERE

    path('view_all_items13/', accounts13.view_all_items13, name='view_all_items13'),
    path('create_new_item13/', accounts13.create_new_item13, name='create_new_item13'),
    path('regi_new_item13/', accounts13.regi_new_item13, name='regi_new_item13'),
    path('delete_item13/<id>',accounts13.delete_item13,name='delete_item13'),
    path('update_item13/<id>', accounts13.update_item13, name='update_item13'),
    path('view_all_items_delete13/',accounts13.view_all_items_delete13,name='view_all_items_delete13'),

    ##*****************ITEM CREATER END HERE


##******************LEDGER CREATER START HERE

    path('view_all_ledger13/', accounts13.view_all_ledger13, name='view_all_ledger13'),
    path('create_new_ledger13/', accounts13.create_new_ledger13, name='create_new_ledger13'),
    path('regi_new_ledger13/', accounts13.regi_new_ledger13, name='regi_new_ledger13'),
    path('delete_ledger13/<id>',accounts13.delete_ledger13,name='delete_ledger13'),
    path('update_ledger13/<id>',accounts13.update_ledger13,name='update_ledger13'),
    path('view_all_ledger_delete13/',accounts13.view_all_ledger_delete13,name='view_all_ledger_delete13'),

##*****************LEDGER CREATER END HERE


##******************ACCOUNTS_BOOK CREATER START HERE

    path('view_all_accounts_book13/', accounts13.view_all_accounts_book13, name='view_all_accounts_book13'),
    path('create_new_accounts_book13/', accounts13.create_new_accounts_book13, name='create_new_accounts_book13'),
    path('regi_new_accounts_book13/', accounts13.regi_new_accounts_book13, name='regi_new_accounts_book13'),
    path('update_accounts_book13/<id>',accounts13.update_accounts_book13,name='update_accounts_book13'),
    path('delete_accounts_book13/<id>',accounts13.delete_accounts_book13,name='delete_accounts_book13'),
    path('view_all_accounts_book_delete13/',accounts13.view_all_accounts_book_delete13,name='view_all_accounts_book_delete13'),

##*****************ACCOUNTS_BOOK CREATER END HERE


#########################################################
###******CREATER MASTER END HERE
###################################################################################

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER START HERE
###################################################################################

    path('get_countries13/', accounts13.get_countries13, name='get_countries13'),

    path('in_exp_items_entry13/', accounts13.in_exp_items_entry13, name='in_exp_items_entry13'),
    path('reg_in_exp_items_entry13/', accounts13.reg_in_exp_items_entry13, name='reg_in_exp_items_entry13'),
    path('delete_journal13/<id>',accounts13.delete_journal13,name='delete_journal13'),
    path('update_in_exp_items_entry13/<id>',accounts13.update_in_exp_items_entry13,name='update_in_exp_items_entry13'),
    path('detailed_journal_report13/',accounts13.detailed_journal_report13,name='detailed_journal_report13'),
    path('journal_report_deleted13/',accounts13.journal_report_deleted13,name='journal_report_deleted13'),

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER END HERE
###################################################################################
#########*******************************************************************************************************************
#########################################################
###******ALL REPORTS  START HERE
###################################################################################


###************* CATEGORY WISE REPORTS  START HERE

    path('daily_category_wise13/', accounts13.daily_category_wise13, name='daily_category_wise13'),
    path('monthly_category_based_reports13/',accounts13.monthly_category_based_reports13,name='monthly_category_based_reports13'),
    path('yearly_category_based_reports13/', accounts13.yearly_category_based_reports13,name='yearly_category_based_reports13'),


###*************CATEGORY WISE REPORTS  END HERE

###*************DAILY DETAILED REPORTS  START HERE

    path('daily_detailed13/', accounts13.daily_detailed13, name='daily_detailed13'),
    path('monthly_detailed13/',accounts13.monthly_detailed13,name='monthly_detailed13'),
    path('yearly_detailed13/',accounts13.yearly_detailed13,name='yearly_detailed13'),

###*************DAILY DETAILED REPORTS  START HERE

###*************ITEM BASED REPORTS  START HERE

    path('item_based_reports13/', accounts13.item_based_reports13, name='item_based_reports13'),
    path('daily_item_based_reports13/',accounts13.daily_item_based_reports13,name='daily_item_based_reports13'),
    path('monthly_item_based_reports13/',accounts13.monthly_item_based_reports13,name='monthly_item_based_reports13'),

###*************ITEM BASED REPORTS  START HERE

###*************LEDGER BASED REPORTS  START HERE

    path('ledger_based_reports13/', accounts13.ledger_based_reports13, name='ledger_based_reports13'),
    path('monthly_ledger_based_reports13/', accounts13.monthly_ledger_based_reports13, name='monthly_ledger_based_reports13'),
    path('daily_ledger_based_reports13/',accounts13.daily_ledger_based_reports13,name='daily_ledger_based_reports13'),

###*************LEDGER BASED REPORTS  START HERE

###*************ACCOUNTS-BOOK BASED REPORTS  START HERE

    path('accounts_book_based_reports13/', accounts13.accounts_book_based_reports13, name='accounts_book_based_reports13'),
    path('daily_accounts_book_based_reports13/',accounts13.daily_accounts_book_based_reports13,name='daily_accounts_book_based_reports13'),
    path('monthly_accounts_book_based_reports13/',accounts13.monthly_accounts_book_based_reports13,name='monthly_accounts_book_based_reports13'),

###*************ACCOUNTS-BOOK BASED REPORTS  END HERE



#########################################################
###******ALL REPORTS  END HERE
###################################################################################

    path('monthly_reports_choose_months13/', accounts13.monthly_reports_choose_months13, name='monthly_reports_choose_months13'),
    path('monthly_detailed_daily_in_exp_items_report13/<mo>',accounts13.monthly_detailed_daily_in_exp_items_report13,name='monthly_detailed_daily_in_exp_items_report13'),

    path('single_monthly_reports_choose_months13/', accounts13.single_monthly_reports_choose_months13,name='single_monthly_reports_choose_months13'),
    path('single_monthly_daily_in_exp_items_report13/<mo>',accounts13.single_monthly_daily_in_exp_items_report13,name='single_monthly_daily_in_exp_items_report13'),

    path('accounts_dash_board13/',accounts13.accounts_dash_board13,name='accounts_dash_board13'),




]

