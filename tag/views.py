# coding: utf-8

# 근데 이건 뭐지
from django.shortcuts import render

# over django 1.2 csrf verification needed unless 403 forbidden csrf verification failed error.
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.http import HttpResponse

@csrf_exempt
def hello(request):
        if request.method == 'POST':
                return HttpResponse("hello")
        else:
                return HttpResponse("get")
