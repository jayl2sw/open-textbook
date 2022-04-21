from nturl2path import url2pathname
from django.shortcuts import redirect

def index(request):
    return redirect('accounts:index')