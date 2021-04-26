from django.shortcuts import render, redirect
import requests
import api.file_crypto as fc
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from .models import *
from django.contrib.auth import authenticate, login as djangoLogin, logout as djangoLogout
from django.contrib.auth.decorators import login_required
# Create your views here.
KEY = b'NtEvVBWbzSEBu6axGA21Aw6pt3MsO1zFM_mCu9Al8oM='


def format_bytes(size):
    # 2**10 = 1024
    power = 2**10
    n = 0
    power_labels = {0: '', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return size, power_labels[n]+'B'


def home(request):
    return render(request, 'main/index.html',{'is_Auth':request.user.is_authenticated})

@login_required(login_url='/login')
def drive_page(request):
    user = request.user
    profile = Profile.objects.filter(user=user)[0]
    print(profile, profile.id)
    x = requests.get('http://127.0.0.1:8000/api/file', params={'profile':profile.id,'is_Auth':request.user.is_authenticated})
    files = x.json()
    for file in files:
        size = format_bytes(file['file_size'])
        file['file_size'] = str("{:.2f}".format(size[0])) + " " + str(size[1])
    return render(request, 'main/drive.html',{'user':user,'profile':profile, 'files':files,'is_Auth':request.user.is_authenticated})

@login_required(login_url='/login')
def profile(request):
    user = request.user
    return render(request, 'main/profile.html', {'user':user,'profile':profile,'is_Auth':request.user.is_authenticated})


def delete_file(request, id):
    x = requests.delete('http://127.0.0.1:8000/api/file/'+id)

    return redirect('/drive')


def view_file(request, id):

    x = requests.get('http://127.0.0.1:8000/api/file/'+id)
    file = x.json()

    data = file['file_data'][2:-1].encode('utf-8')

    decrypted = fc.decrypt(data, KEY)

    return HttpResponse(decrypted, content_type=file['file_content_type'])


@csrf_protect
def register(request):
    if request.method == 'POST':
        data = request.POST
        user = User.objects.create_user(username=data['username'], email=data['email'],
                                        password=data['password'], first_name=data['first_name'], last_name=data['last_name'])
        user.save()
        profile = Profile(user=user)
        profile.save()
        user = authenticate(request, username=data['username'], password=data['password'])
        djangoLogin(request, user)
        return redirect('/drive')

    return render(request, 'main/login.html')


@csrf_protect
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            djangoLogin(request, user)
            return redirect('/drive')
        else:
            return redirect('/login')
    return render(request, 'main/login.html')

def logout(request):
    djangoLogout(request)
    return redirect("/")