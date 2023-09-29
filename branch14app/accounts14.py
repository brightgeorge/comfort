import json

from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from branch14app.models import table1,in_exp_items_daily,opening_balance,category,ledger,accounts_book,background_color
from django.http import JsonResponse


def accounts_dash_board_ob_ch14(request):
    if 'username' in request.session:

        opening_balance = 0

        income_1 = in_exp_items_daily.objects.filter(month='01', type='income', flag=1)
        l_income_1 = []
        for i in income_1:
            l_income_1.append(float(i.amount))
        r_income_1 = sum(l_income_1)
        expense_1 = in_exp_items_daily.objects.filter(month='01', type='expense',flag=1)
        l_expense_1 = []
        for i in expense_1:
            l_expense_1.append(float(i.amount))
        r_expense_1 = sum(l_expense_1)
        r_balance_1 = opening_balance + r_income_1 - r_expense_1

        income_2 = in_exp_items_daily.objects.filter(month='02', type='income',flag=1)
        l_income_2 = []
        for i in income_2:
            l_income_2.append(float(i.amount))
        r_income_2 = sum(l_income_2)
        expense_2 = in_exp_items_daily.objects.filter(month='02', type='expense',flag=1)
        l_expense_2 = []
        for i in expense_2:
            l_expense_2.append(float(i.amount))
        r_expense_2 = sum(l_expense_2)
        r_balance_2 = r_income_2 - r_expense_2

        income_3 = in_exp_items_daily.objects.filter(month='03', type='income',flag=1)
        l_income_3 = []
        for i in income_3:
            l_income_3.append(float(i.amount))
        r_income_3 = sum(l_income_3)
        expense_3 = in_exp_items_daily.objects.filter(month='03', type='expense',flag=1)
        l_expense_3 = []
        for i in expense_3:
            l_expense_3.append(float(i.amount))
        r_expense_3 = sum(l_expense_3)
        r_balance_3 = r_income_3 - r_expense_3

        income_4 = in_exp_items_daily.objects.filter(month='04', type='income', flag=1)
        l_income_4 = []
        for i in income_4:
            l_income_4.append(float(i.amount))
        r_income_4 = sum(l_income_4)
        expense_4 = in_exp_items_daily.objects.filter(month='04', type='expense',flag=1)
        l_expense_4 = []
        for i in expense_4:
            l_expense_4.append(float(i.amount))
        r_expense_4 = sum(l_expense_4)
        r_balance_4 = r_income_4 - r_expense_4

        income_5 = in_exp_items_daily.objects.filter(month='05', type='income', flag=1)
        l_income_5 = []
        for i in income_5:
            l_income_5.append(float(i.amount))
        r_income_5 = sum(l_income_5)
        expense_5 = in_exp_items_daily.objects.filter(month='05', type='expense', flag=1)
        l_expense_5 = []
        for i in expense_5:
            l_expense_5.append(float(i.amount))
        r_expense_5 = sum(l_expense_5)
        r_balance_5 = r_income_5 - r_expense_5

        income_6 = in_exp_items_daily.objects.filter(month='06', type='income', flag=1)
        l_income_6 = []
        for i in income_6:
            l_income_6.append(float(i.amount))
        r_income_6 = sum(l_income_6)
        expense_6 = in_exp_items_daily.objects.filter(month='06', type='expense', flag=1)
        l_expense_6 = []
        for i in expense_6:
            l_expense_6.append(float(i.amount))
        r_expense_6 = sum(l_expense_6)
        r_balance_6 = +r_income_6 - r_expense_6

        income_7 = in_exp_items_daily.objects.filter(month='07', type='income',flag=1)
        l_income_7 = []
        for i in income_7:
            l_income_7.append(float(i.amount))
        r_income_7 = sum(l_income_7)
        expense_7 = in_exp_items_daily.objects.filter(month='07', type='expense',flag=1)
        l_expense_7 = []
        for i in expense_7:
            l_expense_7.append(float(i.amount))
        r_expense_7 = sum(l_expense_7)
        r_balance_7 = r_income_7 - r_expense_7
        ###***************************************
        income_8 = in_exp_items_daily.objects.filter(month='08', type='income',flag=1)
        l_income_8 = []
        for i in income_8:
            l_income_8.append(float(i.amount))
        r_income_8 = sum(l_income_8)
        expense_8 = in_exp_items_daily.objects.filter(month='08', type='expense',flag=1)
        l_expense_8 = []
        for i in expense_8:
            l_expense_8.append(float(i.amount))
        r_expense_8 = sum(l_expense_8)
        r_balance_8 = r_income_8 - r_expense_8

        income_9 = in_exp_items_daily.objects.filter(month='09', type='income',flag=1)
        l_income_9 = []
        for i in income_9:
            l_income_9.append(float(i.amount))
        r_income_9 = sum(l_income_9)
        expense_9 = in_exp_items_daily.objects.filter(month='09', type='expense',flag=1)
        l_expense_9 = []
        for i in expense_9:
            l_expense_9.append(float(i.amount))
        r_expense_9 = sum(l_expense_9)
        r_balance_9 = r_income_9 - r_expense_9

        income_10 = in_exp_items_daily.objects.filter(month='10', type='income', flag=1)
        l_income_10 = []
        for i in income_10:
            l_income_10.append(float(i.amount))
        r_income_10 = sum(l_income_10)
        expense_10 = in_exp_items_daily.objects.filter(month='10', type='expense', flag=1)
        l_expense_10 = []
        for i in expense_10:
            l_expense_10.append(float(i.amount))
        r_expense_10 = sum(l_expense_10)
        r_balance_10 = r_income_10 - r_expense_10

        income_11 = in_exp_items_daily.objects.filter(month='11', type='income', flag=1)
        l_income_11 = []
        for i in income_11:
            l_income_11.append(float(i.amount))
        r_income_11 = sum(l_income_11)
        expense_11 = in_exp_items_daily.objects.filter(month='11', type='expense', flag=1)
        l_expense_11 = []
        for i in expense_11:
            l_expense_11.append(float(i.amount))
        r_expense_11 = sum(l_expense_11)
        r_balance_11 = r_income_11 - r_expense_11

        income_12 = in_exp_items_daily.objects.filter(month='12', type='income', flag=1)
        l_income_12 = []
        for i in income_12:
            l_income_12.append(float(i.amount))
        r_income_12 = sum(l_income_12)
        expense_12 = in_exp_items_daily.objects.filter(month='12', type='expense', flag=1)
        l_expense_12 = []
        for i in expense_12:
            l_expense_12.append(float(i.amount))
        r_expense_12 = sum(l_expense_12)
        r_balance_12 = r_income_12 - r_expense_12

        ##***************************************

        a = in_exp_items_daily.objects.all().filter(flag=1)
        il=[]
        el=[]
        for i in a:
            if i.type == 'income':
                il.append(float(i.amount))
            if i.type == 'expense':
                el.append(float(i.amount))

        sil=sum(il)
        silop = sum(il)+opening_balance
        sel=sum(el)
        d_bal = sil - sel



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



            'sil': sil,
            'sel': sel,
            'd_bal': d_bal,

            'income_1': r_income_1,
            'expense_1': r_expense_1,
            'balance_1': r_balance_1,

            'income_2': r_income_2,
            'expense_2': r_expense_2,
            'balance_2': r_balance_2,

            'income_3': r_income_3,
            'expense_3': r_expense_3,
            'balance_3': r_balance_3,

            'income_4': r_income_4,
            'expense_4': r_expense_4,
            'balance_4': r_balance_4,

            'income_5': r_income_5,
            'expense_5': r_expense_5,
            'balance_5': r_balance_5,

            'income_6': r_income_6,
            'expense_6': r_expense_6,
            'balance_6': r_balance_6,

            'income_7': r_income_7,
            'expense_7': r_expense_7,
            'balance_7': r_balance_7,

            'income_8': r_income_8,
            'expense_8': r_expense_8,
            'balance_8': r_balance_8,

            'income_9': r_income_9,
            'expense_9': r_expense_9,
            'balance_9': r_balance_9,

            'income_10': r_income_10,
            'expense_10': r_expense_10,
            'balance_10': r_balance_10,

            'income_11': r_income_11,
            'expense_11': r_expense_11,
            'balance_11': r_balance_11,

            'income_12': r_income_12,
            'expense_12': r_expense_12,
            'balance_12': r_balance_12,

        }
        return render(request,'branches/branch14/accounts/accounts_dash_board.html',context)
    return render(request, 'index.html')

