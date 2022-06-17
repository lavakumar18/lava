from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def kholi(request):
    return HttpResponse('kholi is the worst batsmen in the world')
