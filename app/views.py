import random
import string

import names
import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import PermissionDenied
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.template.loader import get_template
from django.templatetags.static import static
from django.utils.crypto import get_random_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.decorators.http import require_GET
from ipware import get_client_ip
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.list_name import listname
from .forms import WebleadRegisterForm, SignupForm
from .models import User
from .token import account_activation_token


# LOGIC
def apiproxy(request):
    requestst = "https://iproxy.shop/api/proxyAll.php?key=5b00c4f43935ed6173575cf786a87287330938a6015189e30d4ca5a8b1dd6d3c027076951c32e409977518f427bdebbbf510e6ecd16b80be48eb3f75bf031572&rip=1"
    getipapi = requests.get(requestst)
    getipapi = getipapi.text
    return render(request, "ipproxy.html",{"getipapi":getipapi})

def apiproxy2(request):
    requestst = "https://iproxy.shop/api/proxyAll.php?key=cea02a9a924dddeaf13e312dc62a89c04d0aaa6a40ed0037dfecc666b9e5df96719b07d6a751937577934c5601fb6a4ace0f4b4617923b81e9fa501d6fd9ebfd&rip=1"
    getipapi = requests.get(requestst)
    getipapi = getipapi.text
    return render(request, "ipproxy.html",{"getipapi":getipapi})


def getgeoip(ip_adress):
    resp = requests.get('http://ip-api.com/json/' + str(ip_adress))
    if resp.status_code == 200:
        try:
            ipgeolocal = resp.json()
            ipgeolocal = ipgeolocal["countryCode"]
        except:
            ipgeolocal = 'Unknow'

    else:
        ipgeolocal = 'Unknow'
    return ipgeolocal


class timeline(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        requestst = "https://saviartmedia.tech/api/v2/timeline/?site=lootcash"
        timeline = requests.get(requestst)

        timelinedata = timeline.json()
        return Response(timelinedata)

class MmwallPostBack(APIView):
    permission_classes = [permissions.AllowAny]
    # https://wall.lootcash.net/api/postback/mmwall/success?user_id={user_id}&amount={amount}&payout={payout}&transaction_id={transaction_id}&user_ip={user_ip}&subid={subid}&offerid={offerid}&offername={offername}
    def get(self, request):
        data = request.query_params
        user_id = data['user_id']
        amount = data['amount']
        payout = data['payout']
        offername = data['offername']
        user_ip = data['user_ip']
        requestst = "https://wall.lootcash.net/api/postback/mmwall/?user_id={user_id}&amount={amount}&payout={payout}&user_ip={user_ip}&offername={offername}".format(
            user_id=user_id,amount=amount,payout=payout,offername=offername,user_ip=user_ip)
        r = requests.get(requestst)
        if r.status_code == 200:
            return Response(1, status=status.HTTP_200_OK)
        else:
            return Response(0, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def generateid(numb):
    allowed_chars = ''.join((string.ascii_letters, string.digits))
    unique_id = 'LC-' + ''.join(random.choice(allowed_chars) for _ in range(numb))
    unique_id = unique_id.upper()
    return unique_id


# VIEWS
def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, "Thank you for your email confirmation. Now you can login your account.")
        return render(request, 'index.html')
    else:
        messages.error(request, "Activation link is invalid!")

    return render(request, 'signin.html')


def activateEmail(request, user, to_email):

    mail_title = "Lootcash - Account verification."
    context = {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    }
    html = get_template('template_activate_account.html').render(context)

    email = EmailMultiAlternatives(mail_title, html, to=[to_email])
    email.attach_alternative(html, "text/html")
    if email.send():
        messages.success(request,
                         "Account was created, please go to you email click on received activation link to confirm and complete the registration")
    else:
        messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly.')


def index(request):
    @require_GET
    def get(request):
        data = request.query_params
        user_id = data['user_id']
        amount = data['amount']
        payout = data['payout']
        offername = data['offername']
        user_ip = data['user_ip']
        requestst = "https://wall.lootcash.net/api/postback/mmwall/success?user_id={user_id}&amount={amount}&payout={payout}&user_ip={user_ip}&offername={offername}".format(
            user_id=user_id, amount=amount, payout=payout, offername=offername, user_ip=user_ip)
        r = requests.post(requestst)
        if r.status_code == 200:
            return Response(1, status=status.HTTP_200_OK)
        else:
            return Response(0, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return render(request, "index.html")


def signin(request):
    if request.method == 'POST':  # Nếu như nhận được POST method đăng nhập
        form = AuthenticationForm(request, data=request.POST)
        context = {"form": form}
        if form.is_valid():  # Kiểm tra dữ liệu nhập vào có phù hợp hay không, nếu có thì thực hiện dăng nhâp
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:  # Nếu có user phù hợp với đăng nhập
                if user.is_baned == False:  # User không bị baned
                    login(request, user)
                    user_id = user.user_id
                    total_ref = User.objects.filter(recommended_by=user.username).count()
                    request.session['total_ref'] = total_ref
                    user_joindate = user.date_joined
                    request.session['user_joindate'] = str(user_joindate)
                    getcoins = "https://saviartmedia.tech/api/v1/getusercoins/?membersite_id={user_id}".format(
                        user_id=user_id)
                    r = requests.get(getcoins)
                    if r.status_code == 200:
                        try:
                            raw = r.json()
                            coins = raw['membersite_amount']

                            User.objects.filter(user_id=user_id).update(
                                user_coins=coins)
                        except:
                            print('khong co user')

                        # Đoạn này thêm ghi đè dữ liệu user_coins từ site quản lý về db của site phụ

                        # Gửi post lấy token của user để thực hiện các API yêu cầu quyền

                    payload = {'username': username, 'password': password, 'grant_type': 'password',
                               'client_id': 'bmZ7rnlnPdTut7Ooq3GaP18vGVHcEju96n2miUbf',
                               'client_secret': '2ywAik8tzvq6CgCh7ic8pkqWf7rmYqm71ptCzfhQxnFbht5VzrS6xxlmaXlEisC2wmkrLGCCuoSR0KfS3ogNP0a7UkU3O64qQOVp4fiu31wGuY3SF86Id72APMhEEQ6o'}
                    url = "http://127.0.0.1:8000/o/token/"
                    r = requests.post(url, data=payload)
                    if r.status_code == 200:
                        oauth2token = r.json()
                        token = oauth2token['access_token']

                        request.session['access_token'] = token
                        refresh_token = oauth2token['refresh_token']
                        request.session['oauth2token'] = oauth2token
                    return render(request, "index.html")
                else:
                    form = AuthenticationForm()
                    context = {"form": form}
                    messages.error(request, "Your account has disabled.")
                return render(request, "signin.html", context)


            else:
                form = AuthenticationForm(request.POST)
                context = {"form": form}
                messages.error(request, "Account does not exist, please try again")
            return render(request, 'signin.html', context)
        else:
            form = AuthenticationForm()
            context = {"form": form}
            messages.error(request, "Either your E-mail/Username or password is wrong..")
        return render(request, "signin.html", context)

    return render(request, "signin.html")


def generate_username():
    fakename = names.get_full_name()
    fakenane = fakename.split(" ")
    r = random.randint(1, 3)
    n = random.randint(1, 2)
    if r == 1:
        if n == 1:
            fakename = fakenane[0] + str(random.randint(1, 9999))
        else:
            fakename = fakenane[0] + str(get_random_string(1)) + str(random.randint(1980, 2022))

    elif r == 2:
        if n == 1:
            fakename = fakenane[1] + str(random.randint(1, 2999))
        else:
            fakename = fakenane[1] + str(get_random_string(1)) + str(random.randint(1980, 2022))
    else:
        if n == 1:
            fakename = fakenane[0] + fakenane[1].lower()
        else:
            fakename = fakenane[0] + fakenane[1].lower() + str(random.randint(1, 9999))

    return fakename


def getavatarurl():
    r = random.randint(1, 100)
    if r > 60:
        r = random.randint(100000, 103256)
        urlavatar = static('public/assets/avatar/'+ str(r)+'.jpg')
        urlavatar = 'https://lootcash.net' + str(urlavatar)
    else:
        urlavatar = ''
    return urlavatar


def weblogin(request):
    if "member_id" in request.session:
        if request.session['member_id'] is not None:
            return redirect("/weblead")
    if request.method == 'POST':
        form = WebleadRegisterForm(request.POST)
        if form.is_valid():
            ip, is_routable = get_client_ip(request)
            geo = getgeoip(ip)
            r = random.randint(1, 100)
            if r > 80:
                fakename = generate_username()
            else:
                fakename = random.choice(listname)
            membersite_username = form.cleaned_data['membername']
            membersite_id = generateid(12)
            membersite_site = request.get_host().split(":")[0]
            membersite_ip = ip
            membersite_geo = geo
            membersite_name = fakename
            membersite_avatar = getavatarurl()

            requestst = "https://saviartmedia.tech/api/v1/members/?membersite_username={membersite_username}&membersite_id={membersite_id}&membersite_site={membersite_site}&membersite_geo={membersite_geo}&membersite_name={membersite_name}&membersite_ip={membersite_ip}&membersite_avatar={membersite_avatar}".format(
                membersite_id=membersite_id, membersite_username=membersite_username,
                membersite_site=membersite_site,
                membersite_ip=membersite_ip, membersite_geo=membersite_geo,
                membersite_name=membersite_name, membersite_avatar=membersite_avatar)
            r = requests.post(requestst)
            if r.status_code == 200:
                request.session['member_id'] = membersite_id
                request.session['member_username'] = membersite_username
                return redirect("/weblead")
            else:
                error = r.json()

                return redirect("/weblogin")
        else:
            error = form.errors
            return redirect("/weblogin")

    return render(request, 'weblead/weblogin.html')

def webclick(request):
    if "member_id" in request.session:
        if request.session['member_id'] is not None:
            return redirect("/weblead")
            print('here')
    else:
            print('1')
            ip, is_routable = get_client_ip(request)
            geo = getgeoip(ip)
            r = random.randint(1, 100)
            if r > 80:
                fakename = generate_username()
            else:
                fakename = random.choice(listname)

            membersite_username = 'Click' + str(get_random_string(length=20))
            membersite_id = generateid(12)
            membersite_site = request.get_host().split(":")[0]
            membersite_ip = ip
            membersite_geo = geo
            membersite_name = fakename
            membersite_avatar = getavatarurl()

            requestst = "https://saviartmedia.tech/api/v1/members/?membersite_username={membersite_username}&membersite_id={membersite_id}&membersite_site={membersite_site}&membersite_geo={membersite_geo}&membersite_name={membersite_name}&membersite_ip={membersite_ip}&membersite_avatar={membersite_avatar}".format(
                membersite_id=membersite_id, membersite_username=membersite_username,
                membersite_site=membersite_site,
                membersite_ip=membersite_ip, membersite_geo=membersite_geo,
                membersite_name=membersite_name, membersite_avatar=membersite_avatar)
            r = requests.post(requestst)
            print(r)
            if r.status_code == 200:
                request.session['member_id'] = membersite_id
                request.session['member_username'] = membersite_username
                return redirect("/weblead")
            else:
                error = r.json()
                return redirect("/webclick")
    return render(request, 'weblead/webclick.html')

def weblead(request):
    """Renders the home page."""
    require_login(request)
    members_id = request.session['member_id']
    member_coins = 0
    request.session['member_coins'] = member_coins

    template = loader.get_template('weblead/weblead.html')
    return HttpResponse(
        template.render(
            {"member_id": members_id}, request))


def require_login(request):
    if "member_id" in request.session:
        if request.session['member_id'] is not None:
            return
    raise PermissionDenied


def signup(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect('/')
    # Nếu đã đăng nhập rồi thì chuyển hướng về home
    else:
        form = SignupForm()
        context = {"form": form}
        if request.POST:
            form = SignupForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.user_name = form.cleaned_data["username"]
                user.user_id = generateid(12)
                user.ref_code = user.user_id
                code_ref = str(kwargs.get('ref'))
                ref_user_name = User.objects.filter(ref_code=code_ref).first()
                user.recommended_by = ref_user_name
                user.avatar = ""
                user.save()
                ip, is_routable = get_client_ip(request)
                membersite_username = user.username
                membersite_id = user.user_id
                membersite_site = 'wall.lootcash.net'
                membersite_ip = ip
                geo = getgeoip(ip)
                membersite_geo = geo
                membersite_name = user.username
                membersite_avatar = user.avatar
                requestst = "https://saviartmedia.tech/api/v1/members/?membersite_username={membersite_username}&membersite_id={membersite_id}&membersite_site={membersite_site}&membersite_geo={membersite_geo}&membersite_name={membersite_name}&membersite_ip={membersite_ip}&memberstie_avatar={membersite_avatar}".format(
                    membersite_id=membersite_id, membersite_username=membersite_username,
                    membersite_site=membersite_site,
                    membersite_ip=membersite_ip, membersite_geo=membersite_geo,
                    membersite_name=membersite_name, membersite_avatar=membersite_avatar)
                r = requests.post(requestst)
                activateEmail(request, user, form.cleaned_data.get('email'))
                return redirect("signin")
            else:
                context = {"form": form}
                messages.error(request, form.errors.as_data())
            return render(request, "signup.html", context)
    return render(request, "signup.html", context)




def signout(request):
    request.session.clear()
    logout(request)
    return redirect('/')


def earn(request):
    return render(request, "earn.html")


def withdraw(request):
    return render(request, "withdraw.html")


def ref(request):
    return render(request, "referral.html")


def profile(request):
    return render(request, "profile.html")


def leaderboard(request):
    requestst_ranking = "https://saviartmedia.tech/api/v1/getrankingsite/?site=lootcash"
    rank = requests.get(requestst_ranking)
    rankdata = rank.json()
    for i, item in enumerate(rankdata):
        if i == 0:
            item["prize"] = 1000 - (i*500)
        else:
            item["prize"] = 500 - (i * 5)
    return render(request, "leaderboard.html", {"rankdata": rankdata})


def ltc(request):
    return render(request, "withdraw/payltc.html")


def doge(request):
    return render(request, "withdraw/paydoge.html")


def paypal(request):
    return render(request, "withdraw/paypaypal.html")


def google(request):
    return render(request, "withdraw/paygoogle.html")


def apple(request):
    return render(request, "withdraw/payapple.html")


def amazon(request):
    return render(request, "withdraw/payamazon.html")


def roblox(request):
    return render(request, "withdraw/payroblox.html")


def steam(request):
    return render(request, "withdraw/paysteam.html")


def playstation(request):
    return render(request, "withdraw/payplaystation.html")


def xbox(request):
    return render(request, "withdraw/payxbox.html")


def nintendo(request):
    return render(request, "withdraw/paynintendo.html")

def privacy(request):
    return render(request, "privacy.html")

def terms(request):
    return render(request, "terms.html")

def faq(request):
    return render(request, "faq.html")

def contact(request):
    return render(request, "contact.html")

