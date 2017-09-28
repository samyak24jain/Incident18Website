from django.core.validators import RegexValidator
from django.db import models

# Create your models here.

class Team(models.Model):
	name = models.CharField(max_length=50)

class TeamMember(models.Model):
	team = models.ForeignKey(Team, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	post = models.CharField(max_length=50)
	email = models.EmailField()
	phone_number = models.CharField(max_length=10, validators=[
    	RegexValidator(regex=r'^[7-9][0-9]*$')
    		])