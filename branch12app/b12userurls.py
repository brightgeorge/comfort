from django.urls import path, include

# from . import admin_branch9
#from . import admin_branch9
from . import branch12
#from . import reports9
#from . import payment9
#from . import admin_dashboard_calculations_br9
from . import accounts12

urlpatterns = [

    path('branch1_dashboard12/', branch12.branch1_dashboard12, name='branch1_dashboard12'),



#####********************************************************************************************************
#ACCOUNTS START HERE
####***************************************************


#########################################################
###******CREATER MASTER START HERE
###################################################################################


##******************CATERGORY CREATER START HERE

    path('view_all_category12/', accounts12.view_all_category12, name='view_all_category12'),
    path('create_new_category12/', accounts12.create_new_category12, name='create_new_category12'),
    path('regi_new_category12/', accounts12.regi_new_category12, name='regi_new_category12'),
    path('update_category12/<id>',accounts12.update_category12,name='update_category12'),

    path('delete_category12/<id>', accounts12.delete_category12, name='delete_category12'),
    path('view_all_category_delete12/', accounts12.view_all_category_delete12, name='view_all_category_delete12'),

    ##*****************CATERY CREATER END HERE


##******************ITEM CREATER START HERE

    path('view_all_items12/', accounts12.view_all_items12, name='view_all_items12'),
    path('create_new_item12/', accounts12.create_new_item12, name='create_new_item12'),
    path('regi_new_item12/', accounts12.regi_new_item12, name='regi_new_item12'),
    path('delete_item12/<id>',accounts12.delete_item12,name='delete_item12'),
    path('update_item12/<id>', accounts12.update_item12, name='update_item12'),
    path('view_all_items_delete12/',accounts12.view_all_items_delete12,name='view_all_items_delete12'),

    ##*****************ITEM CREATER END HERE


##******************LEDGER CREATER START HERE

    path('view_all_ledger12/', accounts12.view_all_ledger12, name='view_all_ledger12'),
    path('create_new_ledger12/', accounts12.create_new_ledger12, name='create_new_ledger12'),
    path('regi_new_ledger12/', accounts12.regi_new_ledger12, name='regi_new_ledger12'),
    path('delete_ledger12/<id>',accounts12.delete_ledger12,name='delete_ledger12'),
    path('update_ledger12/<id>',accounts12.update_ledger12,name='update_ledger12'),
    path('view_all_ledger_delete12/',accounts12.view_all_ledger_delete12,name='view_all_ledger_delete12'),

##*****************LEDGER CREATER END HERE


##******************ACCOUNTS_BOOK CREATER START HERE

    path('view_all_accounts_book12/', accounts12.view_all_accounts_book12, name='view_all_accounts_book12'),
    path('create_new_accounts_book12/', accounts12.create_new_accounts_book12, name='create_new_accounts_book12'),
    path('regi_new_accounts_book12/', accounts12.regi_new_accounts_book12, name='regi_new_accounts_book12'),
    path('update_accounts_book12/<id>',accounts12.update_accounts_book12,name='update_accounts_book12'),
    path('delete_accounts_book12/<id>',accounts12.delete_accounts_book12,name='delete_accounts_book12'),
    path('view_all_accounts_book_delete12/',accounts12.view_all_accounts_book_delete12,name='view_all_accounts_book_delete12'),

##*****************ACCOUNTS_BOOK CREATER END HERE


#########################################################
###******CREATER MASTER END HERE
###################################################################################

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER START HERE
###################################################################################

    path('get_countries12/', accounts12.get_countries12, name='get_countries12'),

    path('in_exp_items_entry12/', accounts12.in_exp_items_entry12, name='in_exp_items_entry12'),
    path('reg_in_exp_items_entry12/', accounts12.reg_in_exp_items_entry12, name='reg_in_exp_items_entry12'),
    path('delete_journal12/<id>',accounts12.delete_journal12,name='delete_journal12'),
    path('update_in_exp_items_entry12/<id>',accounts12.update_in_exp_items_entry12,name='update_in_exp_items_entry12'),
    path('detailed_journal_report12/',accounts12.detailed_journal_report12,name='detailed_journal_report12'),
    path('journal_report_deleted12/',accounts12.journal_report_deleted12,name='journal_report_deleted12'),

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER END HERE
###################################################################################
#########*******************************************************************************************************************
#########################################################
###******ALL REPORTS  START HERE
###################################################################################


###************* CATEGORY WISE REPORTS  START HERE

    path('daily_category_wise12/', accounts12.daily_category_wise12, name='daily_category_wise12'),
    path('monthly_category_based_reports12/',accounts12.monthly_category_based_reports12,name='monthly_category_based_reports12'),
    path('yearly_category_based_reports12/', accounts12.yearly_category_based_reports12,name='yearly_category_based_reports12'),


###*************CATEGORY WISE REPORTS  END HERE

###*************DAILY DETAILED REPORTS  START HERE

    path('daily_detailed12/', accounts12.daily_detailed12, name='daily_detailed12'),
    path('monthly_detailed12/',accounts12.monthly_detailed12,name='monthly_detailed12'),
    path('yearly_detailed12/',accounts12.yearly_detailed12,name='yearly_detailed12'),

###*************DAILY DETAILED REPORTS  START HERE

###*************ITEM BASED REPORTS  START HERE

    path('item_based_reports12/', accounts12.item_based_reports12, name='item_based_reports12'),
    path('daily_item_based_reports12/',accounts12.daily_item_based_reports12,name='daily_item_based_reports12'),
    path('monthly_item_based_reports12/',accounts12.monthly_item_based_reports12,name='monthly_item_based_reports12'),

###*************ITEM BASED REPORTS  START HERE

###*************LEDGER BASED REPORTS  START HERE

    path('ledger_based_reports12/', accounts12.ledger_based_reports12, name='ledger_based_reports12'),
    path('monthly_ledger_based_reports12/', accounts12.monthly_ledger_based_reports12, name='monthly_ledger_based_reports12'),
    path('daily_ledger_based_reports12/',accounts12.daily_ledger_based_reports12,name='daily_ledger_based_reports12'),

###*************LEDGER BASED REPORTS  START HERE

###*************ACCOUNTS-BOOK BASED REPORTS  START HERE

    path('accounts_book_based_reports12/', accounts12.accounts_book_based_reports12, name='accounts_book_based_reports12'),
    path('daily_accounts_book_based_reports12/',accounts12.daily_accounts_book_based_reports12,name='daily_accounts_book_based_reports12'),
    path('monthly_accounts_book_based_reports12/',accounts12.monthly_accounts_book_based_reports12,name='monthly_accounts_book_based_reports12'),

###*************ACCOUNTS-BOOK BASED REPORTS  END HERE



#########################################################
###******ALL REPORTS  END HERE
###################################################################################

    path('monthly_reports_choose_months12/', accounts12.monthly_reports_choose_months12, name='monthly_reports_choose_months12'),
    path('monthly_detailed_daily_in_exp_items_report12/<mo>',accounts12.monthly_detailed_daily_in_exp_items_report12,name='monthly_detailed_daily_in_exp_items_report12'),

    path('single_monthly_reports_choose_months12/', accounts12.single_monthly_reports_choose_months12,name='single_monthly_reports_choose_months12'),
    path('single_monthly_daily_in_exp_items_report12/<mo>',accounts12.single_monthly_daily_in_exp_items_report12,name='single_monthly_daily_in_exp_items_report12'),

    path('accounts_dash_board12/',accounts12.accounts_dash_board12,name='accounts_dash_board12'),




]