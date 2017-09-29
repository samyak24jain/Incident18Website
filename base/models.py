from django.core.validators import RegexValidator
from django.db import models

# Create your models here.

class Team(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class TeamMember(models.Model):
	team = models.ForeignKey(Team, on_delete=models.CASCADE, default='1')
	name = models.CharField(max_length=50)
	post = models.CharField(max_length=50)
	email = models.EmailField()
	image = models.ImageField(upload_to= 'teamimages/')
	phone_number = models.CharField(max_length=10, validators=[
    	RegexValidator(regex=r'^[7-9][0-9]*$')
    		])

	def __str__(self):
		return self.name