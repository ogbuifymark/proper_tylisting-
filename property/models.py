from django.db import models
# from django.contrib.postgres.fields import ArrayField
from django_mysql.models import ListCharField

# Create your models here.
class Role(models.Model):
    name= models.TextField(null=False)

class User (models.Model):
    name=models.TextField(null=False)
    phone_number = models.TextField(null=False)
    email = models.TextField(null=False)
    username = models.TextField(null=False)
    password= models.TextField(null=False)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, default=1)

class State(models.Model):
    name = models.TextField(null=False)
    hidden = models.BooleanField(null=False)

class Axis(models.Model):
    name = models.TextField(null=False)
    hidden = models.BooleanField(null=False)

class Type(models.Model):
    name = models.TextField(null=False)
    hidden = models.BooleanField(null=False)

class Property(models.Model):
    title = models.TextField(null=False)
    beds = models.IntegerField(null=False)
    address= models.TextField(null= False)
    states = models.ForeignKey(State, on_delete= models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    disposed = models.BooleanField(null=False)
    published = models.BooleanField(null=False)
    image = ListCharField(base_field=models.CharField(max_length=10, null=True, default='my_directory'),size=6, max_length=(10 * 50))
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    description = models.TextField(null= True)




