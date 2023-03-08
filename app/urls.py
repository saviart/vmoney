"""paidme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('',views.index, name ="index"),
    path('signin/', views.signin, name = "signin"),
    path('signup/', views.signup, name = "signup"),
    path('signup/<str:ref>/', views.signup, name="signupbyref"),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('signout/', views.signout, name = "signout"),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('earn/', views.earn, name="earn"),
    path('withdraw/', views.withdraw, name="rewards"),
    path('leaderboard/', views.leaderboard, name="leaderboard"),
    path('ref/', views.ref, name="affiliate"),
    path('profile/', views.profile, name="profile"),
    path('privacy/', views.privacy, name="privacy"),
    path('terms/', views.terms, name="terms"),
    path('faq/', views.faq, name="faq"),
    path('contact/', views.contact, name="contact"),
    path('withdraw/ltc', views.ltc, name="ltc"),
    path('withdraw/doge', views.doge, name="doge"),
    path('withdraw/paypal', views.paypal, name="paypal"),
    path('withdraw/google', views.google, name="google"),
    path('withdraw/apple', views.apple, name="apple"),
    path('withdraw/amazon', views.amazon, name="amazon"),
    path('withdraw/roblox', views.roblox, name="roblox"),
    path('withdraw/steam', views.steam, name="steam"),
    path('ipproxy/', views.apiproxy, name="apiproxy"),
    path('ipproxy2/', views.apiproxy2, name="apiproxy2"),
    path('success', views.MmwallPostBack.as_view(), name='mmwallPostBack'),


]