from django.contrib import admin
from django.urls import path
from . import views
from . import branch1
from . import branch2
from . import branch3

urlpatterns = [
    path('', views.index, name='index'),
    path('login_request/', views.login_request, name='login_request'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # ****user start here *****
    path('view_all_users/', views.view_all_users, name='view_all_users'),
    path('create_user/', views.create_user, name='create_user'),
    path('user_regi/', views.user_regi, name='user_regi'),
    path('delete_user/<id>', views.delete_user, name='delete_user'),
    path('user_update/<id>', views.user_update, name='user_update'),
    # ****user end here ******

    path('registration_form_create/',views.registration_form_create,name='registration_form_create'),
    path('update_registration_form/',views.update_registration_form,name='update_registration_form'),

#**room creation start here

    path('select_branch/',views.select_branch,name='select_branch'),
    path('branch1_room_create_regi/',views.branch1_room_create_regi,name='branch1_room_create_regi'),
    path('view_all_rooms/',views.view_all_rooms,name='view_all_rooms'),
    path('delete_room/<id>',views.delete_room,name='delete_room'),

    path('branch1_room_create/',views.branch1_room_create,name='branch1_room_create'),


#**room creation end here

#****************************************************************************************************
#head office Reports start HERE
#***********************************

#**unpadid start here**

    path('select_month_all_branch_unpaid_rent/', views.select_month_all_branch_unpaid_rent, name='select_month_all_branch_unpaid_rent'),
    path('all_branch_unpaid_rent/', views.all_branch_unpaid_rent, name='all_branch_unpaid_rent'),

    path('all_jan_unpaid_rent/', views.all_jan_unpaid_rent, name='all_jan_unpaid_rent'),
    path('all_feb_unpaid_rent/', views.all_feb_unpaid_rent, name='all_feb_unpaid_rent'),
    path('all_mar_unpaid_rent/', views.all_mar_unpaid_rent, name='all_mar_unpaid_rent'),
    path('all_april_unpaid_rent/', views.all_april_unpaid_rent, name='all_april_unpaid_rent'),

    path('all_may_unpaid_rent/', views.all_may_unpaid_rent, name='all_may_unpaid_rent'),
    path('all_june_unpaid_rent/', views.all_june_unpaid_rent, name='all_june_unpaid_rent'),
    path('all_july_unpaid_rent/', views.all_july_unpaid_rent, name='all_july_unpaid_rent'),
    path('all_aug_unpaid_rent/', views.all_aug_unpaid_rent, name='all_aug_unpaid_rent'),

    path('all_sept_unpaid_rent/', views.all_sept_unpaid_rent, name='all_sept_unpaid_rent'),
    path('all_oct_unpaid_rent/', views.all_oct_unpaid_rent, name='all_oct_unpaid_rent'),
    path('all_nov_unpaid_rent/', views.all_nov_unpaid_rent, name='all_nov_unpaid_rent'),
    path('all_dec_unpaid_rent/', views.all_dec_unpaid_rent, name='all_dec_unpaid_rent'),

#**unpaid end here**
#**paid start here

    path('select_month_all_branch_paid_rent/', views.select_month_all_branch_paid_rent, name='select_month_all_branch_paid_rent'),

    path('all_jan_paid_rent/', views.all_jan_paid_rent, name='all_jan_paid_rent'),
    path('all_feb_paid_rent/', views.all_feb_paid_rent, name='all_feb_paid_rent'),
    path('all_mar_paid_rent/', views.all_mar_paid_rent, name='all_mar_paid_rent'),
    path('all_april_paid_rent/', views.all_april_paid_rent, name='all_april_paid_rent'),

    path('all_may_paid_rent/', views.all_may_paid_rent, name='all_may_paid_rent'),
    path('all_june_paid_rent/', views.all_june_paid_rent, name='all_june_paid_rent'),
    path('all_july_paid_rent/', views.all_july_paid_rent, name='all_july_paid_rent'),
    path('all_aug_paid_rent/', views.all_aug_paid_rent, name='all_aug_paid_rent'),

    path('all_sept_paid_rent/', views.all_sept_paid_rent, name='all_sept_paid_rent'),
    path('all_oct_paid_rent/', views.all_oct_paid_rent, name='all_oct_paid_rent'),
    path('all_nov_paid_rent/', views.all_nov_paid_rent, name='all_nov_paid_rent'),
    path('all_dec_paid_rent/', views.all_dec_paid_rent, name='all_dec_paid_rent'),

    #**paid end here

#****************************************************************************************************
#head office Reports  HERE
#***********************************

#****************************************************************************************************
#BRANCH ONE START HERE
#***********************************

    path('branch_index/',branch1.branch_index,name='branch_index'),

    path('guest_creation/',branch1.guest_creation,name='guest_creation'),
    path('guest_creation_regi/', branch1.guest_creation_regi, name='guest_creation_regi'),
    path('view_all_guests/',branch1.view_all_guests,name='view_all_guests'),
    path('update_guest_creation/<id>', branch1.update_guest_creation, name='update_guest_creation'),

##################################
# REPORTS START HERE
################################

    path('unpaid_rent/',branch1.unpaid_rent,name='unpaid_rent'),
    path('paid_rent/',branch1.paid_rent,name='paid_rent'),

##################################
# REPORTS START HERE
################################

##################################
#PAYMENTS END HERE
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

#*********reports start here

#unpaid rent start here
    path('unpaid_rent_choose_months/',branch1.unpaid_rent_choose_months,name='unpaid_rent_choose_months'),

    path('jan_unpaid_rent/', branch1.jan_unpaid_rent, name='jan_unpaid_rent'),
    path('feb_unpaid_rent/', branch1.feb_unpaid_rent, name='feb_unpaid_rent'),
    path('mar_unpaid_rent/', branch1.mar_unpaid_rent, name='mar_unpaid_rent'),
    path('april_unpaid_rent/', branch1.april_unpaid_rent, name='april_unpaid_rent'),

    path('may_unpaid_rent/', branch1.may_unpaid_rent, name='may_unpaid_rent'),
    path('june_unpaid_rent/', branch1.june_unpaid_rent, name='june_unpaid_rent'),
    path('july_unpaid_rent/', branch1.july_unpaid_rent, name='july_unpaid_rent'),
    path('aug_unpaid_rent/', branch1.aug_unpaid_rent, name='aug_unpaid_rent'),

    path('sept_unpaid_rent/', branch1.sept_unpaid_rent, name='sept_unpaid_rent'),
    path('oct_unpaid_rent/', branch1.oct_unpaid_rent, name='oct_unpaid_rent'),
    path('nov_unpaid_rent/', branch1.nov_unpaid_rent, name='nov_unpaid_rent'),
    path('dec_unpaid_rent/', branch1.dec_unpaid_rent, name='dec_unpaid_rent'),

#unpaid rent end here

#paid rent start here
    path('paid_rent_choose_months/',branch1.paid_rent_choose_months,name='paid_rent_choose_months'),

    path('jan_paid_rent/', branch1.jan_paid_rent, name='jan_paid_rent'),
    path('feb_paid_rent/', branch1.feb_paid_rent, name='feb_paid_rent'),
    path('mar_paid_rent/', branch1.mar_paid_rent, name='mar_paid_rent'),
    path('april_paid_rent/', branch1.april_paid_rent, name='april_paid_rent'),

    path('may_paid_rent/', branch1.may_paid_rent, name='may_paid_rent'),
    path('june_paid_rent/', branch1.june_paid_rent, name='june_paid_rent'),
    path('july_paid_rent/', branch1.july_paid_rent, name='july_paid_rent'),
    path('aug_paid_rent/', branch1.aug_paid_rent, name='aug_paid_rent'),

    path('sept_paid_rent/', branch1.sept_paid_rent, name='sept_paid_rent'),
    path('oct_paid_rent/', branch1.oct_paid_rent, name='oct_paid_rent'),
    path('nov_paid_rent/', branch1.nov_paid_rent, name='nov_paid_rent'),
    path('dec_paid_rent/', branch1.dec_paid_rent, name='dec_paid_rent'),

#paid rent end here


#*********reports end here

##################################
#PAYMENTS END HERE
################################

#****************************************************************************************************
#BRANCH ONE END HERE
#***********************************
#****************************************************************************************************
#BRANCH TWO START HERE
#***********************************

    path('branch_index2/', branch2.branch_index, name='branch_index'),

    path('guest_creation2/', branch2.guest_creation, name='guest_creation2'),
    path('guest_creation_regi2/', branch2.guest_creation_regi, name='guest_creation_regi2'),
    path('view_all_guests2/', branch2.view_all_guests, name='view_all_guests2'),
    path('update_guest_creation2/<id>', branch2.update_guest_creation, name='update_guest_creation2'),

#*********reports start here

#unpaid rent start here
    path('unpaid_rent_choose_months2/',branch2.unpaid_rent_choose_months,name='unpaid_rent_choose_months2'),

    path('jan_unpaid_rent2/', branch2.jan_unpaid_rent, name='jan_unpaid_rent2'),
    path('feb_unpaid_rent2/', branch2.feb_unpaid_rent, name='feb_unpaid_rent2'),
    path('mar_unpaid_rent2/', branch2.mar_unpaid_rent, name='mar_unpaid_rent2'),
    path('april_unpaid_rent2/', branch2.april_unpaid_rent, name='april_unpaid_rent2'),

    path('may_unpaid_rent2/', branch2.may_unpaid_rent, name='may_unpaid_rent2'),
    path('june_unpaid_rent2/', branch2.june_unpaid_rent, name='june_unpaid_rent2'),
    path('july_unpaid_rent2/', branch2.july_unpaid_rent, name='july_unpaid_rent2'),
    path('aug_unpaid_rent2/', branch2.aug_unpaid_rent, name='aug_unpaid_rent2'),

    path('sept_unpaid_rent2/', branch2.sept_unpaid_rent, name='sept_unpaid_rent2'),
    path('oct_unpaid_rent2/', branch2.oct_unpaid_rent, name='oct_unpaid_rent2'),
    path('nov_unpaid_rent2/', branch2.nov_unpaid_rent, name='nov_unpaid_rent2'),
    path('dec_unpaid_rent2/', branch2.dec_unpaid_rent, name='dec_unpaid_rent2'),

#unpaid rent end here

#paid rent start here
    path('paid_rent_choose_months2/',branch2.paid_rent_choose_months,name='paid_rent_choose_months2'),

    path('jan_paid_rent2/', branch2.jan_paid_rent, name='jan_paid_rent2'),
    path('feb_paid_rent2/', branch2.feb_paid_rent, name='feb_paid_rent2'),
    path('mar_paid_rent2/', branch2.mar_paid_rent, name='mar_paid_rent2'),
    path('april_paid_rent2/', branch2.april_paid_rent, name='april_paid_rent2'),

    path('may_paid_rent2/', branch2.may_paid_rent, name='may_paid_rent2'),
    path('june_paid_rent2/', branch2.june_paid_rent, name='june_paid_rent2'),
    path('july_paid_rent2/', branch2.july_paid_rent, name='july_paid_rent2'),
    path('aug_paid_rent2/', branch2.aug_paid_rent, name='aug_paid_rent2'),

    path('sept_paid_rent2/', branch2.sept_paid_rent, name='sept_paid_rent2'),
    path('oct_paid_rent2/', branch2.oct_paid_rent, name='oct_paid_rent2'),
    path('nov_paid_rent2/', branch2.nov_paid_rent, name='nov_paid_rent2'),
    path('dec_paid_rent2/', branch2.dec_paid_rent, name='dec_paid_rent2'),

#paid rent end here


#*********reports end here

#payments start here

    path('choose_months2/', branch2.choose_months, name='choose_months2'),

    path('jan2/', branch2.jan, name='jan2'),
    path('jan_manke_payments2/<id>', branch1.jan_manke_payments, name='jan_manke_payments2'),

    path('feb2/', branch2.feb, name='feb2'),
    path('feb_manke_payments2/<id>', branch2.feb_manke_payments, name='feb_manke_payments2'),

    path('march2/', branch2.march, name='march2'),
    path('march_manke_payments2/<id>', branch2.march_manke_payments, name='march_manke_payments2'),

    path('april2/', branch2.april, name='april2'),
    path('april_make_payments2/<id>', branch2.april_make_payments, name='april_make_payments2'),

    path('may2/', branch2.may, name='may2'),
    path('may_make_payments2/<id>', branch2.may_make_payments, name='may_make_payments2'),

    path('june2/', branch2.june, name='june2'),
    path('june_make_payments2/<id>', branch2.june_make_payments, name='june_make_payments2'),

    path('july2/', branch2.july, name='july2'),
    path('july_make_payments2/<id>', branch2.july_make_payments, name='july_make_payments2'),

    path('aug2/', branch2.aug, name='aug2'),
    path('aug_make_payments2/<id>', branch2.aug_make_payments, name='aug_make_payments2'),

    path('sept2/', branch2.sept, name='sept2'),
    path('sept_make_payments2/<id>', branch2.sept_make_payments, name='sept_make_payments2'),

    path('oct2/', branch2.oct, name='oct2'),
    path('oct_make_payments2/<id>', branch2.oct_make_payments, name='oct_make_payments2'),

    path('nov2/', branch2.nov, name='nov2'),
    path('nov_make_payments2/<id>', branch2.nov_make_payments, name='nov_make_payments2'),

    path('dec2/', branch2.dec, name='dec2'),
    path('dec_make_payments2/<id>', branch2.dec_make_payments, name='dec_make_payments2'),

    #payments end here



#****************************************************************************************************
#BRANCH TWO END HERE
#***********************************

#****************************************************************************************************
#BRANCH THREE START HERE
#***********************************

    path('branch_index3/', branch3.branch_index, name='branch_index3'),

    path('guest_creation3/', branch3.guest_creation, name='guest_creation3'),
    path('guest_creation_regi3/', branch3.guest_creation_regi, name='guest_creation_regi3'),
    path('view_all_guests3/', branch3.view_all_guests, name='view_all_guests3'),
    path('update_guest_creation3/<id>', branch3.update_guest_creation, name='update_guest_creation3'),

#*********reports start here

#unpaid rent start here
    path('unpaid_rent_choose_months3/',branch3.unpaid_rent_choose_months,name='unpaid_rent_choose_months3'),

    path('jan_unpaid_rent3/', branch3.jan_unpaid_rent, name='jan_unpaid_rent3'),
    path('feb_unpaid_rent3/', branch3.feb_unpaid_rent, name='feb_unpaid_rent3'),
    path('mar_unpaid_rent3/', branch3.mar_unpaid_rent, name='mar_unpaid_rent3'),
    path('april_unpaid_rent3/', branch3.april_unpaid_rent, name='april_unpaid_rent3'),

    path('may_unpaid_rent3/', branch3.may_unpaid_rent, name='may_unpaid_rent3'),
    path('june_unpaid_rent3/', branch3.june_unpaid_rent, name='june_unpaid_rent3'),
    path('july_unpaid_rent3/', branch3.july_unpaid_rent, name='july_unpaid_rent3'),
    path('aug_unpaid_rent3/', branch3.aug_unpaid_rent, name='aug_unpaid_rent3'),

    path('sept_unpaid_rent3/', branch3.sept_unpaid_rent, name='sept_unpaid_rent3'),
    path('oct_unpaid_rent3/', branch3.oct_unpaid_rent, name='oct_unpaid_rent3'),
    path('nov_unpaid_rent3/', branch3.nov_unpaid_rent, name='nov_unpaid_rent3'),
    path('dec_unpaid_rent3/', branch3.dec_unpaid_rent, name='dec_unpaid_rent3'),

#unpaid rent end here

#paid rent start here
    path('paid_rent_choose_months3/',branch3.paid_rent_choose_months,name='paid_rent_choose_months3'),

    path('jan_paid_rent3/', branch3.jan_paid_rent, name='jan_paid_rent3'),
    path('feb_paid_rent3/', branch3.feb_paid_rent, name='feb_paid_rent3'),
    path('mar_paid_rent3/', branch3.mar_paid_rent, name='mar_paid_rent3'),
    path('april_paid_rent3/', branch3.april_paid_rent, name='april_paid_rent3'),

    path('may_paid_rent3/', branch3.may_paid_rent, name='may_paid_rent3'),
    path('june_paid_rent3/', branch3.june_paid_rent, name='june_paid_rent3'),
    path('july_paid_rent3/', branch3.july_paid_rent, name='july_paid_rent3'),
    path('aug_paid_rent3/', branch3.aug_paid_rent, name='aug_paid_rent3'),

    path('sept_paid_rent3/', branch3.sept_paid_rent, name='sept_paid_rent3'),
    path('oct_paid_rent3/', branch3.oct_paid_rent, name='oct_paid_rent3'),
    path('nov_paid_rent3/', branch3.nov_paid_rent, name='nov_paid_rent3'),
    path('dec_paid_rent3/', branch3.dec_paid_rent, name='dec_paid_rent3'),

#paid rent end here


#*********reports end here

#payments start here

    path('choose_months3/', branch3.choose_months, name='choose_months3'),

    path('jan3/', branch3.jan, name='jan3'),
    path('jan_manke_payments3/<id>', branch1.jan_manke_payments, name='jan_manke_payments3'),

    path('feb3/', branch3.feb, name='feb3'),
    path('feb_manke_payments3/<id>', branch3.feb_manke_payments, name='feb_manke_payments3'),

    path('march3/', branch3.march, name='march3'),
    path('march_manke_payments3/<id>', branch3.march_manke_payments, name='march_manke_payments3'),

    path('april3/', branch3.april, name='april3'),
    path('april_make_payments3/<id>', branch3.april_make_payments, name='april_make_payments3'),

    path('may3/', branch3.may, name='may3'),
    path('may_make_payments3/<id>', branch3.may_make_payments, name='may_make_payments3'),

    path('june3/', branch3.june, name='june3'),
    path('june_make_payments3/<id>', branch3.june_make_payments, name='june_make_payments3'),

    path('july3/', branch3.july, name='july3'),
    path('july_make_payments3/<id>', branch3.july_make_payments, name='july_make_payments3'),

    path('aug3/', branch3.aug, name='aug3'),
    path('aug_make_payments2/<id>', branch3.aug_make_payments, name='aug_make_payments3'),

    path('sept3/', branch3.sept, name='sept3'),
    path('sept_make_payments2/<id>', branch3.sept_make_payments, name='sept_make_payments3'),

    path('oct3/', branch3.oct, name='oct3'),
    path('oct_make_payments3/<id>', branch3.oct_make_payments, name='oct_make_payments3'),

    path('nov3/', branch3.nov, name='nov3'),
    path('nov_make_payments3/<id>', branch3.nov_make_payments, name='nov_make_payments3'),

    path('dec3/', branch3.dec, name='dec3'),
    path('dec_make_payments3/<id>', branch3.dec_make_payments, name='dec_make_payments3'),

    #payments end here



#****************************************************************************************************
#BRANCH THREE END HERE
#***********************************

    path('logout/',views.logout,name='logout'),


]