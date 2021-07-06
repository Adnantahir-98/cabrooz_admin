
from django.urls import path
from django.contrib.auth import views as login_view
from . import views


urlpatterns = [
    path('', views.index, name="Home"),
    path('register/', views.register, name='register'),
    path('login/', login_view.LoginView.as_view(template_name="cabroozadmin/login.html"), name='Login'),
    path('logout/', login_view.LogoutView.as_view(template_name="cabroozadmin/logout.html"), name='logout'),
    path('users/', views.users, name="users"),
    path('providers/', views.providers, name="providers"),
    path('dispatcher/', views.dispatchers, name="dispatcher"),
    path('fleetowner/', views.fleetowner, name="fleetowner"),
    path('statements/', views.statements, name="statements"),
    path('maps/', views.maps, name="maps"),
    path('reqhistory/', views.requesthistory, name="reqhistory"),
    path('servicetype/', views.servicetypes, name="servicetype"),
    path('documents/', views.documents, name="documents"),
    path('promocodes/', views.promocodes, name="promocodes"),

]

