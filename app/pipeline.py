import requests
from django.shortcuts import render
from django.contrib import messages
from .models import User
from app.views import generateid, getgeoip


def get_avatar(backend, strategy, details, response,
        user=None, *args, **kwargs):
    url = None
    if backend.name == 'facebook':
        url = "http://graph.facebook.com/%s/picture?type=large"%response['id']
        # if you need a square picture from fb, this line help you
        url = "http://graph.facebook.com/%s/picture?width=150&height=150"%response['id']
    if backend.name == 'twitter':
        url = response.get('profile_image_url', '').replace('_normal','')
    if backend.name == 'google-oauth2':
        url = response.get('picture')
    if url:
        user.avatar = url
        user.user_id = generateid(15)
        user.ref_code = user.user_id
        code_ref = str(kwargs.get('ref'))
        ref_user_name = User.objects.filter(ref_code=code_ref).first()
        user.recommended_by = ref_user_name
        user.user_name = user.username

        #gửi data user về site quản lý
        membersite_username = user.username
        membersite_id = user.user_id
        membersite_site = 'wall.lootcash.net'
        membersite_ip = "Unknow"
        membersite_geo = "Unknow"
        membersite_name = user.username
        membersite_avatar = url
        requestst = "https://saviartmedia.tech/api/v1/members/?membersite_username={membersite_username}&membersite_id={membersite_id}&membersite_site={membersite_site}&membersite_geo={membersite_geo}&membersite_name={membersite_name}&membersite_ip={membersite_ip}&memberstie_avatar={membersite_avatar}".format(
            membersite_id=membersite_id, membersite_username=membersite_username,
            membersite_site=membersite_site,
            membersite_ip=membersite_ip, membersite_geo=membersite_geo,
            membersite_name=membersite_name, membersite_avatar=membersite_avatar)
        r = requests.post(requestst)
        user.save()


