from django.db import models
from django.db.models.fields import DecimalField, IntegerField
from django.contrib.auth.models import User
# Create your models here.



class Dashboard(models.Model):
    totalnoofrides = IntegerField(null=True, blank=True)
    cancelledpercentage = DecimalField(max_digits=4, null=True, blank=True, decimal_places=2)
    totalrevenue = IntegerField(null=True, blank=True)
    fromtotalrides = IntegerField(null=True, blank=True)
    noservicetypes = IntegerField(null=True, blank=True)
    dashboardtotalrides = IntegerField(null=True, blank=True)
    forpercentrides = DecimalField(max_digits=4, null=True, blank=True, decimal_places=2)
    cancelledcount = IntegerField(null=True, blank=True)
    providercancelledcount = IntegerField(null=True, blank=True)
    nooffleet = IntegerField(null=True, blank=True)
    noscheduledrides = IntegerField(null=True, blank=True)
    totalusers = IntegerField(null=True, blank=True)

    # def __str__(self):
    #     return self.user



class RecentRide(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ridersname = models.CharField(max_length=255, null=True, blank=True)
    details = models.TextField()
    time = models.TimeField(auto_now_add=True)
    action = models.CharField(max_length=255, null=True, blank=True)
    totalusers = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.ridersname



class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    fullname = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    time = models.TimeField(auto_now_add=True)
    totaluser = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.fullname



class Provider(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    mobile = models.CharField(max_length=25, null=True, blank=True)
    request = models.CharField(max_length=255, null=True, blank=True)
    time = models.TimeField(auto_now_add=True)
    action = models.CharField(max_length=65, null=True, blank=True)
    totalproviders = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name



class Dispatcher(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    dispatchername = models.CharField(max_length=255, null=True, blank=True)
    time = models.TimeField(auto_now_add=True)
    action = models.CharField(max_length=65, null=True, blank=True)

    def __str__(self):
        return self.dispatchername



class FleetOwner(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    fullname = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    mobile = models.CharField(max_length=25, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    request = models.CharField(max_length=255, null=True, blank=True)
    time = models.TimeField(auto_now_add=True)
    action = models.CharField(max_length=65, null=True, blank=True)

    def __str__(self):
        return self.fullname


class RequestHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    bookingid = models.AutoField(primary_key=True, editable=False)
    providername = models.CharField(max_length=255, null=True, blank=True)
    time = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    Amount = models.IntegerField(null=True, blank=True)
    paymentmode = models.CharField(max_length=255, null=True, blank=True)
    paymentstatus = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.providername


class Statement(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    overallearnings = models.CharField(max_length=255, null=True, blank=True)
    overallcommission = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.overallearnings



class ServiceTypes(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)    
    servicename = models.CharField(max_length=255 ,null=True, blank=True)
    providername = models.CharField(max_length=255 ,null=True, blank=True)
    capacity = models.CharField(max_length=255 ,null=True, blank=True)
    baseprice = models.IntegerField(null=True, blank=True)
    basediscount = models.IntegerField(null=True, blank=True)
    timeprice = models.IntegerField(null=True, blank=True)
    pricecalculations = models.IntegerField(null=True, blank=True)
    serviceimage = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.servicename


class Documents(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)    
    promocode = models.CharField(max_length=255 ,null=True, blank=True)
    discount = models.IntegerField(null=True, blank=True)
    expiration = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=255 ,null=True, blank=True)
    usercount = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return self.promocode


class DriverDetail(models.Model):
    users = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)    
    drivername = models.CharField(max_length=65, null=True, blank=True)
    country = models.CharField(max_length=65, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=65, null=True, blank=True)
    referal = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)
    cnicfront = models.ImageField(null=True, blank=True)
    cnicback = models.ImageField(null=True, blank=True)
    driverslicensefront = models.ImageField(null=True, blank=True)
    driverslicenseback = models.ImageField(null=True, blank=True)
    vehicle = models.CharField(max_length=255, null=True, blank=True)
    statuses = models.CharField(max_length=255, null=True, blank=True)
    times = models.DateField(auto_now_add=True)
    wallet = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return self.drivername







