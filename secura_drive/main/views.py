from django.shortcuts import render, redirect
import requests
import api.file_crypto as fc
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_protect
from .models import *

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
    return render(request, 'main/index.html')


def drive_page(request):
    x = requests.get('http://127.0.0.1:8000/api/file')
    files = x.json()
    for file in files:
        size = format_bytes(file['file_size'])

        file['file_size'] = str("{:.2f}".format(size[0])) + " " + str(size[1])
    return render(request, 'main/drive.html', {"files": files})


def profile(request):
    return render(request, 'main/profile.html')


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
        user = User(username=data['username'],
                    password=data['password'], email=data['email'])
        user.save()
        profile = Profile(user=user)
        profile.save()
        return redirect('index')

    return render(request, 'main/login.html')


@csrf_protect
def login(request):
    return render(request, 'main/login.html')
