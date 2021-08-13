from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from Auth.models import Account
import Auth.Token as token
import time

err_miss = "Missing Fields!"
err_inv = "Invalid Credentials!"


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not email or not password:
            return render(request, "auth/login.html",
                          {'title': 'Login', 'type': '1', 'msg': err_miss})
        acc_exist = Account.objects.filter(email=email).exists()
        if acc_exist:
            data = Account.objects.get(email=email)
            if data.password == token.pass_hash(password):
                payload = {
                    'c_id': data.id,
                    'fname': data.fname, 'lname': data.lname, 'email': data.email, 'time': time.time()
                }
                client_token = token.gen_token(payload)
                data.token = client_token
                data.save()
                res = HttpResponse("Login Success")
                res.set_cookie("Auth", client_token)
                return res
        return render(request, "auth/login.html", {'title': 'Login', 'type': '0', 'msg': err_inv})
    return render(request, "auth/login.html", {'title': 'Login', 'type': '-1', 'msg': ''})


def newAccount(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        gender = request.POST.get('gender')
        country = request.POST.get('country')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not email or not password or not fname or not lname or not gender:
            return render(request, "auth/newAccount.html", {'title': 'New Account', 'type': '1', 'msg': err_miss})
        account = Account.objects.filter(email=email).exists()
        if account:
            return render(request, "auth/newAccount.html", {'title': 'New Account', 'type': '0', 'msg': 'Email Already Exist!'})
        account = Account(fname=fname, lname=lname, gender=gender,
                          country=country, email=email, password=token.pass_hash(password), token="None")
        account.save()
        return render(request, "auth/login.html", {'title': 'Login', 'type': '1', 'msg': 'Account Created Successsfully!'})
    return render(request, "auth/newAccount.html", {'title': 'New Account'})


def forgotPass(request):
    return HttpResponse("ForgotPass Page")
