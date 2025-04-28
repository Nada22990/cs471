from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    price = models.FloatField(default = 0.0)
    edition = models.SmallIntegerField(default = 1)

########################################################################Task1

class Address(models.Model):
    city=models.CharField(max_length = 50)  

    def __str__(self):
        return self.city
       

class Student(models.Model):
    name=models.CharField(max_length = 50)
    age= models.IntegerField()
    address= models.ForeignKey(Address, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    
 ##########################################################################Task2 

class Address22(models.Model):
    city = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.city

class Student22(models.Model):
    name = models.CharField(max_length = 50)
    age = models.IntegerField() 
    address = models.ManyToManyField(Address22)
    
    def __str__(self):
        return self.name
    


class Address33(models.Model):
    city = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.city


class Student33(models.Model):
    name = models.CharField(max_length = 50)
    age = models.IntegerField() 
    address = models.ManyToManyField(Address33)
    
    def __str__(self):
        return self.name

###############################################################################

class Card11(models.Model):
    card_number = models.IntegerField()
    
    def str(self):
        return str(self.card_number)
    
    
class Department11(models.Model):
    name = models.CharField(max_length = 50)
    
    def str(self):
        return self.name
    
class Course11(models.Model):
    title = models.CharField(max_length = 50)
    code = models.IntegerField()
    
    def str(self):
        return f"{self.title} ({self.code})" 
    
class Students11(models.Model):
     name = models.CharField(max_length = 50)
     card = models.OneToOneField(Card11, on_delete=models.PROTECT)
     department = models.ForeignKey(Department11, on_delete=models.CASCADE)
     course = models.ManyToManyField(Course11)



class Book3(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    price=models.FloatField(default=0.0)
    edition=models.SmallIntegerField(default=1)

############################ Task 3

class Profile2(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='profile_photos/')

    def str(self):
        return self.name
