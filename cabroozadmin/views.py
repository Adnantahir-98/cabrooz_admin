from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from django.contrib import messages
from .models import *


# Create your views here.
@login_required
def index(request):
    dashboards = Dashboard.objects.all()
    recentride = RecentRide.objects.all()
    return render(request, 'cabroozadmin/index.html', {"dashboards": dashboards, "recentride":recentride })


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created for {user} !')
            return redirect('login')

    else:
        form = UserRegistrationForm()

    return render(request, 'cabroozadmin/register.html', {'form':form})


def Login(request):
    return render(request, 'cabroozadmin/login.html')


@login_required
def users(request):
    users = User.objects.all()
    return render(request, 'cabroozadmin/users.html', {"users":users})


@login_required
def providers(request):
    provider = Provider.objects.all()
    return render(request, 'cabroozadmin/providers.html', {"provider":provider} )


@login_required
def dispatchers(request):
    dispatch = Dispatcher.objects.all()
    return render(request, 'cabroozadmin/dispatcher.html', {"dispatch":dispatch} )


@login_required
def fleetowner(request):
    fleet = FleetOwner.objects.all()
    return render(request, 'cabroozadmin/fleetowner.html', {"fleet":fleet} )


@login_required
def statements(request):
    statement = Statement.objects.all()
    dispatcher = Dispatcher.objects.all()
    dashboard = Dashboard.objects.all()
    return render(request, 'cabroozadmin/statements.html', {"statement":statement, "dispatcher":dispatcher, "dashboard":dashboard} )


@login_required
def requesthistory(request):
    reqhistory = RequestHistory.objects.all()
    return render(request, 'cabroozadmin/requesthistory.html', {"reqhistory":reqhistory})



def maps(request):
    return render(request, 'cabroozadmin/maps.html')


@login_required
def servicetypes(request):
    servicetype = ServiceTypes.objects.all()

    return render(request, 'cabroozadmin/servicetypes.html', {"servicetype":servicetype})


@login_required
def documents(request):
    document = Documents.objects.all()

    return render(request, 'cabroozadmin/documents.html', {"document":document})


@login_required
def promocodes(request):
    promocode = Documents.objects.all()
    return render(request, 'cabroozadmin/promocodes.html', {"promocode":promocode})



@login_required
def driverdetails(request):
    drive = DriverDetail.objects.all()
    return render(request, 'cabroozadmin/driverdetails.html', {"drive":drive})















