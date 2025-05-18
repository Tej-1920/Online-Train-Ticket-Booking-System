from django.db import models
from django.contrib.auth.models import User

class Register(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    mobile=models.CharField(max_length=10,null=True)
    add=models.CharField(max_length=100,null=True)
    dob=models.DateField(null=True)
    gender=models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.user.first_name

class Add_Train(models.Model):
    trainname=models.CharField(max_length=30,null=True)
    train_no=models.IntegerField(null=True)
    from_city=models.CharField(max_length=30,null=True)
    to_city=models.CharField(max_length=30,null=True)
    departuretime=models.CharField(max_length=30,null=True)
    arrivaltime=models.CharField(max_length=30,null=True)
    traveltime=models.CharField(max_length=100,null=True)
    distance=models.IntegerField(null=True)
    img=models.FileField(null=True)

    def __str__(self):
        return f"{self.trainname} ({self.train_no})"

class Add_route(models.Model):
    train = models.ForeignKey(Add_Train, on_delete=models.CASCADE)
    route = models.CharField(max_length=100,default='Unknown Route')
    fare = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    seats = models.IntegerField(default=0)
    distance = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.train.trainname} - {self.route}"

class Passenger(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    train = models.ForeignKey(Add_Train, on_delete=models.CASCADE)
    route = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    fare = models.DecimalField(max_digits=10, decimal_places=2)
    date1 = models.DateField()
    status = models.CharField(max_length=10, default='pending')

    def __str__(self):
        return f"{self.name} - {self.train.trainname}"

class Book_ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    route = models.CharField(max_length=100)
    fare = models.DecimalField(max_digits=10, decimal_places=2)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    date2 = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.route}"