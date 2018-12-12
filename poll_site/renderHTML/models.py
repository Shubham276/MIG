from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.


class Restaurant(models.Model):
    name = models.TextField()
    street = models.TextField()
    number = models.IntegerField()
    city = models.TextField(default="")
    zipcode = models.IntegerField()
    stateorProvince = models.TextField()
    country = models.TextField()
    telephone = models.TextField()
    url = models.URLField(null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateTimeField(default=date.today)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.TextField()
    description = models.TextField()
    price = models.DecimalField('Euro amount', max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='myrestaurants')
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateTimeField(default=date.today)
    restaurant = models.ForeignKey(Restaurant, null=True, related_name='dishes', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Review(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', choices=RATING_CHOICES)
    comment = models.TextField()
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateTimeField(default=date.today)
    dish = models.ForeignKey(Dish, null=True, related_name='reviews', on_delete=models.CASCADE)


class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=1000)
    email = models.EmailField()
    econtacts = models.CharField(max_length=15)
    eimage = models.ImageField(upload_to='Employee')

    class Meta:
        db_table = 'emp'

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
