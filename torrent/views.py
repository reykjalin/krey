from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Import forms
from .forms import TorrentForm

import subprocess

# Create your views here.

@login_required
def index(request):
    return render(request, 'torrent/index.html')

@login_required
def list(request):
    user = subprocess.check_output(['cat', '/etc/tduser']).decode().strip()
    pw = subprocess.check_output(['cat', '/etc/tdpw']).decode().strip()
    # TODO: Fix sanitation! What if 2 space in torrent name?
    tlist = subprocess.check_output(['transmission-remote', '-n', user + ':' + pw, '-l']).decode()
    tlines = tlist.split('\n')
    print(tlines)
    one_space = []
    for tl in tlines:
        line = ''
        first_space = True
        second_space = False
        for c in tl:
            if c == ' ' and first_space:
                line = line + c
                first_space = False
                second_space = True
            elif c == ' ' and not first_space and second_space:
                line = line + c
                second_space = False
                continue
            elif c == ' ' and not first_space and not second_space:
                continue
            else:
                line = line + c
                first_space = True
        # Slice away empty first column
        line_check = line.split('  ')
        if line_check[0] == '':
            line_check = line_check[1:]
        one_space.append(line_check)


    one_space[-2].insert(0, '')
    one_space[-2].insert(3, '')
    print(one_space)
    header = one_space[0]
    data   = one_space[1:]
    return render(request, 'torrent/list.html', {'header': header, 'data': data})

@login_required
def upload(request):
    if request.method == 'POST':
        print('post')
        form = TorrentForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/torrent/')
    else:
        print('new')
        form = TorrentForm()
    return render(request, 'torrent/upload.html', {'form': form})
