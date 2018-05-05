from django.shortcuts import render
from django.http import HttpResponse
from .models import Property, Type, User
from  .Util import utility


# Create your views here.
def index(request):
    properties = Property.objects.filter(disposed= 1)

    return render(request, 'common/index.html', {'properties':properties})

def add_property(request):
    if request.method == "POST":
        title = request.POST['title']
        beds = request.POST['beds']
        address = request.POST['address']
        email = request.POST['email']
        password = request.POST['password']
        role = 1
        ScrumyUser.objects.create(
            first_name=first_name,
            last_name=last_name,
            user_name=user_name,
            email=email,
            password=password,
            role_id=role
        )

        users = ScrumyUser.objects.all()

        return render(request, 'adduser.html', {'stateDropDown': stateDropDown})


    stateDropDown = utility.state_dropdown_list()
    typeDropDown = utility.type_dropdown_list()
    return render(request, 'agents/save_property.html', {'stateDropDown':stateDropDown,'typeDropDown':typeDropDown })
