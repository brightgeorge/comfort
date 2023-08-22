import datetime as datetime
from django.shortcuts import render
from django.contrib import messages

# from myapp.models import *pg1_new_beds
from branch10app.models import *
# from branch9app.models import pg1_new_beds,pg1_new_guest
import datetime
#from . import admin_dashboard_calculations_br9
import branch9app

database_name = 'cpg'
database_password = '#123.com#'
# database_password = ''
database_user = 'root'
database_host = 'localhost'

import pymysql as py
import pymysql.cursors


def branch1_dashboard10(request):
    if 'username' in request.session:
        us = request.session['username']
        #a = admin_dashboard_calculations_br9.grand_total_collection()
        #from datetime import datetime
        #cmm = datetime.now().month
        #cm = cmm - 1
        #gtc = a[cm]


        us = request.session['username']
        bgs = background_color.objects.all().filter(username=us)
        bg = background_color.objects.all().filter(username=us).exists()
        a = []
        if bg == True:
            a.append(us)
        else:
            a.append('f')

        context = {
            'bg': bgs,
            'us': us,
            'th_us': a[0],
            'name': us,


            'name': us,
            #'total_count_active_guests': admin_dashboard_calculations_br9.total_count_active_guests(),
            #'total_count_vaccant_rooms': admin_dashboard_calculations_br9.total_count_vaccant_rooms(),
            #'grand_total_collection': gtc,
            #'total_collection_advance': admin_dashboard_calculations_br9.total_collection_advance(),
            #'total_discount': admin_dashboard_calculations_br9.total_discount(),

            #'total_colatable_amount': admin_dashboard_calculations_br9.total_colatable_amount(),
            #'total_collected_amount': admin_dashboard_calculations_br9.total_collected_amount(),
            #'total_due': admin_dashboard_calculations_br9.total_due(),
            #'l': admin_dashboard_calculations_br9.grand_total(),
            # 'total_collection_discount_june' : admin_dashboard_calculations_br9.total_collection_discount_june(),
            #'y': admin_dashboard_calculations_br9.bar_chart(),
        }

    return render(request, 'branches/branch10/branch1index.html', context)
    return render(request, 'index.html')

