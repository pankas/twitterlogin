# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from datetime import datetime


def home(request):
    current_user = "Mable Marbles"
    return render(request, 'home.html',
        {'date': datetime.now().year,'login' : current_user})
