from django.db import models
from django.utils import timezone
# Create your models here.


# Class User
class User(models.Model):
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    contact_number = models.IntegerField(null=True)

    def __str__(self):
        return self.user_name


# Lost Items
class LostItems(models.Model):
    item_name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, null=True)
    date = models.DateTimeField('date lost', default=timezone.now)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)


# Found Items
class FoundItems(models.Model):
    item_name = models.CharField(max_length=200)
    desciption = models.CharField(max_length=500, null=True)
    date = models.DateTimeField('date found', default=timezone.now)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)




