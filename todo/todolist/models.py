from django.db import models
from datetime import datetime
# Create your models here.
class todo(models.Model): #Table name, has to wrap models.Model to get the functionality of Django.  
    name = models.CharField(max_length=100, unique=True) #Like a VARCHAR field
    description = models.TextField() #Like a TEXT field
    created = models.DateTimeField(default=datetime.now) #Like a DATETIME field
    def __str__(self): #Tell it to return as a unicode string (The name of the to-do item) rather than just Object.
        return self.name

class users(models.Model):
	name = models.CharField(max_length=25)
	surname = models.TextField()
	def __str__(self):
		return self.name

class emails_sub(models.Model):
	email = models.CharField(max_length=50)
	def __str__(self):
		return self.email

class contact_page_model(models.Model):
	name	= models.CharField(max_length=50)
	email 	= models.CharField(max_length=50)
	phone 	= models.CharField(max_length=50)
	message = models.CharField(max_length=200)
	def __str__(self):
		return self.name