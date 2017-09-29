from django.shortcuts import render
from django.http import HttpResponse
from .models import Team, TeamMember

def index(request):
	return render(request, 'base/home.html')

def team(request):
	teams = Team.objects.all().order_by('name')
	context = { 'teams' : teams }
	return render(request, 'base/team.html', context)

def sponsors(request):
	return render(request, 'base/sponsors.html')