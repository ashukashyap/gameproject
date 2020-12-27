from django.db import models

# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=200)
    timestemp = models.CharField(max_length=200)
    count = models.TextField()


    def __str__(self):
        return self.title

class Rahul(models.Model):
    name = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    num = models.IntegerField(default=0) 
    stor = models.TextField()   

    def __str__(self):
        return self.name
        

class Table(models.Model):
    date = models.CharField(max_length=200)
    deshwer = models.CharField(max_length=100)
    fridabad = models.CharField(max_length=200)
    gaziybad = models.CharField(max_length=100)
    


    def __str__(self):
        return self.date

class Record(models.Model):
    date = models.CharField(max_length=200) 
    gali = models.CharField(max_length=200)
    shrignash = models.CharField(max_length=100)
    delhibazzer = models.CharField(max_length=200)


    def __str__(self):
        return self.date
    


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    desc = models.TextField()


    def __str__(self):
        return self.name



class Singup(models.Model):
    email = models.EmailField()
    timestemp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.email




class blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()        