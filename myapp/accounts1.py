import json

from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from myapp.models import table1,in_exp_items_daily,opening_balance,category,ledger,accounts_book
from django.http import JsonResponse



#########################################################
###******CREATER MASTER START HERE
###################################################################################


##******************CATERGORY CREATER START HERE

def view_all_category(request):
    context = {
        'category' : category.objects.all().order_by('-id'),

    }
    return render(request,'branches/branch1/accounts/creater_master/category/view_all_category.html',context)

def create_new_category(request):
    context = {
        'category' : category.objects.all().order_by('-id'),

    }
    return render(request,'branches/branch1/accounts/creater_master/category/create_new_category.html',context)

def regi_new_category(request):
    category_names = request.POST.get('category')

    ic = category()
    ic.category_name = category_names
    ic.created_by = request.session['username']
    ic.flag = 1
    ic.save()

    context = {
        'category' : category.objects.all().order_by('-id'),

    }
    return render(request,'branches/branch1/accounts/creater_master/category/view_all_category.html',context)


##*****************CATERY CREATER END HERE


##******************ITEM CREATER START HERE

def view_all_items(request):
    context = {
        'item' : table1.objects.all().order_by('-id'),

    }
    return render(request,'branches/branch1/accounts/creater_master/items/view_all_items.html',context)

def create_new_item(request):
    context = {
        'item' : table1.objects.all().order_by('-id'),
        'category': category.objects.all().order_by('-id'),

    }
    return render(request,'branches/branch1/accounts/creater_master/items/create_new_item.html',context)

def regi_new_item(request):
    item_name = request.POST.get('name')
    item_category = request.POST.get('category')
    ir = table1.objects.all().filter(name=item_name).exists()

    if ir == True:
        context = {
            'item': table1.objects.all().order_by('-id'),
            'msg' : 'danger',
            'category': category.objects.all().order_by('-id'),
        }
        messages.info(request,'ITEM ALREADY EXISTS')
        return render(request, 'branches/branch1/accounts/creater_master/items/view_all_items.html', context)
    else:
        ic = table1()
        ic.name = item_name
        ic.item_category = item_category
        ic.created_by = 'CB '+ request.session['username']
        import datetime
        ic.cb_date = datetime.datetime.now()
        ic.flag = 1
        ic.save()

        context = {
            'item' : table1.objects.all().order_by('-id'),
            'msg' : 'success',
            'category': category.objects.all().order_by('-id'),
        }
        messages.info(request, 'ITEM CREATED SUCCESSFULLY !!!')
        return render(request,'branches/branch1/accounts/creater_master/items/view_all_items.html',context)

def delete_item(request,id):
    r=table1.objects.all().filter(id=id).exists()
    if r == True:
        d=table1.objects.get(id=id)
        d.deleted_by = 'DB ' + request.session['username']
        import datetime
        d.db_date = datetime.datetime.now()
        d.flag = 2
        d.save()
        context = {
            'item': table1.objects.all().filter(flag=1).order_by('-id'),
            'msg': 'success',
            'category': category.objects.all().order_by('-id'),
        }
        messages.info(request, 'ITEM Deleted Successfully')
        return render(request, 'branches/branch1/accounts/creater_master/items/view_all_items.html', context)
    else:
        context = {
            'item': table1.objects.all().filter(flag=1).order_by('-id'),
            'msg': 'warning',
            'category': category.objects.all().order_by('-id'),
        }
        messages.info(request, 'ITEM already  Deleted')
        return render(request,'branches/branch1/accounts/creater_master/items/view_all_items.html',context)


def update_item(request,id):
    if request.method == 'POST':
        item_name = request.POST.get('name')
        item_category = request.POST.get('category')
        ir = table1.objects.all().filter(name=item_name).exclude(id=id).exists()

        if ir == True:
            context = {
                'item': table1.objects.all().order_by('-id'),
                'msg' : 'danger',
                'category': category.objects.all().order_by('-id'),
            }
            messages.info(request,'ITEM ALREADY EXISTS')
            return render(request, 'branches/branch1/accounts/creater_master/items/view_all_items.html', context)
        else:
            ic = table1.objects.get(id=id)
            ic.name = item_name
            ic.item_category = item_category
            ic.updated_bys = 'UB '+ request.session['username']
            import datetime
            ic.ub_date = datetime.datetime.now()
            ic.flag = 1
            ic.save()
            context = {
                'item': table1.objects.all().order_by('-id'),
                'msg': 'info',
                'category': category.objects.all().order_by('-id'),
            }
            messages.info(request, 'ITEM UPDATED SUCCESSFULLY')
            return render(request, 'branches/branch1/accounts/creater_master/items/view_all_items.html', context)

    context = {
        'item' : table1.objects.all().order_by('-id'),
        'msg' : 'success',
        'sd' : table1.objects.get(id=id),
        'category': category.objects.all().order_by('-id'),
    }

    return render(request,'branches/branch1/accounts/creater_master/items/update_item.html',context)

##*****************ITEM CREATER END HERE


##******************LEDGER CREATER START HERE

def view_all_ledger(request):
    context = {
        'ledger' : ledger.objects.all().order_by('-id'),

    }
    return render(request,'branches/branch1/accounts/creater_master/ledger/view_all_ledger.html',context)

def create_new_ledger(request):
    context = {
        'ledger' : ledger.objects.all().order_by('-id'),

    }
    return render(request,'branches/branch1/accounts/creater_master/ledger/create_new_ledger.html',context)

def regi_new_ledger(request):
    ledger_name = request.POST.get('ledger_name')
    contact_person_name = request.POST.get('contact_person_name')
    contact_person_number = request.POST.get('contact_person_number')
    addres = request.POST.get('address')

    lr=ledger.objects.all().filter(ledger_name=ledger_name).exists()
    if lr == False:
        ic = ledger()
        ic.ledger_name = ledger_name
        ic.contact_person_name = contact_person_name
        ic.contact_person_mob = contact_person_number
        ic.address = addres
        ic.created_by = request.session['username']
        ic.flag = 1
        ic.save()

        context = {
            'ledger' : ledger.objects.all().order_by('-id'),
            'msg': 'success'
        }
        messages.info(request, 'LEDGER CREATED SUCCESSFULLY')
        return render(request,'branches/branch1/accounts/creater_master/ledger/view_all_ledger.html',context)
    else:
        context = {
            'ledger': ledger.objects.all().order_by('-id'),
            'msg' : 'danger'
        }
        messages.info(request,'LEDGER ALREADY EXISTS')
        return render(request, 'branches/branch1/accounts/creater_master/ledger/view_all_ledger.html', context)


def delete_ledger(request,id):
    r=ledger.objects.all().filter(id=id).exists()
    if r == True:
        d=ledger.objects.get(id=id)
        d.delete()
        context = {
            'ledger': ledger.objects.all().order_by('-id'),
            'msg': 'success'
        }
        messages.info(request, 'LEDGER Deleted Successfully')
        return render(request, 'branches/branch1/accounts/creater_master/ledger/view_all_ledger.html', context)
    else:
        context = {
            'ledger': ledger.objects.all().order_by('-id'),
            'msg': 'warning'
        }
        messages.info(request, 'LEDGER already  Deleted')
        return render(request,'branches/branch1/accounts/creater_master/ledger/view_all_ledger.html',context)


##*****************LEDGER CREATER END HERE


##******************ACCOUNTS_BOfOK CREATER START HERE

def view_all_accounts_book(request):
    context = {
        'accounts_book' : accounts_book.objects.all().order_by('-id'),

    }
    return render(request,'branches/branch1/accounts/creater_master/accounts_book/view_all_accounts_book.html',context)

def create_new_accounts_book(request):
    context = {
        'accounts_book' : accounts_book.objects.all().order_by('-id'),

    }
    return render(request,'branches/branch1/accounts/creater_master/accounts_book/create_new_accounts_book.html',context)

def regi_new_accounts_book(request):
    accounts_book_name = request.POST.get('accounts_book_name')

    ar=accounts_book.objects.all().filter(accounts_book_name=accounts_book_name).exists()

    if ar == True:
        context = {
            'accounts_book': accounts_book.objects.all().order_by('-id'),
            'msg' : 'danger'
        }
        messages.info(request,'ACCOUNTS BOOK Already Exists')
        return render(request, 'branches/branch1/accounts/creater_master/accounts_book/view_all_accounts_book.html',context)
    else:
        ic = accounts_book()
        ic.accounts_book_name = accounts_book_name
        ic.created_by = request.session['username']
        ic.flag = 1
        ic.save()

        context = {
            'accounts_book' : accounts_book.objects.all().order_by('-id'),
            'msg': 'success'
        }
        messages.info(request, 'ACCOUNTS BOOK Created Successfully')
        return render(request,'branches/branch1/accounts/creater_master/accounts_book/view_all_accounts_book.html',context)



def delete_accounts_book(request,id):
    r=accounts_book.objects.all().filter(id=id).exists()
    if r == True:
        d=accounts_book.objects.get(id=id)
        d.delete()
        context = {
            'ledger': accounts_book.objects.all().order_by('-id'),
            'msg': 'success'
        }
        messages.info(request, 'ACCOUNTS BOOK Deleted Successfully')
        return render(request, 'branches/branch1/accounts/creater_master/accounts_book/view_all_accounts_book.html', context)
    else:
        context = {
            'ledger': accounts_book.objects.all().order_by('-id'),
            'msg': 'warning'
        }
        messages.info(request, 'ACCOUNTS BOOK already  Deleted')
        return render(request,'branches/branch1/accounts/creater_master/accounts_book/view_all_accounts_book.html',context)



##*****************ACCOUNTS_BOOK CREATER END HERE


#########################################################
###******CREATER MASTER END HERE
###################################################################################

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER START HERE
###################################################################################

def get_countries(request):

    countries = []
    t1 = table1.objects.all()
    for i in t1:
        countries.append(i.name)

    mimetype = 'application/json'
    return HttpResponse(json.dumps(countries), mimetype)


def in_exp_items_entry(request):
    a='Afghanistan'
    b='Albania'
    l=[]
    l.append(a)
    l.append(b)
    context={
        "countries" : ["Afghanistan", "Albania", "a", 'aaaa', 'aa', "Algeria", "Andorra", "Angola", "Anguilla"],
        'items': in_exp_items_daily.objects.all().order_by('-id'),
        'ledger' : ledger.objects.all(),
        'accounts_book': accounts_book.objects.all(),
    }
    print(context)
    return render(request,'branches/branch1/accounts/journal/in_exp_items_entry.html',context)



def reg_in_exp_items_entry(request):
    particulars = request.POST.get('particular')
    amounts = request.POST.get('amount')
    ledgers = request.POST.get('ledger')
    accounts_book_name = request.POST.get('accounts_book_name')
    types = request.POST.get('type')
    dates = request.POST.get('date')
    descriptions = request.POST.get('description')

    dl = []
    for i in dates:
        dl.append(i)

    dll = []
    dll.append(dl[5])
    dll.append(dl[6])

    print(dll)

    month = ''.join(dll)
    print(month)

    dal = []
    dal.append(dl[8])
    dal.append(dl[9])
    print(dal)
    day = ''.join(dal)
    print('date', day)

    yl = []
    yl.append(dl[0])
    yl.append(dl[1])
    yl.append(dl[2])
    yl.append(dl[3])
    print(yl)
    year = ''.join(yl)
    print('year', year)

    res = in_exp_items_daily.objects.all().filter(particulars=particulars,amount=amounts,accounts_book_name=accounts_book_name,type=types,date=dates,description=descriptions).exists()
    print('res',res)

    if res == True:
        context = {
            'items': in_exp_items_daily.objects.all().order_by('-id'),
            'message_bg' : 'alert-danger',

            'ledger': ledger.objects.all(),
            'accounts_book': accounts_book.objects.all(),
        }
        messages.info(request, 'ITEM already exists')
        return render(request, 'branches/branch1/accounts/journal/in_exp_items_entry.html', context)

    else:
        dup = table1.objects.all().filter(name=particulars).exists()
        if dup == False:
            context = {
                'items': in_exp_items_daily.objects.all().order_by('-id'),
                'message_bg': 'alert-danger',

                'ledger': ledger.objects.all(),
                'accounts_book': accounts_book.objects.all(),
            }
            messages.info(request, 'ITEM NOT FOUND')
            return render(request, 'branches/branch1/accounts/journal/in_exp_items_entry.html', context)

        else:
            cat = table1.objects.all()
            lnam = []
            lcat = []
            for i in cat:
                if i.name == particulars:
                    lnam.append(i.name)
                    lcat.append(i.item_category)
            print('lll nam',lnam)
            print('ljljl ca',lcat)

            ic = in_exp_items_daily()
            ic.particulars = particulars
            ic.amount = float(amounts)
            ic.ledger = ledgers
            ic.accounts_book_name = accounts_book_name
            ic.type = types
            ic.date = dates
            ic.description = descriptions
            ic.day = day
            ic.month = month
            ic.year = year
            ic.enter_by = 'bri'
            ic.flag = 1
            ic.save()

            context = {
                'items' : in_exp_items_daily.objects.all().order_by('-id'),
                'message_bg': 'alert-success',

                'ledger': ledger.objects.all(),
                'accounts_book': accounts_book.objects.all(),
            }
            messages.info(request, 'ITEM Created Successfully')
            return render(request,'branches/branch1/accounts/journal/in_exp_items_entry.html',context)
    return render(request, 'branches/branch1/accounts/journal/in_exp_items_entry.html', context)

def delete_journal(request,id):
    r=in_exp_items_daily.objects.all().filter(id=id).exists()
    if r == True:
        d=in_exp_items_daily.objects.get(id=id)
        d.delete()
        context = {
            'items': in_exp_items_daily.objects.all().order_by('-id'),
            'message_bg': 'alert-success',

            'ledger': ledger.objects.all(),
            'accounts_book': accounts_book.objects.all(),
        }
        messages.info(request, 'ITEM Deleted Successfully')
        return render(request, 'branches/branch1/accounts/journal/in_exp_items_entry.html', context)
    else:
        context = {
            'items': in_exp_items_daily.objects.all().order_by('-id'),
            'message_bg': 'alert-warning',

            'ledger': ledger.objects.all(),
            'accounts_book': accounts_book.objects.all(),
        }
        messages.info(request, 'ITEM already  Deleted')
        return render(request,'branches/branch1/accounts/journal/in_exp_items_entry.html',context)




def update_in_exp_items_entry(request,id):
    if request.method == 'POST':
        particulars = request.POST.get('particular')
        amounts = request.POST.get('amount')
        ledgers = request.POST.get('ledger')
        accounts_book_name = request.POST.get('accounts_book_name')
        types = request.POST.get('type')
        dates = request.POST.get('date')
        descriptions = request.POST.get('description')

        dup = table1.objects.all().filter(name=particulars).exists()
        if dup == False:
            context = {
                'items': in_exp_items_daily.objects.all().order_by('-id'),
                'message_bg': 'alert-danger'
            }
            messages.info(request, 'ITEM NOT FOUND')
            return render(request, 'branches/branch1/accounts/journal/in_exp_items_entry.html', context)
        else:

            dl = []
            for i in dates:
                dl.append(i)

            dll = []
            dll.append(dl[5])
            dll.append(dl[6])

            print(dll)

            month = ''.join(dll)
            print(month)

            dal = []
            dal.append(dl[8])
            dal.append(dl[9])
            print(dal)
            day = ''.join(dal)
            print('date', day)

            yl = []
            yl.append(dl[0])
            yl.append(dl[1])
            yl.append(dl[2])
            yl.append(dl[3])
            print(yl)
            year = ''.join(yl)
            print('year', year)

            cat = table1.objects.all()
            lnam = []
            lcat = []
            for i in cat:
                if i.name == particulars:
                    lnam.append(i.name)
                    lcat.append(i.item_category)

            ic = in_exp_items_daily()
            ic.particulars = particulars
            ic.amount = float(amounts)
            ic.ledger = ledgers
            ic.accounts_book_name = accounts_book_name
            ic.type = types
            ic.date = dates
            ic.description = descriptions
            ic.day = day
            ic.month = month
            ic.year = year
            ic.enter_by = request.session['username']
            ic.flag = 1
            ic.save()

            context = {
                'items': in_exp_items_daily.objects.all().order_by('-id'),
                'message_bg': 'alert-info'
            }
            messages.info(request, 'ITEM Updated Successfully')
            return render(request, 'branches/branch1/accounts/journal/in_exp_items_entry.html', context)

    context = {
        'items': in_exp_items_daily.objects.all().order_by('-id'),
        'message_bg': 'alert-success',

        'ledger': ledger.objects.all(),
        'accounts_book': accounts_book.objects.all(),
        'sd': in_exp_items_daily.objects.get(id=id)
    }
    return render(request, 'branches/branch1/accounts/journal/update_in_exp_items_entry.html', context)


#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER END HERE
###################################################################################
#########*******************************************************************************************************************
#########################################################
###******ALL REPORTS  START HERE
###################################################################################

###*************DAILY DETAILED REPORTS  START HERE


def daily_detailed(request):
    dates = request.POST.get('day')
    import datetime
    if dates == None:
        d = datetime.datetime.now()
        month = d.strftime("%m")
        day=d.strftime(("%d"))
        r_dates = d
    else:
        dl = []
        for i in dates:
            dl.append(i)

        dll = []
        dll.append(dl[5])
        dll.append(dl[6])
        month = ''.join(dll)

        dal = []
        dal.append(dl[8])
        dal.append(dl[9])
        day = ''.join(dal)

        r_dates = dates

    a = in_exp_items_daily.objects.all().filter(day=day,month=month)
    il=[]
    el=[]
    for i in a:
        if i.type == 'income':
            il.append(float(i.amount))
        if i.type == 'expense':
            el.append(float(i.amount))
    print('ill',il)
    sil=sum(il)
    sel=sum(el)

    d_bal = sil - sel

    context={
        'dd' : in_exp_items_daily.objects.all().filter(day=day,month=month),
        'sil' : sil,
        'sel' : sel,
        'd_bal' : d_bal,
        'dates' : r_dates,
    }
    return render(request,'branches/branch1/accounts/accounts_reports/daily_detailed.html',context)

###*************DAILY DETAILED REPORTS  START HERE

###*************ITEM BASED REPORTS  START HERE

def item_based_reports(request):
    particular = request.POST.get('item')

    a=in_exp_items_daily.objects.all().filter(particulars=particular)
    l=[]
    for i in a:
        if i.amount > 0:
            l.append(float(i.amount))
    r=sum(l)

    context={
        'hb' : in_exp_items_daily.objects.all().filter(particulars=particular),
        'hname' : particular,
        'total' : r,
        'item' : in_exp_items_daily.objects.all(),

    }
    return render(request,'branches/branch1/accounts/accounts_reports/item/item_based_reports.html',context)
#particulars

###*************ITEM BASED REPORTS  START HERE

###*************LEDGER BASED REPORTS  START HERE


def daily_ledger_based_reports(request):
    dates = request.POST.get('day')
    ledgers = request.POST.get('ledger')
    import datetime
    if dates == None:
        d = datetime.datetime.now()
        month = d.strftime("%m")
        day=d.strftime(("%d"))
        r_dates = d
    else:
        dl = []
        for i in dates:
            dl.append(i)

        dll = []
        dll.append(dl[5])
        dll.append(dl[6])
        month = ''.join(dll)

        dal = []
        dal.append(dl[8])
        dal.append(dl[9])
        day = ''.join(dal)

        r_dates = dates

    a = in_exp_items_daily.objects.all().filter(day=day,month=month,ledger=ledgers)
    il=[]
    el=[]
    for i in a:
        if i.type == 'income':
            il.append(float(i.amount))
        if i.type == 'expense':
            el.append(float(i.amount))
    print('ill',il)
    sil=sum(il)
    sel=sum(el)

    d_bal = sil - sel

    context={
        'hb' : in_exp_items_daily.objects.all().filter(day=day,month=month,ledger=ledgers),
        'sil' : sil,
        'sel' : sel,
        'd_bal' : d_bal,
        'dates' : r_dates,
        'ledger': ledger.objects.all(),
        'lname': ledgers,
    }
    return render(request,'branches/branch1/accounts/accounts_reports/ledger/daily_ledger_based_reports.html',context)


def ledger_based_reports(request):
    ledgers = request.POST.get('ledger')

    a =  in_exp_items_daily.objects.all().filter(ledger=ledgers)
    l=[]
    for i in a:
        if i.amount > 0:
            l.append(float(i.amount))
    r=sum(l)

    a = in_exp_items_daily.objects.all().filter(ledger=ledgers)
    il = []
    el = []
    for i in a:
        if i.type == 'income':
            il.append(float(i.amount))
        if i.type == 'expense':
            el.append(float(i.amount))
    print('ill', il)
    sil = sum(il)
    sel = sum(el)

    d_bal = sil - sel

    import datetime
    r_dates = datetime.datetime.now()

    context={
        'hb' : in_exp_items_daily.objects.all().filter(ledger=ledgers),
        'hname' : ledgers,
        'total' : r,

        'sil': sil,
        'sel': sel,
        'd_bal': d_bal,
        'dates': r_dates,
        'ledger': ledger.objects.all(),

    }
    return render(request,'branches/branch1/accounts/accounts_reports/ledger/ledger_based_reports.html',context)



def monthly_ledger_based_reports(request):
    ledgers = request.POST.get('ledger')
    month = request.POST.get('month')

    a =  in_exp_items_daily.objects.all().filter(ledger=ledgers,month=month)
    l=[]
    for i in a:
        if i.amount > 0:
            l.append(float(i.amount))
    r=sum(l)

    a = in_exp_items_daily.objects.all().filter(ledger=ledgers,month=month)
    il = []
    el = []
    for i in a:
        if i.type == 'income':
            il.append(float(i.amount))
        if i.type == 'expense':
            el.append(float(i.amount))
    print('ill', il)
    sil = sum(il)
    sel = sum(el)

    d_bal = sil - sel

    import datetime
    r_dates = datetime.datetime.now()

    context={
        'hb' : in_exp_items_daily.objects.all().filter(ledger=ledgers,month=month),
        'hname' : ledgers,
        'total' : r,

        'sil': sil,
        'sel': sel,
        'd_bal': d_bal,
        'dates': r_dates,
        'ledger': ledger.objects.all(),

    }
    return render(request,'branches/branch1/accounts/accounts_reports/ledger/monthly_ledger_based_reports.html',context)


###*************LEDGER BASED REPORTS  START HERE

###*************ACCOUNTS-BOOK BASED REPORTS  START HERE


def accounts_book_based_reports(request):
    accounts_book_name = request.POST.get('accounts_book_name')

    a=in_exp_items_daily.objects.all().filter(accounts_book_name=accounts_book_name)
    l=[]
    for i in a:
        if i.amount > 0:
            l.append(float(i.amount))
    r=sum(l)

    context={
        'hb' : in_exp_items_daily.objects.all().filter(accounts_book_name=accounts_book_name),
        'hname' : accounts_book_name,
        'total' : r,
        'accounts_book' : accounts_book.objects.all(),

    }
    return render(request,'branches/branch1/accounts/accounts_reports/accounts_book/accounts_book_name_based_reports.html',context)


###*************ACCOUNTS-BOOK BASED REPORTS  END HERE



#########################################################
###******ALL REPORTS  END HERE
###################################################################################

def monthly_reports_choose_months(request):
    context = {

    }
    return render(request,'branches/branch1/accounts/monthly_reports/monthly_reports_choose_months.html',context)


def monthly_daily_in_exp_items_report(request):
    d={'name':['ramu','manu','man'],'age':[11,44,66]}
    # generate table and filter down to a subquery.

    queryset = in_exp_items_daily.objects.filter(month='08',type='income')
    totals = queryset.aggregate(sum=Sum('amount'))

    ob = opening_balance.objects.all().filter(month_no='08',month_name='aug')
    l_opening_balance=[]
    for i in ob:
        l_opening_balance.append(float(i.month_amount))
    aug_opening_balance= sum(l_opening_balance)

    color=''
    if aug_opening_balance >0:
        color='green'
    elif aug_opening_balance < 0:
        color = 'red'
    else:
        color = 'orange'


    income_1 = in_exp_items_daily.objects.filter(month='08', type='income', day='01')
    l_income_1 = []
    for i in income_1:
        l_income_1.append(float(i.amount))
    r_income_1 = sum(l_income_1)
    expense_1 = in_exp_items_daily.objects.filter(month='08', type='expense', day='01')
    l_expense_1 = []
    for i in expense_1:
        l_expense_1.append(float(i.amount))
    r_expense_1 = sum(l_expense_1)
    r_balance_1 = aug_opening_balance + r_income_1 - r_expense_1

    income_2 = in_exp_items_daily.objects.filter(month='08', type='income', day='02')
    l_income_2 = []
    for i in income_2:
        l_income_2.append(float(i.amount))
    r_income_2 = sum(l_income_2)
    expense_2 = in_exp_items_daily.objects.filter(month='08', type='expense', day='02')
    l_expense_2 = []
    for i in expense_2:
        l_expense_2.append(float(i.amount))
    r_expense_2 = sum(l_expense_2)
    r_balance_2 = r_balance_1+r_income_2 - r_expense_2

    income_3 = in_exp_items_daily.objects.filter(month='08', type='income', day='03')
    l_income_3 = []
    for i in income_3:
        l_income_3.append(float(i.amount))
    r_income_3 = sum(l_income_3)
    expense_3 = in_exp_items_daily.objects.filter(month='08', type='expense', day='03')
    l_expense_3 = []
    for i in expense_3:
        l_expense_3.append(float(i.amount))
    r_expense_3 = sum(l_expense_3)
    r_balance_3 = r_balance_2+r_income_3 - r_expense_3

    income_4 = in_exp_items_daily.objects.filter(month='08', type='income', day='04')
    l_income_4 = []
    for i in income_4:
        l_income_4.append(float(i.amount))
    r_income_4 = sum(l_income_4)
    expense_4 = in_exp_items_daily.objects.filter(month='08', type='expense', day='04')
    l_expense_4 = []
    for i in expense_4:
        l_expense_4.append(float(i.amount))
    r_expense_4 = sum(l_expense_4)
    r_balance_4 = r_balance_3+r_income_4 - r_expense_4

    income_5 = in_exp_items_daily.objects.filter(month='08', type='income', day='05')
    l_income_5 = []
    for i in income_5:
        l_income_5.append(float(i.amount))
    r_income_5 = sum(l_income_5)
    expense_5 = in_exp_items_daily.objects.filter(month='08', type='expense', day='05')
    l_expense_5 = []
    for i in expense_5:
        l_expense_5.append(float(i.amount))
    r_expense_5 = sum(l_expense_5)
    r_balance_5 = r_balance_4+r_income_5 - r_expense_5

    income_6 = in_exp_items_daily.objects.filter(month='08', type='income', day='06')
    l_income_6 = []
    for i in income_6:
        l_income_6.append(float(i.amount))
    r_income_6 = sum(l_income_6)
    expense_6 = in_exp_items_daily.objects.filter(month='08', type='expense', day='06')
    l_expense_6 = []
    for i in expense_6:
        l_expense_6.append(float(i.amount))
    r_expense_6 = sum(l_expense_6)
    r_balance_6 = r_balance_5+r_income_6 - r_expense_6

    income_7 = in_exp_items_daily.objects.filter(month='08', type='income', day='07')
    l_income_7 = []
    for i in income_7:
        l_income_7.append(float(i.amount))
    r_income_7 = sum(l_income_7)
    expense_7 = in_exp_items_daily.objects.filter(month='08', type='expense', day='07')
    l_expense_7 = []
    for i in expense_7:
        l_expense_7.append(float(i.amount))
    r_expense_7 = sum(l_expense_7)
    r_balance_7 = r_balance_6+r_income_7 - r_expense_7
###***************************************
    income_8 = in_exp_items_daily.objects.filter(month='08', type='income', day='08')
    l_income_8 = []
    for i in income_8:
        l_income_8.append(float(i.amount))
    r_income_8 = sum(l_income_8)
    expense_8 = in_exp_items_daily.objects.filter(month='08', type='expense', day='08')
    l_expense_8 = []
    for i in expense_8:
        l_expense_8.append(float(i.amount))
    r_expense_8 = sum(l_expense_8)
    r_balance_8 = r_balance_7 + r_income_8 - r_expense_8

    income_9 = in_exp_items_daily.objects.filter(month='08', type='income', day='09')
    l_income_9 = []
    for i in income_9:
        l_income_9.append(float(i.amount))
    r_income_9 = sum(l_income_9)
    expense_9 = in_exp_items_daily.objects.filter(month='08', type='expense', day='09')
    l_expense_9 = []
    for i in expense_9:
        l_expense_9.append(float(i.amount))
    r_expense_9 = sum(l_expense_9)
    r_balance_9 = r_balance_8 + r_income_9 - r_expense_9

    income_10 = in_exp_items_daily.objects.filter(month='08', type='income', day='10')
    l_income_10 = []
    for i in income_10:
        l_income_10.append(float(i.amount))
    r_income_10 = sum(l_income_10)
    expense_10 = in_exp_items_daily.objects.filter(month='08', type='expense', day='10')
    l_expense_10 = []
    for i in expense_10:
        l_expense_10.append(float(i.amount))
    r_expense_10 = sum(l_expense_10)
    r_balance_10 = r_balance_9 + r_income_10 - r_expense_10

    income_11 = in_exp_items_daily.objects.filter(month='08', type='income', day='11')
    l_income_11 = []
    for i in income_11:
        l_income_11.append(float(i.amount))
    r_income_11 = sum(l_income_11)
    expense_11 = in_exp_items_daily.objects.filter(month='08', type='expense', day='11')
    l_expense_11 = []
    for i in expense_11:
        l_expense_11.append(float(i.amount))
    r_expense_11 = sum(l_expense_11)
    r_balance_11 = r_balance_10 + r_income_11 - r_expense_11

    income_12 = in_exp_items_daily.objects.filter(month='08', type='income', day='12')
    l_income_12 = []
    for i in income_12:
        l_income_12.append(float(i.amount))
    r_income_12 = sum(l_income_12)
    expense_12 = in_exp_items_daily.objects.filter(month='08', type='expense', day='12')
    l_expense_12 = []
    for i in expense_12:
        l_expense_12.append(float(i.amount))
    r_expense_12 = sum(l_expense_12)
    r_balance_12 = r_balance_11 + r_income_12 - r_expense_12

    income_13 = in_exp_items_daily.objects.filter(month='08', type='income', day='13')
    l_income_13 = []
    for i in income_13:
        l_income_13.append(float(i.amount))
    r_income_13 = sum(l_income_13)
    expense_13 = in_exp_items_daily.objects.filter(month='08', type='expense', day='13')
    l_expense_13 = []
    for i in expense_13:
        l_expense_13.append(float(i.amount))
    r_expense_13 = sum(l_expense_13)
    r_balance_13 = r_balance_12 + r_income_13 - r_expense_13

    income_14 = in_exp_items_daily.objects.filter(month='08', type='income', day='14')
    l_income_14 = []
    for i in income_14:
        l_income_14.append(float(i.amount))
    r_income_14 = sum(l_income_14)
    expense_14 = in_exp_items_daily.objects.filter(month='08', type='expense', day='14')
    l_expense_14 = []
    for i in expense_14:
        l_expense_14.append(float(i.amount))
    r_expense_14 = sum(l_expense_14)
    r_balance_14 = r_balance_13 + r_income_14 - r_expense_14
###*****************************
    income_15 = in_exp_items_daily.objects.filter(month='08', type='income', day='15')
    l_income_15 = []
    for i in income_15:
        l_income_15.append(float(i.amount))
    r_income_15 = sum(l_income_15)
    expense_15 = in_exp_items_daily.objects.filter(month='08', type='expense', day='15')
    l_expense_15 = []
    for i in expense_15:
        l_expense_15.append(float(i.amount))
    r_expense_15 = sum(l_expense_15)
    r_balance_15 = r_balance_14 + r_income_15 - r_expense_15

    income_16 = in_exp_items_daily.objects.filter(month='08', type='income', day='16')
    l_income_16 = []
    for i in income_16:
        l_income_16.append(float(i.amount))
    r_income_16 = sum(l_income_16)
    expense_16 = in_exp_items_daily.objects.filter(month='08', type='expense', day='16')
    l_expense_16 = []
    for i in expense_16:
        l_expense_16.append(float(i.amount))
    r_expense_16 = sum(l_expense_16)
    r_balance_16 = r_balance_15 + r_income_16 - r_expense_16

    income_17 = in_exp_items_daily.objects.filter(month='08', type='income', day='17')
    l_income_17 = []
    for i in income_17:
        l_income_17.append(float(i.amount))
    r_income_17 = sum(l_income_17)
    expense_17 = in_exp_items_daily.objects.filter(month='08', type='expense', day='17')
    l_expense_17 = []
    for i in expense_17:
        l_expense_17.append(float(i.amount))
    r_expense_17 = sum(l_expense_17)
    r_balance_17 = r_balance_16 + r_income_17 - r_expense_17

    income_18 = in_exp_items_daily.objects.filter(month='08', type='income', day='18')
    l_income_18 = []
    for i in income_18:
        l_income_18.append(float(i.amount))
    r_income_18 = sum(l_income_18)
    expense_18 = in_exp_items_daily.objects.filter(month='08', type='expense', day='18')
    l_expense_18 = []
    for i in expense_18:
        l_expense_18.append(float(i.amount))
    r_expense_18 = sum(l_expense_18)
    r_balance_18 = r_balance_17 + r_income_18 - r_expense_18

    income_19 = in_exp_items_daily.objects.filter(month='08', type='income', day='19')
    l_income_19 = []
    for i in income_19:
        l_income_19.append(float(i.amount))
    r_income_19 = sum(l_income_19)
    expense_19 = in_exp_items_daily.objects.filter(month='08', type='expense', day='19')
    l_expense_19 = []
    for i in expense_19:
        l_expense_19.append(float(i.amount))
    r_expense_19 = sum(l_expense_19)
    r_balance_19 = r_balance_18 + r_income_19 - r_expense_19

    income_20 = in_exp_items_daily.objects.filter(month='08', type='income', day='20')
    l_income_20 = []
    for i in income_20:
        l_income_20.append(float(i.amount))
    r_income_20 = sum(l_income_20)
    expense_20 = in_exp_items_daily.objects.filter(month='08', type='expense', day='20')
    l_expense_20 = []
    for i in expense_20:
        l_expense_20.append(float(i.amount))
    r_expense_20 = sum(l_expense_20)
    r_balance_20 = r_balance_19 + r_income_20 - r_expense_20

    income_21 = in_exp_items_daily.objects.filter(month='08', type='income', day='21')
    l_income_21 = []
    for i in income_21:
        l_income_21.append(float(i.amount))
    r_income_21 = sum(l_income_21)
    expense_21 = in_exp_items_daily.objects.filter(month='08', type='expense', day='21')
    l_expense_21 = []
    for i in expense_21:
        l_expense_21.append(float(i.amount))
    r_expense_21 = sum(l_expense_21)
    r_balance_21 = r_balance_20 + r_income_21 - r_expense_21

    income_22 = in_exp_items_daily.objects.filter(month='08', type='income', day='22')
    l_income_22 = []
    for i in income_22:
        l_income_22.append(float(i.amount))
    r_income_22 = sum(l_income_22)
    expense_22 = in_exp_items_daily.objects.filter(month='08', type='expense', day='22')
    l_expense_22 = []
    for i in expense_22:
        l_expense_22.append(float(i.amount))
    r_expense_22 = sum(l_expense_22)
    r_balance_22 = r_balance_21 + r_income_22 - r_expense_22
####************************
    income_23 = in_exp_items_daily.objects.filter(month='08', type='income', day='23')
    l_income_23 = []
    for i in income_23:
        l_income_23.append(float(i.amount))
    r_income_23 = sum(l_income_23)
    expense_23 = in_exp_items_daily.objects.filter(month='08', type='expense', day='23')
    l_expense_23 = []
    for i in expense_23:
        l_expense_23.append(float(i.amount))
    r_expense_23 = sum(l_expense_23)
    r_balance_23 = r_balance_22 + r_income_23 - r_expense_23

    income_24 = in_exp_items_daily.objects.filter(month='08', type='income', day='24')
    l_income_24 = []
    for i in income_24:
        l_income_24.append(float(i.amount))
    r_income_24 = sum(l_income_24)
    expense_24 = in_exp_items_daily.objects.filter(month='08', type='expense', day='24')
    l_expense_24 = []
    for i in expense_24:
        l_expense_24.append(float(i.amount))
    r_expense_24 = sum(l_expense_24)
    r_balance_24 = r_balance_23 + r_income_24 - r_expense_24

    income_25 = in_exp_items_daily.objects.filter(month='08', type='income', day='25')
    l_income_25 = []
    for i in income_25:
        l_income_25.append(float(i.amount))
    r_income_25 = sum(l_income_25)
    expense_25 = in_exp_items_daily.objects.filter(month='08', type='expense', day='25')
    l_expense_25 = []
    for i in expense_25:
        l_expense_25.append(float(i.amount))
    r_expense_25 = sum(l_expense_25)
    r_balance_25 = r_balance_24 + r_income_25 - r_expense_25

    income_26 = in_exp_items_daily.objects.filter(month='08', type='income', day='26')
    l_income_26 = []
    for i in income_26:
        l_income_26.append(float(i.amount))
    r_income_26 = sum(l_income_26)
    expense_26 = in_exp_items_daily.objects.filter(month='08', type='expense', day='26')
    l_expense_26 = []
    for i in expense_26:
        l_expense_26.append(float(i.amount))
    r_expense_26 = sum(l_expense_26)
    r_balance_26 = r_balance_25 + r_income_26 - r_expense_26

    income_27 = in_exp_items_daily.objects.filter(month='08', type='income', day='27')
    l_income_27 = []
    for i in income_27:
        l_income_27.append(float(i.amount))
    r_income_27 = sum(l_income_27)
    expense_27 = in_exp_items_daily.objects.filter(month='08', type='expense', day='27')
    l_expense_27 = []
    for i in expense_27:
        l_expense_27.append(float(i.amount))
    r_expense_27 = sum(l_expense_27)
    r_balance_27 = r_balance_26 + r_income_27 - r_expense_27

    income_28 = in_exp_items_daily.objects.filter(month='08', type='income', day='28')
    l_income_28 = []
    for i in income_28:
        l_income_28.append(float(i.amount))
    r_income_28 = sum(l_income_28)
    expense_28 = in_exp_items_daily.objects.filter(month='08', type='expense', day='28')
    l_expense_28 = []
    for i in expense_28:
        l_expense_28.append(float(i.amount))
    r_expense_28 = sum(l_expense_28)
    r_balance_28 = r_balance_27 + r_income_28 - r_expense_28
####**************************
    income_29 = in_exp_items_daily.objects.filter(month='08', type='income', day='29')
    l_income_29 = []
    for i in income_29:
        l_income_29.append(float(i.amount))
    r_income_29 = sum(l_income_29)
    expense_29 = in_exp_items_daily.objects.filter(month='08', type='expense', day='29')
    l_expense_29 = []
    for i in expense_29:
        l_expense_29.append(float(i.amount))
    r_expense_29 = sum(l_expense_29)
    r_balance_29 = r_balance_28 + r_income_29 - r_expense_29

    income_30 = in_exp_items_daily.objects.filter(month='08', type='income', day='30')
    l_income_30 = []
    for i in income_30:
        l_income_30.append(float(i.amount))
    r_income_30 = sum(l_income_30)
    expense_30 = in_exp_items_daily.objects.filter(month='08', type='expense', day='30')
    l_expense_30 = []
    for i in expense_30:
        l_expense_30.append(float(i.amount))
    r_expense_30 = sum(l_expense_30)
    r_balance_30 = r_balance_29 + r_income_30 - r_expense_30

    income_31 = in_exp_items_daily.objects.filter(month='08', type='income', day='31')
    l_income_31 = []
    for i in income_31:
        l_income_31.append(float(i.amount))
    r_income_31 = sum(l_income_31)
    expense_31 = in_exp_items_daily.objects.filter(month='08', type='expense', day='31')
    l_expense_31 = []
    for i in expense_31:
        l_expense_31.append(float(i.amount))
    r_expense_31 = sum(l_expense_31)
    r_balance_31 = r_balance_30 + r_income_31 - r_expense_31

##****************************************
    a = in_exp_items_daily.objects.all().filter(month='08')
    il=[]
    el=[]
    for i in a:
        if i.type == 'income':
            il.append(float(i.amount))
        if i.type == 'expense':
            el.append(float(i.amount))

    sil=sum(il)
    silop = sum(il)+aug_opening_balance
    sel=sum(el)
    d_bal = sil - sel


    context = {
        'object_list': queryset,
        'totals': totals,
        'res' : in_exp_items_daily.objects.all().filter(month='08'),

        'aug_opening_balance' : aug_opening_balance,
        'color' : color,

        'sil' : sil,
        'silop' : silop,
        'sel' : sel,
        'd_bal' : d_bal,

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

        'income_13': r_income_13,
        'expense_13': r_expense_13,
        'balance_13': r_balance_13,

        'income_14': r_income_14,
        'expense_14': r_expense_14,
        'balance_14': r_balance_14,

        'income_15': r_income_15,
        'expense_15': r_expense_15,
        'balance_15': r_balance_15,

        'income_16': r_income_16,
        'expense_16': r_expense_16,
        'balance_16': r_balance_16,

        'income_17': r_income_17,
        'expense_17': r_expense_17,
        'balance_17': r_balance_17,

        'income_18': r_income_18,
        'expense_18': r_expense_18,
        'balance_18': r_balance_18,

        'income_19': r_income_19,
        'expense_19': r_expense_19,
        'balance_19': r_balance_19,

        'income_20': r_income_20,
        'expense_20': r_expense_20,
        'balance_20': r_balance_20,

        'income_21': r_income_21,
        'expense_21': r_expense_21,
        'balance_21': r_balance_21,

        'income_22': r_income_22,
        'expense_22': r_expense_22,
        'balance_22': r_balance_22,

        'income_23': r_income_23,
        'expense_23': r_expense_23,
        'balance_23': r_balance_23,

        'income_24': r_income_24,
        'expense_24': r_expense_24,
        'balance_24': r_balance_24,

        'income_25': r_income_25,
        'expense_25': r_expense_25,
        'balance_25': r_balance_25,

        'income_26': r_income_26,
        'expense_26': r_expense_26,
        'balance_26': r_balance_26,

        'income_27': r_income_27,
        'expense_27': r_expense_27,
        'balance_27': r_balance_27,

        'income_28': r_income_28,
        'expense_28': r_expense_28,
        'balance_28': r_balance_28,

        'income_29': r_income_29,
        'expense_29': r_expense_29,
        'balance_29': r_balance_29,

        'income_30': r_income_30,
        'expense_30': r_expense_30,
        'balance_30': r_balance_30,

        'income_31': r_income_31,
        'expense_31': r_expense_31,
        'balance_31': r_balance_31,

    }
    return render(request,'branches/branch1/accounts/monthly_reports/monthly_daily_in_exp_items_report.html',context)





def single_monthly_daily_in_exp_items_report(request):
    d={'name':['ramu','manu','man'],'age':[11,44,66]}
    # generate table and filter down to a subquery.

    queryset = in_exp_items_daily.objects.filter(month='08',type='income')
    totals = queryset.aggregate(sum=Sum('amount'))

    #ob = opening_balance.objects.all().filter(month_no='08',month_name='aug')
    #l_opening_balance=[]
    #for i in ob:
        #l_opening_balance.append(float(i.month_amount))
    l_opening_balance=[0]
    aug_opening_balance= sum(l_opening_balance)

    color=''
    if aug_opening_balance >0:
        color='green'
    elif aug_opening_balance < 0:
        color = 'red'
    else:
        color = 'orange'


    income_1 = in_exp_items_daily.objects.filter(month='08', type='income', day='01')
    l_income_1 = []
    for i in income_1:
        l_income_1.append(float(i.amount))
    r_income_1 = sum(l_income_1)
    expense_1 = in_exp_items_daily.objects.filter(month='08', type='expense', day='01')
    l_expense_1 = []
    for i in expense_1:
        l_expense_1.append(float(i.amount))
    r_expense_1 = sum(l_expense_1)
    r_balance_1 = aug_opening_balance + r_income_1 - r_expense_1

    income_2 = in_exp_items_daily.objects.filter(month='08', type='income', day='02')
    l_income_2 = []
    for i in income_2:
        l_income_2.append(float(i.amount))
    r_income_2 = sum(l_income_2)
    expense_2 = in_exp_items_daily.objects.filter(month='08', type='expense', day='02')
    l_expense_2 = []
    for i in expense_2:
        l_expense_2.append(float(i.amount))
    r_expense_2 = sum(l_expense_2)
    r_balance_2 = r_balance_1+r_income_2 - r_expense_2

    income_3 = in_exp_items_daily.objects.filter(month='08', type='income', day='03')
    l_income_3 = []
    for i in income_3:
        l_income_3.append(float(i.amount))
    r_income_3 = sum(l_income_3)
    expense_3 = in_exp_items_daily.objects.filter(month='08', type='expense', day='03')
    l_expense_3 = []
    for i in expense_3:
        l_expense_3.append(float(i.amount))
    r_expense_3 = sum(l_expense_3)
    r_balance_3 = r_balance_2+r_income_3 - r_expense_3

    income_4 = in_exp_items_daily.objects.filter(month='08', type='income', day='04')
    l_income_4 = []
    for i in income_4:
        l_income_4.append(float(i.amount))
    r_income_4 = sum(l_income_4)
    expense_4 = in_exp_items_daily.objects.filter(month='08', type='expense', day='04')
    l_expense_4 = []
    for i in expense_4:
        l_expense_4.append(float(i.amount))
    r_expense_4 = sum(l_expense_4)
    r_balance_4 = r_balance_3+r_income_4 - r_expense_4

    income_5 = in_exp_items_daily.objects.filter(month='08', type='income', day='05')
    l_income_5 = []
    for i in income_5:
        l_income_5.append(float(i.amount))
    r_income_5 = sum(l_income_5)
    expense_5 = in_exp_items_daily.objects.filter(month='08', type='expense', day='05')
    l_expense_5 = []
    for i in expense_5:
        l_expense_5.append(float(i.amount))
    r_expense_5 = sum(l_expense_5)
    r_balance_5 = r_balance_4+r_income_5 - r_expense_5

    income_6 = in_exp_items_daily.objects.filter(month='08', type='income', day='06')
    l_income_6 = []
    for i in income_6:
        l_income_6.append(float(i.amount))
    r_income_6 = sum(l_income_6)
    expense_6 = in_exp_items_daily.objects.filter(month='08', type='expense', day='06')
    l_expense_6 = []
    for i in expense_6:
        l_expense_6.append(float(i.amount))
    r_expense_6 = sum(l_expense_6)
    r_balance_6 = r_balance_5+r_income_6 - r_expense_6

    income_7 = in_exp_items_daily.objects.filter(month='08', type='income', day='07')
    l_income_7 = []
    for i in income_7:
        l_income_7.append(float(i.amount))
    r_income_7 = sum(l_income_7)
    expense_7 = in_exp_items_daily.objects.filter(month='08', type='expense', day='07')
    l_expense_7 = []
    for i in expense_7:
        l_expense_7.append(float(i.amount))
    r_expense_7 = sum(l_expense_7)
    r_balance_7 = r_balance_6+r_income_7 - r_expense_7
###***************************************
    income_8 = in_exp_items_daily.objects.filter(month='08', type='income', day='08')
    l_income_8 = []
    for i in income_8:
        l_income_8.append(float(i.amount))
    r_income_8 = sum(l_income_8)
    expense_8 = in_exp_items_daily.objects.filter(month='08', type='expense', day='08')
    l_expense_8 = []
    for i in expense_8:
        l_expense_8.append(float(i.amount))
    r_expense_8 = sum(l_expense_8)
    r_balance_8 = r_balance_7 + r_income_8 - r_expense_8

    income_9 = in_exp_items_daily.objects.filter(month='08', type='income', day='09')
    l_income_9 = []
    for i in income_9:
        l_income_9.append(float(i.amount))
    r_income_9 = sum(l_income_9)
    expense_9 = in_exp_items_daily.objects.filter(month='08', type='expense', day='09')
    l_expense_9 = []
    for i in expense_9:
        l_expense_9.append(float(i.amount))
    r_expense_9 = sum(l_expense_9)
    r_balance_9 = r_balance_8 + r_income_9 - r_expense_9

    income_10 = in_exp_items_daily.objects.filter(month='08', type='income', day='10')
    l_income_10 = []
    for i in income_10:
        l_income_10.append(float(i.amount))
    r_income_10 = sum(l_income_10)
    expense_10 = in_exp_items_daily.objects.filter(month='08', type='expense', day='10')
    l_expense_10 = []
    for i in expense_10:
        l_expense_10.append(float(i.amount))
    r_expense_10 = sum(l_expense_10)
    r_balance_10 = r_balance_9 + r_income_10 - r_expense_10

    income_11 = in_exp_items_daily.objects.filter(month='08', type='income', day='11')
    l_income_11 = []
    for i in income_11:
        l_income_11.append(float(i.amount))
    r_income_11 = sum(l_income_11)
    expense_11 = in_exp_items_daily.objects.filter(month='08', type='expense', day='11')
    l_expense_11 = []
    for i in expense_11:
        l_expense_11.append(float(i.amount))
    r_expense_11 = sum(l_expense_11)
    r_balance_11 = r_balance_10 + r_income_11 - r_expense_11

    income_12 = in_exp_items_daily.objects.filter(month='08', type='income', day='12')
    l_income_12 = []
    for i in income_12:
        l_income_12.append(float(i.amount))
    r_income_12 = sum(l_income_12)
    expense_12 = in_exp_items_daily.objects.filter(month='08', type='expense', day='12')
    l_expense_12 = []
    for i in expense_12:
        l_expense_12.append(float(i.amount))
    r_expense_12 = sum(l_expense_12)
    r_balance_12 = r_balance_11 + r_income_12 - r_expense_12

    income_13 = in_exp_items_daily.objects.filter(month='08', type='income', day='13')
    l_income_13 = []
    for i in income_13:
        l_income_13.append(float(i.amount))
    r_income_13 = sum(l_income_13)
    expense_13 = in_exp_items_daily.objects.filter(month='08', type='expense', day='13')
    l_expense_13 = []
    for i in expense_13:
        l_expense_13.append(float(i.amount))
    r_expense_13 = sum(l_expense_13)
    r_balance_13 = r_balance_12 + r_income_13 - r_expense_13

    income_14 = in_exp_items_daily.objects.filter(month='08', type='income', day='14')
    l_income_14 = []
    for i in income_14:
        l_income_14.append(float(i.amount))
    r_income_14 = sum(l_income_14)
    expense_14 = in_exp_items_daily.objects.filter(month='08', type='expense', day='14')
    l_expense_14 = []
    for i in expense_14:
        l_expense_14.append(float(i.amount))
    r_expense_14 = sum(l_expense_14)
    r_balance_14 = r_balance_13 + r_income_14 - r_expense_14
###*****************************
    income_15 = in_exp_items_daily.objects.filter(month='08', type='income', day='15')
    l_income_15 = []
    for i in income_15:
        l_income_15.append(float(i.amount))
    r_income_15 = sum(l_income_15)
    expense_15 = in_exp_items_daily.objects.filter(month='08', type='expense', day='15')
    l_expense_15 = []
    for i in expense_15:
        l_expense_15.append(float(i.amount))
    r_expense_15 = sum(l_expense_15)
    r_balance_15 = r_balance_14 + r_income_15 - r_expense_15

    income_16 = in_exp_items_daily.objects.filter(month='08', type='income', day='16')
    l_income_16 = []
    for i in income_16:
        l_income_16.append(float(i.amount))
    r_income_16 = sum(l_income_16)
    expense_16 = in_exp_items_daily.objects.filter(month='08', type='expense', day='16')
    l_expense_16 = []
    for i in expense_16:
        l_expense_16.append(float(i.amount))
    r_expense_16 = sum(l_expense_16)
    r_balance_16 = r_balance_15 + r_income_16 - r_expense_16

    income_17 = in_exp_items_daily.objects.filter(month='08', type='income', day='17')
    l_income_17 = []
    for i in income_17:
        l_income_17.append(float(i.amount))
    r_income_17 = sum(l_income_17)
    expense_17 = in_exp_items_daily.objects.filter(month='08', type='expense', day='17')
    l_expense_17 = []
    for i in expense_17:
        l_expense_17.append(float(i.amount))
    r_expense_17 = sum(l_expense_17)
    r_balance_17 = r_balance_16 + r_income_17 - r_expense_17

    income_18 = in_exp_items_daily.objects.filter(month='08', type='income', day='18')
    l_income_18 = []
    for i in income_18:
        l_income_18.append(float(i.amount))
    r_income_18 = sum(l_income_18)
    expense_18 = in_exp_items_daily.objects.filter(month='08', type='expense', day='18')
    l_expense_18 = []
    for i in expense_18:
        l_expense_18.append(float(i.amount))
    r_expense_18 = sum(l_expense_18)
    r_balance_18 = r_balance_17 + r_income_18 - r_expense_18

    income_19 = in_exp_items_daily.objects.filter(month='08', type='income', day='19')
    l_income_19 = []
    for i in income_19:
        l_income_19.append(float(i.amount))
    r_income_19 = sum(l_income_19)
    expense_19 = in_exp_items_daily.objects.filter(month='08', type='expense', day='19')
    l_expense_19 = []
    for i in expense_19:
        l_expense_19.append(float(i.amount))
    r_expense_19 = sum(l_expense_19)
    r_balance_19 = r_balance_18 + r_income_19 - r_expense_19

    income_20 = in_exp_items_daily.objects.filter(month='08', type='income', day='20')
    l_income_20 = []
    for i in income_20:
        l_income_20.append(float(i.amount))
    r_income_20 = sum(l_income_20)
    expense_20 = in_exp_items_daily.objects.filter(month='08', type='expense', day='20')
    l_expense_20 = []
    for i in expense_20:
        l_expense_20.append(float(i.amount))
    r_expense_20 = sum(l_expense_20)
    r_balance_20 = r_balance_19 + r_income_20 - r_expense_20

    income_21 = in_exp_items_daily.objects.filter(month='08', type='income', day='21')
    l_income_21 = []
    for i in income_21:
        l_income_21.append(float(i.amount))
    r_income_21 = sum(l_income_21)
    expense_21 = in_exp_items_daily.objects.filter(month='08', type='expense', day='21')
    l_expense_21 = []
    for i in expense_21:
        l_expense_21.append(float(i.amount))
    r_expense_21 = sum(l_expense_21)
    r_balance_21 = r_balance_20 + r_income_21 - r_expense_21

    income_22 = in_exp_items_daily.objects.filter(month='08', type='income', day='22')
    l_income_22 = []
    for i in income_22:
        l_income_22.append(float(i.amount))
    r_income_22 = sum(l_income_22)
    expense_22 = in_exp_items_daily.objects.filter(month='08', type='expense', day='22')
    l_expense_22 = []
    for i in expense_22:
        l_expense_22.append(float(i.amount))
    r_expense_22 = sum(l_expense_22)
    r_balance_22 = r_balance_21 + r_income_22 - r_expense_22
####************************
    income_23 = in_exp_items_daily.objects.filter(month='08', type='income', day='23')
    l_income_23 = []
    for i in income_23:
        l_income_23.append(float(i.amount))
    r_income_23 = sum(l_income_23)
    expense_23 = in_exp_items_daily.objects.filter(month='08', type='expense', day='23')
    l_expense_23 = []
    for i in expense_23:
        l_expense_23.append(float(i.amount))
    r_expense_23 = sum(l_expense_23)
    r_balance_23 = r_balance_22 + r_income_23 - r_expense_23

    income_24 = in_exp_items_daily.objects.filter(month='08', type='income', day='24')
    l_income_24 = []
    for i in income_24:
        l_income_24.append(float(i.amount))
    r_income_24 = sum(l_income_24)
    expense_24 = in_exp_items_daily.objects.filter(month='08', type='expense', day='24')
    l_expense_24 = []
    for i in expense_24:
        l_expense_24.append(float(i.amount))
    r_expense_24 = sum(l_expense_24)
    r_balance_24 = r_balance_23 + r_income_24 - r_expense_24

    income_25 = in_exp_items_daily.objects.filter(month='08', type='income', day='25')
    l_income_25 = []
    for i in income_25:
        l_income_25.append(float(i.amount))
    r_income_25 = sum(l_income_25)
    expense_25 = in_exp_items_daily.objects.filter(month='08', type='expense', day='25')
    l_expense_25 = []
    for i in expense_25:
        l_expense_25.append(float(i.amount))
    r_expense_25 = sum(l_expense_25)
    r_balance_25 = r_balance_24 + r_income_25 - r_expense_25

    income_26 = in_exp_items_daily.objects.filter(month='08', type='income', day='26')
    l_income_26 = []
    for i in income_26:
        l_income_26.append(float(i.amount))
    r_income_26 = sum(l_income_26)
    expense_26 = in_exp_items_daily.objects.filter(month='08', type='expense', day='26')
    l_expense_26 = []
    for i in expense_26:
        l_expense_26.append(float(i.amount))
    r_expense_26 = sum(l_expense_26)
    r_balance_26 = r_balance_25 + r_income_26 - r_expense_26

    income_27 = in_exp_items_daily.objects.filter(month='08', type='income', day='27')
    l_income_27 = []
    for i in income_27:
        l_income_27.append(float(i.amount))
    r_income_27 = sum(l_income_27)
    expense_27 = in_exp_items_daily.objects.filter(month='08', type='expense', day='27')
    l_expense_27 = []
    for i in expense_27:
        l_expense_27.append(float(i.amount))
    r_expense_27 = sum(l_expense_27)
    r_balance_27 = r_balance_26 + r_income_27 - r_expense_27

    income_28 = in_exp_items_daily.objects.filter(month='08', type='income', day='28')
    l_income_28 = []
    for i in income_28:
        l_income_28.append(float(i.amount))
    r_income_28 = sum(l_income_28)
    expense_28 = in_exp_items_daily.objects.filter(month='08', type='expense', day='28')
    l_expense_28 = []
    for i in expense_28:
        l_expense_28.append(float(i.amount))
    r_expense_28 = sum(l_expense_28)
    r_balance_28 = r_balance_27 + r_income_28 - r_expense_28
####**************************
    income_29 = in_exp_items_daily.objects.filter(month='08', type='income', day='29')
    l_income_29 = []
    for i in income_29:
        l_income_29.append(float(i.amount))
    r_income_29 = sum(l_income_29)
    expense_29 = in_exp_items_daily.objects.filter(month='08', type='expense', day='29')
    l_expense_29 = []
    for i in expense_29:
        l_expense_29.append(float(i.amount))
    r_expense_29 = sum(l_expense_29)
    r_balance_29 = r_balance_28 + r_income_29 - r_expense_29

    income_30 = in_exp_items_daily.objects.filter(month='08', type='income', day='30')
    l_income_30 = []
    for i in income_30:
        l_income_30.append(float(i.amount))
    r_income_30 = sum(l_income_30)
    expense_30 = in_exp_items_daily.objects.filter(month='08', type='expense', day='30')
    l_expense_30 = []
    for i in expense_30:
        l_expense_30.append(float(i.amount))
    r_expense_30 = sum(l_expense_30)
    r_balance_30 = r_balance_29 + r_income_30 - r_expense_30

    income_31 = in_exp_items_daily.objects.filter(month='08', type='income', day='31')
    l_income_31 = []
    for i in income_31:
        l_income_31.append(float(i.amount))
    r_income_31 = sum(l_income_31)
    expense_31 = in_exp_items_daily.objects.filter(month='08', type='expense', day='31')
    l_expense_31 = []
    for i in expense_31:
        l_expense_31.append(float(i.amount))
    r_expense_31 = sum(l_expense_31)
    r_balance_31 = r_balance_30 + r_income_31 - r_expense_31

##****************************************
    a = in_exp_items_daily.objects.all().filter(month='08')
    il=[]
    el=[]
    for i in a:
        if i.type == 'income':
            il.append(float(i.amount))
        if i.type == 'expense':
            el.append(float(i.amount))

    sil=sum(il)
    silop = sum(il)+aug_opening_balance
    sel=sum(el)
    d_bal = sil - sel


    context = {
        'object_list': queryset,
        'totals': totals,
        'res' : in_exp_items_daily.objects.all().filter(month='08'),

        'aug_opening_balance' : aug_opening_balance,
        'color' : color,

        'sil' : sil,
        'silop' : silop,
        'sel' : sel,
        'd_bal' : d_bal,

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

        'income_13': r_income_13,
        'expense_13': r_expense_13,
        'balance_13': r_balance_13,

        'income_14': r_income_14,
        'expense_14': r_expense_14,
        'balance_14': r_balance_14,

        'income_15': r_income_15,
        'expense_15': r_expense_15,
        'balance_15': r_balance_15,

        'income_16': r_income_16,
        'expense_16': r_expense_16,
        'balance_16': r_balance_16,

        'income_17': r_income_17,
        'expense_17': r_expense_17,
        'balance_17': r_balance_17,

        'income_18': r_income_18,
        'expense_18': r_expense_18,
        'balance_18': r_balance_18,

        'income_19': r_income_19,
        'expense_19': r_expense_19,
        'balance_19': r_balance_19,

        'income_20': r_income_20,
        'expense_20': r_expense_20,
        'balance_20': r_balance_20,

        'income_21': r_income_21,
        'expense_21': r_expense_21,
        'balance_21': r_balance_21,

        'income_22': r_income_22,
        'expense_22': r_expense_22,
        'balance_22': r_balance_22,

        'income_23': r_income_23,
        'expense_23': r_expense_23,
        'balance_23': r_balance_23,

        'income_24': r_income_24,
        'expense_24': r_expense_24,
        'balance_24': r_balance_24,

        'income_25': r_income_25,
        'expense_25': r_expense_25,
        'balance_25': r_balance_25,

        'income_26': r_income_26,
        'expense_26': r_expense_26,
        'balance_26': r_balance_26,

        'income_27': r_income_27,
        'expense_27': r_expense_27,
        'balance_27': r_balance_27,

        'income_28': r_income_28,
        'expense_28': r_expense_28,
        'balance_28': r_balance_28,

        'income_29': r_income_29,
        'expense_29': r_expense_29,
        'balance_29': r_balance_29,

        'income_30': r_income_30,
        'expense_30': r_expense_30,
        'balance_30': r_balance_30,

        'income_31': r_income_31,
        'expense_31': r_expense_31,
        'balance_31': r_balance_31,

    }
    return render(request,'branches/branch1/accounts/monthly_inc_exp/single_monthly_daily_in_exp_items_report.html',context)


