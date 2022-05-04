from .models import Dealer
from .models import Employee
from .models import Customer
from .models import Medicine
from .models import Purchase
from .models import Appointemnt
from django.shortcuts import render
from django.db import IntegrityError


def home(request):
    return render(request, 'pharma/index.html')


def dealerform(request):
    dict = {'add': True, }
    return render(request, 'pharma/dealer.html', dict)


def dealerforminsert(request):
    try:
        dealer = Dealer()
        dealer.dname = request.POST['dname']
        dealer.address = request.POST['address']
        dealer.phn_no = request.POST['pno']
        dealer.email = request.POST['email']
        dealer.save()
    except IntegrityError:
        return render(request, "pharma/new.html")
    return render(request, 'pharma/index.html')


def dealerformupdate(request, foo):
    try:
        dealer = Dealer.objects.get(pk=foo)
        dealer.dname = request.POST['dname']
        dealer.address = request.POST['address']
        dealer.phn_no = request.POST['pno']
        dealer.email = request.POST['email']
        dealer.save()
    except IntegrityError:
        return render(request, "pharma/new.html")
    return render(request, 'pharma/index.html')


def dealerformview(request, foo):
    dealer = Dealer.objects.get(pk=foo)
    dict = {'dealer': dealer}
    return render(request, 'pharma/dealer.html', dict)


def dealerformdelete(request, foo):
    dealer = Dealer.objects.get(pk=foo)
    dealer.delete()
    return render(request, 'pharma/index.html')


def dealertable(request):
    dealer = Dealer.objects.all()
    dict = {"dealer": dealer}
    return render(request, 'pharma/dealertable.html', dict)


def empform(request):
    dict = {'add': True}
    return render(request, 'pharma/emp.html', dict)


def empforminsert(request):
    try:
        emp = Employee()
        emp.e_id = request.POST['eid']
        emp.fname = request.POST['fname']
        emp.lname = request.POST['lname']
        emp.address = request.POST['address']
        emp.phn_no = request.POST['pno']
        emp.email = request.POST['email']
        emp.sal = request.POST['sal']
        emp.save()
    except IntegrityError:
        return render(request, "pharma/new.html")
    return render(request, 'pharma/index.html')


def empformupdate(request, foo):
    try:
        emp = Employee.objects.get(pk=foo)
        emp.e_id = request.POST['eid']
        emp.fname = request.POST['fname']
        emp.lname = request.POST['lname']
        emp.address = request.POST['address']
        emp.phn_no = request.POST['pno']
        emp.email = request.POST['email']
        emp.sal = request.POST['sal']
        emp.save()
    except IntegrityError:
        return render(request, "pharma/new.html")
    return render(request, 'pharma/index.html')


def empformview(request, foo):
    emp = Employee.objects.get(pk=foo)
    dict = {'emp': emp}
    return render(request, 'pharma/emp.html', dict)


def empformdelete(request, foo):
    emp = Employee.objects.get(pk=foo)
    emp.delete()
    return render(request, 'pharma/index.html')


def emptable(request):
    emp = Employee.objects.all()
    dict = {"emp": emp}
    return render(request, 'pharma/emptable.html', dict)


def custform(request):
    dict = {'add': True}
    return render(request, 'pharma/cust.html', dict)


def custforminsert(request):
    try:
        cust = Customer()
        cust.fname = request.POST['fname']
        cust.lname = request.POST['lname']
        cust.address = request.POST['address']
        cust.phn_no = request.POST['pno']
        cust.email = request.POST['email']
        cust.save()
    except IntegrityError:
        return render(request, "pharma/new.html")
    return render(request, 'pharma/index.html')


def custformupdate(request, foo):
    try:
        cust = Customer.objects.get(pk=foo)
        cust.fname = request.POST['fname']
        cust.lname = request.POST['lname']
        cust.address = request.POST['address']
        cust.phn_no = request.POST['pno']
        cust.email = request.POST['email']
        cust.save()
    except IntegrityError:
        return render(request, "pharma/new.html")
    return render(request, 'pharma/index.html')


def custformview(request, foo):
    cust = Customer.objects.get(pk=foo)
    dict = {'cust': cust}
    return render(request, 'pharma/cust.html', dict)


def custformdelete(request, foo):
    cust = Customer.objects.get(pk=foo)
    cust.delete()
    return render(request, 'pharma/index.html')


def custtable(request):
    cust = Customer.objects.all()
    dict = {"cust": cust}
    return render(request, 'pharma/custtable.html', dict)


def medform(request):
    dict = {'add': True}
    return render(request, 'pharma/med.html', dict)


def medforminsert(request):
    try:
        med = Medicine()
        med.m_id = request.POST['mid']
        med.mname = request.POST['mname']
        med.dname = request.POST['dname']
        med.desc = request.POST['desc']
        med.price = request.POST['price']
        med.stock = request.POST['stock']
        med.save()
    except IntegrityError:
        return render(request, "pharma/new.html")
    return render(request, 'pharma/index.html')


def medformupdate(request, foo):
    try:
        med = Medicine.objects.get(pk=foo)
        med.m_id = request.POST['mid']
        med.mname = request.POST['mname']
        med.dname = request.POST['dname']
        med.desc = request.POST['desc']
        med.price = request.POST['price']
        med.stock = request.POST['stock']
        med.save()
    except IntegrityError:
        return render(request, "pharma/new.html")
    return render(request, 'pharma/index.html')


def medformview(request, foo):
    med = Medicine.objects.get(pk=foo)
    dict = {'med': med}
    return render(request, 'pharma/med.html', dict)


def medformdelete(request, foo):
    med = Medicine.objects.get(pk=foo)
    med.delete()
    return render(request, 'pharma/index.html')


def medtable(request):
    med = Medicine.objects.all()
    dict = {"med": med}
    return render(request, 'pharma/medtable.html', dict)


def purchaseform(request):
    dict = {'add': True}
    return render(request, 'pharma/purchase.html', dict)


def purchaseforminsert(request):
    try:
        purchase = Purchase()
        purchase.pname = request.POST['pname']
        purchase.fname = request.POST['fname']
        purchase.lname = request.POST['lname']
        purchase.qty = request.POST['qty']
        purchase.phn_no = request.POST['pno']
        purchase.price = request.POST['price']
        a = (int(purchase.price)) * (int(purchase.qty))
        purchase.total = a
        purchase.save()
    except IntegrityError:
        return render(request, "pharma/new.html")
    return render(request, 'pharma/index.html')


def purchaseformupdate(request, foo):
    try:
        purchase = Purchase.objects.get(pk=foo)
        purchase.pname = request.POST['pname']
        purchase.fname = request.POST['fname']
        purchase.lname = request.POST['lname']
        purchase.qty = request.POST['qty']
        purchase.phn_no = request.POST['pno']
        purchase.price = request.POST['price']
        a = (int(purchase.price)) * (int(purchase.qty))
        purchase.total = a
        purchase.save()
    except IntegrityError:
        return render(request, "pharma/new.html")
    return render(request, 'pharma/index.html')


def purchaseformview(request, foo):
    purchase = Purchase.objects.get(pk=foo)
    dict = {'purchase': purchase}
    return render(request, 'pharma/purchase.html', dict)


def purchaseformdelete(request, foo):
    purchase = Purchase.objects.get(pk=foo)
    purchase.delete()
    return render(request, 'pharma/index.html')


def purchasetable(request):
    purchase = Purchase.objects.all()
    dict = {"purchase": purchase}
    return render(request, 'pharma/purchasetable.html', dict)


def appform(request):
    dict = {'add': True}
    return render(request, 'pharma/app.html', dict)


def appforminsert(request):
    try:
        app = Appointemnt()
        app.fname = request.POST['fname']
        app.lname = request.POST['lname']
        app.sickness = request.POST['address']
        app.phn_no = request.POST['pno']
        app.date = request.POST['email']
        app.save()
    except IntegrityError:
        return render(request, "pharma/new.html")
    return render(request, 'pharma/index.html')


def appformupdate(request, foo):
    try:
        app = Appointemnt.objects.get(pk=foo)
        app.fname = request.POST['fname']
        app.lname = request.POST['lname']
        app.sickness = request.POST['address']
        app.phn_no = request.POST['pno']
        app.date = request.POST['email']
        app.save()
    except IntegrityError:
        return render(request, "pharma/new.html")
    return render(request, 'pharma/index.html')


def appformview(request, foo):
    app = Appointemnt.objects.get(pk=foo)
    dict = {'app': app}
    return render(request, 'pharma/app.html', dict)


def appformdelete(request, foo):
    app = Appointemnt.objects.get(pk=foo)
    app.delete()
    return render(request, 'pharma/index.html')


def apptable(request):
    app = Appointemnt.objects.all()
    dict = {"app": app}
    return render(request, 'pharma/apptable.html', dict)

