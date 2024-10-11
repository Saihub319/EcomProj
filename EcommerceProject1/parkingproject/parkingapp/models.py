from django.db import models
from django.contrib.auth.hashers import make_password

class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    parking_area_no = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=100)
    vehicle_limit = models.CharField(max_length=200)
    parking_charge = models.IntegerField()
    status = models.CharField(max_length=10)
    doc = models.DateTimeField()

    def __str__(self):
        return self.parking_area_no


# class Admin(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=120)
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name



class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)  # Should store hashed passwords

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Hash the password before saving
        if not self.pk or not Admin.objects.filter(pk=self.pk).exists():  # Hash only when creating a new Admin
            self.password = make_password(self.password)
        super(Admin, self).save(*args, **kwargs)



class AddVehicle(models.Model):
    id = models.AutoField(primary_key=True)
    vehicle_no = models.CharField(max_length=200)
    parking_area_no = models.CharField(max_length=200)
    vehicle_type = models.CharField(max_length=200)
    parking_charge = models.IntegerField()
    status = models.CharField(max_length=10)
    arrival_time = models.DateTimeField()

    def __str__(self):
        return self.vehicle_no
