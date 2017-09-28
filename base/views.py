from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return render(request, 'base/home.html')

def team(request):
	return render(request, 'base/team.html')