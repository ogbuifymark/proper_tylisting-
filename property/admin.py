from django.contrib import admin

from .models import User, Role, State, Axis,Property, Type
# Register your models here.

admin.site.register(User)
admin.site.register(Role)
admin.site.register(State)
admin.site.register(Axis)
admin.site.register(Property)
admin.site.register(Type)