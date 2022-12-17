from django.db import models

# Create your models here.
class Category(models.Model):
    Cname=models.CharField(max_length=20)
    Curl=models.CharField(max_length=20)
    Cimage=models.ImageField(upload_to='cimage')
    def __str__(self):
        return self.Cname

class ContactUs(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Mobile=models.CharField(max_length=20)
    City=models.CharField(max_length=20)
    def __str__(self):
        return self.Name

class Advocates(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image',null=False)
    def __str__(self):
        return self.name


class Astrologers(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image',null=False)
    def __str__(self):
        return self.name

class AutomobileRepair(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image',null=False)
    def __str__(self):
        return self.name

class Bakeries(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image',null=False)
    def __str__(self):
        return self.name  

class Banks(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image',null=False)
    def __str__(self):
        return self.name

class Books_Stationaries(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image',null=False)
    def __str__(self):
        return self.name  

class Builders(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image',null=False)
    def __str__(self):
        return self.name

class CA(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image',null=False)
    def __str__(self):
        return self.name      

class Carpenters(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image',null=False)
    def __str__(self):
        return self.name

class  Cloths(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image',null=False)
    def __str__(self):
        return self.name

class Computers(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image',null=False)
    def __str__(self):
        return self.name

class Catering(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image',null=False)
    def __str__(self):
        return self.name

class Courier(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image',null=False)
    def __str__(self):
        return self.name

class Doctors(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image',null=False)
    def __str__(self):
        return self.name

class Drivers(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image',null=False)
    def __str__(self):
        return self.name 

class DryCleaners(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image',null=False)
    def __str__(self):
        return self.name

class Electricians(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image',null=False)
    def __str__(self):
        return self.name        
class Electronics(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image',null=False)
    def __str__(self):
        return self.name

class EventManagement(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class FastFood(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Footwear(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Furniture(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class GasAgencies(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class GiftShops(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Gyms(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class HairSaloon(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Hotels(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Jwellery(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class KiranaGeneral(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Labours(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Medical(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tiffin(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Milk(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    def __str__(self):
        return self.name


class News(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Opticals(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    def __str__(self):
        return self.name


class PetrolPump(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    def __str__(self):
        return self.name


class PStudio(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Plumber(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    def __str__(self):
        return self.name


class PropertyDealer(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    def __str__(self):
        return self.name


class School(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Tailor(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    def __str__(self):
        return self.name


class TentHouse(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Transport(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    def __str__(self):
        return self.name


class WaterRO(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    def __str__(self):
        return self.name