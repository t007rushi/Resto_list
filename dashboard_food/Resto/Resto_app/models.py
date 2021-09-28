from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import OrderBy
from django.db.models.fields import AutoField
from django.db.models.fields.related import ForeignKey

# Create your models here.

# PK 1


class Resto_list(models.Model, OrderBy=id):
    id = models.IntegerField(primary_key=True, AutoField=True)
    Name = models.CharField(max_length=100)
    Review = models.IntegerField(default=1)
    sale = models.IntegerField()
    date = models.DateField()
    status = models.CharField(max_length=10)

# PK 2


class Resto_Details(models.Model):
    Id = models.ForeignKey(Resto_list, max_length=100,
                           primary_key=True, on_delete=CASCADE)
    Name = models.CharField(max_length=20)
    number = models.IntegerField(max_length=10)
    altnumber = models.IntegerField(max_length=10)
    whatsapp = models.BooleanField(null=False)
    Email = models.EmailField(max_length=25)
    status = models.CharField(max_length=10)


class Acknow(models.Model):
    Esign = models.ImageField()
    photo = models.ImageField(width_field="640px", height_field="720px")
    menu = models.ImageField(width_field="640px", height_field="720px")


class owner(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    aadhar = models.IntegerField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)


class Gst_Pan(models.Model):
    Gnumber = models.IntegerField(max_length=10)
    Gphoto = models.ImageField(width_field="640px", height_field="720px")
    address = models.CharField(max_length=20)
    panphoto = models.ImageField(width_field="640px", height_field="720px")


class BANK(models.Model):
    name = models.CharField(max_length=100)
    accntNo = models.IntegerField(max_length=20, primary_key=True, unique=True)
    name = models.CharField(max_length=10)
    IFSC = models.CharField(max_length=20)
    owner_id = models.ForeignKey(max_length=10, on_delete=CASCADE)
