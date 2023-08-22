from django.urls import path, include

# from . import admin_branch9
#from . import admin_branch9
from . import branch10
#from . import reports9
#from . import payment9
#from . import admin_dashboard_calculations_br9
from . import accounts10

urlpatterns = [

    path('branch1_dashboard10/', branch10.branch1_dashboard10, name='branch1_dashboard10'),


#####********************************************************************************************************
#ACCOUNTS START HERE
####***************************************************


#########################################################
###******CREATER MASTER START HERE
###################################################################################


##******************CATERGORY CREATER START HERE

    path('view_all_category10/', accounts10.view_all_category10, name='view_all_category10'),
    path('create_new_category10/', accounts10.create_new_category10, name='create_new_category10'),
    path('regi_new_category10/', accounts10.regi_new_category10, name='regi_new_category10'),
    path('update_category10/<id>',accounts10.update_category10,name='update_category10'),

    path('delete_category10/<id>', accounts10.delete_category10, name='delete_category10'),
    path('view_all_category_delete10/', accounts10.view_all_category_delete10, name='view_all_category_delete10'),

    ##*****************CATERY CREATER END HERE


##******************ITEM CREATER START HERE

    path('view_all_items10/', accounts10.view_all_items10, name='view_all_items10'),
    path('create_new_item10/', accounts10.create_new_item10, name='create_new_item10'),
    path('regi_new_item10/', accounts10.regi_new_item10, name='regi_new_item10'),
    path('delete_item10/<id>',accounts10.delete_item10,name='delete_item10'),
    path('update_item10/<id>', accounts10.update_item10, name='update_item10'),
    path('view_all_items_delete10/',accounts10.view_all_items_delete10,name='view_all_items_delete10'),

    ##*****************ITEM CREATER END HERE


##******************LEDGER CREATER START HERE

    path('view_all_ledger10/', accounts10.view_all_ledger10, name='view_all_ledger10'),
    path('create_new_ledger10/', accounts10.create_new_ledger10, name='create_new_ledger10'),
    path('regi_new_ledger10/', accounts10.regi_new_ledger10, name='regi_new_ledger10'),
    path('delete_ledger10/<id>',accounts10.delete_ledger10,name='delete_ledger10'),
    path('update_ledger10/<id>',accounts10.update_ledger10,name='update_ledger10'),
    path('view_all_ledger_delete10/',accounts10.view_all_ledger_delete10,name='view_all_ledger_delete10'),

##*****************LEDGER CREATER END HERE


##******************ACCOUNTS_BOOK CREATER START HERE

    path('view_all_accounts_book10/', accounts10.view_all_accounts_book10, name='view_all_accounts_book10'),
    path('create_new_accounts_book10/', accounts10.create_new_accounts_book10, name='create_new_accounts_book10'),
    path('regi_new_accounts_book10/', accounts10.regi_new_accounts_book10, name='regi_new_accounts_book10'),
    path('update_accounts_book10/<id>',accounts10.update_accounts_book10,name='update_accounts_book10'),
    path('delete_accounts_book10/<id>',accounts10.delete_accounts_book10,name='delete_accounts_book10'),
    path('view_all_accounts_book_delete10/',accounts10.view_all_accounts_book_delete10,name='view_all_accounts_book_delete10'),

##*****************ACCOUNTS_BOOK CREATER END HERE


#########################################################
###******CREATER MASTER END HERE
###################################################################################

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER START HERE
###################################################################################

    path('get_countries10/', accounts10.get_countries10, name='get_countries10'),

    path('in_exp_items_entry10/', accounts10.in_exp_items_entry10, name='in_exp_items_entry10'),
    path('reg_in_exp_items_entry10/', accounts10.reg_in_exp_items_entry10, name='reg_in_exp_items_entry10'),
    path('delete_journal10/<id>',accounts10.delete_journal10,name='delete_journal10'),
    path('update_in_exp_items_entry10/<id>',accounts10.update_in_exp_items_entry10,name='update_in_exp_items_entry10'),
    path('detailed_journal_report10/',accounts10.detailed_journal_report10,name='detailed_journal_report10'),
    path('journal_report_deleted10/',accounts10.journal_report_deleted10,name='journal_report_deleted10'),

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER END HERE
###################################################################################
#########*******************************************************************************************************************
#########################################################
###******ALL REPORTS  START HERE
###################################################################################


###************* CATEGORY WISE REPORTS  START HERE

    path('daily_category_wise10/', accounts10.daily_category_wise10, name='daily_category_wise10'),
    path('monthly_category_based_reports10/',accounts10.monthly_category_based_reports10,name='monthly_category_based_reports10'),
    path('yearly_category_based_reports10/', accounts10.yearly_category_based_reports10,name='yearly_category_based_reports10'),


###*************CATEGORY WISE REPORTS  END HERE

###*************DAILY DETAILED REPORTS  START HERE

    path('daily_detailed10/', accounts10.daily_detailed10, name='daily_detailed10'),
    path('monthly_detailed10/',accounts10.monthly_detailed10,name='monthly_detailed10'),
    path('yearly_detailed10/',accounts10.yearly_detailed10,name='yearly_detailed10'),

###*************DAILY DETAILED REPORTS  START HERE

###*************ITEM BASED REPORTS  START HERE

    path('item_based_reports10/', accounts10.item_based_reports10, name='item_based_reports10'),
    path('daily_item_based_reports10/',accounts10.daily_item_based_reports10,name='daily_item_based_reports10'),
    path('monthly_item_based_reports10/',accounts10.monthly_item_based_reports10,name='monthly_item_based_reports10'),

###*************ITEM BASED REPORTS  START HERE

###*************LEDGER BASED REPORTS  START HERE

    path('ledger_based_reports10/', accounts10.ledger_based_reports10, name='ledger_based_reports10'),
    path('monthly_ledger_based_reports10/', accounts10.monthly_ledger_based_reports10, name='monthly_ledger_based_reports10'),
    path('daily_ledger_based_reports10/',accounts10.daily_ledger_based_reports10,name='daily_ledger_based_reports10'),

###*************LEDGER BASED REPORTS  START HERE

###*************ACCOUNTS-BOOK BASED REPORTS  START HERE

    path('accounts_book_based_reports10/', accounts10.accounts_book_based_reports10, name='accounts_book_based_reports10'),
    path('daily_accounts_book_based_reports10/',accounts10.daily_accounts_book_based_reports10,name='daily_accounts_book_based_reports10'),
    path('monthly_accounts_book_based_reports10/',accounts10.monthly_accounts_book_based_reports10,name='monthly_accounts_book_based_reports10'),

###*************ACCOUNTS-BOOK BASED REPORTS  END HERE



#########################################################
###******ALL REPORTS  END HERE
###################################################################################

    path('monthly_reports_choose_months10/', accounts10.monthly_reports_choose_months10, name='monthly_reports_choose_months10'),
    path('monthly_detailed_daily_in_exp_items_report10/<mo>',accounts10.monthly_detailed_daily_in_exp_items_report10,name='monthly_detailed_daily_in_exp_items_report10'),

    path('single_monthly_reports_choose_months10/', accounts10.single_monthly_reports_choose_months10,name='single_monthly_reports_choose_months10'),
    path('single_monthly_daily_in_exp_items_report10/<mo>',accounts10.single_monthly_daily_in_exp_items_report10,name='single_monthly_daily_in_exp_items_report10'),

    path('accounts_dash_board10/',accounts10.accounts_dash_board10,name='accounts_dash_board10'),





]